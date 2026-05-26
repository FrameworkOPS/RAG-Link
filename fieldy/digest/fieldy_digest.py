"""
fieldy_digest.py — Generate a daily Fieldy digest and post to Slack

Summarises yesterday's conversations using Claude Haiku, posts formatted
digest to Slack channel C0B5RN4JSE7 (#email-daily-digest).

Env vars required:
    FIELDY_API_KEY      — Fieldy API key
    ANTHROPIC_API_KEY   — Claude API key
    SLACK_BOT_TOKEN     — Slack bot token (xoxb-...)
    SLACK_DIGEST_CHANNEL — (optional override, default: C0B5RN4JSE7)

Usage:
    python fieldy_digest.py                  # yesterday's conversations
    python fieldy_digest.py --hours 48       # last 48 hrs
    python fieldy_digest.py --dry-run        # print to terminal, skip Slack
"""

import os
import sys
import time
import logging
import argparse
from datetime import datetime, timedelta, timezone
from typing import Optional

import requests
import anthropic
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
)
log = logging.getLogger(__name__)

# ── Config ────────────────────────────────────────────────────────────────────
FIELDY_API_KEY    = os.environ["FIELDY_API_KEY"]
ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]
SLACK_BOT_TOKEN   = os.environ["SLACK_BOT_TOKEN"]
SLACK_CHANNEL     = os.environ.get("SLACK_DIGEST_CHANNEL", "C0B5RN4JSE7")

FIELDY_BASE       = "https://api.fieldy.ai/api/public/v2"
CLAUDE_MODEL      = "claude-haiku-4-5-20251001"
RATE_LIMIT_RPS    = 30
MIN_DELAY         = 60 / RATE_LIMIT_RPS

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

    while True:
        params = {
            "start_date": start_dt.isoformat(),
            "end_date":   end_dt.isoformat(),
            "per_page":   page_size,
            "page":       page,
        }
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


def fetch_open_tasks(days: int = 7) -> list[dict]:
    """Fetch open/pending tasks created in the last N days."""
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    try:
        data = _get("/tasks", params={
            "status":     "open",   # Fieldy may use open/pending/incomplete
            "start_date": cutoff.isoformat(),
        })
        items = data if isinstance(data, list) else (
            data.get("data") or data.get("tasks") or data.get("items") or []
        )
        # Filter client-side as a fallback in case API doesn't support status filter
        open_tasks = [
            t for t in items
            if _safe(t, "status", "state", default="open").lower()
            not in ("completed", "done", "closed")
        ]
        return open_tasks
    except Exception as exc:
        log.warning("Could not fetch tasks: %s", exc)
        return []


def fetch_transcript_text(conversation_id: str) -> str:
    """Return transcript as plain text for summarization."""
    try:
        data = _get("/transcriptions", params={"conversation_id": conversation_id})
        segments = (
            data if isinstance(data, list)
            else data.get("segments") or data.get("transcript") or data.get("transcription") or []
        )
        lines = []
        for seg in segments[:100]:   # cap at 100 segments to control token usage
            speaker = _safe(seg, "speaker", "speaker_name", "name", default="Unknown")
            text    = _safe(seg, "text", "content", "transcript", default="")
            lines.append(f"{speaker}: {text}")
        return "\n".join(lines)
    except Exception:
        return ""


# ── Claude summarization ──────────────────────────────────────────────────────
def _build_summary_prompt(conversations: list[dict], open_tasks: list[dict], date_str: str) -> str:
    conv_blocks = []
    for conv in conversations:
        title       = _safe(conv, "title", "name", default="Untitled")
        summary     = _safe(conv, "summary", "description", default="")
        participants = _safe(conv, "participants", "speakers", default=[])

        if isinstance(participants, list):
            names = [
                (p.get("name") or p.get("speaker") or str(p)) if isinstance(p, dict) else str(p)
                for p in participants
            ]
        else:
            names = [str(participants)]

        conv_id  = str(_safe(conv, "id", "conversation_id", "uuid", default=""))
        transcript_snippet = fetch_transcript_text(conv_id)[:1500] if conv_id else ""

        conv_blocks.append(f"""
CONVERSATION: {title}
Participants: {', '.join(names)}
Summary: {summary}
Transcript (excerpt):
{transcript_snippet}
""")

    task_blocks = []
    for task in open_tasks:
        t_title = _safe(task, "title", "name", "subject", default="Untitled task")
        t_due   = _safe(task, "due_date", "due", "deadline", default="")
        due_str = f" (due: {t_due})" if t_due else ""
        task_blocks.append(f"- {t_title}{due_str}")

    all_convs = "\n---\n".join(conv_blocks) if conv_blocks else "No conversations recorded."
    all_tasks = "\n".join(task_blocks) if task_blocks else "No open tasks."

    return f"""You are summarizing Chance's daily conversations captured by his Fieldy wearable AI device. Chance runs Framework OPS LLC, a fractional COO consulting practice targeting home service companies (roofing, HVAC, etc.). He is the COO of a large roofing company.

Today is {date_str}.

CONVERSATIONS FROM TODAY:
{all_convs}

OPEN TASKS (last 7 days):
{all_tasks}

Create a concise daily digest covering:
1. Key conversations and decisions made
2. Commitments made (by Chance or others)
3. Open action items with owners/due dates
4. People mentioned and context

Rules:
- Be direct, no fluff, no filler phrases
- Flag anything time-sensitive or high-stakes
- If you see patterns across conversations (same person, same topic), call them out
- Max 400 words total

Format your response as JSON with these exact keys:
{{
  "conversations": [{{"title": "...", "one_liner": "..."}}],
  "key_decisions": ["decision 1", "decision 2"],
  "open_tasks": [{{"task": "...", "owner": "...", "due": "..."}}],
  "people_mentioned": [{{"name": "...", "context": "..."}}],
  "flags": ["anything urgent or time-sensitive"]
}}"""


def summarize_with_claude(prompt: str) -> dict:
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    msg = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    raw = msg.content[0].text.strip()

    # Extract JSON from response (Claude may wrap in ```json)
    import json, re
    match = re.search(r"\{[\s\S]*\}", raw)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass

    # Fallback: return raw text in a structured wrapper
    log.warning("Could not parse Claude JSON response — using raw text")
    return {
        "conversations": [],
        "key_decisions": [raw],
        "open_tasks": [],
        "people_mentioned": [],
        "flags": [],
    }


# ── Slack formatting ──────────────────────────────────────────────────────────
def format_slack_message(digest: dict, conversations: list[dict], open_tasks: list[dict], date_str: str) -> list[dict]:
    """Build Slack Block Kit blocks for the digest."""
    blocks = []

    # Header
    blocks.append({
        "type": "header",
        "text": {"type": "plain_text", "text": f"📝 Fieldy Daily Digest — {date_str}"},
    })

    blocks.append({"type": "divider"})

    # Conversations
    conv_count = len(conversations)
    conv_items = digest.get("conversations") or []
    conv_lines = "\n".join(
        f"• *{c.get('title', 'Unknown')}* — {c.get('one_liner', '')}"
        for c in conv_items
    ) or "_No conversations recorded_"

    blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": f"*Conversations ({conv_count})*\n{conv_lines}",
        },
    })

    # Key Decisions
    decisions = digest.get("key_decisions") or []
    if decisions:
        decision_lines = "\n".join(f"• {d}" for d in decisions)
        blocks.append({
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"*Key Decisions*\n{decision_lines}"},
        })

    blocks.append({"type": "divider"})

    # Open Tasks
    task_count = len(open_tasks)
    task_items = digest.get("open_tasks") or []
    if task_items:
        task_lines = "\n".join(
            f"• {t.get('task', 'Unknown')} "
            + (f"→ {t.get('owner', '')}" if t.get("owner") else "")
            + (f" 📅 {t.get('due', '')}" if t.get("due") else "")
            for t in task_items
        )
    else:
        task_lines = "_No open tasks_"

    blocks.append({
        "type": "section",
        "text": {"type": "mrkdwn", "text": f"*Open Tasks ({task_count})*\n{task_lines}"},
    })

    # People Mentioned
    people = digest.get("people_mentioned") or []
    if people:
        people_lines = "\n".join(
            f"• *{p.get('name', '?')}* — {p.get('context', '')}"
            for p in people
        )
        blocks.append({
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"*People Mentioned*\n{people_lines}"},
        })

    # Flags / Urgent items
    flags = digest.get("flags") or []
    if flags:
        flag_lines = "\n".join(f"⚠️ {f}" for f in flags)
        blocks.append({
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"*Flags*\n{flag_lines}"},
        })

    blocks.append({"type": "divider"})
    blocks.append({
        "type": "context",
        "elements": [{"type": "mrkdwn", "text": "_Generated by Fieldy + Framework OPS automation_"}],
    })

    return blocks


def post_to_slack(blocks: list[dict], date_str: str, dry_run: bool = False):
    fallback_text = f"📝 Fieldy Daily Digest — {date_str}"

    if dry_run:
        import json
        print("\n" + "=" * 60)
        print(f"[DRY RUN] Would post to Slack channel {SLACK_CHANNEL}")
        print(json.dumps(blocks, indent=2))
        return

    client = WebClient(token=SLACK_BOT_TOKEN)
    try:
        client.chat_postMessage(
            channel=SLACK_CHANNEL,
            text=fallback_text,
            blocks=blocks,
        )
        log.info("Digest posted to Slack channel %s", SLACK_CHANNEL)
    except SlackApiError as exc:
        log.error("Slack API error: %s", exc.response["error"])
        raise


# ── Main ──────────────────────────────────────────────────────────────────────
def run(start_dt: datetime, end_dt: datetime, dry_run: bool = False):
    date_str = start_dt.strftime("%B %d, %Y")
    log.info("Generating Fieldy digest for %s", date_str)

    conversations = fetch_conversations(start_dt, end_dt)
    log.info("Found %d conversations", len(conversations))

    open_tasks = fetch_open_tasks(days=7)
    log.info("Found %d open tasks", len(open_tasks))

    if not conversations and not open_tasks:
        log.info("Nothing to digest — skipping Slack post")
        return

    prompt = _build_summary_prompt(conversations, open_tasks, date_str)
    log.info("Summarizing with Claude Haiku...")
    digest = summarize_with_claude(prompt)

    blocks = format_slack_message(digest, conversations, open_tasks, date_str)
    post_to_slack(blocks, date_str, dry_run=dry_run)

    log.info("Digest complete")


def parse_args():
    parser = argparse.ArgumentParser(description="Post Fieldy daily digest to Slack")
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

    run(start_dt, end_dt, dry_run=args.dry_run)
