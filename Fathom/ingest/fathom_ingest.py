"""
fathom_ingest.py — Ingest Fathom meetings into Supabase pgvector (RAG)

Env vars required:
    FATHOM_API_KEY            — Fathom API key (generate at fathom.video/settings/api)
    SUPABASE_URL              — https://xxxx.supabase.co
    SUPABASE_SERVICE_ROLE_KEY — service_role key
    VOYAGE_API_KEY            — pa-...

Usage (standalone):
    python fathom_ingest.py                        # last 24 hrs
    python fathom_ingest.py --hours 48
    python fathom_ingest.py --start 2026-05-01 --end 2026-05-26
    python fathom_ingest.py --dry-run
"""

import os
import time
import logging
import argparse
from datetime import datetime, timedelta, timezone
from typing import Optional

import httpx
from dotenv import load_dotenv
from supabase import create_client

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

log = logging.getLogger(__name__)

FATHOM_API_KEY  = os.environ.get("FATHOM_API_KEY", "")
SUPABASE_URL    = os.environ.get("SUPABASE_URL", "")
SUPABASE_KEY    = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "")
VOYAGE_KEY      = os.environ.get("VOYAGE_API_KEY", "")

FATHOM_BASE     = "https://api.fathom.ai/external/v1"
VOYAGE_URL      = "https://api.voyageai.com/v1/embeddings"
VOYAGE_MODEL    = "voyage-code-2"
SUPABASE_TABLE  = "documents"
REPO            = "framework-ops/fathom-meetings"
SOURCE_TYPE     = "meeting"
EMBED_BATCH     = 8
RATE_SLEEP      = 25          # seconds between Voyage batches (free tier)


# ── Fathom API ────────────────────────────────────────────────────────────────

def _fathom_headers() -> dict:
    return {"X-Api-Key": FATHOM_API_KEY, "Content-Type": "application/json"}


def fetch_meetings(start_dt: datetime, end_dt: datetime) -> list[dict]:
    """Paginate through /meetings for the given window, with full content."""
    meetings = []
    cursor = None

    while True:
        params = {
            "created_after": start_dt.isoformat(),
            "created_before": end_dt.isoformat(),
            "include_transcript": "true",
            "include_summary": "true",
            "include_action_items": "true",
        }
        if cursor:
            params["cursor"] = cursor

        resp = httpx.get(
            f"{FATHOM_BASE}/meetings",
            headers=_fathom_headers(),
            params=params,
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()

        items = data.get("items", [])
        if not items:
            break

        meetings.extend(items)
        log.info("  → fetched %d meetings so far", len(meetings))

        cursor = data.get("next_cursor")
        if not cursor:
            break

    return meetings


# ── Chunking ──────────────────────────────────────────────────────────────────

def _participants(meeting: dict) -> list[str]:
    names = set()
    rb = meeting.get("recorded_by", {})
    if rb.get("name"):
        names.add(rb["name"])
    for inv in meeting.get("calendar_invitees", []):
        if inv.get("name"):
            names.add(inv["name"])
    return sorted(names)


def _format_transcript(items: list[dict]) -> str:
    lines = []
    for item in (items or []):
        speaker = item.get("speaker", {}).get("display_name", "Unknown")
        ts      = item.get("timestamp", "")
        text    = item.get("text", "")
        ts_str  = f" [{ts}]" if ts else ""
        lines.append(f"**{speaker}**{ts_str}: {text}")
    return "\n\n".join(lines)


def _format_action_items(items: list[dict]) -> str:
    lines = []
    for item in (items or []):
        desc     = item.get("description", "")
        assignee = (item.get("assignee") or {}).get("name") or "Unassigned"
        ts       = item.get("recording_timestamp", "")
        url      = item.get("recording_playback_url", "")
        line = f"- [ ] **{assignee}** — {desc}"
        if ts:
            line += f" `[{ts}]`"
        if url:
            line += f" [▶]({url})"
        lines.append(line)
    return "\n".join(lines)


def build_chunks(meeting: dict) -> list[dict]:
    title       = meeting.get("title") or meeting.get("meeting_title") or "Untitled Meeting"
    date_str    = (meeting.get("created_at") or "")[:10]
    url         = meeting.get("url", "")
    participants = _participants(meeting)
    participants_str = ", ".join(participants) if participants else "Unknown"

    summary_md  = (meeting.get("default_summary") or {}).get("markdown_formatted") or ""
    action_md   = _format_action_items(meeting.get("action_items") or [])
    transcript  = _format_transcript(meeting.get("transcript") or [])

    meta_base = {
        "date": date_str,
        "participants": participants,
        "meeting_type": "fathom",
        "recording_id": meeting.get("recording_id"),
        "url": url,
        "tags": ["fathom", "meeting"],
    }

    # --- Chunk 1: Overview + summary ---
    overview = f"""# {title}
Date: {date_str} | Participants: {participants_str}
Recording: {url}

## Summary
{summary_md or '_No summary available._'}"""

    # --- Chunk 2: Action items ---
    actions = f"""# Action Items — {title} ({date_str})
{action_md or '_No action items._'}
Recording: {url}"""

    chunks = [
        {"title": f"{title} — Overview & Summary", "content": overview},
        {"title": f"{title} — Action Items",        "content": actions},
    ]

    # --- Transcript chunks (split at ~1400 chars) ---
    if transcript:
        lines       = transcript.split("\n\n")
        buffer      = f"# Transcript — {title} ({date_str})\n\n"
        chunk_num   = 1
        for line in lines:
            if len(buffer) + len(line) + 2 > 1400:
                chunks.append({
                    "title": f"{title} — Transcript (part {chunk_num})",
                    "content": buffer.strip(),
                })
                chunk_num += 1
                buffer = f"# Transcript — {title} ({date_str}) cont.\n\n"
            buffer += line + "\n\n"
        if buffer.strip():
            chunks.append({
                "title": f"{title} — Transcript (part {chunk_num})",
                "content": buffer.strip(),
            })

    total = len(chunks)
    for i, chunk in enumerate(chunks):
        chunk["metadata"] = {**meta_base, "chunk_index": i, "total_chunks": total}
        chunk["url"] = url
        chunk["path"] = f"fathom/{date_str}-{title[:40].lower().replace(' ', '-')}.md"

    return chunks


# ── Voyage embeddings ─────────────────────────────────────────────────────────

def embed_texts(texts: list[str]) -> list[list[float]]:
    resp = httpx.post(
        VOYAGE_URL,
        headers={"Authorization": f"Bearer {VOYAGE_KEY}", "Content-Type": "application/json"},
        json={"model": VOYAGE_MODEL, "input": texts, "input_type": "document"},
        timeout=60,
    )
    resp.raise_for_status()
    return [item["embedding"] for item in resp.json()["data"]]


# ── Supabase upsert ───────────────────────────────────────────────────────────

def _db():
    return create_client(SUPABASE_URL, SUPABASE_KEY)


def already_ingested(recording_id: int) -> bool:
    db = _db()
    result = db.table(SUPABASE_TABLE).select("id").eq(
        "repo", REPO
    ).contains("metadata", {"recording_id": recording_id}).execute()
    return len(result.data) > 0


def upsert_chunks(chunks: list[dict], embeddings: list[list[float]]):
    db = _db()
    rows = [
        {
            "repo":        REPO,
            "source_type": SOURCE_TYPE,
            "path":        c["path"],
            "title":       c["title"],
            "url":         c["url"],
            "content":     c["content"],
            "metadata":    c["metadata"],
            "embedding":   emb,
        }
        for c, emb in zip(chunks, embeddings)
    ]
    db.table(SUPABASE_TABLE).insert(rows).execute()


# ── Main run function ─────────────────────────────────────────────────────────

def run(start_dt: datetime, end_dt: datetime, dry_run: bool = False) -> tuple[int, int, int]:
    ingested = skipped = errors = 0

    if not FATHOM_API_KEY:
        raise RuntimeError("FATHOM_API_KEY is not set")
    if not dry_run and (not SUPABASE_URL or not SUPABASE_KEY or not VOYAGE_KEY):
        raise RuntimeError("SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, or VOYAGE_API_KEY not set")

    log.info("Fetching Fathom meetings %s → %s", start_dt.date(), end_dt.date())
    meetings = fetch_meetings(start_dt, end_dt)
    log.info("Found %d meeting(s)", len(meetings))

    for meeting in meetings:
        title  = meeting.get("title") or "Untitled"
        rec_id = meeting.get("recording_id")

        if not dry_run and already_ingested(rec_id):
            log.info("  SKIP (already ingested): %s [%s]", title, rec_id)
            skipped += 1
            continue

        try:
            chunks = build_chunks(meeting)
            log.info("  %s — %d chunks", title, len(chunks))

            if dry_run:
                for c in chunks:
                    log.info("    [DRY] %s (%d chars)", c["title"], len(c["content"]))
                ingested += 1
                continue

            texts = [c["content"] for c in chunks]
            for i in range(0, len(texts), EMBED_BATCH):
                batch_chunks = chunks[i:i + EMBED_BATCH]
                batch_texts  = texts[i:i + EMBED_BATCH]
                embeddings   = embed_texts(batch_texts)
                upsert_chunks(batch_chunks, embeddings)
                if i + EMBED_BATCH < len(texts):
                    log.info("    rate-limit sleep %ss...", RATE_SLEEP)
                    time.sleep(RATE_SLEEP)

            log.info("  ✓ ingested: %s", title)
            ingested += 1

        except Exception as exc:
            log.error("  ✗ error on meeting %s: %s", title, exc, exc_info=True)
            errors += 1

    return ingested, skipped, errors


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    parser = argparse.ArgumentParser()
    parser.add_argument("--hours",   type=float, default=24)
    parser.add_argument("--start",   help="YYYY-MM-DD")
    parser.add_argument("--end",     help="YYYY-MM-DD")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    now = datetime.now(timezone.utc)
    if args.start:
        start = datetime.fromisoformat(args.start).replace(tzinfo=timezone.utc)
        end   = datetime.fromisoformat(args.end).replace(tzinfo=timezone.utc) if args.end else now
    else:
        end   = now
        start = end - timedelta(hours=args.hours)

    run(start, end, dry_run=args.dry_run)
