"""Claude generation with streaming via Anthropic SDK."""

import logging
from collections.abc import AsyncGenerator

import anthropic

from app.config import settings
from app.retrieval.kb_store import KbSearchResult

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are RAG-Link, an intelligent assistant for the Framework OPS team.
You answer questions about code, architecture, processes, and engineering decisions using
the retrieved context below.

Guidelines:
- Be concise and precise — this is a technical audience.
- Always cite the source of information (file path, issue number, PR number, etc.).
- If the context doesn't contain enough information to answer confidently, say so.
- Format code snippets with proper markdown code fences and language tags.
- Prioritize recent information when sources conflict."""


def _format_context(results: list[KbSearchResult]) -> str:
    if not results:
        return "No relevant documents found."

    parts: list[str] = []
    for i, r in enumerate(results, 1):
        label = r.metadata.get("path") or r.title or r.source
        parts.append(
            f"[{i}] **{r.source.upper()}** — `{label}` (similarity: {r.similarity:.2f})\n"
            f"Source: {r.url or 'not provided'}\n\n"
            f"```\n{r.content[:3000]}\n```"
        )
    return "\n\n---\n\n".join(parts)


async def stream_answer(
    query: str,
    context: list[KbSearchResult],
) -> AsyncGenerator[str, None]:
    client = anthropic.AsyncAnthropic(api_key=settings.anthropic_api_key)
    formatted_context = _format_context(context)

    user_message = (
        f"<context>\n{formatted_context}\n</context>\n\n"
        f"<question>{query}</question>"
    )

    async with client.messages.stream(
        model=settings.anthropic_model,
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    ) as stream:
        async for text in stream.text_stream:
            yield text


async def answer(
    query: str,
    context: list[KbSearchResult],
) -> str:
    """Non-streaming variant for webhook or batch use."""
    client = anthropic.AsyncAnthropic(api_key=settings.anthropic_api_key)
    formatted_context = _format_context(context)

    user_message = (
        f"<context>\n{formatted_context}\n</context>\n\n"
        f"<question>{query}</question>"
    )

    response = await client.messages.create(
        model=settings.anthropic_model,
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    )
    return response.content[0].text
