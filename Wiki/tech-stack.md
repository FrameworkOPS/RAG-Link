---
title: Framework OPS Tech Stack
date: 2026-05-27
source: manual
type: wiki
tags: [tech-stack, tools, infrastructure, ai, automation, rag]
---

# Framework OPS Tech Stack

## Core Operations
| Tool | Purpose | Notes |
|------|---------|-------|
| **Mercury** | Business banking | Primary business account |
| **QuickBooks Online (QBO)** | Bookkeeping + invoicing | Connected via MCP for AI access |
| **ClickUp** | Project/task management | Connected via MCP; Workspace: Clients → Lead Statement → Trial → Ongoing Retainer |
| **Gmail** | Email | Connected via MCP for AI-assisted triage |
| **Google Calendar** | Scheduling | Connected via MCP |

## AI & Automation Infrastructure
| Tool | Purpose | Notes |
|------|---------|-------|
| **Supabase (pgvector)** | RAG knowledge base | Project: cnvvvxltuebymowemwpk; voyage-code-2 embeddings (1536-dim) |
| **Voyage AI** | Embeddings | Model: voyage-code-2; input_type: document |
| **Anthropic Claude** | AI assistant + automation | claude-haiku-4-5 for digests; claude-sonnet-4-6 for reasoning |
| **FastMCP** | RAG server for Claude Code | mcp_server.py connects Claude Code to Supabase RAG |
| **Claude in Cowork** | Daily operations assistant | This system — orchestrates tasks, writes files, runs code |

## Knowledge Management
| Tool | Purpose | Notes |
|------|---------|-------|
| **Obsidian** | Personal knowledge base | Vault at /Users/Skyright/Documents/Framework-OPS; obsidian-git plugin |
| **Fathom** | Meeting intelligence | Auto-records, transcribes, summarizes meetings; connected via MCP |
| **Fieldy** | Wearable AI note-taking | API: api.fieldy.ai; MCP endpoint: api.fieldy.ai/mcp; ingested into RAG + Obsidian daily |

## Communication
| Tool | Purpose | Notes |
|------|---------|-------|
| **Slack** | Team/client communication | Digest channel: #email-daily-digest (C0B5RN4JSE7); automated daily digests |

## Ingest Pipeline (RAG)
Located at `/Users/Skyright/Documents/Framework-OPS/ingest/` (and `/fieldy/ingest/`):
- `manual.py` — Manual document ingestion
- `fathom.py` — Meeting transcript ingestion from Fathom
- `clickup.py` — ClickUp task/doc ingestion
- `fieldy/ingest/fieldy.py` — Fieldy conversation ingestion (daily automated)
- `fieldy/obsidian/fieldy_to_obsidian.py` — Fieldy → Obsidian notes
- `fieldy/digest/fieldy_digest.py` — Daily Fieldy digest → Slack
- `fieldy/scheduled_fieldy.py` — Daily entry point (runs all three in sequence)
- `ingest/ingest_wikis.py` — Wiki document ingestion (this system)

## Client-Facing Tools (Skyright)
- EOS/L10 meeting facilitation tools
- KPI dashboards (QBO-integrated)
- Process documentation (SOPs)

## RAG Document Structure
```
documents table:
  id          uuid
  content     text          -- full chunk text
  embedding   vector(1536)  -- Voyage AI voyage-code-2
  metadata    jsonb         -- {repo, file, chunk_index, type, client, date, ...}
  source_type text          -- code | issue | pr | wiki | discussion | readme | meeting
  repo        text          -- e.g. framework-ops/wiki/company-profile
  created_at  timestamptz
```
