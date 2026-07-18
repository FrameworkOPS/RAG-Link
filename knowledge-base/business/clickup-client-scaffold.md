---
type: business
tags: [clickup, scaffold, client-management, sop, engagement]
last_updated: 2026-05-14
---

# ClickUp Client Scaffold

The repeatable structure applied to every Framework OPS client engagement in ClickUp. One folder per client. Lists by engagement stage. Custom fields for hours, phase, problem area, and deliverable type. Universal scaffold — scoped down per tier, not duplicated per tier.

This doc is the source of truth. The `_TEMPLATE — New Client` folder in ClickUp must mirror this exactly. If the structure changes, update this doc first, then update the template.

---

## 1. Why a Scaffold Exists

Three reasons. First, every client engagement runs through the same six-stage process documented in `engagement-process.md` — the scaffold makes that process executable instead of aspirational. Second, hour budgets are tier-bound (Light 8–12, Active 15–20, Embedded 30–40 monthly) and overrun kills retainer profit — the scaffold tracks hours at the task level so overrun shows up in week 2, not month 3. Third, monthly client reporting is required per `engagement-process.md` Stage 6 — the scaffold's tagging structure produces that report from filters, not from memory.

A solo practice cannot afford to rebuild project structure for every new client. The scaffold is applied once via Folder Template, then customized.

---

## 2. Hierarchy

```
Workspace
└── Space: "Clients"                          ← all client work lives here
    ├── _TEMPLATE — New Client                ← saved as Folder Template, never modified directly
    ├── [Client Name] — [Tier]                ← e.g., "Daniel Construction — Active"
    │   ├── 0 — Pre-Engagement
    │   ├── 1 — Discovery & Diagnostic
    │   ├── 2 — Onboarding (Days 1–30)
    │   ├── 3 — Quick Wins (Days 31–60)
    │   ├── 4 — 90-Day Review & Roadmap
    │   ├── 5 — Ongoing Retainer
    │   ├── 6 — Meetings & Notes
    │   └── 7 — Reference & Deliverables
    └── [Next Client] — [Tier]
```

A separate Space called "Framework OPS — Internal" holds business-development work (LinkedIn pipeline, prospect tracking, internal SOPs). Client work and internal work do not mix in the same Space — filtering and reporting break if they do.

### Folder naming convention

`[Client Short Name] — [Tier]`

Examples: `Daniel Construction — Active`, `Smith HVAC — Light`, `Apex Roofing — Sprint (SOP)`, `Rodriguez Plumbing — OPS Assessment`.

The tier in the name is intentional. When scanning the Space sidebar, you see at a glance who's on what commitment level. Update the tier in the folder name when a client upgrades or downgrades.

---

## 3. The Eight Lists

Lists map to the six stages in `engagement-process.md` plus two utility lists. Stage lists are sequential — work moves through them, then settles into Ongoing Retainer for the long tail of the engagement.

### List 0 — Pre-Engagement
**Purpose:** Pre-sale work that doesn't yet have a signed agreement. Tasks: discovery call prep, intake form sent, intake form returned, diagnostic scheduled, proposal drafted, proposal sent, proposal follow-up.

**When the folder gets created:** As soon as discovery call is scheduled. The folder exists during the sales cycle, not just after signing.

**When this list closes out:** Day of signed agreement + first month payment received. Tasks here are then archived (set to Closed status, not deleted).

### List 1 — Discovery & Diagnostic
**Purpose:** Stages 1–3 from `engagement-process.md`. Tasks: discovery call notes, intake form review, diagnostic session, document review (P&L, FSM, org chart), diagnostic summary written, debrief call.

**When this list closes out:** Diagnostic summary delivered.

### List 2 — Onboarding (Days 1–30)
**Purpose:** Everything in `onboarding-checklist.md` that runs in Month 1. Tasks: signed agreement filed, payment received in QBO, kickoff call held, access gathered (QBO, FSM, payroll, bank, calendar, Slack), financial baseline pulled, operational baseline documented, KPI dashboard built, cash flow model built (if relevant), first quick win delivered, 30-day summary sent.

**When this list closes out:** Day 30 summary sent to client.

### List 3 — Quick Wins (Days 31–60)
**Purpose:** Days 31–60 implementation. Tasks: 2–3 implementable changes selected, executed, results measured. Specific named SOPs, automations, or process changes.

**When this list closes out:** Day 60. Anything not done rolls to Ongoing Retainer.

### List 4 — 90-Day Review & Roadmap
**Purpose:** The 90-day review per `engagement-process.md` Stage 6. Tasks: progress vs. initial priorities written, updated KPI snapshot, next-90-day roadmap drafted, renewal conversation held (if 3-month initial term), updated agreement signed if applicable.

**When this list closes out:** 90-day review meeting held + roadmap accepted.

### List 5 — Ongoing Retainer
**Purpose:** The long tail. Where most retainer hours actually get spent (months 4 through end of engagement). Tasks created weekly or per session: SOP development, automation builds, KPI reviews, AR aging reviews, monthly summaries, ad-hoc requests.

**Behavior:** This list never closes out until the engagement ends. Recurring tasks (weekly working session, monthly summary, monthly KPI review) live here as recurring tasks.

### List 6 — Meetings & Notes
**Purpose:** Every working session, kickoff, 30/60/90 review, and ad-hoc call. One task per meeting, named `YYYY-MM-DD — [Meeting type]`. Description holds the agenda before and notes after.

**Why a separate list:** Keeps the operational lists focused on deliverables. Meeting tasks become the audit trail when a client asks "what did we cover in March?"

### List 7 — Reference & Deliverables
**Purpose:** Permanent reference for this client only. Tasks here aren't action items — they're parking spots for things that need to live somewhere. Examples: client tech stack inventory, key contacts, login locations (the secret itself goes in 1Password — this just notes that 1Password has it), final SOPs delivered, final dashboards delivered, contract on file.

**Behavior:** Tasks here usually stay in a single status ("Reference") and don't move.

---

## 4. Statuses

Folder-level status set, applied to every list. Five statuses, no more. Long status sets get ignored.

| Status | Meaning | Color convention |
|---|---|---|
| **To Do** | Identified, not started | Gray |
| **In Progress** | Actively being worked this week | Blue |
| **Waiting on Client** | Blocked pending client action (access, decision, document) | Yellow |
| **Done** | Delivered or completed | Green |
| **Closed / Archived** | Closed out at end of stage, kept for record | Dark gray |

**The "Waiting on Client" status is non-negotiable.** It's the single most useful filter in a fractional COO practice. Pull a Waiting-on-Client view across all clients every Monday morning — that's your follow-up list.

---

## 5. Custom Fields (Folder-Level)

These four fields apply to every task in every client folder. They produce the reporting that justifies the retainer.

### Field 1 — Engagement Phase (Dropdown)
Options: `Pre-Engagement`, `Discovery & Diagnostic`, `Onboarding`, `Quick Wins`, `90-Day Review`, `Ongoing Retainer`, `Off-Scope`.

**Why:** A task lives in a list (e.g., "Onboarding") but the actual work might support a different phase (e.g., a quick win started during onboarding). The phase field captures intent; the list captures location. Filter across folders by phase to see "every active client's Quick Wins right now."

### Field 2 — Estimated Hours (Number) and Actual Hours (Number)
Two separate fields.

**Why:** Active retainer is 15–20 hrs/month. If estimated hours sum past 20 in a given month, you've over-scoped. If actual exceeds estimated by 25%+ on most tasks, your scoping is broken. Both data points are needed monthly to either (a) renegotiate scope, (b) push back on the client, or (c) tighten estimating.

**Rule:** Every task gets an Estimated Hours value at creation, even if it's a guess. Actual Hours updated when task moves to Done.

### Field 3 — Problem Area (Dropdown)
Options pulled from `home-service-common-problems.md`:

1. Scheduling & Dispatch Chaos
2. No SOPs
3. Poor Cash Flow Visibility
4. No KPI Tracking
5. High Field Turnover
6. Owner Bottleneck
7. Inconsistent Sales Process
8. Uncontrolled Job Costs
9. No Recruiting/Hiring System
10. Tech Sprawl or Avoidance
11. Other (free-text in description)

**Why:** Monthly summary writes itself. "This month: 8 hrs against Owner Bottleneck (delegation infrastructure), 5 hrs against Job Costs (per-job margin tracking), 4 hrs against No SOPs (dispatch, closeout, complaint handling)." That's the report. Without this field, you reconstruct it from memory every month.

### Field 4 — Deliverable Type (Dropdown)
Options: `SOP`, `Automation`, `KPI / Dashboard`, `Analysis / Report`, `Meeting`, `Training`, `Coaching`, `Admin`, `Other`.

**Why:** End-of-engagement asset list. Client asks "what did I get for $24K over six months?" Filter Deliverable Type ≠ Meeting/Admin and you have the artifact list.

---

## 6. Starter Task Set (Pre-Loaded in the Template)

Every new client folder, when applied from the template, comes with a fixed set of starter tasks. These are not aspirational — they are the work that runs on every engagement regardless of tier. Trim what doesn't apply for the tier; do not skip what does.

### List 0 — Pre-Engagement starter tasks
- Discovery call scheduled (Date/Time)
- Discovery call held — notes captured
- Pre-diagnostic intake form sent (Date)
- Pre-diagnostic intake form returned (Date)
- Diagnostic session scheduled
- Proposal drafted per `proposal-structure.md`
- Proposal delivered + walk-through scheduled
- Proposal decision (Date) — Won / Lost / Wait
- Agreement sent for signature
- First month payment received in Mercury / QBO

### List 1 — Discovery & Diagnostic starter tasks
- Discovery call notes filed
- Intake form findings summarized
- Diagnostic session held (90 min)
- P&L (last 12 months) reviewed
- FSM walkthrough completed
- Org chart documented
- Diagnostic summary written (1–2 pages)
- Diagnostic debrief call held

### List 2 — Onboarding (Days 1–30) starter tasks
- Signed agreement filed in client folder
- First month payment confirmed in QBO
- Recurring monthly invoice set up in QBO
- Kickoff call scheduled
- Kickoff call held
- QBO access received
- FSM/CRM access received
- Bank read access received (Mercury or client bank)
- Payroll access received
- Google Drive / shared folder access received
- Calendar access received
- Slack channel or comms tool set up
- 12-month P&L pulled
- Chart of accounts reviewed (issues flagged)
- Gross margin by service line calculated
- AR aging report pulled
- Cash balance + banking history reviewed
- FSM walkthrough — active jobs, dispatch, estimate flow
- Job costing data pulled (if available)
- As-is scheduling process documented
- Org chart documented (formal or informal)
- Key person dependencies identified
- KPI dashboard v1 built (8–12 metrics)
- Cash flow model built (if cash flow is a stated concern)
- First quick win identified
- First quick win delivered
- 30-day written summary sent to client
- 90-day roadmap draft shared

### List 3 — Quick Wins (Days 31–60) starter tasks
- 2–3 quick wins selected with client
- Quick win #1 — scope and execute
- Quick win #2 — scope and execute
- Quick win #3 — scope and execute (if applicable)
- Results measured and documented
- 60-day check-in held

### List 4 — 90-Day Review & Roadmap starter tasks
- Progress vs. initial priorities written
- Updated KPI snapshot pulled
- Next-90-day roadmap drafted
- 90-day review meeting held
- Roadmap accepted by owner
- Renewal conversation held (if 3-month initial term)
- Updated agreement signed if changing tier

### List 5 — Ongoing Retainer recurring tasks
- Weekly working session — recurring (per cadence in `service-tiers.md`)
- Monthly written summary — recurring, due last business day of month
- Monthly KPI review — recurring
- Quarterly business review — recurring every 90 days
- AR aging review — recurring monthly (if DSO is in scope)

### List 6 — Meetings & Notes
- Empty at template creation. Tasks added per meeting.

### List 7 — Reference & Deliverables starter tasks
- Tech stack inventory (this client)
- Key contacts list
- Login storage location reference (1Password vault name)
- Signed agreement on file (link to Drive)
- Diagnostic summary delivered (link)
- Final SOPs index (link)
- Final dashboards index (link)

---

## 7. Per-Tier Scope-Down Rules

The template is universal. Scope it down at folder creation, not by maintaining separate templates.

### OPS Assessment ($997, one-off)
Keep: Lists 0, 1, 7. Delete Lists 2, 3, 4, 5, 6 (or move 6 into Reference).

### Sprints (SOP, Automation, KPI Dashboard — $2,000 each)
Keep: Lists 0, 1, 2 (rename to "Sprint Execution"), 6, 7. Delete Lists 3, 4, 5. Hard close folder at sprint end.

### Advisory Retainer ($1,500/mo)
Keep all lists. List 5 (Ongoing Retainer) carries 2x monthly call recurring tasks only — no SOP/automation/KPI build tasks. Trim List 2 to access gathering + KPI dashboard review only (no build).

### Light Retainer ($2,500/mo)
Keep all lists. List 5 carries weekly call, monthly summary, monthly KPI review, 1 SOP/month, 1 automation/quarter. Cap monthly task estimated hours at 12.

### Active Retainer ($4,000/mo) — **default scaffold**
Keep all lists, all starter tasks. List 5 carries weekly call, monthly summary, monthly KPI review, 2–3 SOPs/month, 1–2 automations/quarter. Cap monthly task estimated hours at 20.

### Embedded Retainer ($6,000/mo)
Keep all lists. Add an additional list "8 — Manager Coaching" for 1:1 coaching tasks with the client's managers. List 5 carries 2x weekly call, monthly summary, monthly KPI review, full SOP library cadence, monthly automation, quarterly on-site. Cap monthly task estimated hours at 40.

---

## 8. Task Naming Conventions

Consistent naming makes filtering across clients work. Inconsistent naming makes the scaffold useless within 60 days.

- **Verb-first.** "Pull 12-month P&L" not "12-month P&L." "Build KPI dashboard v1" not "KPI dashboard."
- **Specific outputs.** "Document dispatch SOP" not "SOP work."
- **Meeting tasks:** `YYYY-MM-DD — [Type]`. Example: `2026-05-14 — Weekly working session` or `2026-05-21 — 90-day review`.
- **Recurring tasks:** prefix with `[Recurring]`. Example: `[Recurring] Monthly client summary`.
- **Quick wins:** prefix with `[Quick Win]`. Example: `[Quick Win] Activate review request automation`.
- **Deliverables to client:** prefix with `[Deliverable]`. Example: `[Deliverable] 30-day written summary`.

---

## 9. Folder Template Application Workflow

When a new client signs (or earlier — when a discovery call is booked, if you want pre-engagement tracked):

1. In ClickUp Space "Clients", apply Folder Template `_TEMPLATE — New Client`.
2. Rename the folder to `[Client Short Name] — [Tier]`.
3. Open List 0 (Pre-Engagement). Set due dates on the active starter tasks.
4. Apply the per-tier scope-down rules from Section 7. Delete or archive lists/tasks that don't apply.
5. Set Engagement Phase custom field on each surviving task.
6. Set Estimated Hours on every active task (best guess is fine — refine later).
7. In List 5, configure the weekly working session as recurring per the tier's cadence.
8. Add the client's Slack channel link and Drive folder link as task descriptions in List 7.
9. Take 5 minutes. The folder is ready.

This should take 15–20 minutes per new client. Anything longer means the template needs simplification or the per-tier scope-down rules aren't being followed.

---

## 10. Reporting Views to Build (One-Time Setup)

These views live at the Space level and pull across all client folders. Build them once after the template is in place:

- **All "Waiting on Client"** — filter status = Waiting on Client. Reviewed every Monday.
- **This Week — In Progress** — filter status = In Progress, due this week. Reviewed daily.
- **Hours by Client (this month)** — group by folder, sum Actual Hours custom field. Reviewed weekly to catch overrun before month-end.
- **Phase = Onboarding** — filter Engagement Phase = Onboarding. Shows which clients are in their first 30 days. Used for capacity planning.
- **Deliverables this month** — filter Deliverable Type ≠ Meeting/Admin/Other, Done date this month. The raw input for monthly client summaries.

---

## 11. What This Scaffold Doesn't Do

Naming the limits keeps expectations honest.

- **Does not replace `engagement-process.md` or `onboarding-checklist.md`.** Those are the process; this is the structure that holds the process. If they conflict, update both.
- **Does not handle CRM functions.** Pre-Engagement is for sale work already in motion (discovery scheduled+). Cold prospecting and pipeline tracking belong in a separate CRM (Pipedrive, HubSpot Free, or even a single ClickUp list in the Internal Space) — not duplicated per client.
- **Does not store client documents.** The scaffold links to where docs live (Drive, Notion, 1Password). It does not become the document repository — ClickUp is a worse Drive than Drive.
- **Does not auto-bill.** Recurring invoices live in QBO. The scaffold tracks delivery; QBO tracks payment.
- **Does not solve hour-overrun by itself.** The Estimated/Actual fields surface overrun; the human running the practice still has to act on it.

---

## 12. Maintenance Rules

- **Edit this doc first, then the template.** Template drift from doc means future Claude sessions will rebuild the wrong thing.
- **Review the template quarterly.** Three live engagements will reveal what's missing from the starter task set. Add it.
- **Don't add custom fields without removing one.** Field bloat kills adoption — including yours.
- **If a client asks for a different structure, the answer is no.** This is Framework OPS's operating system, not the client's. The client gets visibility (shared view), not structural control.
