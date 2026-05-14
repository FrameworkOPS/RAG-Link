# Automation Playbook for Home Service Companies

## Why Automation Matters

At $5M revenue with 20 employees, a home service company is spending roughly $80K–$150K per year on manual tasks that could be partially or fully automated. The highest-value targets are repetitive, rules-based processes where timing and consistency matter: follow-up, confirmations, reminders, reviews, and reporting.

Automation does not replace people — it removes the low-value tasks that distract people from high-value work.

---

## Automation Priority Tier 1: High Impact, Low Complexity

These should be built first. Each delivers measurable ROI quickly.

### 1. Lead Response / Follow-Up Automation
**Problem:** Leads that aren't contacted within 5 minutes convert at 10x the rate of leads contacted after 30 minutes. Most home service companies take 30 minutes to 24 hours to follow up.

**Automation:** When a new lead comes in (web form, Google LSA, paid ad), trigger an immediate SMS and email to the prospect. If no response in 2 hours, trigger a second message. If no response in 24 hours, create a task in the FSM for manual follow-up.

**Tools:** Zapier/Make + Twilio (SMS) + FSM webhook. Or native to HouseCall Pro/ServiceTitan for connected lead sources.

**Expected lift:** 15–30% increase in estimate scheduling rate from existing lead volume.

### 2. Appointment Confirmation and Reminders
**Problem:** No-shows and "forgot about you" cancellations cost 1–3% of total scheduled capacity. Technician drive time to a vacant address is pure waste.

**Automation:** 48-hour confirmation SMS/email asking customer to confirm. 2-hour day-of reminder with tech name and arrival window. If customer doesn't respond to confirmation, dispatcher flagged to call.

**Tools:** Most FSMs (HouseCall Pro, ServiceTitan, Jobber) have this native. If not, Zapier + Twilio.

**Expected lift:** 30–50% reduction in no-shows and late cancellations.

### 3. Invoice and Payment Follow-Up
**Problem:** Invoices sitting unpaid extend DSO and create cash flow drag. Manual collection calls take admin time and feel awkward.

**Automation:** Invoice sent automatically at job completion via FSM. If unpaid at 3 days: reminder SMS/email. If unpaid at 7 days: second reminder + phone call task assigned. If unpaid at 14 days: overdue notice with payment link.

**Tools:** Native to most FSMs. Integrate with Stripe or Square for payment link. QBO for AR reconciliation.

**Expected lift:** 5–10 day reduction in DSO for the average invoice.

### 4. Review Request Automation
**Problem:** Most customers who have a good experience don't leave reviews unless asked. Most companies don't ask consistently.

**Automation:** 24–48 hours after job completion and invoice paid, send a personalized SMS asking for a Google review with a direct link. If customer clicked but didn't review, one follow-up 72 hours later.

**Tools:** NiceJob or Podium (purpose-built, $200–$400/month). Or build in Make/Zapier + FSM + Google My Business API.

**Expected lift:** 3–5x increase in monthly review volume. Compounding effect on local SEO over 6–12 months.

---

## Automation Priority Tier 2: High Impact, Medium Complexity

These deliver significant value but require more setup time or integration work.

### 5. Automated Weekly Reporting
**Problem:** Owner spends 2–4 hours per week manually compiling revenue, close rate, and job cost data from FSM and QBO. Or doesn't do it at all, so no one has visibility.

**Automation:** Schedule a weekly query of FSM data + QBO → compile into a Google Sheet or dashboard → send summary email/Slack message to owner every Monday morning with key metrics.

**Tools:** Make or n8n + FSM API + QBO API + Google Sheets API. ServiceTitan has scheduled reports natively.

**Metrics to include:** Revenue vs. goal (week and MTD), jobs completed, close rate, gross margin (if job costing is clean), AR balance.

**Time saved:** 2–4 hours/week for owner or operations manager.

### 6. Hiring Funnel Automation
**Problem:** Job applicants apply on Indeed and then wait days for a response. Top candidates take other offers. The manual process of screening and scheduling is time-consuming.

**Automation:** Indeed application → Zapier trigger → send automated acknowledgment email with pre-screening questionnaire (Google Form or Typeform) → responses logged in spreadsheet → qualified candidates automatically receive a calendar link to schedule a phone screen.

**Tools:** Indeed Webhook/RSS + Zapier + Google Forms + Calendly.

**Expected lift:** 40–60% reduction in time to first phone screen.

### 7. Seasonal Reactivation Campaigns
**Problem:** Past customers who haven't booked in 12+ months represent low-hanging revenue. No one has time to manually email 500 past customers.

**Automation:** Monthly or quarterly, pull customers from FSM where last job date > 12 months → send personalized reactivation SMS/email ("It's been a while since we serviced your [system/roof] — here's a special offer for returning customers").

**Tools:** FSM export + Mailchimp or ActiveCampaign + conditional logic for suppression (don't contact active customers or people who unsubscribed).

**Expected lift:** 3–8% reactivation rate on the cold list. At 500 contacts and $500 average job, that's $7,500–$20,000 in revenue per campaign.

---

## Automation Priority Tier 3: Emerging AI Automation

These are newer and require more technical setup but are increasingly viable.

### 8. AI-Powered Lead Triage
**Problem:** Not all leads are equal. Dispatchers spend time on tire-kickers, wrong-area requests, and low-budget jobs that won't close.

**Automation:** When a lead comes in via web form or inbound call transcript, send to an AI model with a prompt that categorizes: urgency, scope, likelihood to convert. Flag low-quality leads for lower-priority follow-up. High-quality leads routed immediately to senior dispatcher or salesperson.

**Tools:** n8n + Claude API or OpenAI API. Twilio for call transcription.

**Maturity level:** Emerging. Viable for technically capable teams or with a builder's help.

### 9. AI Job Summary for Techs
**Problem:** Field techs spend 15–30 minutes on admin after each job (notes, photos, invoice review). Time that could go toward the next job.

**Automation:** Tech dictates a 60-second voice note at job closeout → AI transcribes and generates structured job notes → auto-populates FSM job notes field.

**Tools:** Whisper (OpenAI transcription) + Claude/GPT for formatting → FSM API.

### 10. Automated P&L Commentary
**Problem:** Monthly financials are reviewed but no one writes the narrative explaining variances. Owner lacks context for decisions.

**Automation:** QBO API pulls monthly P&L → sends to AI model with prior month for comparison → generates a 3–5 sentence narrative summary of key variances → delivered in the weekly report email.

**Tools:** QBO API + n8n + Claude API.

---

## Implementation Sequence

**Month 1:** Lead response automation + appointment confirmations (Tier 1 items 1 and 2)
**Month 2:** Review requests + invoice follow-up (Tier 1 items 3 and 4)
**Month 3:** Weekly reporting automation (Tier 2)
**Month 4+:** Reactivation campaigns, hiring automation, AI tools

Build one automation, let it run for 2–4 weeks, confirm it works, then build the next one. Automation debt (broken flows no one monitors) is worse than no automation.
