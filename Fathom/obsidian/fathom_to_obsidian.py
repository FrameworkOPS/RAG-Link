"""
fathom_to_obsidian.py — Sync Fathom meetings to your Obsidian vault

Creates one .md note per meeting under:
    {OBSIDIAN_VAULT_PATH}/Fathom/{YYYY}/{MM-MMMM}/{YYYY-MM-DD} - {Participants} - {Title}.md

Env vars required:
    FATHOM_API_KEY         — Fathom API key
    OBSIDIAN_VAULT_PATH    — Path to vault root (default: ~/Documents/Framework-OPS)

Usage:
    python fathom_to_obsidian.py                   # last 24 hrs
    python fathom_to_obsidian.py --hours 48
    python fathom_to_obsidian.py --start 2026-05-01 --end 2026-05-26
    python fathom_to_obsidian.py --dry-run
"""

import os
import re
import logging
import argparse
from datetime import datetime, timedelta, timezone
from pathlib import Path

import httpx
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

log = logging.getLogger(__name__)

FATHOM_API_KEY = os.environ.get("FATHOM_API_KEY", "")
OBSIDIAN_VAULT = Path(
    os.environ.get("OBSIDIAN_VAULT_PATH", os.path.expanduser("~/Documents/Framework-OPS"))
)
FATHOM_BASE    = "https://api.fathom.ai/external/v1"

MONTH_NAMES = [
    "", "01-January", "02-February", "03-March", "04-April",
    "05-May", "06-June", "07-July", "08-August",
    "09-September", "10-October", "11-November", "12-December",
]


# ── Fathom API ────────────────────────────────────────────────────────────────

def fetch_meetings(start_dt: datetime, end_dt: datetime) -> list[dict]:
    meetings = []
    cursor = None

    while True:
        params = {
            "created_after":    start_dt.isoformat(),
            "created_before":   end_dt.isoformat(),
            "include_transcript":   "true",
            "include_summary":      "true",
            "include_action_items": "true",
        }
        if cursor:
            params["cursor"] = cursor

        resp = httpx.get(
            f"{FATHOM_BASE}/meetings",
            headers={"X-Api-Key": FATHOM_API_KEY},
            params=params,
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()

        items = data.get("items", [])
        meetings.extend(items)

        cursor = data.get("next_cursor")
        if not cursor or not items:
            break

    return meetings


# ── Formatting helpers ────────────────────────────────────────────────────────

def _slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", " ", text).strip()
    return text


def _participants(meeting: dict) -> list[str]:
    names = []
    rb = meeting.get("recorded_by", {})
    if rb.get("name"):
        names.append(rb["name"])
    for inv in meeting.get("calendar_invitees", []):
        n = inv.get("name")
        if n and n not in names:
            names.append(n)
    return names


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


def render_note(meeting: dict) -> str:
    title       = meeting.get("title") or meeting.get("meeting_title") or "Untitled Meeting"
    created_at  = meeting.get("created_at", "")
    date_str    = created_at[:10] if created_at else datetime.now().strftime("%Y-%m-%d")
    url         = meeting.get("url", "")
    participants = _participants(meeting)
    participants_str = ", ".join(participants) if participants else "Unknown"

    summary_md  = (meeting.get("default_summary") or {}).get("markdown_formatted") or ""
    action_md   = _format_action_items(meeting.get("action_items") or [])
    transcript  = _format_transcript(meeting.get("transcript") or [])

    try:
        dt = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        display_date = dt.strftime("%B %-d, %Y")
    except Exception:
        display_date = date_str

    tags_yaml = "[fathom, meeting]"

    note = f"""---
title: {title}
date: {date_str}
participants: [{participants_str}]
source: fathom
type: meeting
url: {url}
tags: {tags_yaml}
---

# {title}
**Date:** {display_date}
**Participants:** {participants_str}
**Recording:** [View on Fathom]({url})

---

## Summary

{summary_md or '_No summary available._'}

---

## Action Items

{action_md or '_No action items._'}

---

## Transcript

{transcript or '_Transcript not available._'}
"""
    return note.strip()


def note_path(meeting: dict) -> Path:
    created_at = meeting.get("created_at", "")
    title = meeting.get("title") or meeting.get("meeting_title") or "Untitled Meeting"
    participants = _participants(meeting)

    try:
        dt = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
    except Exception:
        dt = datetime.now()

    year  = dt.strftime("%Y")
    month = MONTH_NAMES[dt.month]

    # Build participant slug (first two names, last name only)
    def last_name(n): return n.split()[-1] if n else n
    participant_slug = " & ".join(last_name(p) for p in participants[:2])

    safe_title = _slugify(title)[:60]
    filename   = f"{dt.strftime('%Y-%m-%d')} - {participant_slug} - {safe_title}.md"

    return OBSIDIAN_VAULT / "Fathom" / year / month / filename


# ── Main run function ─────────────────────────────────────────────────────────

def run(start_dt: datetime, end_dt: datetime, dry_run: bool = False) -> tuple[int, int, int]:
    written = skipped = errors = 0

    if not FATHOM_API_KEY:
        raise RuntimeError("FATHOM_API_KEY is not set")

    log.info("Fetching Fathom meetings %s → %s", start_dt.date(), end_dt.date())
    meetings = fetch_meetings(start_dt, end_dt)
    log.info("Found %d meeting(s)", len(meetings))

    for meeting in meetings:
        title = meeting.get("title") or "Untitled"
        path  = note_path(meeting)

        if path.exists():
            log.info("  SKIP (exists): %s", path.name)
            skipped += 1
            continue

        try:
            content = render_note(meeting)

            if dry_run:
                log.info("  [DRY] Would write: %s", path)
                written += 1
                continue

            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            log.info("  ✓ written: %s", path.name)
            written += 1

        except Exception as exc:
            log.error("  ✗ error on %s: %s", title, exc, exc_info=True)
            errors += 1

    return written, skipped, errors


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
