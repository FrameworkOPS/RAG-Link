---
name: buffer-performance-scraper
description: Scrape Buffer recap emails from Gmail, pull post text from Buffer API, score and rank posts by engagement, identify what content patterns are working, and write findings into the LinkedIn content skill's voice profile. Trigger with "analyze my buffer performance", "what's performing", "scrape my buffer emails", "what posts are working", or "update the voice profile with performance data".
---

# Buffer Performance Scraper — Framework OPS

This skill pulls real engagement data from Buffer's daily recap emails in Gmail, cross-references it against full post text from the Buffer API, scores and ranks posts, identifies what's working, and writes the findings into the LinkedIn content skill's voice profile so future batches are informed by actual results.

**Key constraint:** Buffer's email metrics are captured within 24 hours of publishing. Until the LinkedIn audience grows beyond ~500-1,000 followers, most posts will show 0 comments / 0 reactions. The scraper still runs and builds a ranked list from whatever data exists — it just gets sharper over time.

---

## Step 1 — Pull all Buffer recap emails from Gmail

Search Gmail for every Buffer daily recap email:

```
from:hello@buffermail.com subject:"daily recap"
```

Use `search_threads` with `pageSize: 50`. If `hasNextPage` is true, paginate with the returned cursor until you have all threads.

For each thread, call `get_thread` with `messageFormat: FULL_CONTENT`. From the HTML body, extract:

- **Date** of the recap (parse from the email body header, e.g., "Thursday 28 May 2026" → 2026-05-28)
- **Post snippet** (the truncated post text shown in the email — typically 140 chars)
- **Comments count** (integer after "Comments" label)
- **Reactions count** (integer after "Reactions" label)

Parse with a regex or string scan pattern like: look for the pattern `Post published Comments Reactions [N] [N] [N]` where first N = posts published, second N = comments, third N = reactions. The numbers appear as plain text between the HTML-stripped spans.

Build a list of email records:
```
{
  date: "2026-05-28",
  snippet: "Another solid week. The guys executed...",
  comments: 0,
  reactions: 0,
  email_score: 0  # comments*5 + reactions*1
}
```

---

## Step 2 — Pull all sent posts from Buffer API

Call `list_posts` with:
- `organizationId: 69ffb7b73e4597b26fe3af37`
- `channelId: 69ffb8205c4c051afa2bdfda`
- `status: ["sent"]`

Paginate through all pages until `hasNextPage` is false. Build a list of post records:
```
{
  id: "...",
  sent_date: "2026-05-27",   # date portion of sentAt
  text: "... full post text ...",
  word_count: N,
  linkedin_url: externalLink
}
```

---

## Step 3 — Match emails to posts by date

For each email record, find the Buffer post whose `sent_date` matches the email's `date`. LinkedIn posts go out on a specific day; the recap email covers that same UTC day. One email = one post (Buffer sends one recap per day per channel).

If a post has no matching email (no recap was sent), assign `comments: 0, reactions: 0`.

Build a unified **post performance table**:

| Rank | Date | Score | Comments | Reactions | Words | Text Preview (50 chars) |
|------|------|-------|----------|-----------|-------|------------------------|
| 1    | ...  | ...   | ...      | ...       | ...   | ...                    |

Scoring formula: `score = (comments × 5) + (reactions × 1)`

Rank descending. Ties broken by word count descending (longer educational posts win ties — they tend to perform better on LinkedIn for this ICP).

---

## Step 4 — Analyze content patterns in top performers

Take the top 5 scoring posts (or all posts if fewer than 5 total). For each, classify:

**Post format:**
- `one-liner bundle` — 3 or fewer sentences, punchy observation
- `short tactical` — 4–10 lines, one concrete point
- `long-form teardown` — 11+ lines, full process breakdown

**Topic bucket** (pick one):
- `job costing / financials` — cash flow, AR, WIP, margins, collections
- `operations / systems` — SOPs, crew management, delegation, documentation
- `estimating / scope` — bid accuracy, change orders, scope creep
- `leadership / hiring` — team building, culture, owner-operator mindset
- `tech / automation` — software, FSM, AI tools, integrations
- `field story` — real-world crew/job vignettes with a lesson

**Opening style:**
- `concrete observation` — starts with a statement of fact or situation
- `diagnostic framing` — names the problem the reader has
- `question` — opens with a question (generally performs worse per voice profile)

**Closing style:**
- `soft CTA` — implies the problem is fixable with the right help
- `no CTA` — ends on the insight
- `hard sell` — avoid (voice profile bans this)

---

## Step 5 — Write findings to the voice profile

Read `/Users/Skyright/Documents/Framework-OPS/linkedin-content/voice-profile.md`.

If the file doesn't exist yet, check the bundled seed at `/var/folders/62/013gnsjs22v1664bvtfps3f40000gp/T/claude-hostloop-plugins/618fe07ca93f92f8/skills/linkedin-content/references/voice-profile.md`, copy it to the canonical path, then proceed.

Find the `## What resonates` section (create it if missing). Append a dated performance update block:

```markdown
### Performance update — [DATE RUN]

**Data window:** [first post date] → [last post date] ([N] posts, [N] with email engagement data)

**Top-performing posts by score:**
1. [date] · Score [N] ([comments]c / [reactions]r) · [format] · [topic] · "[50-char preview]"
2. ...
3. ...

**Pattern observations:**
- [Format that's winning, e.g., "Long-form teardowns (150+ words) are outperforming one-liners 3:1 by reactions"]
- [Topic that's winning, e.g., "Job costing / financials posts average 2.1 reactions vs 0.4 for field stories"]
- [Opening style that's winning, e.g., "Posts opening with a diagnostic statement outperform question openers"]
- [Closing style, e.g., "Soft CTA posts average N reactions vs N for no-CTA posts"]

**Recommended batch weighting for next 2 weeks:**
- [Topic A]: 2 of 4 posts
- [Topic B]: 1 of 4 posts
- [Topic C]: 1 of 4 posts

**Data quality note:** [If most posts show 0 engagement, say: "Engagement counts are pre-audience-scale — rankings are based on [N] posts with nonzero data. Pattern analysis is more reliable than absolute scores at this stage."]
```

Save the updated voice profile.

---

## Step 6 — Present findings and offer to generate content

After writing the voice profile, present a brief summary to Chance:

- Total posts analyzed
- Top 3 posts by score with their previews
- The 2–3 most actionable pattern observations
- Caveat on data quality if relevant

Then ask: "Want me to run the LinkedIn content skill now using these insights?"

If yes, invoke the `linkedin-content` skill. It will read the updated voice profile and already have the performance data baked in.

---

## IDs reference (stable unless reconnected)

- Buffer organization ID: `69ffb7b73e4597b26fe3af37`
- LinkedIn channel ID: `69ffb8205c4c051afa2bdfda`
- Gmail sender to search: `hello@buffermail.com`

---

## Running on a schedule

This skill can be set up to run automatically weekly (e.g., every Monday) via `mcp__scheduled-tasks__create_scheduled_task`. If requested, create a task with the cron expression `0 9 * * 1` (9am Monday) that triggers this skill and writes findings to the voice profile. The LinkedIn content skill then gets smarter each week without manual effort.
