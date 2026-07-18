"""End-to-end ingestion pipeline: fetch → chunk → embed → store."""

import asyncio
import logging
import uuid
from datetime import datetime, UTC

from supabase import create_client

from app.config import settings
from app.embeddings.voyage import VoyageClient
from app.ingestion.chunker import Chunk, chunk_document
from app.ingestion.github_client import GitHubClient

logger = logging.getLogger(__name__)

EMBED_BATCH_SIZE = 16        # Conservative for Voyage free tier
EMBED_SLEEP_SECONDS = 22     # Stay under the ~3 req/min free-tier rate limit


def _supabase():
    return create_client(settings.supabase_url, settings.supabase_service_role_key)


async def _upsert_chunks(chunks: list[Chunk], embeddings: list[list[float]]) -> None:
    db = _supabase()
    rows = [
        {
            "repo": chunk.repo,
            "source_type": chunk.source_type,
            "path": chunk.path,
            "title": chunk.title,
            "url": chunk.url,
            "content": chunk.content,
            "metadata": {
                **chunk.metadata,
                "chunk_index": chunk.chunk_index,
                "total_chunks": chunk.total_chunks,
            },
            "embedding": emb,
        }
        for chunk, emb in zip(chunks, embeddings)
    ]
    db.table("documents").insert(rows).execute()


async def run_ingestion(
    job_id: str,
    owner: str,
    name: str,
    source_types: list[str],
) -> None:
    db = _supabase()
    repo = f"{owner}/{name}"

    def _update_job(**kwargs):
        db.table("ingestion_jobs").update(kwargs).eq("id", job_id).execute()

    try:
        _update_job(status="running", started_at=datetime.now(UTC).isoformat())

        # 1. Delete existing docs for repo to avoid duplicates on re-index
        db.rpc("delete_repo_documents", {"target_repo": repo}).execute()

        # 2. Fetch raw documents from GitHub
        github = GitHubClient(settings.github_token)
        raw_docs = await github.fetch_all(owner, name, source_types)
        logger.info("Fetched %d raw documents from %s", len(raw_docs), repo)

        # 3. Chunk all documents
        all_chunks: list[Chunk] = []
        for doc in raw_docs:
            all_chunks.extend(
                chunk_document(doc, size=settings.chunk_size, overlap=settings.chunk_overlap)
            )
        logger.info("Created %d chunks from %s", len(all_chunks), repo)
        _update_job(total_chunks=len(all_chunks))

        if not all_chunks:
            _update_job(
                status="completed",
                completed_at=datetime.now(UTC).isoformat(),
                indexed_chunks=0,
            )
            return

        # 4. Embed + store in batches
        voyage = VoyageClient(settings.voyage_api_key, settings.voyage_model)
        indexed = 0
        for i in range(0, len(all_chunks), EMBED_BATCH_SIZE):
            batch = all_chunks[i: i + EMBED_BATCH_SIZE]
            texts = [c.content for c in batch]
            embeddings = await voyage.embed(texts, input_type="document")
            await _upsert_chunks(batch, embeddings)
            indexed += len(batch)
            _update_job(indexed_chunks=indexed)
            logger.info("Indexed %d/%d chunks for %s", indexed, len(all_chunks), repo)
            # Pace requests to stay under the Voyage rate limit
            await asyncio.sleep(EMBED_SLEEP_SECONDS)

        # 5. Mark repo as indexed
        db.table("repositories").upsert(
            {
                "owner": owner,
                "name": name,
                "last_indexed_at": datetime.now(UTC).isoformat(),
            },
            on_conflict="owner,name",
        ).execute()

        _update_job(
            status="completed",
            completed_at=datetime.now(UTC).isoformat(),
            indexed_chunks=indexed,
        )
        logger.info("Ingestion complete for %s: %d chunks indexed", repo, indexed)

    except Exception as exc:
        logger.exception("Ingestion failed for %s", repo)
        _update_job(status="failed", error=str(exc))


def create_job(owner: str, name: str, source_types: list[str]) -> str:
    job_id = str(uuid.uuid4())
    db = _supabase()
    db.table("ingestion_jobs").insert(
        {
            "id": job_id,
            "repo": f"{owner}/{name}",
            "status": "pending",
            "source_types": source_types,
        }
    ).execute()
    return job_id
