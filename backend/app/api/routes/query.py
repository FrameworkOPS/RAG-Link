"""Query endpoint — retrieves context and streams a Claude answer."""

import json
import logging
from typing import Annotated

from fastapi import APIRouter, Depends, Query
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

from app.embeddings.voyage import VoyageClient
from app.generation.claude import stream_answer
from app.retrieval.kb_store import KbSearchResult, search_kb
from app.config import settings
from app.api.auth import require_api_key

logger = logging.getLogger(__name__)

router = APIRouter()


class QueryRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=4000)
    repo: str | None = None
    source_types: list[str] | None = None
    match_count: int = Field(default=8, ge=1, le=20)
    threshold: float = Field(default=0.4, ge=0.0, le=1.0)


class SourceDoc(BaseModel):
    id: str
    repo: str
    source_type: str
    path: str | None
    title: str | None
    url: str | None
    similarity: float


def _to_source(r: KbSearchResult) -> SourceDoc:
    return SourceDoc(
        id=r.id,
        repo=r.metadata.get("repo") or r.source,
        source_type=r.source,
        path=r.metadata.get("path"),
        title=r.title,
        url=r.url,
        similarity=round(r.similarity, 4),
    )


async def _sse_stream(query: str, results: list[KbSearchResult]):
    """Yields Server-Sent Events: first sources, then streamed answer tokens."""
    # Send sources as first event
    sources = [_to_source(r).model_dump() for r in results]
    yield f"event: sources\ndata: {json.dumps(sources)}\n\n"

    # Stream answer tokens
    async for token in stream_answer(query, results):
        payload = json.dumps({"token": token})
        yield f"event: token\ndata: {payload}\n\n"

    yield "event: done\ndata: {}\n\n"


@router.post("/query", dependencies=[Depends(require_api_key)])
async def query_rag(req: QueryRequest):
    voyage = VoyageClient(settings.voyage_api_key, settings.voyage_model)
    embedding = await voyage.embed_query(req.query)

    results = await search_kb(
        embedding,
        limit=req.match_count,
        threshold=req.threshold,
        sources=req.source_types,
        tenant_id="skyright",
    )

    return StreamingResponse(
        _sse_stream(req.query, results),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )
