"""One-time repair for canonical KB rows that are missing Voyage-3 vectors."""

from __future__ import annotations

import asyncio

from supabase import create_client

from app.config import settings
from app.embeddings.voyage import VoyageClient

BATCH_SIZE = 64


async def main() -> None:
    db = create_client(settings.supabase_url, settings.supabase_service_role_key)
    response = (
        db.table("kb_documents")
        .select("id,content,source")
        .is_("embedding", "null")
        .in_("source", ["skyright_knowledge_compiler", "manual"])
        .order("id")
        .limit(1000)
        .execute()
    )
    rows = response.data or []
    voyage = VoyageClient(settings.voyage_api_key, settings.voyage_model)
    for index in range(0, len(rows), BATCH_SIZE):
        batch = rows[index : index + BATCH_SIZE]
        embeddings = await voyage.embed([row["content"] for row in batch], input_type="document")
        for row, embedding in zip(batch, embeddings, strict=True):
            (
                db.table("kb_documents")
                .update({"embedding": embedding, "embedding_model": settings.voyage_model})
                .eq("id", row["id"])
                .execute()
            )
        print(f"embedded {min(index + BATCH_SIZE, len(rows))}/{len(rows)}")
    print(f"re-embedded {len(rows)} canonical KB rows")


if __name__ == "__main__":
    asyncio.run(main())

