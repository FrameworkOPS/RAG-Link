"""Query endpoint — retrieves context and streams a Claude answer."""

import json
import logging
from typing import Annotated

from fastapi import APIRouter, Query
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

from app.embeddings.voyage import VoyageClient
from app.generation.claude import stream_answer
from app.retrieval.vector_store import SearchResult, similarity_search
from app.config import settings

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
    url: str
    similarity: float


def _to_source(r: SearchResult) -> SourceDoc:
    return SourceDoc(
        id=r.id,
        repo=r.repo,
        source_type=r.source_type,
        path=r.path,
        title=r.title,
        url=r.url,
        similarity=round(r.similarity, 4),
    )


async def _sse_stream(query: str, results: list[SearchResult]):
    """Yields Server-Sent Events: first sources, then streamed answer tokens."""
    # Send sources as first event
    sources = [_to_source(r).model_dump() for r in results]
    yield f"event: sources\ndata: {json.dumps(sources)}\n\n"

    # Stream answer tokens
    async for token in stream_answer(query, results):
        payload = json.dumps({"token": token})
        yield f"event: token\ndata: {payload}\n\n"

    yield "event: done\ndata: {}\n\n"


@router.post("/query")
async def query_rag(req: QueryRequest):
    voyage = VoyageClient(settings.voyage_api_key, settings.voyage_model)
    embedding = await voyage.embed_query(req.query)

    results = await similarity_search(
        query_embedding=embedding,
        match_count=req.match_count,
        match_threshold=req.threshold,
        filter_repo=req.repo,
        filter_types=req.source_types,
    )

    return StreamingResponse(
        _sse_stream(req.query, results),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )
