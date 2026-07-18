"""Canonical Framework OPS knowledge-base retrieval and ingestion."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any

from supabase import create_client

from app.config import settings


@dataclass
class KbSearchResult:
    id: str
    title: str | None
    content: str
    url: str | None
    source: str
    source_id: str | None
    tenant_id: str
    metadata: dict[str, Any]
    similarity: float


def _supabase():
    return create_client(settings.supabase_url, settings.supabase_service_role_key)


async def search_kb(
    query_embedding: list[float],
    *,
    limit: int,
    sources: list[str] | None,
    tenant_id: str,
    threshold: float,
) -> list[KbSearchResult]:
    response = _supabase().rpc(
        "match_kb_documents_v2",
        {
            "query_embedding": query_embedding,
            "filter_tenant_id": tenant_id,
            "filter_sources": sources,
            "match_threshold": threshold,
            "result_limit": min(max(limit, 1), 50),
        },
    ).execute()
    return [
        KbSearchResult(
            id=row["id"],
            title=row.get("title"),
            content=row["content"],
            url=row.get("url"),
            source=row["source"],
            source_id=row.get("source_id"),
            tenant_id=row["tenant_id"],
            metadata=row.get("metadata") or {},
            similarity=float(row["similarity"]),
        )
        for row in (response.data or [])
    ]


def split_text(content: str, chunk_size: int, overlap: int) -> list[str]:
    """Split on paragraph boundaries where possible with deterministic overlap."""
    text = content.strip()
    if not text:
        return []
    if len(text) <= chunk_size:
        return [text]

    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        if end < len(text):
            boundary = text.rfind("\n\n", start + max(1, chunk_size // 2), end)
            if boundary < 0:
                boundary = text.rfind("\n", start + max(1, chunk_size // 2), end)
            if boundary > start:
                end = boundary
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end >= len(text):
            break
        next_start = max(end - overlap, start + 1)
        start = next_start
    return chunks


async def replace_document_chunks(
    *,
    source: str,
    external_id: str,
    title: str | None,
    content: str,
    url: str | None,
    metadata: dict[str, Any],
    tenant_id: str,
    embeddings: list[list[float]],
    chunks: list[str],
) -> list[str]:
    db = _supabase()
    external_document_id = f"{source}:{external_id}"
    (
        db.table("kb_documents")
        .delete()
        .eq("tenant_id", tenant_id)
        .eq("source", source)
        .filter("metadata->>external_document_id", "eq", external_document_id)
        .execute()
    )
    (
        db.table("kb_documents")
        .delete()
        .eq("tenant_id", tenant_id)
        .eq("source", source)
        .eq("source_id", external_id)
        .execute()
    )
    now = datetime.now(UTC).isoformat()
    rows = []
    for index, (chunk, embedding) in enumerate(zip(chunks, embeddings, strict=True)):
        digest = hashlib.sha256(chunk.encode("utf-8")).hexdigest()
        rows.append(
            {
                "source": source,
                "source_id": f"{external_id}#chunk={index}",
                "title": title,
                "content": chunk,
                "url": url,
                "tenant_id": tenant_id,
                "embedding": embedding,
                "embedding_model": settings.voyage_model,
                "metadata": {
                    **metadata,
                    "external_document_id": external_document_id,
                    "external_id": external_id,
                    "chunk_index": index,
                    "chunk_count": len(chunks),
                    "content_sha256": digest,
                },
                "updated_at": now,
            }
        )
    if not rows:
        return []
    response = db.table("kb_documents").insert(rows).execute()
    return [row["id"] for row in (response.data or [])]


async def source_counts(tenant_id: str) -> list[dict[str, Any]]:
    response = _supabase().rpc(
        "kb_source_counts_v2", {"filter_tenant_id": tenant_id}
    ).execute()
    return response.data or []
