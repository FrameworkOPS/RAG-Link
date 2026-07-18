# Framework OPS Knowledge Base

**Owner:** Chance Peare
**Last updated:** May 2026
**Purpose:** RAG knowledge base for AI tools (Claude, Claude Code, custom agents) to retrieve relevant context when assisting with Framework OPS work.

## Structure

Files are organized by domain. Each file is self-contained but cross-references related files via wiki-style links: `[[filename]]`.

### 01-operator/
Personal context — who Chance is, preferences, working style.
- [[operator-profile]] — background, credentials, communication preferences
- [[work-capacity]] — available hours, current commitments, energy management

### 02-business-model/
The business itself — ICP, offers, pricing, revenue targets.
- [[icp-definition]] — target customer profile
- [[offer-ladder]] — all 6 productized services with full specs
- [[pricing-strategy]] — pricing rationale, increase triggers, anchoring risks
- [[revenue-targets]] — 2026/2027 goals with realistic projections
- [[contract-requirements]] — mandatory clauses (case studies, scope mgmt)

### 03-current-state/
Snapshot of where Framework OPS is right now.
- [[active-clients]] — current engagements (Daniel @ Lead Statement)
- [[website-status]] — frameworkopsllc.com state and pending changes
- [[linkedin-status]] — followers, posting cadence, content strategy
- [[tech-stack]] — tools in use across the business

### 04-build-plan/
The 60-day plan to outreach launch (July 5, 2026).
- [[60-day-overview]] — weekly milestones summary
- [[week-01-foundation]] through [[week-08-launch]] — detailed weekly plans
- [[deferred-to-phase-2]] — explicitly NOT building yet

### 05-systems/
Internal infrastructure being built.
- [[clickup-hierarchy]] — full nested structure of ClickUp command center
- [[engagement-template-generator]] — Claude Code project spec
- [[audit-system]] — productized audit delivery system
- [[sop-library-v1]] — 15-20 core home service SOPs
- [[outreach-infrastructure]] — cold email, LinkedIn, CRM setup

### 06-philosophy/
How decisions get made.
- [[build-philosophy]] — what gets built and why
- [[scope-management]] — guardrails against scope creep
- [[build-in-public]] — content/marketing approach

### 07-risks/
Known failure modes and mitigation.
- [[failure-modes]] — top risks to watch
- [[pessimistic-forecasts]] — realistic worst-case scenarios

## How to use this KB

When asking Claude (or any AI tool) for help with Framework OPS work:
1. For broad strategy questions: load `02-business-model/` + `03-current-state/`
2. For build/execution questions: load `04-build-plan/` + `05-systems/`
3. For pricing/sales questions: load `02-business-model/offer-ladder` + `02-business-model/pricing-strategy`
4. For Daniel engagement: load `03-current-state/active-clients` + relevant systems files

## Update cadence

This KB updates every Sunday during the weekly checkpoint. Anything that changes during the week gets logged and committed Sunday evening.
