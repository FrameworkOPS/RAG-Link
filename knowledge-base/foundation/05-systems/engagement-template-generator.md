# Engagement Template Generator

Claude Code project. Built Weeks 3-4 of [[60-day-overview]].

## Purpose

Take discovery notes + audit findings → output a fully scaffolded ClickUp engagement workspace for a new client.

**Why it matters:** Difference between onboarding taking 10 hours or 1 hour. This is the scale lever.

## Inputs

JSON config containing:
- Client metadata: name, business type, revenue, sub-vertical, owner name
- Engagement type: Audit / Sprint / Light / Active / Embedded
- Audit findings: list of identified gaps tagged to standard categories
- Sub-vertical (roofing, HVAC, plumbing, etc.) for SOP customization
- Engagement duration and session count

## Outputs

Cloned ClickUp space in the "Active Clients" folder (per [[clickup-hierarchy]]):

- All standard lists from [[TEMPLATE] Engagement folder
- Custom fields pre-configured
- Pre-loaded SOP shells based on gap tags
- Pre-loaded session prep tasks based on engagement type
- Dashboard with client-specific views
- Initial action items in client-facing list

## Technical approach

**Language:** Python (using clickup-python or direct requests) or Node (TypeScript with @clickup/clickup-sdk).

**Architecture:**
1. Config validation layer
2. ClickUp API client wrapper (handles auth, rate limits, retries)
3. Template engine (reads from [[clickup-hierarchy]] config)
4. Gap-to-SOP mapping logic
5. Post-creation polish (assign owners, set due dates)

**Reuses:** ClickUp API integration code from Week 1 command center build. Work compounds.

## Validation test

**Week 3-4 acceptance test:** Regenerate Daniel's current ClickUp space from scratch using his audit findings.

Success criteria:
- All lists match current Daniel space
- Custom fields populated correctly
- SOP shells loaded for known gaps (missing onboarding checklists, no editor SOP, etc.)
- Time to generate < 5 minutes (vs ~10 hours manually)

## Limitations / known gaps

- **Dashboard widgets:** API support is limited. Some manual config required.
- **Some view types:** Gantt, Timeline may need manual tweaking.
- **Automation creation:** Basic only via API. Complex automations built manually.
- **Permissions:** Sharing settings handled manually.

Acceptable: 85% automated, 15% manual polish per new engagement. Manual time per client drops from 10 hrs to 1-2 hrs.

## Future enhancements (Phase 2)

- AI-driven gap → SOP mapping (vs. rule-based)
- Auto-populate session agendas from engagement type + week number
- Generate kickoff email + intake form from same config
- Slack channel creation + invite via API
- Drive folder structure creation parallel to ClickUp

## Related files
- [[clickup-hierarchy]]
- [[week-03-generator-p1]]
- [[week-04-generator-p2]]
- [[active-clients]]
- [[deferred-to-phase-2]]
