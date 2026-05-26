"""
fieldy_to_obsidian.py — Sync Fieldy conversations to your Obsidian vault

Creates one .md note per conversation under:
    {OBSIDIAN_VAULT_PATH}/Fieldy/{YYYY}/{MM-MMMM}/{YYYY-MM-DD} - {title}.md

Env vars required:
    FIELDY_API_KEY        — Fieldy API key
    OBSIDIAN_VAULT_PATH   — Path to vault root (default: ~/Documents/ObsidianVault)

Usage:
    python fieldy_to_obsidian.py                 # last 24 hrs
    python fieldy_to_obsidian.py --hours 48
    python fieldy_to_obsidian.py --start 2026-05-01 --end 2026-05-26
    python fieldy_to_obsidian.py --dry-run        # show filenames, don't write
"""

import os
import re
import sys
import time
import logging
import argparse
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

import requests
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
)
log = logging.getLogger(__name__)

# ── Config ────────────────────────────────────────────────────────────────────
FIELDY_API_KEY  = os.environ["FIELDY_API_KEY"]
OBSIDIAN_VAULT  = Path(
    os.environ.get("OBSIDIAN_VAULT_PATH", "/Users/Skyright/Documents/Framework-OPS")
).expanduser()

FIELDY_BASE     = "https://api.fieldy.ai/api/public/v2"
RATE_LIMIT_RPS  = 30
MIN_DELAY       = 60 / RATE_LIMIT_RPS

MONTH_NAMES = [
    "", "01-January", "02-February", "03-March", "04-April",
    "05-May", "06-June", "07-July", "08-August",
    "09-September", "10-October", "11-November", "12-December",
]

# ── HTTP helpers ──────────────────────────────────────────────────────────────
_session = requests.Session()
_session.headers.update({"Authorization": f"Bearer {FIELDY_API_KEY}"})


def _get(path: str, params: dict = None, retries: int = 4) -> dict:
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
            time.sleep(MIN_DELAY)
            return resp.json()
        except requests.HTTPError as exc:
            if attempt == retries - 1:
                raise
            log.warning("HTTP error %s — retry %d/%d", exc, attempt + 1, retries)
            time.sleep(wait)
            wait *= 2
    raise RuntimeError(f"Failed after {retries} retries: {url}")


def _safe(obj: dict, *keys, default=""):
    for k in keys:
        v = obj.get(k)
        if v is not None:
            return v
    return default


# ── Fieldy API ────────────────────────────────────────────────────────────────
def fetch_conversations(start_dt: datetime, end_dt: datetime) -> list[dict]:
    conversations = []
    page = 1
    page_size = 50

    params_base = {
        "start_date": start_dt.isoformat(),
        "end_date":   end_dt.isoformat(),
        "per_page":   page_size,
    }

    while True:
        params = {**params_base, "page": page}
        log.info("Fetching conversations page %d ...", page)
        data = _get("/conversations", params=params)

        items = data if isinstance(data, list) else (
            data.get("data") or data.get("conversations") or data.get("items") or []
        )

        if not items:
            break

        conversations.extend(items)

        meta = data.get("meta") or data.get("pagination") or {}
        total_pages = meta.get("total_pages") or meta.get("last_page")
        if total_pages and page >= int(total_pages):
            break
        if len(items) < page_size:
            break

        page += 1

    return conversations


def fetch_transcript(conversation_id: str) -> list[dict]:
    try:
        data = _get("/transcriptions", params={"conversation_id": conversation_id})
        return (
            data if isinstance(data, list)
            else data.get("segments") or data.get("transcript") or data.get("transcription") or []
        )
    except Exception as exc:
        log.warning("No transcript for %s: %s", conversation_id, exc)
        return []


def fetch_tasks(conversation_id: str) -> list[dict]:
    try:
        data = _get("/tasks", params={"conversation_id": conversation_id})
        return data if isinstance(data, list) else (
            data.get("data") or data.get("tasks") or data.get("items") or []
        )
    except Exception as exc:
        log.warning("No tasks for %s: %s", conversation_id, exc)
        return []


# ── Note generation ───────────────────────────────────────────────────────────
def _sanitize_filename(s: str, max_len: int = 60) -> str:
    """Strip chars illegal in filenames; truncate to max_len."""
    s = re.sub(r'[\\/:*?"<>|#%&{}]', "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s[:max_len].rstrip(". ")


def _parse_dt(timestamp: str) -> Optional[datetime]:
    """Try to parse an ISO-ish timestamp; return None on failure."""
    if not timestamp:
        return None
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%d %H:%M:%S",
                "%Y-%m-%dT%H:%M:%S.%f%z", "%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%d"):
        try:
            return datetime.strptime(timestamp[:26], fmt)
        except ValueError:
            continue
    return None


def _yaml_list(items) -> str:
    """Render a Python list as a YAML inline list string."""
    if not items:
        return "[]"
    clean = []
    for item in items:
        if isinstance(item, dict):
            val = item.get("name") or item.get("speaker") or item.get("title") or str(item)
        else:
            val = str(item)
        # Escape quotes in YAML
        val = val.replace('"', '\\"')
        clean.append(f'"{val}"')
    return "[" + ", ".join(clean) + "]"


def build_note(conv: dict, segments: list[dict], tasks: list[dict]) -> tuple[str, datetime]:
    """Return (markdown_content, parsed_datetime)."""
    title        = _safe(conv, "title", "name", "subject", default="Untitled Conversation")
    timestamp    = _safe(conv, "created_at", "date", "started_at", "timestamp", default="")
    summary      = _safe(conv, "summary", "description", "overview", default="")
    participants = _safe(conv, "participants", "speakers", "attendees", default=[])
    keywords     = _safe(conv, "keywords", "tags", "topics", default=[])
    conv_id      = str(_safe(conv, "id", "conversation_id", "uuid", default=""))

    dt = _parse_dt(timestamp) or datetime.now()

    date_str = dt.strftime("%Y-%m-%d")
    time_str = dt.strftime("%H:%M")

    # Normalise participants to list of names
    if isinstance(participants, list):
        participant_names = [
            (p.get("name") or p.get("speaker") or str(p)) if isinstance(p, dict) else str(p)
            for p in participants
        ]
    else:
        participant_names = [str(participants)] if participants else []

    # Normalise keywords
    if isinstance(keywords, list):
        keyword_list = [
            (k.get("name") or k.get("label") or str(k)) if isinstance(k, dict) else str(k)
            for k in keywords
        ]
    else:
        keyword_list = [str(keywords)] if keywords else []

    # Task titles for frontmatter
    task_titles = [
        _safe(t, "title", "name", "subject", default="Untitled task")
        for t in tasks
    ]

    # ── Frontmatter ──
    title_escaped = title.replace('"', '\\"')
    frontmatter = f"""---
title: "{title_escaped}"
date: {date_str}
time: "{time_str}"
participants: {_yaml_list(participant_names)}
keywords: {_yaml_list(keyword_list)}
tasks: {_yaml_list(task_titles)}
source: fieldy
type: conversation
conversation_id: "{conv_id}"
---"""

    # ── Transcript section ──
    transcript_lines = []
    for seg in segments:
        speaker = _safe(seg, "speaker", "speaker_name", "name", default="Unknown")
        text    = _safe(seg, "text", "content", "transcript", default="")
        ts      = _safe(seg, "timestamp", "start_time", "time", default="")
        ts_str  = f" `[{ts}]`" if ts else ""
        transcript_lines.append(f"**{speaker}**{ts_str}: {text}")

    transcript_body = "\n\n".join(transcript_lines) if transcript_lines else "_No transcript available._"

    # ── Tasks section ──
    task_lines = []
    for task in tasks:
        t_title  = _safe(task, "title", "name", "subject", default="Untitled task")
        t_status = _safe(task, "status", "state", default="open")
        t_due    = _safe(task, "due_date", "due", "deadline", default="")
        t_notes  = _safe(task, "description", "notes", "body", default="")
        checkbox = "x" if t_status.lower() in ("completed", "done", "closed") else " "
        due_str  = f" 📅 {t_due}" if t_due else ""
        notes_str = f"\n  _{t_notes}_" if t_notes else ""
        task_lines.append(f"- [{checkbox}] {t_title}{due_str}{notes_str}")

    tasks_body = "\n".join(task_lines) if task_lines else "_No action items recorded._"

    # ── Assemble note ──
    note = f"""{frontmatter}

# {title}

> **Date:** {date_str} at {time_str}
> **Participants:** {', '.join(participant_names) if participant_names else 'Unknown'}
> **Keywords:** {', '.join(keyword_list) if keyword_list else '—'}

## Summary

{summary if summary else '_No summary available._'}

## Transcript

{transcript_body}

## Action Items

{tasks_body}

---
_Captured by Fieldy wearable · Imported {datetime.now().strftime('%Y-%m-%d %H:%M')}_
"""
    return note.strip(), dt


# ── File path logic ───────────────────────────────────────────────────────────
def target_path(title: str, dt: datetime) -> Path:
    """Build the vault path: Fieldy/YYYY/MM-Month/YYYY-MM-DD - Title.md"""
    year_str  = dt.strftime("%Y")
    month_str = MONTH_NAMES[dt.month]
    date_prefix = dt.strftime("%Y-%m-%d")
    safe_title = _sanitize_filename(title)
    filename = f"{date_prefix} - {safe_title}.md"

    return OBSIDIAN_VAULT / "Fieldy" / year_str / month_str / filename


def safe_write(path: Path, content: str) -> Path:
    """Write to path; if exists, increment suffix (-v2, -v3 …). Returns final path."""
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    version = 2
    while True:
        candidate = parent / f"{stem}-v{version}{suffix}"
        if not candidate.exists():
            candidate.parent.mkdir(parents=True, exist_ok=True)
            candidate.write_text(content, encoding="utf-8")
            return candidate
        version += 1


# ── Main ──────────────────────────────────────────────────────────────────────
def run(start_dt: datetime, end_dt: datetime, dry_run: bool = False):
    log.info("Syncing Fieldy → Obsidian vault: %s", OBSIDIAN_VAULT)
    log.info("Window: %s → %s", start_dt, end_dt)

    conversations = fetch_conversations(start_dt, end_dt)
    log.info("Found %d conversations", len(conversations))

    written = skipped = errors = 0

    for conv in conversations:
        conv_id = str(_safe(conv, "id", "conversation_id", "uuid", default=""))
        title   = _safe(conv, "title", "name", default="Untitled")

        log.info("  Processing: %s (%s)", title, conv_id)

        try:
            segments = fetch_transcript(conv_id) if conv_id else []
            tasks    = fetch_tasks(conv_id) if conv_id else []
            content, dt = build_note(conv, segments, tasks)
            path     = target_path(title, dt)

            if dry_run:
                print(f"\n[DRY RUN] Would write: {path}")
                print(content[:500] + "...\n")
                written += 1
                continue

            final_path = safe_write(path, content)
            if final_path != path:
                log.info("    → File existed, wrote: %s", final_path.name)
            else:
                log.info("    → Wrote: %s", final_path)
            written += 1

        except Exception as exc:
            log.error("  Error processing %s: %s", title, exc)
            errors += 1

    log.info("Done — written: %d, skipped: %d, errors: %d", written, skipped, errors)
    return written, skipped, errors


def parse_args():
    parser = argparse.ArgumentParser(description="Sync Fieldy conversations to Obsidian vault")
    parser.add_argument("--hours", type=float, default=24)
    parser.add_argument("--start", help="YYYY-MM-DD")
    parser.add_argument("--end",   help="YYYY-MM-DD")
    parser.add_argument("--dry-run", action="store_true")
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

    written, skipped, errors = run(start_dt, end_dt, dry_run=args.dry_run)
    sys.exit(0 if errors == 0 else 1)
