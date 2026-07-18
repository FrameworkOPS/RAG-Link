"""Authenticated canonical RAG and agent-contract endpoints."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from app.api.auth import require_api_key
from app.config import settings
from app.embeddings.voyage import VoyageClient
from app.retrieval.kb_store import (
    replace_document_chunks,
    search_kb,
    source_counts,
    split_text,
)
from app.telemetry import RagRun

router = APIRouter()


class SearchRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=8000)
    limit: int = Field(default=6, ge=1, le=50)
    sources: list[str] | None = None
    tenant_id: str = Field(default="skyright", min_length=1, max_length=128)
    threshold: float = Field(default=0.4, ge=-1.0, le=1.0)
    caller_agent: str = Field(..., min_length=1, max_length=128)
    parent_run_id: str | None = None


class UpsertDocument(BaseModel):
    source: str = Field(..., min_length=1, max_length=128)
    external_id: str = Field(..., min_length=1, max_length=512)
    title: str | None = Field(default=None, max_length=1000)
    content: str = Field(..., min_length=1)
    url: str | None = Field(default=None, max_length=4000)
    metadata: dict[str, Any] = Field(default_factory=dict)
    tenant_id: str = Field(default="skyright", min_length=1, max_length=128)


class UpsertRequest(BaseModel):
    documents: list[UpsertDocument] = Field(..., min_length=1, max_length=100)
    caller_agent: str = Field(..., min_length=1, max_length=128)
    parent_run_id: str | None = None


def _serialize(result):
    return {
        "id": result.id,
        "title": result.title,
        "content": result.content,
        "url": result.url,
        "source": result.source,
        "source_id": result.source_id,
        "tenant_id": result.tenant_id,
        "metadata": result.metadata,
        "similarity": round(result.similarity, 6),
    }


async def perform_search(req: SearchRequest) -> dict[str, Any]:
    run = RagRun(
        caller_agent=req.caller_agent,
        record_type="rag_search",
        parent_run_id=req.parent_run_id,
        inputs={
            "query_sha256": __import__("hashlib").sha256(req.query.encode()).hexdigest(),
            "limit": req.limit,
            "sources": req.sources,
            "tenant_id": req.tenant_id,
            "threshold": req.threshold,
        },
    )
    await run.start()
    try:
        voyage = VoyageClient(settings.voyage_api_key, settings.voyage_model)
        embedding = await voyage.embed_query(req.query)
        results = await search_kb(
            embedding,
            limit=req.limit,
            sources=req.sources,
            tenant_id=req.tenant_id,
            threshold=req.threshold,
        )
        ids = [result.id for result in results]
        await run.finish(status="completed", document_ids=ids)
        return {"results": [_serialize(result) for result in results], "run_id": run.run_id}
    except Exception as exc:
        await run.finish(status="failed", document_ids=[], error_message=str(exc))
        raise


@router.post("/api/v1/search", dependencies=[Depends(require_api_key)])
async def canonical_search(req: SearchRequest):
    return await perform_search(req)


@router.post("/api/v1/documents/upsert", dependencies=[Depends(require_api_key)])
async def canonical_upsert(req: UpsertRequest):
    run = RagRun(
        caller_agent=req.caller_agent,
        record_type="rag_ingest",
        parent_run_id=req.parent_run_id,
        inputs={
            "document_count": len(req.documents),
            "sources": sorted({document.source for document in req.documents}),
            "tenant_ids": sorted({document.tenant_id for document in req.documents}),
        },
    )
    await run.start()
    document_ids: list[str] = []
    try:
        voyage = VoyageClient(settings.voyage_api_key, settings.voyage_model)
        for document in req.documents:
            chunks = split_text(document.content, settings.chunk_size, settings.chunk_overlap)
            embeddings = await voyage.embed(chunks, input_type="document")
            document_ids.extend(
                await replace_document_chunks(
                    source=document.source,
                    external_id=document.external_id,
                    title=document.title,
                    content=document.content,
                    url=document.url,
                    metadata=document.metadata,
                    tenant_id=document.tenant_id,
                    embeddings=embeddings,
                    chunks=chunks,
                )
            )
        await run.finish(status="completed", document_ids=document_ids)
        return {
            "status": "completed",
            "document_ids": document_ids,
            "document_count": len(req.documents),
            "chunk_count": len(document_ids),
            "run_id": run.run_id,
        }
    except Exception as exc:
        await run.finish(status="failed", document_ids=document_ids, error_message=str(exc))
        raise


@router.get("/api/v1/sources/counts", dependencies=[Depends(require_api_key)])
async def canonical_source_counts(tenant_id: str = "skyright"):
    return {"tenant_id": tenant_id, "sources": await source_counts(tenant_id)}


@router.get("/agent/describe", dependencies=[Depends(require_api_key)])
async def describe_agent():
    return {
        "name": "rag.agent",
        "version": settings.agent_version,
        "service_url": settings.agent_service_url or None,
        "skills": [
            {
                "name": "search_kb",
                "description": "Search the canonical Framework OPS knowledge base with tenant and source filters.",
                "input_schema": SearchRequest.model_json_schema(),
            }
        ],
    }


class InvokeRequest(BaseModel):
    skill: str
    input: dict[str, Any]
    caller_agent: str | None = None
    parent_run_id: str | None = None


@router.post("/agent/invoke", dependencies=[Depends(require_api_key)])
async def invoke_agent(req: InvokeRequest):
    if req.skill != "search_kb":
        raise HTTPException(404, "Unknown skill")
    payload = {
        **req.input,
        "caller_agent": req.caller_agent or req.input.get("caller_agent") or "unknown",
        "parent_run_id": req.parent_run_id or req.input.get("parent_run_id"),
    }
    return await perform_search(SearchRequest.model_validate(payload))

