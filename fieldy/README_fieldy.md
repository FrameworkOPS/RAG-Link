# Fieldy Integration — Framework OPS

Automated pipeline: **Fieldy wearable → RAG (Supabase) + Obsidian + Slack digest**

---

## What This Does

| Script | What it does |
|--------|-------------|
| `ingest/fieldy.py` | Pulls conversations from Fieldy API, embeds them (OpenAI), stores in Supabase pgvector for RAG |
| `obsidian/fieldy_to_obsidian.py` | Creates one Obsidian note per conversation in `/Users/Skyright/Documents/Framework-OPS/Fieldy/` |
| `digest/fieldy_digest.py` | Summarises conversations with Claude Haiku, posts daily digest to Slack `#email-daily-digest` |
| `scheduled_fieldy.py` | Single entry point that runs all three in sequence |

---

## Prerequisites

- Python 3.10+
- Supabase project with `pgvector` extension enabled and a `documents` table (same as your existing RAG pipeline)
- Slack bot with `chat:write` scope installed to your workspace
- Anthropic API key
- OpenAI API key

---

## Setup

### 1. Install dependencies

```bash
cd /path/to/fieldy
pip install -r requirements_fieldy.txt
```

### 2. Configure environment variables

```bash
cp .env.example .env
# Edit .env with your actual keys
```

Required vars:

| Variable | Used by | Notes |
|----------|---------|-------|
| `FIELDY_API_KEY` | all scripts | Your Fieldy API key |
| `SUPABASE_URL` | ingest | `https://xxxx.supabase.co` |
| `SUPABASE_KEY` | ingest | Service role key |
| `OPENAI_API_KEY` | ingest | For `text-embedding-3-small` |
| `ANTHROPIC_API_KEY` | digest | Claude Haiku for summarization |
| `SLACK_BOT_TOKEN` | digest | `xoxb-...` |
| `SLACK_DIGEST_CHANNEL` | digest | Default: `C0B5RN4JSE7` |
| `OBSIDIAN_VAULT_PATH` | obsidian | Default: `/Users/Skyright/Documents/Framework-OPS` |

### 3. Verify Supabase table exists

Your existing RAG pipeline uses a `documents` table. Confirm it has these columns:

```sql
-- If table doesn't exist yet:
create extension if not exists vector;

create table documents (
  id bigserial primary key,
  content text,
  embedding vector(1536),
  metadata jsonb
);

create index on documents using ivfflat (embedding vector_cosine_ops);
```

---

## Running Manually

### Full pipeline (all three steps)
```bash
python scheduled_fieldy.py
```

### Individual scripts
```bash
# RAG ingestion only
python ingest/fieldy.py

# Obsidian sync only
python obsidian/fieldy_to_obsidian.py

# Slack digest only
python digest/fieldy_digest.py
```

### Custom date range
```bash
python scheduled_fieldy.py --start 2026-05-01 --end 2026-05-26

# Last 48 hours
python scheduled_fieldy.py --hours 48
```

### Dry run (no writes, prints output)
```bash
python scheduled_fieldy.py --dry-run
```

### Skip individual steps
```bash
python scheduled_fieldy.py --skip-ingest --skip-obsidian   # digest only
python scheduled_fieldy.py --skip-digest                   # no Slack post
```

---

## Scheduling (Daily at 6 AM)

### macOS cron
```bash
crontab -e
```
Add:
```
0 6 * * * cd /path/to/fieldy && /usr/local/bin/python3 scheduled_fieldy.py >> /tmp/fieldy_daily.log 2>&1
```

### macOS LaunchAgent (more reliable than cron on Mac)
Create `~/Library/LaunchAgents/com.frameworkops.fieldy.plist`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.frameworkops.fieldy</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/python3</string>
        <string>/path/to/fieldy/scheduled_fieldy.py</string>
    </array>
    <key>WorkingDirectory</key>
    <string>/path/to/fieldy</string>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>6</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>/tmp/fieldy_daily.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/fieldy_daily_err.log</string>
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/usr/local/bin:/usr/bin:/bin</string>
    </dict>
</dict>
</plist>
```
Load it:
```bash
launchctl load ~/Library/LaunchAgents/com.frameworkops.fieldy.plist
```

---

## Adding Fieldy MCP to Claude Desktop

This lets you query Fieldy conversations directly in Claude Desktop chat.

Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "fieldy": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-fetch"],
      "env": {
        "FETCH_HEADERS": "{\"Authorization\": \"Bearer sk-f-your-key-here\"}"
      }
    }
  }
}
```

Or if Fieldy provides a native MCP server:

```json
{
  "mcpServers": {
    "fieldy": {
      "url": "https://api.fieldy.ai/mcp",
      "headers": {
        "Authorization": "Bearer sk-f-your-key-here"
      }
    }
  }
}
```

Restart Claude Desktop after editing. You'll see Fieldy tools available in the tool panel.

---

## Obsidian Notes Structure

Notes are saved to your existing vault at:
```
/Users/Skyright/Documents/Framework-OPS/
└── Fieldy/
    └── 2026/
        └── 05-May/
            ├── 2026-05-26 - Roofing Company Q2 Review.md
            ├── 2026-05-26 - Client Onboarding Call.md
            └── ...
```

obsidian-git is already installed in your vault, so notes will auto-sync on your configured commit interval.

Each note includes full YAML frontmatter (title, date, participants, keywords, tasks, source) making them queryable via Dataview if you use that plugin.

---

## Troubleshooting

**API auth errors**: Verify `FIELDY_API_KEY` starts with `sk-f-` and hasn't expired.

**Field name mismatches**: The scripts use `.get()` with fallback keys for common field name variants. If Fieldy's API returns unexpected field names, check the raw response with:
```bash
python3 -c "
import requests, json, os
from dotenv import load_dotenv
load_dotenv()
r = requests.get(
    'https://api.fieldy.ai/api/public/v2/conversations?limit=1',
    headers={'Authorization': f'Bearer {os.environ[\"FIELDY_API_KEY\"]}'}
)
print(json.dumps(r.json(), indent=2))
"
```
Then update the `_safe(conv, ...)` calls in the scripts with the correct field names.

**Supabase embedding errors**: Confirm your `documents` table uses `vector(1536)` — that's the dimension for `text-embedding-3-small`.

**Slack errors**: Bot needs `chat:write` scope. Confirm the bot is added to channel `C0B5RN4JSE7`.
