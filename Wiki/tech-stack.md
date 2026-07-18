---
title: Framework OPS Internal Tech Stack
date: 2026-05-27
source: manual
type: wiki
tags: [framework-ops, wiki, tech-stack, supabase, voyage, fathom, fieldy, clickup, obsidian, mcp, rag]
---

# Framework OPS Internal Tech Stack

This document covers the tools Framework OPS uses to run its own practice — not the tech stack recommendations for clients (see knowledge-base/playbooks/tech-stack-home-service.md for that).

---

## AI / RAG Infrastructure

### Supabase (pgvector RAG)
**Project ID:** cnvvvxltuebymowemwpk
**Role:** The knowledge base vector store. All Framework OPS documents — meeting transcripts, wiki pages, code, process documentation — are embedded and stored here as searchable vectors.

**Schema:** The `documents` table holds:
- `content` — the text chunk
- `embedding` — 1536-dimension vector (Voyage AI)
- `source_type` — one of: code, issue, pr, wiki, discussion, readme, meeting
- `repo` — logical namespace (e.g., `framework-ops/fathom-meetings`, `framework-ops/wiki`)
- `metadata` — JSON blob with fields like: `client`, `date`, `chunk_index`, `total_chunks`, `meeting_type`, `participants`, `tags`

**Current document counts (as of May 2026):**
- meeting: 460+ rows (Fathom meeting transcripts)
- code: 64 rows (from FrameworkOPS/RAG-Link repo)
- wiki: 0 (being built now — this wiki layer is the new addition)

### Voyage AI
**Model:** voyage-code-2
**Dimensions:** 1536
**Endpoint:** https://api.voyageai.com/v1/embeddings
**Input type:** `document` for indexing, `query` for retrieval
**Role:** Embedding model for all documents going into Supabase. voyage-code-2 is optimized for code-heavy and mixed technical/prose content — appropriate for a knowledge base that mixes meeting transcripts, SOPs, code, and markdown docs.

### FastMCP Server
**Role:** The MCP (Model Context Protocol) server that exposes the Supabase RAG to Claude and other AI clients. Framework OPS runs a FastMCP server built on top of the RAG Link repo. When Chance asks Claude a question, the MCP server retrieves relevant document chunks from Supabase and injects them as context.

**RAG Link repo:** FrameworkOPS/RAG-Link (on GitHub)
**Tech:** FastAPI + Supabase pgvector + Voyage AI embeddings
**Hosting:** TBD (Vercel likely for FastAPI backend)

---

## Knowledge Management

### Obsidian
**Vault location:** /Users/Skyright/Documents/Framework-OPS (the full repo root is the vault)
**Role:** Primary knowledge management system. All markdown files in knowledge-base/ are Obsidian notes. Wiki/, playbooks/, business/, clients/, meetings/ folders all render in Obsidian.

**Why Obsidian:** Bidirectional links ([[file-name]] syntax), graph view for understanding relationships between documents, local files (no vendor lock-in), and direct integration with the file system that the RAG ingest scripts can read.

**Frontmatter standard:** All wiki and KB files use YAML frontmatter:
```yaml
---
title: [title]
date: YYYY-MM-DD
source: manual
type: wiki
tags: [tag1, tag2, ...]
---
```

---

## Meeting Intelligence

### Fathom
**Role:** AI meeting recorder and summarizer. Fathom joins every client call and Zoom/Google Meet session, records it, transcribes it, and generates a structured summary.

**Integration with RAG:** Fathom meeting transcripts are ingested into Supabase as source_type='meeting' with metadata including client, date, meeting_type, participants, and tags. This means every client conversation is searchable in the RAG.

**Repos in Supabase:**
- `framework-ops/fathom-meetings` — the primary meeting transcript repo
- `framework-ops/meetings` — additional meeting notes

**Meeting metadata fields:** date, client, meeting_type, participants, recording_id, url, tags, chunk_index, total_chunks

### Fieldy (Wearable AI)
**Role:** Wearable AI device that captures ambient conversations and notes. Used for field context, ad-hoc capture, and situations where a laptop isn't available.

**Integration:** Fieldy output feeds into the same knowledge management workflow — transcripts can be formatted and ingested into Supabase or saved to the Obsidian vault as meeting notes.

---

## Project Management

### ClickUp
**Role:** Primary operating system for Framework OPS. Manages:
- Client engagement tasks and deliverables
- Weekly to-do items from L10 meetings
- Content calendar (LinkedIn post queue)
- Build plan execution (60-day launch roadmap)
- Per-client project spaces (see clickup-client-scaffold.md)

**ClickUp hierarchy:** Workspace → Spaces (per client or function) → Folders → Lists → Tasks

---

## Financial

### Mercury
**Role:** Business banking. All Framework OPS revenue (invoices, retainer payments) flows through Mercury. Mercury's API and data exports can be piped to QBO via automation.

**Why Mercury:** Clean UI, strong API, startup/startup-friendly banking, free ACH, solid integration with QBO and n8n/Zapier.

### QuickBooks Online (QBO)
**Role:** Bookkeeping. All income and expenses tracked in QBO. P&L, cash flow, and tax prep all run through QBO.

**Integration:** Mercury → QBO sync via Zapier (planned if not already live).

---

## Communication

### Gmail / Google Workspace
**Email:** chance@frameworkopsllc.com
**Role:** Primary email for client communication, invoicing, discovery call scheduling, and all external correspondence.
**Calendar:** Google Calendar (PT timezone) — all client sessions, discovery calls, and working sessions scheduled here.

### Slack
**Role:** Async team/client communication. Framework OPS uses Slack for internal workflow notifications and client channels where the client prefers Slack.
**Integrations planned:** ClickUp → Slack task notifications, Fathom → Slack recap delivery.

### Loom
**Role:** Async video for training content, client deliverable walkthroughs, SOPs that benefit from screen recording.

---

## Automation

### n8n
**Role:** Primary automation platform. Self-hosted or cloud. Used for:
- Complex multi-step workflows (Fathom transcript → format → Supabase ingest)
- AI-augmented workflows (meeting transcript → Claude API for summary → ClickUp task creation)
- Mercury → QBO sync
- Reporting pulls from FSM APIs for client dashboards

**Why n8n over Zapier:** Open source, self-hostable, no per-task pricing at scale, more powerful for complex flows. Chance builds the same for clients.

### Zapier
**Role:** Secondary automation for simple integrations. Used when n8n is overkill or when a client's stack has a Zapier-native connector that doesn't have an n8n equivalent.

---

## Development

### Claude / Claude Code
**Role:** AI assistant for the entire practice. Powers the RAG-backed assistant (via FastMCP), writes automation scripts, builds client tools, drafts content, and runs the Cowork workspace.

**Model used:** claude-sonnet-4-6 (current default)

### GitHub
**Repo:** FrameworkOPS/RAG-Link — the FastMCP + Supabase RAG server
**Version control** for all scripts, ingest pipelines, ClickUp configs, and tooling

### Vercel (planned)
**Role:** Hosting for any custom web tooling (FastAPI backend, potential client-facing dashboards)

---

## Tool Stack Map

```
Meeting capture:     Fathom / Fieldy
                     ↓
Transcript ingest:   n8n pipeline → Voyage AI (embed) → Supabase (store)
                     ↓
Knowledge base:      Obsidian vault (markdown) + Supabase (vectors)
                     ↓
AI retrieval:        FastMCP server → Claude (via Cowork)
                     ↓
Task management:     ClickUp (all actions, deliverables, client work)
                     ↓
Financial:           Mercury (banking) → QBO (bookkeeping) → n8n (sync)
                     ↓
Communication:       Gmail + Google Calendar + Slack + Loom
```

---

## Related Files
- Client tech stack recommendations: knowledge-base/playbooks/tech-stack-home-service.md
- Automation playbook (for clients): knowledge-base/playbooks/automation-playbook.md
- ClickUp structure: knowledge-base/business/clickup-client-scaffold.md
- RAG Link repo: FrameworkOPS/RAG-Link (GitHub)
