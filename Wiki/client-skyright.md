---
title: Client Profile — Skyright (Roofing)
date: 2026-05-27
source: manual
type: wiki
tags: [framework-ops, wiki, client, skyright, roofing, retainer, eos, l10]
---

# Client Profile: Skyright

## Overview

Skyright is a large roofing company and Framework OPS's highest-value active client. Chance Peare serves as fractional COO and is embedded in the company's leadership operations, running EOS/L10 meetings and driving operational systems work.

This is also the company where Chance is the full-time COO — making Skyright both the day-job employer and the highest-tier consulting engagement. Context: Framework OPS was built in parallel with Chance's COO role at Skyright. The engagement reflects the Embedded retainer model in practice.

## Engagement Details

- **Monthly retainer:** $8,000/month
- **Retainer tier:** Above the published Embedded tier — reflects the depth of involvement, on-site time, and full operational leadership scope
- **Engagement type:** Ongoing fractional/embedded COO
- **Industry:** Residential and commercial roofing
- **Company size:** Large (specific headcount not documented here — refer to meeting notes)

## What Chance Does at Skyright

### EOS / L10 Meeting Facilitation
Chance runs Level 10 (L10) meetings with the Skyright leadership team using the Entrepreneurial Operating System (EOS) framework. This includes:

- Weekly L10 meetings with the leadership/management team
- Maintaining the company Scorecard (KPIs tracked weekly: revenue, close rate, job completions, callbacks, AR balance, etc.)
- Managing the Rocks process (quarterly 90-day priorities for the company and each leader)
- Issues List (IDS: Identify, Discuss, Solve) — surfacing and resolving operational issues at the leadership level
- To-Do tracking (7-day action items owned by specific team members)

### Operational Systems
- Job costing and gross margin monitoring
- Cash flow management (13-week rolling cash flow model; see skyright-cashflow skill)
- Work-in-Progress (WIP) schedule management
- Subcontractor and crew performance tracking
- Dispatch and scheduling oversight
- P&L review and financial visibility for ownership

### Tech Stack and Automation
Skyright runs a complex operational stack for a large roofing company. Chance's role includes:
- FSM oversight (dispatch, job management, reporting)
- QBO integration and financial reporting
- Automation builds where applicable (lead follow-up, review requests, reporting)
- AI tooling evaluation and deployment

## Key Operational Priorities

For a large roofing company, the standard operational focus areas are:

1. **Gross margin protection** — benchmarks: 38–52% for residential re-roof; commercial lower (28–40%). Any decline is the first signal of systems failure.
2. **Cash flow** — roofing companies carry material float risk (7–21 days between PO and job revenue); draw schedules on commercial jobs; DSO management (benchmark: 15–35 days retail, 45–60 days insurance)
3. **Job costing discipline** — materials as % of job revenue (benchmark: 30–40%), labor as % (18–28%). Without clean job costing, gross margin numbers are fiction.
4. **Crew utilization** — benchmark: 75–85% utilization (days working vs. days available). Below 70% = scheduling or pipeline problem.
5. **Callbacks/quality** — benchmark: <2% of jobs as callbacks/warranty calls. Above 3% = installation quality problem.
6. **Key person dependencies** — large roofing companies are often dependent on 1–2 production managers or lead salespeople. Documenting their processes before turnover is critical.

## EOS L10 Meeting Structure at Skyright

A standard L10 meeting runs 90 minutes with a fixed agenda:

| Segment | Time | Purpose |
|---|---|---|
| Segue / good news | 5 min | Energy check, personal/professional good news |
| Scorecard review | 5 min | Review weekly KPIs — red vs. green, no discussion yet |
| Rock review | 5 min | Are Rocks on-track or off-track? |
| Customer/employee headlines | 5 min | Good news only on customers and employees |
| To-Do list review | 5 min | Did last week's 7-day actions get done? |
| IDS (Issues) | 60 min | The core — identify, discuss, solve the most important issues |
| Conclude | 5 min | Recap to-dos, cascading messages, rating the meeting |

The power is in the discipline. The same format, every week, no exceptions.

## Skyright Cash Flow Tool

A custom cash flow forecasting tool exists for Skyright — the `skyright-cashflow` skill in Cowork. This skill builds:
- A Work-in-Progress (WIP) schedule (active jobs, contract values, % complete, remaining revenue)
- A 13-week rolling cash flow forecast (weekly cash in/out, projected cash balance, low-water marks)
- Conservative projections by default — haircut AR collections, assume payroll runs on schedule, flag weeks below minimum cash floor

See the skyright-cashflow skill for the full methodology.

## Industry Context: Roofing Benchmarks

Key benchmarks Chance uses to evaluate Skyright's performance:

| Metric | Benchmark |
|---|---|
| Gross margin (residential re-roof) | 38–52% |
| Gross margin (commercial) | 28–40% |
| Net profit margin (well-run company) | 8–15% |
| Overhead as % of revenue | 18–28% |
| DSO (retail) | 15–35 days |
| DSO (insurance) | 45–60 days |
| Callbacks as % of jobs | <2% |
| Crew utilization | 75–85% |
| Revenue per salesperson | $800K–$1.5M/yr |
| Annual growth (healthy) | 15–30% |

## Related Files
- Meeting notes: knowledge-base/meetings/ (Fathom-ingested transcripts in RAG)
- Skyright cash flow skill: skyright-cashflow
- Roofing benchmarks: knowledge-base/playbooks/roofing-operations-benchmarks.md
- EOS/L10 framework: Wiki/eos-l10-framework.md
