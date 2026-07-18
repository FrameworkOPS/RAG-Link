# Outreach Infrastructure

Week 7 build. All systems needed to start running outreach on July 5, 2026.

## Components

### 1. Cold email stack

**Platform:** Instantly or Smartlead (TBD — Instantly slightly easier for solo operator)

**Setup:**
- Secondary domain (frameworkops.co or similar) for cold sending — protects primary domain
- 2-3 sending mailboxes for volume
- Domain warmup: 2-3 weeks before full sending volume
- DMARC, SPF, DKIM configured
- CAN-SPAM compliant: physical address + unsubscribe in every email

**Sequence structure:** 3-touch minimum, 4-7 days apart
- Email 1: Pattern interrupt + specific value (operator POV insight)
- Email 2: Case study reference or social proof
- Email 3: Direct ask + soft exit

**Personalization:** Company-level minimum (their tech stack, recent news, sub-vertical pain point). Avoid generic "saw your website" openers.

### 2. LinkedIn outreach

**Connection request scripts** (3 variants):
- Variant A: Operator-to-operator ("Sitting COO at roofing co, building tools for $1-3M home services")
- Variant B: Specific compliment + value ("Saw your post on X, would love to connect")
- Variant C: Mutual connection mention

**Follow-up scripts** (2-touch after connection accepted):
- Touch 1: Light intro + offer specific resource (e.g., free assessment template)
- Touch 2: Direct ask for discovery call

**Volume guideline:** 15-20 connection requests/day max. Higher triggers LinkedIn limits.

### 3. Referral request templates

For warm network (roofing industry, MBA cohort, vendors, Daniel's network).

**Template structure:**
- Personal opener (not template-feeling)
- What you're doing (1-2 sentences)
- ICP description (specific, not generic)
- Specific ask (e.g., "Anyone in HVAC owner network you'd suggest I talk to?")
- Easy out (no pressure)

### 4. Calendar booking flow

**Tool:** Cal.com (preferred, open source, integrates with Google Cal)

**Booking types:**
- 30-min Discovery Call (default)
- 15-min Quick Call (for warm intros)
- 60-min Audit Findings Review (for paying clients)

**Pre-call requirements:**
- Intake form completed before call
- Calendar buffer: 15 min before/after
- Auto-confirmation email with prep instructions

### 5. Intake form for discovery calls

**Tool:** Tally (free) or Typeform

**Required fields:**
- Company name + URL
- Owner name + role
- Annual revenue range
- Employee count
- Sub-vertical
- Top 3 operational pain points
- What they've tried already
- Specific outcome hoped for

Auto-creates ClickUp lead in Discovery Calls Booked list.

### 6. CRM in ClickUp

Per [[clickup-hierarchy]] Sales & Pipeline space.

**Flow:**
1. Lead captured (form submission, manual entry, LinkedIn DM)
2. Lands in Cold Outreach / Warm Network / Inbound list
3. Moves through pipeline: Discovery Booked → Discovery Held → Proposal Out → Closed Won/Lost
4. Closed Won triggers [[engagement-template-generator]]

### 7. Discovery call structure

60-90 min format:

- 5 min: Rapport + agenda
- 10 min: Their story + business
- 30 min: Operational deep dive (pain points, tech, team, goals)
- 10 min: Framework OPS approach explanation
- 10 min: Offer ladder walkthrough + next steps
- 5 min: Wrap, action items, calendar follow-up

Goal: Book Audit ($997) or send proposal within 48 hours.

## Compliance reminders

- **CAN-SPAM:** Physical address + unsubscribe in every cold email
- **GDPR / CCPA:** Probably not applicable to US-only home services but verify
- **LinkedIn ToS:** No automation tools that touch the LinkedIn interface (no Dux-Soup, Phantombuster, etc.)
- **Email volume:** Warmup properly. Never blast cold from primary domain.

## Realistic outcomes

First 30 days post-launch (week 8 onward):
- Cold email: 1-3% reply rate at this list quality, 20-30% to discovery call from interested replies
- LinkedIn: 2-5 conversations from 100 connection requests
- Warm network: 5-10 conversations from 30 personalized asks
- Total expected discovery calls: 5-15 in first 30 days
- Expected to close: 1-2 paying engagements in first 30 days

## Related files
- [[icp-definition]]
- [[offer-ladder]]
- [[linkedin-status]]
- [[week-07-outreach-infra]]
- [[clickup-hierarchy]]
