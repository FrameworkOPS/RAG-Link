"""MCP server exposing RAG-Link as tools for Claude clients."""

from fastmcp import FastMCP

from app.config import settings
from app.embeddings.voyage import VoyageClient
from app.retrieval.kb_store import search_kb
from app.retrieval.vector_store import get_repositories

mcp = FastMCP(name="RAG-Link")


@mcp.tool
async def search_rag_link(
    query: str,
    repo: str | None = None,
    source_types: list[str] | None = None,
    match_count: int = 8,
) -> list[dict]:
    """Search the Framework OPS knowledge base for relevant code, issues, PRs, and docs.

    Args:
        query: Natural-language question or search phrase.
        repo: Optional `owner/name` filter to restrict results to a single repository.
        source_types: Optional list of source types to include. Valid values:
            `code`, `issue`, `pr`, `readme`, `wiki`, `discussion`.
        match_count: Number of chunks to return (1-20). Default 8.

    Returns:
        List of matching chunks. Each chunk has `repo`, `source_type`, `path`, `title`,
        `url`, `content` (truncated to 3000 chars), and `similarity` (0.0-1.0).
    """
    voyage = VoyageClient(settings.voyage_api_key, settings.voyage_model)
    embedding = await voyage.embed_query(query)

    sources = source_types
    results = await search_kb(
        embedding,
        limit=max(1, min(match_count, 20)),
        threshold=settings.retrieval_threshold,
        sources=sources,
        tenant_id="skyright",
    )

    return [
        {
            "repo": r.metadata.get("repo") or r.source,
            "source_type": r.source,
            "path": r.metadata.get("path"),
            "title": r.title,
            "url": r.url,
            "content": r.content[:3000],
            "similarity": round(r.similarity, 4),
        }
        for r in results
    ]


@mcp.tool
async def list_indexed_repositories() -> list[dict]:
    """List repositories that have been ingested into the knowledge base."""
    return await get_repositories()


mcp_app = mcp.http_app(path="/")
