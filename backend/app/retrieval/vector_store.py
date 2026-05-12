"""Supabase pgvector retrieval — calls the match_documents RPC."""

import logging
from dataclasses import dataclass
from typing import Any

from supabase import create_client

from app.config import settings

logger = logging.getLogger(__name__)


@dataclass
class SearchResult:
    id: str
    repo: str
    source_type: str
    path: str | None
    title: str | None
    url: str
    content: str
    metadata: dict[str, Any]
    similarity: float


def _supabase():
    return create_client(settings.supabase_url, settings.supabase_service_role_key)


async def similarity_search(
    query_embedding: list[float],
    match_count: int | None = None,
    match_threshold: float | None = None,
    filter_repo: str | None = None,
    filter_types: list[str] | None = None,
) -> list[SearchResult]:
    db = _supabase()
    params: dict[str, Any] = {
        "query_embedding": query_embedding,
        "match_count": match_count or settings.retrieval_match_count,
        "match_threshold": match_threshold or settings.retrieval_threshold,
    }
    if filter_repo:
        params["filter_repo"] = filter_repo
    if filter_types:
        params["filter_types"] = filter_types

    response = db.rpc("match_documents", params).execute()
    rows = response.data or []

    results = [
        SearchResult(
            id=row["id"],
            repo=row["repo"],
            source_type=row["source_type"],
            path=row.get("path"),
            title=row.get("title"),
            url=row["url"],
            content=row["content"],
            metadata=row.get("metadata", {}),
            similarity=row["similarity"],
        )
        for row in rows
    ]
    logger.debug("Found %d results for query", len(results))
    return results


async def get_repositories() -> list[dict]:
    db = _supabase()
    resp = db.table("repositories").select("*").order("created_at", desc=True).execute()
    return resp.data or []


async def get_ingestion_jobs(limit: int = 20) -> list[dict]:
    db = _supabase()
    resp = (
        db.table("ingestion_jobs")
        .select("*")
        .order("created_at", desc=True)
        .limit(limit)
        .execute()
    )
    return resp.data or []


async def get_job(job_id: str) -> dict | None:
    db = _supabase()
    resp = db.table("ingestion_jobs").select("*").eq("id", job_id).maybe_single().execute()
    return resp.data
