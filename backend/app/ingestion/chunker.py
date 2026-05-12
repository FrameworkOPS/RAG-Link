"""Text chunking: splits documents into overlapping chunks."""

import re
from dataclasses import dataclass, field
from typing import Any

from app.ingestion.github_client import RawDocument


@dataclass
class Chunk:
    repo: str
    source_type: str
    path: str | None
    title: str | None
    url: str
    content: str
    chunk_index: int
    total_chunks: int
    metadata: dict[str, Any] = field(default_factory=dict)


def _split_by_chars(text: str, size: int, overlap: int) -> list[str]:
    """Simple character-level sliding window split."""
    if len(text) <= size:
        return [text]
    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = start + size
        chunk = text[start:end]
        # Try to break at a newline near the boundary
        if end < len(text):
            boundary = chunk.rfind("\n", size - overlap)
            if boundary != -1:
                end = start + boundary + 1
                chunk = text[start:end]
        chunks.append(chunk.strip())
        start = end - overlap
        if start >= len(text):
            break
    return [c for c in chunks if c]


def _split_code(text: str, size: int, overlap: int) -> list[str]:
    """Split code by top-level definitions first, then fall back to chars."""
    # Identify top-level function/class boundaries
    pattern = re.compile(
        r"^(?:def |class |async def |function |const |export (?:default )?(?:function|class|const))",
        re.MULTILINE,
    )
    boundaries = [m.start() for m in pattern.finditer(text)] + [len(text)]

    if len(boundaries) <= 2:
        return _split_by_chars(text, size, overlap)

    sections: list[str] = []
    for i in range(len(boundaries) - 1):
        section = text[boundaries[i]: boundaries[i + 1]].strip()
        if section:
            sections.append(section)

    # Merge small sections, split large ones
    chunks: list[str] = []
    buffer = ""
    for section in sections:
        if len(buffer) + len(section) + 1 <= size:
            buffer = (buffer + "\n" + section).strip()
        else:
            if buffer:
                chunks.extend(_split_by_chars(buffer, size, overlap))
            buffer = section
    if buffer:
        chunks.extend(_split_by_chars(buffer, size, overlap))

    return chunks


def _split_markdown(text: str, size: int, overlap: int) -> list[str]:
    """Split markdown by H2/H3 headers first."""
    pattern = re.compile(r"^#{1,3} .+", re.MULTILINE)
    boundaries = [m.start() for m in pattern.finditer(text)] + [len(text)]

    if len(boundaries) <= 1:
        return _split_by_chars(text, size, overlap)

    sections: list[str] = []
    for i in range(len(boundaries) - 1):
        section = text[boundaries[i]: boundaries[i + 1]].strip()
        if section:
            sections.append(section)

    chunks: list[str] = []
    for section in sections:
        chunks.extend(_split_by_chars(section, size, overlap))
    return chunks


CODE_EXTENSIONS = {
    ".py", ".js", ".ts", ".tsx", ".jsx", ".go", ".rs",
    ".java", ".rb", ".php", ".c", ".cpp", ".h", ".cs",
    ".swift", ".sh", ".sql", ".graphql",
}

MARKDOWN_EXTENSIONS = {".md", ".mdx", ".txt"}


def chunk_document(doc: RawDocument, size: int = 1500, overlap: int = 200) -> list[Chunk]:
    ext = "." + doc.path.rsplit(".", 1)[-1].lower() if doc.path and "." in doc.path else ""

    if doc.source_type in ("issue", "pr"):
        raw_chunks = _split_markdown(doc.content, size, overlap)
    elif doc.source_type in ("readme",) or ext in MARKDOWN_EXTENSIONS:
        raw_chunks = _split_markdown(doc.content, size, overlap)
    elif ext in CODE_EXTENSIONS:
        raw_chunks = _split_code(doc.content, size, overlap)
    else:
        raw_chunks = _split_by_chars(doc.content, size, overlap)

    total = len(raw_chunks)
    return [
        Chunk(
            repo=doc.repo,
            source_type=doc.source_type,
            path=doc.path,
            title=doc.title,
            url=doc.url,
            content=raw_chunk,
            chunk_index=i,
            total_chunks=total,
            metadata=doc.metadata,
        )
        for i, raw_chunk in enumerate(raw_chunks)
        if raw_chunk.strip()
    ]
