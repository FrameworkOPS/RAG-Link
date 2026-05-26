"""
fieldy.py — Ingest Fieldy conversations into Supabase pgvector (RAG)

Env vars required:
    FIELDY_API_KEY     — Fieldy API key (sk-f-...)
    SUPABASE_URL       — e.g. https://xxxx.supabase.co
    SUPABASE_KEY       — service_role key
    OPENAI_API_KEY     — for text-embedding-3-small

Usage:
    python fieldy.py                        # ingests last 24 hrs
    python fieldy.py --hours 48             # ingests last 48 hrs
    python fieldy.py --start 2026-05-01 --end 2026-05-26   # date range
    python fieldy.py --dry-run              # print docs, skip DB write
"""

import os
import sys
import time
import json
import logging
import argparse
from datetime import datetime, timedelta, timezone
from typing import Optional

import requests
from dotenv import load_dotenv
from openai import OpenAI
from supabase import create_client, Client

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
)
log = logging.getLogger(__name__)

# ── Config ──────────────────────────────────────────────────────────────────
FIELDY_API_KEY  = os.environ["FIELDY_API_KEY"]
SUPABASE_URL    = os.environ["SUPABASE_URL"]
SUPABASE_KEY    = os.environ["SUPABASE_KEY"]
OPENAI_API_KEY  = os.environ["OPENAI_API_KEY"]

FIELDY_BASE     = "https://api.fieldy.ai/api/public/v2"
EMBED_MODEL     = "text-embedding-3-small"
SUPABASE_TABLE  = "documents"
RATE_LIMIT_RPS  = 30          # Fieldy allows 30 req/min → ~0.5/sec
MIN_DELAY       = 60 / RATE_LIMIT_RPS   # seconds between requests

# ── HTTP helpers ─────────────────────────────────────────────────────────────
_session = requests.Session()
_session.headers.update({"Authorization": f"Bearer {FIELDY_API_KEY}"})

def _get(path: str, params: dict = None, retries: int = 4) -> dict:
    """GET with exponential backoff on rate-limit / 5xx."""
    url = f"{FIELDY_BASE}/{path.lstrip('/')}"
    wait = 2
    for attempt in range(retries):
        try:
            resp = _session.get(url, params=params, timeout=30)
            if resp.status_code == 429:
                retry_after = int(resp.headers.get("Retry-After", wait))
                log.warning("Rate limited — sleeping %ss", retry_after)
                time.sleep(retry_after)
                wait *= 2
                continue
            resp.raise_for_status()
            time.sleep(MIN_DELAY)    # proactive rate-limit guard
            return resp.json()
        except requests.HTTPError as exc:
            if attempt == retries - 1:
                raise
            log.warning("HTTP error %s — retry %d/%d", exc, attempt + 1, retries)
            time.sleep(wait)
            wait *= 2
    raise RuntimeError(f"Failed after {retries} retries: {url}")


# ── Fieldy API ────────────────────────────────────────────────────────────────
def fetch_conversations(start_dt: datetime, end_dt: datetime) -> list[dict]:
    """Paginate through /conversations for the given time window."""
    conversations = []
    page = 1
    page_size = 50

    # Fieldy may accept ISO strings or Unix timestamps — try both formats
    params_base = {
        "start_date": start_dt.isoformat(),
        "end_date":   end_dt.isoformat(),
        # Alternative param names Fieldy might use:
        # "from": int(start_dt.timestamp()),
        # "to":   int(end_dt.timestamp()),
        "per_page": page_size,
    }

    while True:
        params = {**params_base, "page": page}
        log.info("Fetching conversations page %d ...", page)
        data = _get("/conversations", params=params)

        # Handle both list-at-root and {data: [...]} envelope patterns
        items = data if isinstance(data, list) else (
            data.get("data") or data.get("conversations") or data.get("items") or []
        )

        if not items:
            break

        conversations.extend(items)
        log.info("  → %d conversations retrieved so far", len(conversations))

        # Pagination: check for next page token / total pages
        meta = data.get("meta") or data.get("pagination") or {}
        total_pages = meta.get("total_pages") or meta.get("last_page")
        if total_pages and page >= int(total_pages):
            break
        if len(items) < page_size:
            break   # short page = last page

        page += 1

    return conversations


def fetch_transcript(conversation_id: str) -> list[dict]:
    """Fetch full transcript segments for a conversation."""
    try:
        data = _get(f"/transcriptions", params={"conversation_id": conversation_id})
        # Some APIs nest under /conversations/{id}/transcription
        segments = (
            data if isinstance(data, list)
            else data.get("segments")
            or data.get("transcript")
            or data.get("transcription")
            or []
        )
        return segments
    except Exception as exc:
        log.warning("Could not fetch transcript for %s: %s", conversation_id, exc)
        return []


def fetch_tasks(conversation_id: str = None) -> list[dict]:
    """Fetch tasks, optionally scoped to a conversation."""
    params = {}
    if conversation_id:
        params["conversation_id"] = conversation_id
    try:
        data = _get("/tasks", params=params)
        items = data if isinstance(data, list) else (
            data.get("data") or data.get("tasks") or data.get("items") or []
        )
        return items
    except Exception as exc:
        log.warning("Could not fetch tasks for conversation %s: %s", conversation_id, exc)
        return []


# ── Formatting ────────────────────────────────────────────────────────────────
def _safe(conv: dict, *keys, default=""):
    """Try multiple field name variants and return first match."""
    for k in keys:
        v = conv.get(k)
        if v is not None:
            return v
    return default


def format_markdown(conv: dict, segments: list[dict], tasks: list[dict]) -> str:
    """Render a conversation + transcript + tasks as a Markdown document."""
    title        = _safe(conv, "title", "name", "subject", default="Untitled Conversation")
    timestamp    = _safe(conv, "created_at", "date", "started_at", "timestamp", default="")
    summary      = _safe(conv, "summary", "description", "overview", default="")
    participants = _safe(conv, "participants", "speakers", "attendees", default=[])
    keywords     = _safe(conv, "keywords", "tags", "topics", default=[])

    # Normalise participants to list of strings
    if isinstance(participants, list):
        names = [
            p.get("name") or p.get("speaker") or str(p)
            if isinstance(p, dict) else str(p)
            for p in participants
        ]
    else:
        names = [str(participants)]

    keyword_str = ", ".join(str(k) for k in (keywords or []))
    participants_str = ", ".join(names) if names else "Unknown"

    # Transcript lines
    transcript_lines = []
    for seg in segments:
        speaker = _safe(seg, "speaker", "speaker_name", "name", default="Unknown")
        text    = _safe(seg, "text", "content", "transcript", default="")
        ts      = _safe(seg, "timestamp", "start_time", "time", default="")
        ts_str  = f" [{ts}]" if ts else ""
        transcript_lines.append(f"**{speaker}**{ts_str}: {text}")

    transcript_section = "\n".join(transcript_lines) if transcript_lines else "_No transcript available_"

    # Tasks
    task_lines = []
    for task in tasks:
        t_title  = _safe(task, "title", "name", "subject", default="Untitled task")
        t_status = _safe(task, "status", "state", default="open")
        t_due    = _safe(task, "due_date", "due", "deadline", default="")
        due_str  = f" (due: {t_due})" if t_due else ""
        task_lines.append(f"- [{t_status.upper()}] {t_title}{due_str}")

    tasks_section = "\n".join(task_lines) if task_lines else "_No action items_"

    doc = f"""# {title}
Date: {timestamp}
Participants: {participants_str}
Keywords: {keyword_str}

## Summary
{summary if summary else "_No summary available_"}

## Transcript
{transcript_section}

## Action Items
{tasks_section}
"""
    return doc.strip()


# ── Embeddings ────────────────────────────────────────────────────────────────
_oai = OpenAI(api_key=OPENAI_API_KEY)

def embed(text: str) -> list[float]:
    resp = _oai.embeddings.create(input=text, model=EMBED_MODEL)
    return resp.data[0].embedding


# ── Supabase ──────────────────────────────────────────────────────────────────
_supa: Client = None

def get_supabase() -> Client:
    global _supa
    if _supa is None:
        _supa = create_client(SUPABASE_URL, SUPABASE_KEY)
    return _supa


def already_ingested(conversation_id: str) -> bool:
    """Return True if this conversation_id is already in the DB."""
    db = get_supabase()
    result = (
        db.table(SUPABASE_TABLE)
        .select("id")
        .eq("metadata->>conversation_id", conversation_id)
        .limit(1)
        .execute()
    )
    return len(result.data) > 0


def upsert_document(content: str, embedding: list[float], metadata: dict):
    db = get_supabase()
    db.table(SUPABASE_TABLE).upsert({
        "content":   content,
        "embedding": embedding,
        "metadata":  metadata,
    }).execute()


# ── Main ──────────────────────────────────────────────────────────────────────
def run(start_dt: datetime, end_dt: datetime, dry_run: bool = False):
    log.info("Ingesting Fieldy conversations from %s → %s", start_dt, end_dt)

    conversations = fetch_conversations(start_dt, end_dt)
    log.info("Found %d conversations", len(conversations))

    ingested = skipped = errors = 0

    for conv in conversations:
        conv_id = str(_safe(conv, "id", "conversation_id", "uuid", default=""))
        title   = _safe(conv, "title", "name", default="Untitled")

        if not conv_id:
            log.warning("Conversation missing ID — skipping: %s", title)
            errors += 1
            continue

        if not dry_run and already_ingested(conv_id):
            log.info("  [SKIP] Already ingested: %s (%s)", title, conv_id)
            skipped += 1
            continue

        log.info("  [INGEST] %s (%s)", title, conv_id)

        segments = fetch_transcript(conv_id)
        tasks    = fetch_tasks(conv_id)

        markdown  = format_markdown(conv, segments, tasks)
        timestamp = _safe(conv, "created_at", "date", "started_at", default="")

        metadata = {
            "source":          "fieldy",
            "conversation_id": conv_id,
            "title":           title,
            "date":            timestamp,
            "participants":    _safe(conv, "participants", "speakers", default=[]),
            "keywords":        _safe(conv, "keywords", "tags", default=[]),
        }

        if dry_run:
            print("=" * 60)
            print(markdown[:1000])
            print(f"\n[METADATA] {json.dumps(metadata, default=str)}")
            ingested += 1
            continue

        try:
            embedding = embed(markdown)
            upsert_document(markdown, embedding, metadata)
            ingested += 1
        except Exception as exc:
            log.error("  Failed to ingest %s: %s", conv_id, exc)
            errors += 1

    log.info("Done — ingested: %d, skipped: %d, errors: %d", ingested, skipped, errors)
    return ingested, skipped, errors


def parse_args():
    parser = argparse.ArgumentParser(description="Ingest Fieldy conversations into Supabase RAG")
    parser.add_argument("--hours", type=float, default=24, help="Look-back window in hours (default: 24)")
    parser.add_argument("--start", help="Start date YYYY-MM-DD (overrides --hours)")
    parser.add_argument("--end",   help="End date YYYY-MM-DD (default: now)")
    parser.add_argument("--dry-run", action="store_true", help="Print docs, skip DB write")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    now = datetime.now(timezone.utc)

    if args.start:
        start_dt = datetime.fromisoformat(args.start).replace(tzinfo=timezone.utc)
        end_dt   = (
            datetime.fromisoformat(args.end).replace(tzinfo=timezone.utc)
            if args.end else now
        )
    else:
        end_dt   = now
        start_dt = end_dt - timedelta(hours=args.hours)

    ingested, skipped, errors = run(start_dt, end_dt, dry_run=args.dry_run)
    sys.exit(0 if errors == 0 else 1)
