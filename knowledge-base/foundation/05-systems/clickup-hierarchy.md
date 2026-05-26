# ClickUp Hierarchy

Full nested structure of the Framework OPS command center. Built via API in Week 1 (see [[week-01-foundation]]).

## Workspace: Framework OPS

### Space 1: 🎯 Sales & Pipeline

**Folder: Leads & Outreach**
- List: Cold Outreach (Apollo/Clay sourced)
- List: Warm Network
- List: LinkedIn Inbound
- List: Referrals

**Folder: Active Pipeline**
- List: Discovery Calls Booked
- List: Audits in Progress
- List: Proposals Out
- List: Closed Won
- List: Closed Lost (with loss reason)

**Folder: Sales Assets**
- List: SOW Templates
- List: Sales Page Drafts
- List: Email Sequences
- List: Objection Handling Library

**Custom fields:** Company Name, Owner Name, Revenue Range, Sub-vertical, Source, Deal Stage, Expected Value, Close Probability %, Next Action, Next Action Date, Decision Maker Contact, Notes URL.

### Space 2: 📦 Client Delivery

**Folder: [TEMPLATE] Engagement** *(cloned per client via [[engagement-template-generator]])*
- List: Discovery & Onboarding
- List: Audit Phase
- List: Implementation Sessions
- List: SOPs to Build
- List: Automations to Build
- List: Action Items (client-facing)
- List: Internal Prep & Recaps
- List: Deliverables Tracker

**Folder: Active Clients**
- Subfolder per client (cloned from template)
- Currently: Lead Statement (Daniel)

**Folder: Past Clients** *(candidate to defer — empty until first engagement closes)*

**Custom fields:** Client, Session Number, Session Date, Status, Owner, Priority, Estimated Hours, Actual Hours, Blocked By, Deliverable Link, Recap Link.

### Space 3: 🛠 Product & SOPs

**Folder: SOP Library (Master)**
- List: Sales & Marketing SOPs
- List: Operations SOPs
- List: Finance & Admin SOPs
- List: HR & Hiring SOPs
- List: Customer Experience SOPs

**Folder: Automation Library**
- List: Workflows (combined N8N/Zapier/Make — split when 20+ automations)
- List: Build Specs & Documentation

**Folder: Productized Service Specs**
- List: OPS Assessment ($997)
- List: SOP Sprint ($1,500)
- List: Automation Build ($2,000)
- List: Retainers (Light / Active / Embedded)

**Custom fields:** SOP Status (Draft/Review/Published), Owner, Last Updated, Vertical Applicability, Linked Automations, Reusability Score 1-5.

### Space 4: 📣 Marketing & Content

**Folder: Content Calendar**
- List: LinkedIn Posts (Drafted)
- List: LinkedIn Posts (Scheduled)
- List: LinkedIn Posts (Published)
- List: Long-form (Blog/Newsletter)
- List: Case Studies

**Folder: Content Assets**
- List: Hooks Library
- List: Story Bank (operator anecdotes)
- List: Data & Stats Library
- List: Screenshots & Visuals

**Folder: Audience & Engagement**
- List: ICP Target List (150 companies)
- List: Engagement Targets (people to build relationship with)
- List: Saved Inspiration Posts

**Custom fields:** Post Date, Status, Angle (Build-in-public / Operator POV / Tactical / Case Study), Hook, Body URL, Engagement Count, Comments Count, Leads Generated, Repurpose Plan.

### Space 5: 💼 Framework OPS (Internal)

**Folder: Financials**
- List: Revenue Tracking (synced from Stripe/Mercury via Zapier)
- List: Expenses
- List: Tax & Compliance
- List: Monthly Close Tasks

**Folder: Goals & OKRs**
- List: 2026 Annual Goals
- List: Quarterly OKRs
- List: Weekly Priorities

**Folder: Admin**
- List: Vendor Management
- List: Subscriptions & Tools
- List: Legal & Insurance
- List: Personal Productivity / Inbox Zero

### Space 6: 🧠 Knowledge Base ⚠️ *Candidate to defer*

Originally planned but likely better served by Notion or Drive folder. Decide before building.

If kept:
- Folder: Frameworks (Yours) — Audit Methodology, Onboarding Playbook, Scope Management Playbook, Pricing Decision Tree
- Folder: Industry Research — Home Services Vertical Notes, Competitor Tracking, Tool Evaluations
- Folder: Reference — Books/Courses/Podcasts, Key Concepts, Useful Prompts

## Build approach

**Build via API** — Python or Node script that takes JSON config and pushes via ClickUp API.

**Why:**
1. Reproducibility (this script = 60% of engagement template generator)
2. Version control (structure in GitHub)
3. Speed (5-10 min vs 4-6 hrs manual)

**ClickUp API endpoints used:**
- `POST /team/{team_id}/space` — create spaces
- `POST /space/{space_id}/folder` — create folders
- `POST /folder/{folder_id}/list` — create lists in folders
- `POST /space/{space_id}/list` — folderless lists
- `POST /list/{list_id}/field` — custom fields
- `POST /space/{space_id}/template/{template_id}` — clone templates

**Manual polish required:**
- Dashboard widget configuration
- Some view configurations (Gantt, Timeline tweaks)
- Permissions and sharing

Allocate 60-90 min for manual polish after script runs.

## Related files
- [[engagement-template-generator]]
- [[week-01-foundation]]
- [[tech-stack]]
