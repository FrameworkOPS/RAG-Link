---
title: Framework OPS — Session 4: Break-Even Review, Onboarding Automation & VA Hiring Plan
date: 2026-05-09
participants: [William Peare, daniel@leadstatement.com]
source: fathom
type: meeting
url: https://fathom.video/calls/667293716
tags: [fathom, meeting]
---

# Framework OPS — Session 4: Break-Even Review, Onboarding Automation & VA Hiring Plan
**Date:** May 9, 2026
**Participants:** William Peare, daniel@leadstatement.com
**Recording:** [View on Fathom](https://fathom.video/calls/667293716)

---

## Summary

## Meeting Purpose

[Review Daniel's automation progress and build a lead generation pipeline.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=251.0)

## Key Takeaways

  - [**Onboarding Automation:** Daniel built a Zapier-based onboarding system (Stripe → Slack/GHL/Drive) but needs help automating ClickUp fulfillment templates.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=1341.0)
  - [**AI Video for Speed:** Daniel is using AI video tools (Kling AI, Higgsfield.ai) to bypass client filming bottlenecks and accelerate ad testing.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=2177.0)
  - [**Lead Gen Pipeline Built:** The session used Claude Code, Google Cloud, and Apollo to build a lead scraper, proving the concept despite Apollo's free-plan API limits.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=5537.0)
  - [**Hiring Plan & Financials:** The next steps are to finalize the financial model and breakeven analysis, then develop a detailed VA hiring and onboarding plan.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=7233.0)

## Topics

### Onboarding Automation Review

  - [Daniel built an onboarding system triggered by a new Stripe subscription.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=578.0)
  - [**Workflow:** Stripe → Zapier → Slack channel creation, GHL status update, and Google Drive folder creation.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=578.0)
  - [**Client Input:** A detailed Typeform replaces a manual Google Doc to gather client info (ISDP, ad history, reviews) and streamline data collection.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=420.0)
  - [**ClickUp Integration Gap:** The system lacks automation for ClickUp, which holds the master fulfillment template.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=1341.0)
      - [**Goal:** Replicate the master template for each new client, using their business name from the Typeform.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=1576.0)
      - [**Proposed Solution:** Use Claude Code to scrape the template structure and automate its replication via Zapier.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=1473.0)

### AI Video for Fulfillment Speed

  - [Daniel is using AI video tools to bypass client filming bottlenecks and accelerate ad testing.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=2177.0)
  - [**Tools:** Kling AI and Higgsfield.ai.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=2177.0)
  - [**Use Cases:**](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=2203.0)
      - [Generate videos with avatars that resonate with the target audience (e.g., blue-collar avatars for home service ads).](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=2203.0)
      - [Create videos from scripts using a client's avatar, bypassing issues like accents or poor delivery.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=2308.0)
  - [**Business Impact:** Faster ad rollout → faster case studies → enables higher pricing (e.g., +$1k/client) and better margins.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=2361.0)

### Building the Automated Lead Scraper

  - [The session built a lead scraper to automate client acquisition.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=4612.0)
  - [**Process:**](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=4612.0)
    1.  [**Scrape Companies:** Claude Code used the Google Places API to find tax firms.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=4612.0)
    2.  [**Enrich Leads:** The script used the Apollo API to find contact info for firm owners.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=6280.0)
  - [**Blockers & Solutions:**](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=5537.0)
      - [**API Version Mismatch:** The script used a legacy Google Places API; Claude Code updated it to the current version.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=5537.0)
      - [**Apollo API Limits:** The free Apollo plan has a rate limit and does not return contact data via API.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=6752.0)
          - [**Solution:** Upgrade to the $65/month Apollo plan to unlock API enrichment.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=6914.0)
  - [**Outcome:** The scraper successfully generated a CSV of \~430 leads, proving the concept.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=6460.0)

### Hiring & Scaling Strategy

  - [**Trigger for Hiring:** Daniel will hire a VA once the lead generation and client acquisition processes are predictable.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=3182.0)
  - [**VA Roles:** Initial hires may focus on outreach or client delivery.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=3224.0)
  - [**Hiring Process:** A rigorous application process (e.g., long forms, video submissions) will be used to vet for quality and commitment.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=7578.0)
  - [**Onboarding:** The VA onboarding process will be structured in ClickUp, linking to SOPs in Google Drive.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=2048.0)
  - [**Expectation Setting:** Hiring a VA will increase Daniel's workload for the first 90 days due to training and oversight.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=7329.0)

## Next Steps

  - [**Daniel:**](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=2952.0)
      - [Finalize the tax firm Gamma Doc.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=6491.0)
      - [Test the lead scraper with the upgraded Apollo plan.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=6981.0)
      - [Build the ClickUp automation to replicate the fulfillment template.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=1473.0)
      - [Prepare financial data for the breakeven analysis.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=3417.0)
  - [**William:**](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=7233.0)
      - [Prepare a financial model document.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=7233.0)
      - [Assist with VA hiring strategy and interviews.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=7383.0)
  - [**Both:**](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=7233.0)
      - [Meet Monday at 5 PM Pacific for the financial modeling and breakeven review.](https://fathom.video/share/zHFSL7HY8bizi5ZwBDJs1c7dyuwr-jfm?tab=summary&timestamp=7710.0)


---

## Action Items

- [ ] **Daniel Kalinin** — Build onboarding funnel + video; link Typeform, Slack, Drive, booking `[00:08:17]` [▶](https://fathom.video/calls/667293716?timestamp=497.9999)
- [ ] **Daniel Kalinin** — Test onboarding E2E via Stripe test; verify Slack, Drive, GHL, ClickUp `[00:19:22]` [▶](https://fathom.video/calls/667293716?timestamp=1162.9999)
- [ ] **Daniel Kalinin** — Set up ClickUp Client custom field as Text; map Typeform business name via Zap `[00:28:34]` [▶](https://fathom.video/calls/667293716?timestamp=1714.9999)
- [ ] **Daniel Kalinin** — Create GHL outreach pipeline; add stages + personalization templates `[00:50:29]` [▶](https://fathom.video/calls/667293716?timestamp=3029.9999)
- [ ] **Daniel Kalinin** — Update Claude Code scraper to Places API New; add Apollo Contact Search; run enrichment `[01:32:06]` [▶](https://fathom.video/calls/667293716?timestamp=5526.9999)
- [ ] **William Peare** — Prepare financial model + breakeven doc for next session `[02:00:22]` [▶](https://fathom.video/calls/667293716?timestamp=7222.9999)
- [ ] **William Peare** — Send next-steps email to Daniel `[02:08:06]` [▶](https://fathom.video/calls/667293716?timestamp=7686.9999)
- [ ] **William Peare** — Schedule next session w/ Daniel: Mon 5 pm PT `[02:08:19]` [▶](https://fathom.video/calls/667293716?timestamp=7699.9999)

---

## Transcript

**Daniel Kalinin** [00:00:00]: Um, I was playing around with it to like 4 a.m.

**Daniel Kalinin** [00:00:03]: I went to at like 4.30 and I just had bloodshot eyes.

**William Peare** [00:00:08]: Yeah, yeah.

**William Peare** [00:00:09]: No, it's every night for me it's like 12 or 1 and I'm like, okay, enough.

**William Peare** [00:00:15]: Yeah, so I'll walk you through everything.

**Daniel Kalinin** [00:00:18]: Um, I'm not, I think I understand like people build cool  with them, like infrastructures and stuff like that, but I don't really know the application, but I made some folders like research, SOPs, all that kind of stuff.

**Daniel Kalinin** [00:00:30]: I took all of our calls, I plugged it into like this onboarding SOP that I made and Manus basically told me I need to keep refining it because it's going to be like the database or something.

**Daniel Kalinin** [00:00:40]: I don't really know what I'm doing, but I was playing around with it and, uh, yeah.

**Daniel Kalinin** [00:00:43]: Did you set up an RAG?

**William Peare** [00:00:46]: No clue what that is.

**Daniel Kalinin** [00:00:48]: Should be, sure.

**William Peare** [00:00:49]: Um, at least with a Claude, so to speak, and pretty much all LLMs, they have memory, but the memory is like somewhat.

**William Peare** [00:00:59]: Yeah.

**William Peare** [00:00:59]: Limited.

**William Peare** [00:01:00]: So like you lose context over a period of time.

**William Peare** [00:01:02]: If you set up an RAG, which we can go through, it's, you get a, I'm guessing it's kind of similar to like what you were talking about with those people building the brain dumps for 25,000.

**William Peare** [00:01:15]: So an RAG is pretty much a hosted database.

**William Peare** [00:01:19]: Did it have you set up Railway or Netlify or any kind of hosting platform?

**Daniel Kalinin** [00:01:25]: No, I think one of my friends uses Obsidian, if you know what that is.

**William Peare** [00:01:29]: Yeah.

**William Peare** [00:01:30]: Yep.

**William Peare** [00:01:30]: Is that a RAG?

**William Peare** [00:01:33]: Um, it probably is, depending on how he's using it.

**William Peare** [00:01:37]: Let me see what its features are.

**William Peare** [00:01:39]: I've heard of it, but I don't know.

**William Peare** [00:01:42]: Yeah, if you search up, I'll send you his channel right now.

**Daniel Kalinin** [00:01:46]: Um, this guy was the guy that taught me how to do copywriting.

**Daniel Kalinin** [00:02:00]: And he ended up pivoting to AI like two, three years later, and his videos blew up on like, I think it was Claude Cowork and then Obsidian, and now he has so much inbound for like AI infrastructures for businesses.

**William Peare** [00:02:15]: That's crazy.

**William Peare** [00:02:19]: So he's pretty good?

**William Peare** [00:02:22]: Yeah, he's really good.

**Daniel Kalinin** [00:02:23]: He lives in a, he lives in like an apartment complex in like Georgia with like, it's like an HOA, got everything, like gyms, pools, whatever, blah, blah, blah.

**Daniel Kalinin** [00:02:32]: And, uh, the owner of the, uh, the, the, the, the complex, he, uh, he actually saw the video too and ended up hiring him.

**Daniel Kalinin** [00:02:41]: Really?

**William Peare** [00:02:42]: Yeah.

**Daniel Kalinin** [00:02:43]: He was like, he, cause, cause KJ, he works at like their coworking space.

**Daniel Kalinin** [00:02:47]: They got one on site.

**William Peare** [00:02:48]: I don't Walked in one day.

**Daniel Kalinin** [00:02:49]: He's like, wait, I thought I saw your video.

**Daniel Kalinin** [00:02:51]: I thought you looked so familiar.

**Daniel Kalinin** [00:02:52]: Can you help me?

**Daniel Kalinin** [00:02:52]: So yeah, everybody's on it now.

**Daniel Kalinin** [00:02:55]: Yes.

**William Peare** [00:02:56]: Yes.

**William Peare** [00:02:56]: This is pretty much, um, Um,

**William Peare** [00:03:00]: Essentially.

**William Peare** [00:03:02]: I'm going to download this actually now and play with it.

**William Peare** [00:03:08]: Yes, you can use a program like this that's already a program.

**William Peare** [00:03:12]: Or, I mean, you can just Railway and Netlify.

**William Peare** [00:03:15]: There's a ton of them.

**William Peare** [00:03:16]: But there, you heard of Heroku either?

**William Peare** [00:03:21]: No, I'm really new to a lot of this stuff.

**William Peare** [00:03:27]: Think like a, not a website, but like it gives you a URL.

**William Peare** [00:03:32]: It's got online, it's essentially a hosting capability.

**William Peare** [00:03:35]: That way it's got somewhere it's pinging and it can make a SQL database.

**William Peare** [00:03:39]: And then it will grab all of what you're putting in and it'll throw it into that database.

**William Peare** [00:03:44]: So then like when you're talking to it, I'm pretty much guaranteeing that's what the Obsidian is doing just locally, or at least in one structured place.

**William Peare** [00:03:53]: But it stores all that data.

**William Peare** [00:03:55]: That way, whenever you're talking about something, you can tell it like a reference pass.

**William Peare** [00:03:59]: Conversations and it'll scour the database really quick, grab anything that's relevant, use that context for the conversation instead of just the limited memory that it has.

**William Peare** [00:04:09]: Yeah.

**William Peare** [00:04:11]: Before we go into the VA thing, I'd like to see what you've done so far and compare it against what I've done.

**William Peare** [00:04:17]: So what I did is kind of a test concept because we have a very similar onboarding model, honestly.

**William Peare** [00:04:24]: I get slightly different in terms that I don't have to get a bunch of creative and stuff from them, but the same process in terms of like, you know, a drive, the tasks into ClickUp, all that stuff.

**William Peare** [00:04:35]: So what I built out last night, I did too.

**William Peare** [00:04:40]: The night before I did it in N8N, last night I did it totally through code, hosted in Railway.

**William Peare** [00:04:46]: So when we, I do a session with Fathom, you know, like you get the little transcript and stuff from Fathom and then you could, my previous way of doing it was I would put that then into Claude and I would get it refined and then I would send out.

**William Peare** [00:05:00]: The email, the calendar, invite, and do the agendas.

**William Peare** [00:05:03]: So it will automatically parse all that for me.

**William Peare** [00:05:06]: It will automatically set the draft email because it can't manually send the emails unless you use a different one.

**William Peare** [00:05:11]: And I prefer actually having a draft that I can look through.

**William Peare** [00:05:14]: So it'll automatically make my draft for me for the person.

**William Peare** [00:05:17]: It'll automatically line out the action steps.

**William Peare** [00:05:19]: It'll take the action steps and the due dates, automatically put them into ClickUp as tasks for me.

**William Peare** [00:05:24]: It'll automatically make the calendar event, the drive, all of that just based on the Fathom webhook.

**William Peare** [00:05:30]: With the conversation being done.

**William Peare** [00:05:32]: Yeah.

**William Peare** [00:05:32]: That was, it was probably like a two hour, three hour build with, and that was a lot of testing.

**William Peare** [00:05:38]: So super easy use case.

**William Peare** [00:05:41]: Got it.

**Daniel Kalinin** [00:05:42]: Let me, yeah, let me just walk through everything that I did then.

**Daniel Kalinin** [00:05:46]: Um, all right, I'm going to open up a few things because I did a good chunk.

**Daniel Kalinin** [00:06:03]: Like Zapier.

**Daniel Kalinin** [00:06:05]: Screw an 8M, by the way.

**Daniel Kalinin** [00:06:06]: Zapier is so much easier.

**Daniel Kalinin** [00:06:08]: It's a lot easier.

**William Peare** [00:06:09]: It's just less robust.

**William Peare** [00:06:11]: It's super easy to work with.

**William Peare** [00:06:13]: It's just a little bit more limited in terms of what it does.

**William Peare** [00:06:16]: And a little bit more expensive in terms of the cost.

**William Peare** [00:06:20]: The Zapps can get pretty expensive.

**William Peare** [00:06:23]: All right, let me know if you see my screen.

**William Peare** [00:06:25]: I'm with you.

**William Peare** [00:06:27]: All right, cool.

**William Peare** [00:06:28]: Let me go into the leadstatement one.

**Daniel Kalinin** [00:06:35]: Okay, so this is going to be the entire kind of infrastructure for onboarding.

**Daniel Kalinin** [00:06:44]: It's going to be this right here.

**Daniel Kalinin** [00:06:49]: Cool.

**Daniel Kalinin** [00:06:50]: it's going to here.

**William Peare** [00:06:51]: Cool.

**William Peare** [00:06:52]: Cool.

**Daniel Kalinin** [00:06:54]: And, yeah.

**Daniel Kalinin** [00:06:55]: Okay, so previously I had a...

**Daniel Kalinin** [00:07:00]: I kind of just leaned in on how can I make onboarding as professional and clean as possible.

**Daniel Kalinin** [00:07:05]: So I did the ISDP document where it's like a Google Doc that they fill out a lot and I converted that to a type form.

**Daniel Kalinin** [00:07:11]: Yes.

**Daniel Kalinin** [00:07:12]: This type form is pretty in-depth.

**Daniel Kalinin** [00:07:16]: I should get pretty much everything that I need to know about them.

**Daniel Kalinin** [00:07:18]: So the service they sell, if they target a niche or just broad business owners, stuff about their ISDP, like their dream outcomes and desires, a bit about their business.

**Daniel Kalinin** [00:07:30]: Have they ran ads?

**Daniel Kalinin** [00:07:31]: Also kind of screening.

**Daniel Kalinin** [00:07:33]: I think one thing that I want to kind of make them feel is like I'm more of a partner or something like that.

**Daniel Kalinin** [00:07:39]: So I took their money.

**Daniel Kalinin** [00:07:41]: So part of this is like, you know, were your ads good, decent, disappointing if they've ran ads before?

**Daniel Kalinin** [00:07:49]: You know, I asked them why, what problems they had, maybe something like they could have done better that we can, so that we can iterate on it.

**Daniel Kalinin** [00:07:55]: Monthly budget for ads, so on and so forth.

**Daniel Kalinin** [00:07:59]: And do they have...

**Daniel Kalinin** [00:08:00]: Do reviews?

**Daniel Kalinin** [00:08:00]: they have written reviews?

**Daniel Kalinin** [00:08:01]: If they don't, can they get it?

**Daniel Kalinin** [00:08:03]: So on and so forth.

**Daniel Kalinin** [00:08:05]: So it should just make my life a bit easier in terms of not having to ask around for different things.

**William Peare** [00:08:13]: Yeah, think that a type form was the way, 100%.

**Daniel Kalinin** [00:08:17]: Yeah, I think from my understanding with onboarding and honestly anything, you just have to repeatedly bash it into their head what you need.

**Daniel Kalinin** [00:08:28]: So part of like this whole type form thing is going to be, I need to create an onboarding funnel.

**Daniel Kalinin** [00:08:34]: It's just going to, I'm going to send it through the onboarding email.

**Daniel Kalinin** [00:08:39]: There's going to be like a video there, again, telling them exactly what they need to do, like, especially like, you know, complete the form, upload any testimonials, your client reviews that you have, make sure to join Slack, so on and so forth.

**Daniel Kalinin** [00:08:51]: That way there's just no miscommunication.

**Daniel Kalinin** [00:08:54]: So I'm going to build it out on this and I'll create like a quick video for that and like reinforce their decision making.

**Daniel Kalinin** [00:08:59]: So just reminder.

**Daniel Kalinin** [00:09:00]: And then why they're in the first place.

**Daniel Kalinin** [00:09:01]: So like, you know, you're here because you're relying on referrals, word of mouth, blah, blah, um, the onboarding sequence, um, it's going to get, Zapier's going to auto pull them, but this is like a backup if they get tagged for begin onboarding, quick email sequence, action steps, blah, blah, blah.

**Daniel Kalinin** [00:09:18]: Let's ram through this quickly and efficiently.

**Daniel Kalinin** [00:09:20]: Um, onboarding context.

**Daniel Kalinin** [00:09:22]: So your onboarding form is going to be linked below schedule your onboarding call.

**Daniel Kalinin** [00:09:25]: you haven't already Slack invitation, Google drive folder invitation, um, to add in your video.

**Daniel Kalinin** [00:09:31]: Testimonials and reviews, um, all that kind of stuff.

**Daniel Kalinin** [00:09:35]: So then I need to link these.

**Daniel Kalinin** [00:09:36]: I just haven't created the funnel yet for that.

**Daniel Kalinin** [00:09:38]: Um, with the zap, two zaps.

**Daniel Kalinin** [00:09:43]: So I triggered this through a new subscription on Stripe.

**Daniel Kalinin** [00:09:47]: Um, first things just making their private channel and then inviting them, uh, to that private channel.

**William Peare** [00:09:55]: So as opposed to like, cause I mean, really a contract is all well and good.

**William Peare** [00:09:58]: It's one thing, but you say

**William Peare** [00:10:00]: Sending them a payment link with the scope of work and them paying is a contract and like by contract law.

**William Peare** [00:10:04]: It's really intent is a contract.

**William Peare** [00:10:08]: So like you're the program here is that you're going to send them off the stripe.

**William Peare** [00:10:13]: They pay that kicks everything off because you do the stripe on the call.

**William Peare** [00:10:17]: Yeah.

**Daniel Kalinin** [00:10:18]: Yes.

**Daniel Kalinin** [00:10:19]: Okay.

**William Peare** [00:10:19]: Yeah.

**Daniel Kalinin** [00:10:20]: And I mean, if they need like a contract, I'm sure a lot of people, they're fine paying first and getting the contract after.

**Daniel Kalinin** [00:10:26]: Right.

**Daniel Kalinin** [00:10:26]: Is that standard?

**William Peare** [00:10:29]: No, I would not say that's standard.

**William Peare** [00:10:31]: If there's a contract involved, it's generally contract first, pay second.

**William Peare** [00:10:35]: But I think that I can tell you get to the point where you're, you know, 5,000 a month or something like that.

**William Peare** [00:10:42]: You're probably not going to get a whole lot of pushback on not having a contract as long as the scope of work is clear.

**William Peare** [00:10:48]: Really, the contract just protects you against like people trying to fight for refunds.

**William Peare** [00:10:55]: And at the end of the day, like that's always kind of like you can either hide behind your car.

**William Peare** [00:11:00]: Contract and then get bad reviews or a bad sentiment with people if you just tell them to screw off.

**William Peare** [00:11:05]: like even with a contract, it's generally best to just shake hands and part ways and just get realistically.

**William Peare** [00:11:13]: So it's just to protect you against in what case you have to give money back.

**William Peare** [00:11:18]: Yeah.

**William Peare** [00:11:20]: Yeah.

**Daniel Kalinin** [00:11:21]: So new subscription trigger, create the Slack channel.

**Daniel Kalinin** [00:11:24]: If there's an error creating it, I just get an email.

**Daniel Kalinin** [00:11:26]: That way I can quickly manually do it.

**Daniel Kalinin** [00:11:29]: Update their Go High-Level status and add them to the onboarding workflow.

**William Peare** [00:11:34]: That way they get the onboarding sequence.

**Daniel Kalinin** [00:11:39]: I believe I also tag them right here.

**Daniel Kalinin** [00:11:42]: Yeah.

**Daniel Kalinin** [00:11:42]: So I give them the begin onboarding tag.

**Daniel Kalinin** [00:11:43]: That way it's just a double confirmation that it's going to work.

**Daniel Kalinin** [00:11:46]: Second part is going to be creating the Google Drive folder, which is pretty sick, by the way.

**Daniel Kalinin** [00:11:50]: I don't dabble into this at all.

**Daniel Kalinin** [00:11:53]: Yeah.

**William Peare** [00:11:54]: But it's cool that, yeah, new subscription starts.

**Daniel Kalinin** [00:11:56]: I split their first name and last name from the subscription.

**Daniel Kalinin** [00:12:00]: And, you know, name, create their client folder, create the fulfillment folders within it.

**William Peare** [00:12:06]: Yes.

**William Peare** [00:12:06]: Yeah.

**William Peare** [00:12:07]: It's pretty simple.

**Daniel Kalinin** [00:12:09]: And then I believe, yeah, right here, I send them access to it.

**Daniel Kalinin** [00:12:13]: This is actually going to load.

**Daniel Kalinin** [00:12:15]: I think I just cracked.

**Daniel Kalinin** [00:12:16]: No, I didn't.

**Daniel Kalinin** [00:12:16]: Okay.

**Daniel Kalinin** [00:12:17]: Yeah.

**Daniel Kalinin** [00:12:17]: I send them access to it.

**William Peare** [00:12:19]: So, yeah.

**Daniel Kalinin** [00:12:22]: I mean, yeah, that's what I built for onboarding.

**William Peare** [00:12:27]: then for ClickUp.

**William Peare** [00:12:29]: You're already ahead of the game here, bud.

**William Peare** [00:12:30]: But, yeah, it's super time-heavy on the front end.

**William Peare** [00:12:33]: But, mean, say you put in 10 or 20 hours to test it and then it's done.

**William Peare** [00:12:36]: Then you just don't have to worry about it again until you want to tweak it.

**William Peare** [00:12:39]: Like, yeah.

**Daniel Kalinin** [00:12:40]: And this is probably where you could chip in because, man, it's kind of instructed me with all this.

**Daniel Kalinin** [00:12:47]: But I don't you know, what I don't know.

**Daniel Kalinin** [00:12:52]: Main thing is, like, I have a client delivery space right here, a review.

**Daniel Kalinin** [00:12:57]: And I'm able to see things that are overdue due this week.

**Daniel Kalinin** [00:13:00]: Waiting on client, blocked or at risk, workload by assignee, and so on and so forth.

**Daniel Kalinin** [00:13:05]: This is like the folder that I'm kind of like using as the template or whatever.

**William Peare** [00:13:10]: Yeah.

**William Peare** [00:13:11]: Yeah.

**Daniel Kalinin** [00:13:13]: Different views.

**William Peare** [00:13:14]: So let me see.

**William Peare** [00:13:17]: Each one of these are just like a different part of my fulfillment.

**Daniel Kalinin** [00:13:20]: So like 0-0 is basically just like overall.

**Daniel Kalinin** [00:13:25]: I honestly don't even know what this is.

**Daniel Kalinin** [00:13:27]: I'm guessing it's just like links that I need to have, client overview and success criteria, audit risk, account risk log.

**Daniel Kalinin** [00:13:35]: So if the client's doing something stupid, I could just log it here or something like that.

**Daniel Kalinin** [00:13:39]: Communication rules.

**Daniel Kalinin** [00:13:40]: I don't know, man.

**Daniel Kalinin** [00:13:40]: just telling me to put that in.

**Daniel Kalinin** [00:13:42]: Here's where it makes a bit more sense.

**Daniel Kalinin** [00:13:44]: send onboarding form, call, blah, blah, blah, collect meta access, market research.

**Daniel Kalinin** [00:13:49]: So just sprinting through the ISTP, competitor analysis, so on and so forth.

**Daniel Kalinin** [00:13:52]: Some of these have checklists within, which I guess this might be like for the VA.

**Daniel Kalinin** [00:13:57]: That's maybe what the logic

**William Peare** [00:14:00]: Yeah.

**Daniel Kalinin** [00:14:01]: It's a checklist, offering funnel strategy, copy, funnel building.

**William Peare** [00:14:08]: Did you have to manually build this or did it get built through the Zap or did it get built by Manus?

**William Peare** [00:14:14]: I don't know.

**William Peare** [00:14:15]: Manus is- I built this myself.

**Daniel Kalinin** [00:14:18]: Okay.

**William Peare** [00:14:19]: But it's so gave the context to what you wanted to Manus.

**William Peare** [00:14:23]: Manus gave you prompts step-by-step.

**William Peare** [00:14:24]: You could iterate and ask questions as you went and good.

**William Peare** [00:14:28]: But yeah, honestly, that's the best, that's the best way to learn.

**William Peare** [00:14:31]: That's how I learned.

**William Peare** [00:14:32]: So it's nothing I could teach you that it's not teaching you because so much of it's personal preference.

**William Peare** [00:14:36]: You know what I mean?

**William Peare** [00:14:37]: Like, this is actually just how you learn in the process.

**William Peare** [00:14:40]: Hold on.

**William Peare** [00:14:40]: I got to find more pouches, man.

**William Peare** [00:14:42]: I'm out of pouches.

**William Peare** [00:14:43]: Get serious.

**William Peare** [00:14:48]: Manus, cannot help you right now.

**William Peare** [00:14:50]: have my own.

**William Peare** [00:15:17]: Okay, I forgot this dress falls off of you.

**William Peare** [00:15:42]: I'm sorry.

**William Peare** [00:15:43]: I'm sorry, are you okay?

**William Peare** [00:15:45]: It's okay, we're just gonna put your hair up real quick.

**William Peare** [00:15:48]: It's okay, just quit.

**William Peare** [00:15:58]: You're almost done.

**William Peare** [00:15:59]: Move your hand.

**William Peare** [00:16:00]: When you get your hair on your eyes, I'm sorry.

**William Peare** [00:16:03]: I'm sorry, baby.

**William Peare** [00:16:04]: Almost done.

**William Peare** [00:16:09]: Almost done.

**William Peare** [00:16:11]: Oh my gosh.

**William Peare** [00:16:13]: If I had my thumb, this would be so much better.

**William Peare** [00:16:15]: I'm so sorry.

**William Peare** [00:16:16]: Okay, move your hand.

**William Peare** [00:16:18]: There.

**William Peare** [00:16:18]: Okay, it's okay.

**William Peare** [00:16:19]: There.

**William Peare** [00:16:20]: Good.

**William Peare** [00:16:20]: Good.

**William Peare** [00:16:22]: Let me see.

**William Peare** [00:16:23]: Okay.

**William Peare** [00:16:24]: Good.

**William Peare** [00:16:24]: Beautiful.

**William Peare** [00:16:28]: Okay.

**William Peare** [00:16:29]: Hold on.

**William Peare** [00:16:29]: Hold on.

**William Peare** [00:16:30]: Stop moving.

**William Peare** [00:16:32]: Okay.

**William Peare** [00:16:33]: Look at mommy.

**William Peare** [00:16:35]: Beautiful.

**William Peare** [00:16:35]: Okay.

**William Peare** [00:16:36]: We gotta go.

**William Peare** [00:16:36]: You ready?

**William Peare** [00:16:37]: Come on.

**William Peare** [00:16:38]: go grab this.

**William Peare** [00:16:39]: What?

**William Peare** [00:16:40]: What do you want?

**William Peare** [00:16:41]: Grab it.

**William Peare** [00:16:41]: Grab it quick.

**William Peare** [00:16:42]: What are you looking for?

**William Peare** [00:16:43]: What do you mean?

**William Peare** [00:16:48]: No.

**William Peare** [00:16:48]: We're not playing with that today.

**William Peare** [00:16:49]: Okay.

**William Peare** [00:16:50]: Let's go.

**William Peare** [00:16:51]: We gotta go.

**William Peare** [00:16:53]: Come on.

**William Peare** [00:16:54]: on.

**William Peare** [00:16:54]: Okay.

**William Peare** [00:16:55]: Okay.

**William Peare** [00:17:01]: All right, we gotta go!

**William Peare** [00:17:23]: See you in a fight, bye.

**William Peare** [00:18:31]: Sorry, that was, that was very critical.

**William Peare** [00:18:34]: Uh-huh.

**Daniel Kalinin** [00:18:36]: Yeah.

**William Peare** [00:18:37]: Okay.

**William Peare** [00:18:38]: Yeah, honestly, the engine is great.

**William Peare** [00:18:40]: Really great.

**William Peare** [00:18:41]: How long, I mean, what are you thinking?

**William Peare** [00:18:42]: Like, how many hours?

**William Peare** [00:18:44]: A lot?

**Daniel Kalinin** [00:18:45]: Yeah, probably like eight, because I didn't really know what I was supposed to do, but I'm still trying to.

**Daniel Kalinin** [00:18:51]: Yeah, I'm still trying to understand, though, um, how to actually make all this work together.

**Daniel Kalinin** [00:19:00]: Like, I have it built out, but it's almost like Claude, where, like, I did it, but I don't really know how to implement it.

**William Peare** [00:19:07]: When you say implement it, do you mean, like, do it without the help of Claude code, or do you mean, like, actually test it and iterate it?

**William Peare** [00:19:14]: Have you ran the sequence and it worked?

**William Peare** [00:19:18]: No, not really.

**Daniel Kalinin** [00:19:19]: I mean, I don't even know, like, how to...

**William Peare** [00:19:22]: Integrate?

**Daniel Kalinin** [00:19:24]: Yeah.

**Daniel Kalinin** [00:19:24]: I mean, yeah, I don't really...

**Daniel Kalinin** [00:19:27]: Like, it's there, but I don't really see how I'm going to apply it.

**Daniel Kalinin** [00:19:30]: But, like, know I can, but, like, talk...

**William Peare** [00:19:33]: send yourself a Stripe, I mean, once this is published, Stripe payment link yourself with your personal name, kick it through the sequence, or do a test run, go up to the top part of the Zap and, like, get some test data from Stripe, because it should be able to pull your old stuff.

**William Peare** [00:19:51]: Are you looking at Zapier or ClickUp?

**William Peare** [00:19:54]: Oh, I was thinking kicking it off through...

**William Peare** [00:19:57]: No, yeah, Zapier worked.

**William Peare** [00:19:59]: Zapier worked.

**Daniel Kalinin** [00:20:00]: Yeah, I'm not worried about that.

**Daniel Kalinin** [00:20:01]: I'm saying like, I have ClickUp built, which cool, like internal ops.

**Daniel Kalinin** [00:20:04]: I just, I haven't ever used it for anything.

**Daniel Kalinin** [00:20:08]: So I see it's built, but I don't know how I'm going to get it to be useful.

**William Peare** [00:20:13]: Yeah, I mean, main benefit, I would say, is that kind of like your go high level for the funnels.

**William Peare** [00:20:23]: You have one place that you're dealing with for multiple clients.

**William Peare** [00:20:27]: Like you could go in here, you know, you have your main workspace, and then you could kind of pick how you want to do this.

**William Peare** [00:20:32]: Personally, for me, I prefer to have one space, like you have the space that is lead statement.

**William Peare** [00:20:36]: I would keep one space, and then have lists for each client, and then tasks within them.

**William Peare** [00:20:43]: Because you could either choose to have your workspace, which is lead statement, and then you could choose to have a space for each client, which the benefit to that would be, if it's going to have like external facing, if you're going to have customer tasks in there that they're doing, or if you

**William Peare** [00:21:00]: If multiple VAs and you didn't want VAs getting in to like outside of their scope stuff, if they were only working with client X, Y, and Z, and you didn't want them to see client one, two, and three, then you'd want to pivot this and change your hierarchy to the point where your workspace was leadstatement, you had a space for each client, and then you were delegating out permissions for those spaces to the different parties.

**William Peare** [00:21:22]: And then within there, you have lists within here and then there's tasks within the lists.

**Daniel Kalinin** [00:21:29]: Yeah, and in terms of automation, that's also what I wasn't able to crack.

**William Peare** [00:21:35]: Yes, each one is keyed, so like you'll have your workspace ID, and then your space ID, and then you'll have a list ID.

**William Peare** [00:21:45]: So that's the one tricky part about ClickUp when it comes to automation, is that you have to have a very clear plan of where you want the data to go each time, because since you're coding it in or zapping it in, you need to know.

**William Peare** [00:22:00]: You where you want to end up or it's going to mess  up.

**William Peare** [00:22:04]: Yeah.

**William Peare** [00:22:05]: All right.

**Daniel Kalinin** [00:22:05]: I mean, we can talk about ClickUp later, but it's definitely something that I just want to start implementing.

**Daniel Kalinin** [00:22:11]: I just don't know what I don't know.

**Daniel Kalinin** [00:22:13]: And I just know that I have like the base structure of it, if that makes sense.

**Daniel Kalinin** [00:22:16]: But in terms of actually using it, that's like where I'm kind of stuck up on.

**William Peare** [00:22:21]: Did you, so when you ran the Zap, is it pushing tasks into ClickUp?

**William Peare** [00:22:26]: No.

**William Peare** [00:22:27]: So Zap isn't doing anything with ClickUp yet.

**Daniel Kalinin** [00:22:29]: Zap is solely to create the Google Drive file for the new client and then to trigger the onboarding and add them to go high level.

**William Peare** [00:22:35]: Yeah.

**William Peare** [00:22:36]: Okay.

**William Peare** [00:22:37]: And that all did everything you wanted, made the sub account, did it.

**William Peare** [00:22:40]: Beautiful.

**William Peare** [00:22:40]: Yeah.

**William Peare** [00:22:41]: So in terms of this, we can go into the ClickUp later if you want.

**William Peare** [00:22:47]: Let me just get some background.

**William Peare** [00:22:49]: That way I have it for Fathom and for my kind of research and thinking.

**William Peare** [00:22:54]: So you have these tasks in here.

**William Peare** [00:22:55]: You have all this stuff built out.

**William Peare** [00:22:57]: Yeah.

**William Peare** [00:22:58]: But obviously.

**William Peare** [00:23:00]: So you're going to like clear that task and then it's going to be completed.

**William Peare** [00:23:03]: So are you, is this just kind of like the base structure you want to follow?

**William Peare** [00:23:06]: And then this will get replicated for each client that comes in?

**William Peare** [00:23:10]: Pretty much.

**Daniel Kalinin** [00:23:11]: This is like, this is all my fulfillment, like from every step.

**Daniel Kalinin** [00:23:16]: So onboarding market research, all from funnel, copying, creative, funnel building, launching them, optimizing.

**Daniel Kalinin** [00:23:23]: So this, for example, is a weekly cadence.

**Daniel Kalinin** [00:23:26]: Yep.

**Daniel Kalinin** [00:23:26]: Reporting is also a weekly cadence.

**William Peare** [00:23:29]: Yeah.

**Daniel Kalinin** [00:23:31]: And then I guess this is just like a decision library that we have or approved library.

**Daniel Kalinin** [00:23:38]: Yeah.

**Daniel Kalinin** [00:23:39]: So that way I can always just look back at approvals.

**Daniel Kalinin** [00:23:43]: Copy.

**William Peare** [00:23:44]: Yeah.

**William Peare** [00:23:44]: So, I mean, off the top of my head, what I think I would do is, so say we have this client delivery thing.

**William Peare** [00:23:50]: I, first off, does Manus take APIs and you can link Manus straight to other stuff like code?

**William Peare** [00:23:58]: Um.

**Daniel Kalinin** [00:24:01]: They take APIs.

**Daniel Kalinin** [00:24:03]: don't know if you can do it with code.

**Daniel Kalinin** [00:24:05]: I feel like you can't, I want to say.

**Daniel Kalinin** [00:24:07]: Their API definitely is less advanced.

**Daniel Kalinin** [00:24:10]: Okay.

**William Peare** [00:24:11]: So I think after we get through the VA thing, and then we get through financial modeling, when we actually start rolling this out, and you're obviously getting after it on the background, so I could probably just give you some guidance and you can start clicking into it, and then we can kind of, the parts you're getting caught up on, review those.

**William Peare** [00:24:29]: That way, you know, we're not going through stuff you can't figure out on your own.

**William Peare** [00:24:33]: My initial thought would be that in Claude, you grab your Claude API key, because I know you can do it through Claude.

**William Peare** [00:24:40]: You have it scrape this, you have it copy this structure, and then you either put it into Zap or a Claude code that's self-hosted.

**William Peare** [00:24:50]: It doesn't really matter.

**William Peare** [00:24:52]: The one benefit to code, obviously, is that you can just talk through it with iteration.

**William Peare** [00:24:57]: So, like, if you have it coasted in Railway or...

**William Peare** [00:25:00]: We'll just call it hosted.

**William Peare** [00:25:01]: You can host it wherever you want.

**William Peare** [00:25:02]: It's living somewhere.

**William Peare** [00:25:05]: And then you want to make a tweak to it.

**William Peare** [00:25:07]: You can just hop in there and be like, hey, I want to remove X, Y, and Z step.

**William Peare** [00:25:10]: I want to add this.

**William Peare** [00:25:11]: I want to add this.

**William Peare** [00:25:11]: I want to add this blocker.

**William Peare** [00:25:13]: It'll go through there, make all your iterations for you and change it as opposed to you manually having to go through this app and tweak  and manually go through ClickUp and tweak it.

**William Peare** [00:25:21]: But then what I would do probably is I would have every time it gets triggered, would have it replicate this entire stack with the subheading for the list under the client's name or space, depending on where you want to land there.

**William Peare** [00:25:35]: It doesn't really make a difference.

**William Peare** [00:25:37]: And then replicate this entire thing.

**William Peare** [00:25:38]: So you have the client delivery locked as kind of your template.

**William Peare** [00:25:41]: So you can always see what's going on.

**William Peare** [00:25:43]: And then every time this gets triggered, it's going to replicate this entire thing for each client with that, you know, instead of client delivery, it's going to be called, you know, this booster.

**William Peare** [00:25:52]: And then you'll have this same tree to work through every time and store.

**William Peare** [00:25:56]: Yeah.

**Daniel Kalinin** [00:25:56]: I think the way Manus wanted it structured was this.

**Daniel Kalinin** [00:26:00]: Base would be for all my clients.

**Daniel Kalinin** [00:26:02]: So we simpletize the folder.

**Daniel Kalinin** [00:26:05]: And every time there's a new client, there'd just be a new client folder within client delivery, if that makes sense.

**Daniel Kalinin** [00:26:10]: Totally.

**William Peare** [00:26:11]: And that's fine.

**William Peare** [00:26:12]: That works.

**William Peare** [00:26:12]: Yeah.

**William Peare** [00:26:15]: Yeah.

**William Peare** [00:26:16]: No, no.

**Daniel Kalinin** [00:26:16]: And you're saying what I can do is, for example, could it be possible that one of my type form name or questions is like, what's your business name?

**Daniel Kalinin** [00:26:25]: So if someone put in BizBooster, Zap could link to create template, and it creates template, puts the business name there, and that's just automatic?

**William Peare** [00:26:36]: Totally.

**William Peare** [00:26:37]: I can't.

**William Peare** [00:26:39]: You could, through Zapier, it's probably going to be a little clunkier through Zapier than it is through code.

**William Peare** [00:26:43]: Just because it's, you can put coding into Zapier.

**William Peare** [00:26:50]: It's just slightly less robust in terms of what it allows you to do as opposed to it being like hard-coded or even N8N, because N8N, you can just put code nodes.

**William Peare** [00:26:58]: I have only...

**William Peare** [00:27:00]: Use Zapier for things that are Zapier native because it's so easy to use and its UI is so friendly that if you're like, I'm guessing that Google Drive and all these things you did had native Zapier nodes.

**William Peare** [00:27:13]: So if you're working with something that's completely Zapier native, it's super easy, but you are limited somewhat to the filters that are kicked out in the packet.

**William Peare** [00:27:24]: Because if it's not in the packet, you can't really filter and trigger off of it.

**William Peare** [00:27:29]: Where with NADN or with Cloud Code, you're parsing that data so you can teach it and train it however you want it parsed.

**William Peare** [00:27:36]: I'm assuming, yeah, like if you had a field in there, it's probably going to kick out everything in that field.

**William Peare** [00:27:42]: So if you had that field in type form, it's probably going to have business name and then you can tell ClickUp map this to, you know, this.

**Daniel Kalinin** [00:27:50]: Yeah, so create folder, this would be a folder, by the way, right?

**Daniel Kalinin** [00:27:55]: Like this thing right here?

**William Peare** [00:27:56]: Yes.

**Daniel Kalinin** [00:27:57]: Okay, so create folder can probably confirm.

**Daniel Kalinin** [00:28:00]: It's just some sort of space, so client delivery, yeah, I feel like that should be possible, where it just auto-creates everything.

**William Peare** [00:28:07]: 100%.

**William Peare** [00:28:07]: It's definitely easily possible.

**Daniel Kalinin** [00:28:09]: The main thing that got me really stumped was, I know, for example, like, it had me add custom fields.

**William Peare** [00:28:20]: Yes.

**Daniel Kalinin** [00:28:20]: I wouldn't know how to, well, one, I don't even know how to add the value, like client.

**Daniel Kalinin** [00:28:30]: Right there.

**William Peare** [00:28:32]: So this would just be the value?

**William Peare** [00:28:35]: Yeah, but so this is a drop-down option.

**William Peare** [00:28:39]: When you made the custom field, did it give you an opportunity to select what type of data field it was?

**Daniel Kalinin** [00:28:45]: Yeah, think Manus wanted it to be drop-down, but I mean, if it's going to be a folder specific to a client, it probably should just be text, right?

**William Peare** [00:28:52]: Text, correct.

**William Peare** [00:28:53]: So, like, drop-down, that would make sense if, say, you had, like, you know, MedSpa, you know, if you had, like...

**William Peare** [00:29:00]: Three different types of clients and they always fit in this.

**William Peare** [00:29:02]: I'd wanted to drop down with only those selected options, essentially, and then it would just kick through there.

**William Peare** [00:29:11]: Got it.

**William Peare** [00:29:11]: I wonder if...

**William Peare** [00:29:12]: you're trying to pull a name, you definitely want it to be text.

**William Peare** [00:29:15]: That way, it's just copying whatever they put in.

**William Peare** [00:29:17]: Yeah.

**Daniel Kalinin** [00:29:18]: And I would just basically create the folder and then I can have Zaps just update the custom fields like right here based on certain questions.

**Daniel Kalinin** [00:29:28]: So if they put their name as like Ryan Lynch or something like that, it would update.

**Daniel Kalinin** [00:29:32]: I would do this and it could update the client, whatever, right?

**William Peare** [00:29:38]: Oh, yeah.

**William Peare** [00:29:39]: Okay, cool.

**William Peare** [00:29:40]: That would probably make things a lot easier.

**Daniel Kalinin** [00:29:42]: And then again, like, we don't have to do this today because I know it's not on agenda, but also just understanding how my team would interact with everything in here.

**Daniel Kalinin** [00:29:52]: Yeah.

**Daniel Kalinin** [00:29:53]: Because, yeah, like, the first one's going to be a VA that's just going to be the low-hanging fruit.

**Daniel Kalinin** [00:29:58]: And it's just like, what...

**Daniel Kalinin** [00:30:00]: They do, how do I make sure they understand everything that they need to do, have a view for them where they can't miss a thing, so on and so forth?

**William Peare** [00:30:11]: Yeah, so I mean, most of that, you can store documents in here, obviously, or you could have your training SOPs somewhere else.

**William Peare** [00:30:18]: But as the team grows and as you get more people, I would update the code or the ZAP or however it's getting into there.

**William Peare** [00:30:25]: It's going to be able to pull the data from ClickUp.

**William Peare** [00:30:27]: So say you have VA1, you have Copywriter, you have other person 3.

**William Peare** [00:30:33]: I would set it up on the front end where it's like, hey, these are all the tasks, and then you're going to tell it, like, all these tasks get assigned to this person.

**William Peare** [00:30:39]: These are the due dates I like on them, and you can just have it as a leading indicator, like, date, today's date, plus 3, today's date, plus 5.

**William Peare** [00:30:46]: And it'll go in there, assign it to the parties who are relevant, blah, blah, blah, blah, blah, go all the way down the list.

**William Peare** [00:30:52]: And then they, A, can either go through this whole folder, or when you're just in here, you can go to the My Task.

**William Peare** [00:31:00]: It's assigned to me on the left, and they'll see all their tasks by due date, and they can kind of just work through them as needed.

**William Peare** [00:31:07]: And then there's numerous stages.

**William Peare** [00:31:09]: You know, they can have a complete date for review, for Daniel review, for copywriter review.

**William Peare** [00:31:13]: Like, you can set different stages.

**William Peare** [00:31:15]: And once they click it off to that, it'll push it to the next person like, hey, Daniel, this is ready for a final copyright review.

**William Peare** [00:31:20]: Or, hey, copywriter, all ICP documents are done.

**William Peare** [00:31:24]: It's ready to kick off on your end.

**William Peare** [00:31:27]: Yeah.

**Daniel Kalinin** [00:31:27]: I feel like I did those stages as well.

**Daniel Kalinin** [00:31:31]: These automations, which, yeah, so I have recurring task automations here.

**Daniel Kalinin** [00:31:36]: That's for the stuff that's going to have to be done weekly, so like new copy or whatever.

**Daniel Kalinin** [00:31:43]: I think this stuff is like notifications whenever someone's like high risk.

**Daniel Kalinin** [00:31:47]: Yeah.

**Daniel Kalinin** [00:31:47]: And I also want to say I did statuses, like maybe task statuses.

**Daniel Kalinin** [00:31:52]: Yes, you did.

**William Peare** [00:31:53]: Yeah.

**William Peare** [00:31:54]: None of those are native.

**William Peare** [00:31:55]: Well, most of them aren't native, at least.

**William Peare** [00:31:57]: Is that a problem?

**William Peare** [00:31:59]: No.

**William Peare** [00:32:00]: Oh, not at all.

**William Peare** [00:32:00]: That's how you want it to be.

**William Peare** [00:32:01]: You want to customize it.

**William Peare** [00:32:02]: That's the point of this.

**William Peare** [00:32:03]: So then you could go, you know, a step further.

**William Peare** [00:32:05]: I think you had a couple automations, like you had the internal review clicking off.

**William Peare** [00:32:09]: So you can just have the automation, you know, content done or whatever, and then it would automatically click over an automation to hit the copywriter.

**William Peare** [00:32:18]: Hey, your stage is ready.

**William Peare** [00:32:19]: Fly.

**William Peare** [00:32:20]: You go fly.

**William Peare** [00:32:21]: Yeah.

**William Peare** [00:32:22]: Okay.

**William Peare** [00:32:23]: Yeah.

**William Peare** [00:32:23]: And I mean, the big benefit to this, because there's so many different things you can do for lists and tasks.

**William Peare** [00:32:27]: It's just not like, this is like groundbreaking in terms of making lists or tasks.

**William Peare** [00:32:31]: There's a million ways to do this.

**William Peare** [00:32:32]: The nice part is it gives one easy place for you as the high-level person to hop in, look at 12 different accounts, look at what stage they're at, look how many outstanding tasks are going on.

**William Peare** [00:32:42]: You can easily look and see who's not doing their tasks, who's behind on their tasks in one easy place.

**William Peare** [00:32:48]: Yeah.

**William Peare** [00:32:50]: It's also got a pretty nice UI.

**William Peare** [00:32:52]: Yeah.

**William Peare** [00:32:54]: Yeah.

**William Peare** [00:32:55]: That's kind of the use case for it.

**William Peare** [00:32:58]: Anything else that I should explore, like...

**Daniel Kalinin** [00:33:00]: Like, I know, I don't know if there's anything to do with Planner or AI or Teams, Docs, Dashboards.

**William Peare** [00:33:06]: So the dashboards I haven't played with much or the goals, Planner is literally just a calendar.

**William Peare** [00:33:12]: So it's just all your ClickUp stuff into a calendar.

**William Peare** [00:33:15]: Essentially, it can, you know, it'll take your stuff.

**William Peare** [00:33:19]: It'll take your calendar that's linked.

**William Peare** [00:33:20]: You can have AI look at it.

**William Peare** [00:33:22]: It's essentially just a calendar.

**William Peare** [00:33:25]: I haven't used the AI within this a crazy amount.

**William Peare** [00:33:29]: I do like the whiteboarding.

**William Peare** [00:33:31]: Whiteboarding is decent.

**William Peare** [00:33:34]: The Docs, I have not personally used it to store Docs.

**William Peare** [00:33:38]: Every use case I've used for ClickUp, it's been part of a tech stack.

**William Peare** [00:33:41]: So I've just had it integrated to Myro and Google Sheets and everything else where we were storing the data.

**William Peare** [00:33:48]: And it would just provide links like, oh, this is the reference doc for this.

**William Peare** [00:33:52]: I haven't used it to natively store Docs.

**William Peare** [00:33:54]: I know you could, but you're probably better off since you already have Google Drive and all.

**William Peare** [00:34:00]: And it's got a super robust API is having an internal lead statement.

**William Peare** [00:34:05]: Your SOPs all live and drive.

**William Peare** [00:34:08]: And then as you're onboarding new people, you could even have a list or a folder in here that's onboarding for your hire.

**William Peare** [00:34:15]: So they would go through this 12-step process upon hire like, hey, you need to watch these 12 videos that I made.

**William Peare** [00:34:22]: You need to read these SOPs.

**William Peare** [00:34:24]: Then you need to have, after three days, a training session with me to ask questions.

**William Peare** [00:34:28]: And then you go to this phase.

**William Peare** [00:34:29]: You can use it to structure your onboarding as well.

**Daniel Kalinin** [00:34:33]: Got it.

**Daniel Kalinin** [00:34:34]: Any room for wikis?

**Daniel Kalinin** [00:34:35]: I know wikis are like reference points, I guess, within ClickUp.

**Daniel Kalinin** [00:34:39]: I have not dealt with the wikis.

**William Peare** [00:34:41]: So I can't, I can't give you a reference on that.

**William Peare** [00:34:44]: Um, my use case for it has primarily been running and planning projects.

**William Peare** [00:34:50]: Um, so I have not used it as like my main source of truth for documentation and stuff.

**William Peare** [00:34:56]: I've only used it as a piece of the puzzle.

**William Peare** [00:34:58]: Okay.

**William Peare** [00:34:59]: Yeah.

**William Peare** [00:35:00]: But, worth looking into.

**William Peare** [00:35:03]: Okay.

**William Peare** [00:35:04]: Yeah, the next thing I would do for you on this, the next, like, step I would take is set up the, like, get it mapped out to something else.

**William Peare** [00:35:12]: So you have all those templates mapped out, the folder that Man has had you make.

**William Peare** [00:35:16]: And then I would set that up so it's auto-replicating upon those triggers.

**William Peare** [00:35:20]: You know, set up another Zap.

**William Peare** [00:35:22]: Yeah.

**William Peare** [00:35:22]: Mapped out as in what?

**William Peare** [00:35:25]: I mean, you're either going to have to do it manually to put it into the Zap, or I would get the API key from this link it to cloud code.

**William Peare** [00:35:32]: I would ask code to scrape that, take all those statuses, tell it, you know, hey, this is my base.

**William Peare** [00:35:38]: This is my base folder.

**William Peare** [00:35:40]: This is what they're going to go through every single time.

**William Peare** [00:35:42]: My use case is that when it gets triggered, I'm going to be running a Zap.

**William Peare** [00:35:45]: It's going to take their name.

**William Peare** [00:35:46]: It's going to automatically recreate this and get that mapped out.

**William Peare** [00:35:51]: Okay.

**William Peare** [00:35:52]: Yeah.

**William Peare** [00:35:53]: That's how I would run it.

**William Peare** [00:35:54]: Because once you have that done, you know, you're going to have the Google Drive created.

**William Peare** [00:35:58]: You're going to have the email sent out.

**William Peare** [00:36:00]: They're going to be in GoHighLevel, and then they're going to be in ClickUp.

**William Peare** [00:36:02]: You're at the 90% line there with what you need to roll to probably $50,000, $75,000 a month.

**William Peare** [00:36:08]: At that point, that's a pretty robust system.

**William Peare** [00:36:11]: And then we're really looking into how we're training your people to run it at that point.

**Daniel Kalinin** [00:36:17]: Yeah, I think, too, another thing that I want to show you is I was trying to figure out how I can be less reliant on my clients in terms of filming, because that's also something that really kills me.

**Daniel Kalinin** [00:36:35]: So I was looking into Higgs Field and Kling AI for AI video generation.

**Daniel Kalinin** [00:36:43]: And I don't know if you're going to be able to hear this, but this is one client where we do home service ads for him.

**Daniel Kalinin** [00:36:53]: I can't hear it, but that's okay.

**William Peare** [00:36:57]: Yeah, but...

**William Peare** [00:36:58]: Did he actually make that, or AI?

**William Peare** [00:37:00]: I made it with AI.

**Daniel Kalinin** [00:37:02]: It's like, this is for home service bookkeepers, or home service bookkeeping.

**Daniel Kalinin** [00:37:08]: So just made a bunch of home service looking guys.

**Daniel Kalinin** [00:37:15]: Yeah, and it spits them out very fast.

**Daniel Kalinin** [00:37:17]: So I think part of my delivery moving forward is going to be like, I don't want to wait for my clients.

**Daniel Kalinin** [00:37:22]: I can give them scripts, but while they record that, I can probably create a good amount of AI stuff and start just testing out different offers with them.

**William Peare** [00:37:33]: Huh, so you would get their face, or how would it be then?

**Daniel Kalinin** [00:37:42]: I don't even need their face.

**Daniel Kalinin** [00:37:43]: I mean, like, if my ICP is going to be a home service guy, like, the best thing I can do is put a home service guy on the screen.

**Daniel Kalinin** [00:37:51]: Because that's just going to subconsciously make a lot of blue-collar guys stop the scroll because they relate to it, so on and so forth.

**William Peare** [00:37:57]: Right.

**William Peare** [00:37:59]: Yeah.

**William Peare** [00:38:01]: And so I guess for some reason, I thought that the home, like the videos they were doing had to be them pitching.

**William Peare** [00:38:09]: Ideally, it would be them.

**Daniel Kalinin** [00:38:12]: But, you know, like one client, for example, he's doing home service bookkeeping, but he looks like a nerd.

**Daniel Kalinin** [00:38:19]: And it's like, you know, it's hard to resonate with a blue-collar guy if you look like a nerd.

**William Peare** [00:38:25]: Yes.

**William Peare** [00:38:26]: Yes.

**William Peare** [00:38:27]: Absolutely.

**Daniel Kalinin** [00:38:28]: Other clients, like this woman right here, she, let me see something.

**Daniel Kalinin** [00:38:38]: Boom.

**Daniel Kalinin** [00:38:39]: She has a really Asian accent.

**Daniel Kalinin** [00:38:42]: So whenever I'd like, I'd try to get her to say something, there's like a lot of mistakes and all that stuff and like mispronunciation.

**Daniel Kalinin** [00:38:49]: So I'd cling just basically replicate her and we create, like I create, this is all AI.

**Daniel Kalinin** [00:38:56]: So it's like best tech strategies, your seven figure business owners.

**William Peare** [00:39:03]: That is hilarious.

**William Peare** [00:39:05]: Expensive?

**Daniel Kalinin** [00:39:09]: That is a good question.

**Daniel Kalinin** [00:39:12]: I don't think it's too expensive.

**Daniel Kalinin** [00:39:13]: think through volume it will be, but if it helps me roll out my offer fast or these people's offers fast.

**William Peare** [00:39:21]: That's your biggest bottleneck.

**Daniel Kalinin** [00:39:22]: Yeah, and I think, too, what I can do, if I maybe roll out offers faster, I can get case studies and results a lot faster, too.

**Daniel Kalinin** [00:39:35]: I'm at a point right now where $2,000 really isn't  for what I do, and I spoke to some of the guys at that mastermind, and they were like, yeah, man, you've got to increase those prices because you're just not going to have the margin that you want, and they're right because, you know, as soon as I start making hires, like, know, yay and be like a creative strategist to actually generate these for me or whatever, you know, my margin is going to get sliced a good chunk.

**William Peare** [00:39:59]: Yeah.

**Daniel Kalinin** [00:40:00]: If I can add $1,000 per client, and let's say my AI cost for that client is going to be like, I don't know, $200, $300 a month.

**Daniel Kalinin** [00:40:12]: I mean, I still have so much more padding room.

**Daniel Kalinin** [00:40:16]: So yeah, I guess I was just trying to work on speeds and implementation, if that makes sense.

**Daniel Kalinin** [00:40:22]: 100% makes sense, yeah.

**William Peare** [00:40:23]: No, I think this is a fantastic strategy.

**William Peare** [00:40:26]: I've never...

**William Peare** [00:40:26]: That is wild.

**William Peare** [00:40:28]: And they look pretty freaking good.

**William Peare** [00:40:30]: Yeah, it's terrifying, in fact.

**William Peare** [00:40:32]: And it's only going to get better.

**Daniel Kalinin** [00:40:34]: So yeah, I mean, I'm happy with it.

**Daniel Kalinin** [00:40:40]: And their hand movements, I know I'm interrupting, but it's just, it's crazy, because I haven't done this before, and it's just like, if it says click the link below, it'll literally just go like, click the link below.

**Daniel Kalinin** [00:40:53]: That's insane.

**Daniel Kalinin** [00:40:54]: Yeah, that's really good.

**William Peare** [00:40:56]: So I mean, like, even for myself, if I didn't want to do like a bunch of...

**William Peare** [00:41:00]: LinkedIn video content, I could just upload myself and tell it what I want to do, and it'll just be spitting out videos for me, because I just do posts right now, but videos resonate better.

**William Peare** [00:41:09]: So I could literally just have it cranking out two videos a week for me.

**William Peare** [00:41:13]: Yeah, yeah.

**Daniel Kalinin** [00:41:15]: What I learned was it's not good to, like this is where you prompt shot it, I guess.

**Daniel Kalinin** [00:41:23]: It's not good to add like a million words and make it like 15 seconds long, because that's the max it does.

**Daniel Kalinin** [00:41:31]: Because it ends up like going out of lip sync.

**Daniel Kalinin** [00:41:34]: Yeah.

**Daniel Kalinin** [00:41:35]: So I've been keeping it like sub 10 seconds, and yeah, it's really fire.

**Daniel Kalinin** [00:41:42]: mean, like, this is the first time last night where I actually try to prompt it as well, because I want to see if it was like, if it did anything.

**Daniel Kalinin** [00:41:49]: And yeah, and it's just like, it's fire.

**William Peare** [00:41:57]: Yeah, that's wild.

**William Peare** [00:41:59]: Now, do you pay per...

**William Peare** [00:42:00]: Pay video, pay per month?

**William Peare** [00:42:01]: Explain the model to me.

**William Peare** [00:42:03]: It's a credit purchase system.

**Daniel Kalinin** [00:42:05]: So I just purchase credits and every generation is a certain amount based on the length of the video.

**William Peare** [00:42:12]: Okay.

**William Peare** [00:42:13]: And the resolution.

**William Peare** [00:42:15]: But yeah.

**William Peare** [00:42:16]: Man, I'm trying it for myself.

**William Peare** [00:42:19]: I'll tell you that.

**William Peare** [00:42:20]: try it.

**Daniel Kalinin** [00:42:21]: But yeah, this should make it a lot easier for me.

**Daniel Kalinin** [00:42:23]: And I know Higgs field, which is going to be kind of the next step that I'm probably going to take with Cloud Code once I understand it.

**Daniel Kalinin** [00:42:31]: Um, what do you call it?

**Daniel Kalinin** [00:42:38]: They, uh, MCP.

**Daniel Kalinin** [00:42:41]: Yeah, so they have a Cloud Code MCP.

**Daniel Kalinin** [00:42:43]: Yeah.

**Daniel Kalinin** [00:42:44]: And I'm guessing what could happen would be I can feed Cloud Code the scripts and it just generates a crap load of videos or I can probably train it on a lot of the scripts that I write.

**Daniel Kalinin** [00:42:57]: Yes.

**Daniel Kalinin** [00:42:58]: Um.

**Daniel Kalinin** [00:43:00]: But yeah, I mean, if there's going to be a point where I can automate like 30 videos in like an hour, I mean, my whole bottleneck of speed is going to be gone completely.

**Daniel Kalinin** [00:43:15]: Yeah, it's wild.

**William Peare** [00:43:16]: Yeah.

**Daniel Kalinin** [00:43:18]: That is great.

**Daniel Kalinin** [00:43:20]: I spoke to, and I think I might have told you this, but this might be a guy that you want to kind of follow, Cameron England.

**Daniel Kalinin** [00:43:31]: I met him, he was a speaker at the Mastermind, and then I went to the Brickell City Center Mall, and he was just chilling there too, so I got to speak with him again.

**Daniel Kalinin** [00:43:42]: And he's like, he's that guy with like the employee kind of like office thing where like his little AI employees run around and shouldn't like work.

**Daniel Kalinin** [00:43:51]: But he's literally just going into businesses right now, pitching like 30 to 50K and just automating.

**Daniel Kalinin** [00:44:00]: Everything that they do in, like, an instant.

**Daniel Kalinin** [00:44:03]: And, yeah, I mean, he basically said, like, if you don't get on top of this within the next, like, 12 to 24 months, you are, like, cooked.

**Daniel Kalinin** [00:44:10]: Big time.

**William Peare** [00:44:11]: Yeah.

**William Peare** [00:44:12]: Yeah.

**William Peare** [00:44:14]: Yeah, I'm following him for sure.

**William Peare** [00:44:16]: Harvey England.

**William Peare** [00:44:18]: Yeah, I guess that's his, like, thing now.

**Daniel Kalinin** [00:44:20]: Like, if I were Harvey England or, like, Clavicular, I think, was another guy.

**Daniel Kalinin** [00:44:24]: Yeah, like, this is how I would automate my stuff.

**Daniel Kalinin** [00:44:26]: But, yeah, he was, like, he was, like, there's a pyramid of, like, employees and it's, like, like, people that do repetitive tasks and, like, and managers and, like, CEOs.

**Daniel Kalinin** [00:44:38]: And he's, like, soon the bottom layer of that pyramid is going to be gone completely.

**William Peare** [00:44:44]: Yeah.

**William Peare** [00:44:44]: of AI.

**Daniel Kalinin** [00:44:45]: And the only way to protect yourself is to be, like, a, I mean, he said operators are going to get cooked later down the line, too, as well.

**Daniel Kalinin** [00:44:55]: He said the only way to protect yourself is to be, like, that business owner and just leverage everything.

**Daniel Kalinin** [00:45:00]: That way you kind of like orchestrate it and you can't really get replaced in that way, at least for now.

**William Peare** [00:45:06]: Yeah, absolutely.

**William Peare** [00:45:07]: Oh, he's out of England.

**Daniel Kalinin** [00:45:09]: Yeah, he lives in Dubai, but they started bombing his .

**Daniel Kalinin** [00:45:13]: So he went to Miami and he's shown there for now, but I think he's going to New York after Miami just to chill for a bit.

**Daniel Kalinin** [00:45:23]: Nice.

**William Peare** [00:45:24]: Yeah.

**William Peare** [00:45:24]: Okay.

**William Peare** [00:45:24]: So he's not from America.

**Daniel Kalinin** [00:45:27]: No, no.

**Daniel Kalinin** [00:45:28]: He's from England.

**Daniel Kalinin** [00:45:30]: Nice.

**William Peare** [00:45:31]: Yeah.

**William Peare** [00:45:33]: Oh, yeah.

**William Peare** [00:45:35]: Yeah, he looks good.

**William Peare** [00:45:38]: Okay.

**William Peare** [00:45:39]: License and scale is the name.

**William Peare** [00:45:41]: Yeah.

**Daniel Kalinin** [00:45:43]: So he's been on this a while.

**Daniel Kalinin** [00:45:45]: I don't think so for a while.

**Daniel Kalinin** [00:45:48]: I think he just found a gap in the market because his thing was he has a med spot agency and they do like a couple of six.

**Daniel Kalinin** [00:46:00]: Six figures a month.

**Daniel Kalinin** [00:46:02]: So his license and scale was his like coaching program where he just helped agency owners scale, basically just copying off his model.

**Daniel Kalinin** [00:46:10]: And then I think he just found a gap in AI and automation where like a lot of agencies were kind of running things old way, manual, blah, blah, blah.

**Daniel Kalinin** [00:46:22]: So now he does like a B2B kind of ops offer.

**Daniel Kalinin** [00:46:24]: Yeah, that's great.

**William Peare** [00:46:28]: Yeah.

**William Peare** [00:46:28]: Yeah.

**William Peare** [00:46:29]: He looks good.

**William Peare** [00:46:31]: Okay.

**William Peare** [00:46:33]: We'll focus.

**William Peare** [00:46:34]: Let's get you through your SOP.

**William Peare** [00:46:36]: I read the, I read the job description.

**William Peare** [00:46:40]: Good.

**William Peare** [00:46:40]: I mean, that was an internal one based on some of the wording, but the structure's there.

**William Peare** [00:46:44]: Correct.

**William Peare** [00:46:46]: Did, where are you at on cold outreach?

**Daniel Kalinin** [00:46:48]: Um, that's one of the goals for today.

**Daniel Kalinin** [00:46:52]: I need to create the gamma doc.

**Daniel Kalinin** [00:46:54]: Um, and then from there, I want to get cloud code.

**Daniel Kalinin** [00:47:01]: To be able to scrape leads for me, because I know, and I don't know if I need to connect this to Appify or something, or if I can do like a skill or something, I don't really know how that works.

**William Peare** [00:47:10]: Yeah, so what you're going to do, are you set up in Google Console already?

**Daniel Kalinin** [00:47:15]: Yeah, for my business email, yeah.

**William Peare** [00:47:19]: Yeah, so Google Cloud Console, you're going to go in there and you're going to get API keys from Google.

**William Peare** [00:47:25]: There's a fuckload, because Google owns a bunch of stuff.

**William Peare** [00:47:28]: But you're going to need to give it an API key and scopes to Google, and then it's going to API straight through your Google and scrape away.

**William Peare** [00:47:37]: And then essentially you need to pick where you want them to go.

**William Peare** [00:47:45]: Like you could put them just into a database, you could have them go to a spreadsheet, you could build a custom UI that's hosted somewhere, you could have them go into GoHuntLevel.

**William Peare** [00:47:53]: Or like, that's really a matter of personal preference, it's not really a right or wrong.

**William Peare** [00:47:58]: But what you're going to do then.

**William Peare** [00:48:00]: There is get the API key, tell it what you want to do, tell it what your target, your ICP is, tell it how you want the data stored.

**William Peare** [00:48:09]: It's a decent process, probably another six to eight, like you put it on this to really get it rolling.

**William Peare** [00:48:15]: But after we discussed that, I ran through it just to see because I hadn't built that out myself.

**William Peare** [00:48:20]: And yeah, 100% doable.

**William Peare** [00:48:23]: It's all just done through Google is the easiest way.

**Daniel Kalinin** [00:48:27]: Yeah, I think last few days, my main focus was click-up and onboarding.

**Daniel Kalinin** [00:48:33]: I think I'm good with onboarding at this point.

**Daniel Kalinin** [00:48:36]: I just need to create the funnel.

**Daniel Kalinin** [00:48:40]: reinforce everything.

**Daniel Kalinin** [00:48:42]: Man has kept telling me, for example, my welcome email was too repetitive, but I want that to be repetitive because I don't want people to then ask me, where am I supposed to get my Stripe link, where is the onboarding form, all that stuff.

**Daniel Kalinin** [00:48:54]: So, yeah, I'd rather do that.

**William Peare** [00:48:56]: common denominator.

**William Peare** [00:48:57]: You're like, I just want to make this.

**William Peare** [00:48:59]: Keep it simple.

**William Peare** [00:48:59]: simple.

**Daniel Kalinin** [00:49:03]: Yeah.

**Daniel Kalinin** [00:49:03]: And ClickUp was the other one, which I guess I'll figure out what I need to do to finalize just some zaps and stuff like that.

**Daniel Kalinin** [00:49:12]: So at this point, it's just going to be finish off the GammaDoc for tax firms.

**Daniel Kalinin** [00:49:19]: I'll see how I can set up cloud code to just repeatedly just scrape me the leads that I need.

**Daniel Kalinin** [00:49:25]: So if I branch into like B2B consultants or something like that, it can do that as well.

**Daniel Kalinin** [00:49:33]: And from there, yeah, I'll send outreach.

**Daniel Kalinin** [00:49:35]: I know later down the line, I can probably just have VA outreach to these people on my behalf, or maybe just claw to can connect to Instagram.

**Daniel Kalinin** [00:49:48]: It can maybe send stuff through Gmail, through my Gmail, so it's outreach to these people with the document.

**Daniel Kalinin** [00:49:56]: So I'll figure out how to automate that after I've kind of gotten.

**Daniel Kalinin** [00:50:00]: Proof of concept, and I got people booking calls with me.

**Daniel Kalinin** [00:50:02]: Totally.

**William Peare** [00:50:03]: Absolutely.

**William Peare** [00:50:04]: I see, and I got something out of this.

**William Peare** [00:50:06]: I'm going to start on, I'm going to go with the Higgs field, I think, open art.

**William Peare** [00:50:13]: Yeah.

**William Peare** [00:50:15]: No, no, no, no.

**Daniel Kalinin** [00:50:16]: I don't think, I think that's like, they got some good SEO.

**Daniel Kalinin** [00:50:20]: They got some good pay-per-click or whatever thing Bobby got going on Google.

**William Peare** [00:50:24]: I see it.

**William Peare** [00:50:25]: Yeah.

**Daniel Kalinin** [00:50:27]: Higgsfield.ai is the domain.

**Daniel Kalinin** [00:50:31]: And then what else did I want to say?

**Daniel Kalinin** [00:50:36]: Yeah.

**William Peare** [00:50:37]: What else you got?

**Daniel Kalinin** [00:50:39]: Yeah.

**Daniel Kalinin** [00:50:40]: So I understand that I need a outreach pipeline now.

**Daniel Kalinin** [00:50:44]: Do you recommend doing that through ClickUp or GoHighLevel?

**Daniel Kalinin** [00:50:49]: Probably GoHighLevel.

**William Peare** [00:50:51]: ClickUp's good.

**William Peare** [00:50:51]: for...

**William Peare** [00:50:52]: Not really.

**William Peare** [00:50:53]: You kind of saw how it's UI is.

**William Peare** [00:50:55]: It's really good for task-based stuff.

**William Peare** [00:50:57]: It would be a  to navigate it.

**William Peare** [00:51:00]: Where Go High Level, you could have your own pipeline and then just have it with your, like, elite, I believe they're called opportunities in Go High Level.

**William Peare** [00:51:08]: You can just have them staged there.

**William Peare** [00:51:10]: That way, when it's doing its scraping, it can be like, oh, you got 280 new qualified people.

**William Peare** [00:51:16]: And then you also need to pick the tempo you're pulling at.

**William Peare** [00:51:19]: Like, do you want those to pull daily, once a day?

**William Peare** [00:51:21]: Is it pulling once a week?

**William Peare** [00:51:22]: That way, you have a week to sort them.

**William Peare** [00:51:23]: Because depending on how much you refine the, what it's scraping for, you could get a fuckload.

**William Peare** [00:51:34]: Like, more than you want to actually go through.

**William Peare** [00:51:36]: So I would start, like, super, super, super selective.

**William Peare** [00:51:40]: And then if you're like, okay, it only got me 12 people, I know with conversion rates that's going to suck, then ramp it up.

**William Peare** [00:51:45]: Because if you start too broad, I mean, you could probably put a limit and tell it's top after 1,000, but you could get so many.

**William Peare** [00:51:51]: Yeah, okay.

**William Peare** [00:51:52]: So I would put them in Go High Level.

**William Peare** [00:51:54]: That way, you can sort them.

**William Peare** [00:51:56]: Like, oh, first outreach done.

**William Peare** [00:51:57]: Second outreach.

**William Peare** [00:51:58]: I've done my fifth outreach.

**William Peare** [00:51:59]: Now they're either one two.

**William Peare** [00:52:00]: We're lost.

**William Peare** [00:52:00]: It'll be easier for you to track it and go high level.

**William Peare** [00:52:03]: Okay.

**Daniel Kalinin** [00:52:05]: Yep.

**William Peare** [00:52:05]: And I'm assuming I haven't done much with API with go high level, but it's a very popular one.

**William Peare** [00:52:10]: So I'm sure there's tons.

**William Peare** [00:52:11]: That's probably going to be very easy for you to do.

**William Peare** [00:52:14]: And I would, Zapier's easier, but it is going to get expensive with scale, which isn't necessarily, you're not huge on like everything has to be cost cutting, but the more you're getting into it, I would start leaning more into cloud code than I would Zapier because it's going to give you more customization and less cost overall, because you could have like a railway server for $5 a month that runs all of these and you already pay for your cloud subscription, as opposed to you could easily get into hundreds a month with Zapier.

**William Peare** [00:52:49]: And the sooner you get more comfortable with code, it's just going to be easier for you.

**William Peare** [00:52:53]: Yeah.

**William Peare** [00:52:53]: So Okay.

**William Peare** [00:52:57]: Now I got your email.

**William Peare** [00:52:59]: What's your

**William Peare** [00:53:00]: So you're going to start the outreach.

**William Peare** [00:53:02]: At that point, what are you thinking, time to get this VA on and time to launch this puppy?

**William Peare** [00:53:10]: Because this is really your next step.

**William Peare** [00:53:12]: I think once I just see someone coming in.

**Daniel Kalinin** [00:53:17]: Yeah, once I know that client acquisition is kind of like in my control, that's when I'll do it.

**Daniel Kalinin** [00:53:26]: Like if I know that if I do, I don't know, a thousand outreaches a month to tax firms with over 50 Google reviews or something like that, and I can sign like six or something, that's when I would probably want the VA going in.

**Daniel Kalinin** [00:53:44]: I'll probably have them.

**Daniel Kalinin** [00:53:46]: I might have one just solely focus on outreach.

**Daniel Kalinin** [00:53:49]: might have one just solely focus on delivery, client delivery, or like just admin stuff.

**Daniel Kalinin** [00:53:55]: But yeah, I think once everything's kind of predictable for me, then I'll do.

**Daniel Kalinin** [00:54:00]: Okay.

**Daniel Kalinin** [00:54:01]: Copy that.

**Daniel Kalinin** [00:54:02]: good news, by the way, I got my first PIF on that 6K.

**William Peare** [00:54:06]: You did?

**Daniel Kalinin** [00:54:08]: Yeah.

**Daniel Kalinin** [00:54:08]: Yeah.

**Daniel Kalinin** [00:54:09]: So that felt good.

**Daniel Kalinin** [00:54:11]: How many did you have to pitch before you locked it?

**Daniel Kalinin** [00:54:15]: Only two.

**Daniel Kalinin** [00:54:16]: I mean, the first one, he closed too, but he closed on a payment plan and he was a  of a client.

**Daniel Kalinin** [00:54:22]: And that's also something for me to learn.

**Daniel Kalinin** [00:54:25]: I need to start vetting people a bit better, even like the micro stuff.

**Daniel Kalinin** [00:54:30]: Because when I hate a client, I hate my business.

**William Peare** [00:54:33]: Yeah.

**Daniel Kalinin** [00:54:34]: He needed like a payment plan because he was like, I just paid like 25K to host my mastermind.

**Daniel Kalinin** [00:54:40]: So I'll do like 1.5 right now and then three later this month and three or 1.5 later this month and then three next month.

**Daniel Kalinin** [00:54:46]: But on that call, he mentioned that he had like four agencies that he worked with in the last three months.

**Daniel Kalinin** [00:54:52]: And I guess I like, I overlooked that.

**Daniel Kalinin** [00:54:54]: But my first question should have been, how did you cycle through four agencies in three months?

**Daniel Kalinin** [00:54:59]: And it's.

**Daniel Kalinin** [00:55:00]: Because he's very stuck up.

**Daniel Kalinin** [00:55:02]: He wants to do his own thing.

**Daniel Kalinin** [00:55:03]: It was like a fitness coaching offer for execs and entrepreneurs.

**Daniel Kalinin** [00:55:10]: And he wanted the whole thing to be like, implement my dad bod sculptor system to blah, blah, blah.

**Daniel Kalinin** [00:55:17]: And I'm like, dude, these people don't know you.

**Daniel Kalinin** [00:55:19]: What is a dad bod sculptor system?

**Daniel Kalinin** [00:55:21]: Explain what you're actually going to do to them.

**Daniel Kalinin** [00:55:22]: And I gave him like references on like B2B coaching offers.

**Daniel Kalinin** [00:55:25]: Like, you know, we're going to, we'll implement like a health performance system so that you, you know, operate at peak performance and stuff like that, blah, blah, blah.

**Daniel Kalinin** [00:55:33]: So I'm like, this is how it should be modeled off of.

**Daniel Kalinin** [00:55:35]: He's like, no, I wanted to be dad bod sculptor.

**Daniel Kalinin** [00:55:37]: So it was just like, it was a nightmare.

**William Peare** [00:55:40]: Yeah, that sounds like a nightmare.

**William Peare** [00:55:43]: Yeah, that sounds fun.

**Daniel Kalinin** [00:55:45]: Thank God we, it was the easiest parting.

**Daniel Kalinin** [00:55:49]: He was just like, you know, I don't think we're, we align like you can keep the, whatever I paid you and we're not going to go from here.

**Daniel Kalinin** [00:55:55]: I'm like, no problem.

**Daniel Kalinin** [00:55:57]: Thank God.

**William Peare** [00:55:58]: Yeah.

**William Peare** [00:56:02]: Okay.

**William Peare** [00:56:03]: Okay.

**William Peare** [00:56:04]: Let's get this going.

**William Peare** [00:56:06]: Okay.

**William Peare** [00:56:07]: I mean, honestly, I think that the SOP, we got that, the job description.

**William Peare** [00:56:13]: I think we can shelf that for now and kind of just move on to what's next.

**William Peare** [00:56:18]: You already made massive progress on the ClickUp thing.

**William Peare** [00:56:23]: Next one, we'll do the financial modeling.

**William Peare** [00:56:26]: So, I mean, let me look through what I had because you've kind of skipped ahead.

**William Peare** [00:56:30]: You've kind of skipped ahead.

**William Peare** [00:56:32]: You're going to outgrow me before I know it.

**William Peare** [00:56:33]: But let's take a look here and see what.

**William Peare** [00:56:42]: What questions do you have on code?

**William Peare** [00:56:45]: I think that's going to be your biggest point of leverage as you grow.

**William Peare** [00:56:48]: So let's go through what you have on questions on that and then kind of what you want to learn next besides the financial modeling because I'd like to set that up.

**William Peare** [00:56:57]: And then did you get the breakeven analysis done?

**Daniel Kalinin** [00:57:00]: Yeah, it might make sense that I do it for next session, too, because I know some of those numbers are off.

**Daniel Kalinin** [00:57:06]: Sure.

**Daniel Kalinin** [00:57:08]: But let me pull up everything that I have with Claude.

**Daniel Kalinin** [00:57:16]: So I guess my thing with Claude is very similar to my problem with ClickUp.

**Daniel Kalinin** [00:57:25]: Like, I have it.

**Daniel Kalinin** [00:57:26]: I don't know what the hell I'm supposed to do.

**Daniel Kalinin** [00:57:28]: So let me open up bit or git dash.

**Daniel Kalinin** [00:57:32]: Git bash, okay.

**Daniel Kalinin** [00:57:33]: Okay, all right.

**Daniel Kalinin** [00:57:35]: I don't know why I need this open, but I think I just need it open.

**Daniel Kalinin** [00:57:38]: And then Claude.

**Daniel Kalinin** [00:57:40]: You do not need that open.

**Daniel Kalinin** [00:57:42]: I don't need it, because I was interacting with it through it, like, for the entire setup.

**William Peare** [00:57:48]: What the hell?

**Daniel Kalinin** [00:57:49]: Yeah, I had to install, like, something into PowerShell, and then I had to...

**William Peare** [00:57:53]: Oh, you're on a Windows.

**William Peare** [00:57:55]: Yeah.

**William Peare** [00:57:57]: Mmm.

**William Peare** [00:57:58]: Mmm.

**William Peare** [00:57:59]: Okay.

**Daniel Kalinin** [00:58:00]: Is Windows gay for code?

**Daniel Kalinin** [00:58:01]: No, it's honestly probably better for coding.

**William Peare** [00:58:04]: I just have only ever ran a Mac.

**William Peare** [00:58:07]: Windows are normally more open for that.

**William Peare** [00:58:09]: Okay.

**William Peare** [00:58:10]: Now, you haven't even interacted with code at all, it doesn't look like.

**William Peare** [00:58:15]: In you have nothing in there.

**Daniel Kalinin** [00:58:17]: Yeah.

**Daniel Kalinin** [00:58:18]: Yesterday, we, or I guess me, this is everything that I was setting up.

**Daniel Kalinin** [00:58:23]: So program files.

**Daniel Kalinin** [00:58:26]: Holy .

**Daniel Kalinin** [00:58:27]: Okay.

**William Peare** [00:58:29]: No, this is just all my general ones.

**Daniel Kalinin** [00:58:31]: Oh, I was like, geez.

**William Peare** [00:58:34]: Thing bin.

**Daniel Kalinin** [00:58:34]: No, that's the dash one.

**Daniel Kalinin** [00:58:36]: There should be a program file here that's for.

**Daniel Kalinin** [00:58:39]: Where?

**William Peare** [00:58:41]: Okay.

**William Peare** [00:58:42]: Explain to me how you got to this if you weren't doing it through code.

**William Peare** [00:58:44]: Did you start it through coworker chat and it prompted you to set this up?

**William Peare** [00:58:48]: No, I was doing everything through this thing.

**Daniel Kalinin** [00:58:51]: I had to install a package in here.

**Daniel Kalinin** [00:58:53]: But to install that package, I need to add like an environmental variable to my PowerShell.

**Daniel Kalinin** [00:58:58]: Yes.

**Daniel Kalinin** [00:59:00]: So then it created some folders for me inside of, like, the...

**Daniel Kalinin** [00:59:07]: Yeah, the ENV files and all kinds of  like that.

**William Peare** [00:59:10]: That way it has reference stuff.

**William Peare** [00:59:11]: Yeah.

**William Peare** [00:59:12]: Yeah, but now I can't even remember.

**William Peare** [00:59:17]: PowerShell was at the bottom, yeah.

**William Peare** [00:59:20]: Let me see.

**William Peare** [00:59:20]: Okay, go over to Claude really quick into chat for the code.

**William Peare** [00:59:24]: Code chat.

**William Peare** [00:59:25]: No, sorry, code, yeah, but just go down there.

**William Peare** [00:59:28]: Give it a prompt.

**William Peare** [00:59:30]: Like, we'll just start with, I want to build a web scraper, and I want to see how it's interacting with you.

**William Peare** [00:59:50]: Because I definitely have to do terminal commands and things of that case.

**William Peare** [00:59:58]: But that is not how I...

**William Peare** [01:00:00]: I with it.

**William Peare** [01:00:00]: I interact with it through Claude.

**Daniel Kalinin** [01:00:08]: What was the path to get to my Claude folder?

**Daniel Kalinin** [01:00:15]: And yeah, it created like ClaudeMD and stuff like that.

**Daniel Kalinin** [01:00:19]: So yeah, yeah, yeah.

**William Peare** [01:00:21]: All right.

**Daniel Kalinin** [01:00:22]: Let's see.

**William Peare** [01:00:24]: Oh, I understand now.

**William Peare** [01:00:25]: You were running, you were getting this set up through Manus.

**William Peare** [01:00:30]: Now I was like, why is there no history?

**William Peare** [01:00:31]: Like, how did you get all this information?

**William Peare** [01:00:34]: Oh, yeah.

**William Peare** [01:00:34]: was asking, man.

**Daniel Kalinin** [01:00:36]: It's for everything.

**Daniel Kalinin** [01:00:38]: I guess I tried to do some stuff before, but yeah, I mean, I probably just didn't use it properly because I never installed this thing before.

**Daniel Kalinin** [01:00:49]: All right.

**Daniel Kalinin** [01:00:49]: So, yeah, it's projects and then agency OS.

**Daniel Kalinin** [01:00:56]: So.

**William Peare** [01:01:02]: So I would get out of this completely for now.

**William Peare** [01:01:09]: To make my life easier.

**Daniel Kalinin** [01:01:11]: Totally.

**William Peare** [01:01:11]: Out of this or out of?

**William Peare** [01:01:13]: Yes.

**William Peare** [01:01:14]: Both of all of those.

**William Peare** [01:01:15]: Copy and paste that project from Manus.

**William Peare** [01:01:21]: Copy that.

**William Peare** [01:01:22]: Put that into the right there and tell this is the project I want this to live in.

**Daniel Kalinin** [01:01:29]: This is my agency operating system.

**Daniel Kalinin** [01:01:31]: This is kind of my part two.

**Daniel Kalinin** [01:01:32]: I know I'm supposed to keep this organized and stuff like that.

**Daniel Kalinin** [01:01:35]: But Manus basically told me that if something is for like a completely separate task or something, it needs to make a new one.

**William Peare** [01:01:42]: Something like that.

**William Peare** [01:01:43]: Yeah.

**William Peare** [01:01:44]: Okay.

**William Peare** [01:01:45]: Well, in that case, just ask it to set up a folder, a path on your computer for this project we're talking about.

**William Peare** [01:01:51]: So it has a place for it to live.

**William Peare** [01:02:06]: Yeah.

**William Peare** [01:02:11]: Yeah.

**William Peare** [01:02:12]: You can put it under the projects folder.

**William Peare** [01:02:14]: That's fine.

**William Peare** [01:02:14]: I would not manually do it all through Git Bash.

**William Peare** [01:02:23]: You're going to be doing a shitload of copy and pasting and stuff of that nature.

**William Peare** [01:02:28]: If you build this out and code is linked to it, you can pretty much, I mean, you'll have to approve a lot of things, but it will be doing pretty much all of this for you.

**William Peare** [01:02:38]: So there's some things, like when it comes to API keys and stuff like that, and a matter of personal preference and security, it's always going to want you to just go and put them in yourself.

**William Peare** [01:02:48]: You can just put it into code and make it do it.

**William Peare** [01:02:50]: It depends on how sensitive the information is.

**William Peare** [01:02:52]: If it's like QuickBooks or something like that, like, yeah, probably, probably smart to do that.

**William Peare** [01:02:59]: If you're giving...

**William Peare** [01:03:00]: Permission to search Google.

**William Peare** [01:03:01]: I personally don't get that huffy-puffy about it.

**William Peare** [01:03:04]: Some people are very, that's a matter of preference.

**William Peare** [01:03:07]: I can't say that's right or wrong.

**William Peare** [01:03:08]: It's going to default to being as safe as possible.

**William Peare** [01:03:13]: Yeah, this is the folder.

**Daniel Kalinin** [01:03:16]: agency OS, what I did.

**Daniel Kalinin** [01:03:20]: Question, by the way, do I always need a CloudMD file for every parent folder?

**Daniel Kalinin** [01:03:25]: I don't believe so.

**William Peare** [01:03:27]: But so the markdown file is, it's not code, but it's almost like the instructions, like if you were writing project instructions.

**William Peare** [01:03:35]: So it's what it's going to reference to describe what it's doing.

**William Peare** [01:03:39]: Got it.

**Daniel Kalinin** [01:03:40]: So hypothetically, if I've got lead scraper project and I should have a CloudMD file there that just says like, hey, we are targeting, you know, B2B businesses, blah, blah, blah.

**Daniel Kalinin** [01:03:51]: Every time I write this prompt or ask you, verify what niche I want to target and then scrape 200 leads from that niche, right?

**Daniel Kalinin** [01:04:01]: Yes.

**William Peare** [01:04:02]: I mean, there's a few ways to do this.

**William Peare** [01:04:08]: So you can either build it as a general one, which it's going to know what it's doing, or you can build it into the code that, like, you know, prompt me, ask me these questions whenever I kick this off.

**William Peare** [01:04:19]: It depends on what the trigger is.

**William Peare** [01:04:20]: I personally have never done it in the way that it's having you do it with agency OS.

**William Peare** [01:04:25]: So I guess I'd be curious to see if there's, like, increased functionality in terms of doing it that way.

**William Peare** [01:04:32]: Yeah.

**William Peare** [01:04:32]: I've had very, very good functionality in the way I do it.

**William Peare** [01:04:38]: I am...

**William Peare** [01:04:39]: Where did you get to with it?

**William Peare** [01:04:40]: Was it doing anything for you?

**William Peare** [01:04:43]: No, I didn't have it do anything for me.

**Daniel Kalinin** [01:04:45]: The main thing that Manus was saying that was that I need to give agency OS, like, as much information as possible of my agency.

**Daniel Kalinin** [01:04:55]: That way it has, like, a foundation build off of.

**Daniel Kalinin** [01:04:57]: So I know yesterday, for example,

**Daniel Kalinin** [01:05:00]: I was filling this up, and this is like the Ops Consulting things that we were doing.

**Daniel Kalinin** [01:05:05]: it kind of branched out a bunch of different things that are my bottlenecks, scaling strategies, financial models.

**Daniel Kalinin** [01:05:14]: I also put in SOPs, so client onboarding, SOP, whatever, blah, blah, blah.

**Daniel Kalinin** [01:05:19]: I don't understand half this , but it managed to just branch it out, and it said that's probably the best way.

**Daniel Kalinin** [01:05:24]: And it just said that over time, I need to keep updating this.

**Daniel Kalinin** [01:05:28]: So if I don't have an onboarding bottleneck anymore, I probably shouldn't be putting, you know, you know, research on onboarding bottlenecks or something like that.

**William Peare** [01:05:38]: Mm-hmm.

**William Peare** [01:05:39]: Hmm.

**William Peare** [01:05:40]: Yeah, I'm, my guess is that it's using this like an RAG, like I was talking about.

**William Peare** [01:05:45]: It's probably using this as like a base of reference material.

**William Peare** [01:05:49]: Yeah.

**William Peare** [01:05:51]: That way it has a place to go, whereas if you're doing it specifically in code each time, it's going to be in that.

**William Peare** [01:05:59]: right.

**William Peare** [01:05:59]: All All

**William Peare** [01:06:00]: Chat, so to speak, like in that one project you're doing.

**William Peare** [01:06:04]: So if you were doing a repeatable task over and over, I normally do them in the sense that they live and are hosted somewhere else.

**William Peare** [01:06:12]: So if I need to make an update or speak to it, I just give it the repository that I'm trying to go to and say, hey, cool, reference material is here.

**William Peare** [01:06:22]: I want to make these changes.

**William Peare** [01:06:23]: It'll scan it, scrape it really quick, and then it'll make my pivots from there.

**William Peare** [01:06:29]: Got it.

**Daniel Kalinin** [01:06:30]: Kind of a follow-up question now that I think about it.

**Daniel Kalinin** [01:06:33]: This whole folder stuff, do I always need a folder for something?

**Daniel Kalinin** [01:06:37]: Okay.

**Daniel Kalinin** [01:06:38]: Yes.

**William Peare** [01:06:39]: Got it.

**Daniel Kalinin** [01:06:39]: And if things are very similar, like let's say instead of it scraping Google, I want it to, I don't know, scrape something else, connect to AppFind, scrape phone numbers, or I don't know, whatever.

**Daniel Kalinin** [01:06:53]: Would I just tell it, hey, use the lead scraping folder?

**Daniel Kalinin** [01:06:58]: You could, and then you could.

**William Peare** [01:07:00]: You subpaths within there.

**William Peare** [01:07:01]: That could be the root, and then you could have subpaths within there.

**William Peare** [01:07:04]: Or you could say, hey, I'm building a very similar one.

**William Peare** [01:07:07]: These are going to be the changes.

**William Peare** [01:07:08]: Please duplicate this as lead scraping, hash, Appify, make these tweaks to it, and then have two different reference points.

**William Peare** [01:07:16]: Okay, cool.

**William Peare** [01:07:17]: It depends how much information's in there and how cluttered it's going to get.

**William Peare** [01:07:20]: Because it being anything that's token-based, know what mean?

**William Peare** [01:07:23]: Like, if you have this  monster where you've put six different things in, you're just going to burn more usage, you know, having it scrape through all the stuff if it's not relevant.

**Daniel Kalinin** [01:07:33]: Yeah.

**Daniel Kalinin** [01:07:34]: Do you know how to have this also sink into my MacBook?

**Daniel Kalinin** [01:07:41]: Because I remember I got cooked one time because I was using Claude and I had a bunch of prompts in chat for copywriting.

**Daniel Kalinin** [01:07:47]: You can't do that.

**William Peare** [01:07:48]: It doesn't, unless, yeah, it's  super annoying.

**William Peare** [01:07:51]: Because I have, like, one, like a $4,000 high-end MacBook Pro, and then I have another, like, I don't average Mac.

**William Peare** [01:08:00]: Book Air.

**William Peare** [01:08:02]: And this sucks because I had my nice computer at my normal work because I do a lot of like, my main job is estimating.

**William Peare** [01:08:11]: So I'm always looking at like very heavy graphic PDF files.

**William Peare** [01:08:14]: So it just goes through them cleaner.

**William Peare** [01:08:16]: But next week, actually, next week will be my last week in the office and then I'm going completely full remote.

**William Peare** [01:08:21]: So.

**William Peare** [01:08:21]: Hell yeah.

**Daniel Kalinin** [01:08:22]: Are you going to still work for them or are you going to scale Framework Ops?

**Daniel Kalinin** [01:08:27]: Yeah.

**William Peare** [01:08:28]: It's actually kind of funny because I pretty, I pretty much told him I just wanted to work on my own thing.

**William Peare** [01:08:34]: And I was like, hey, man, like, I don't have the time to run this for you full time and grow my thing.

**William Peare** [01:08:38]: And he's like, how about I just give you a raise?

**William Peare** [01:08:40]: And we move forward the sell of the business and you get your 5% equity share sold out, you know, this fall.

**William Peare** [01:08:46]: And you can just work completely from home and do your own stuff as long as you get the quotes done.

**William Peare** [01:08:50]: I was like, all right, all right.

**William Peare** [01:08:52]: What's the, um.

**William Peare** [01:08:53]: Pretty hard to argue with that.

**Daniel Kalinin** [01:08:54]: he has a good business where he doesn't have debt.

**Daniel Kalinin** [01:08:57]: What would the multiple be on that?

**William Peare** [01:08:59]: .

**William Peare** [01:09:00]: I think we'll probably get five to seven.

**Daniel Kalinin** [01:09:02]: Okay, that's all, and it does like what, one to two a year?

**William Peare** [01:09:06]: In profit or revenue?

**William Peare** [01:09:09]: When people care about multiples, they care about profit or?

**William Peare** [01:09:12]: Yes, multiples are off.

**William Peare** [01:09:14]: Well, I mean, there's, that's not really, there's not really like a fixed set in stone.

**William Peare** [01:09:21]: Generally, multiples are going to be off EBITDA.

**William Peare** [01:09:24]: So like profit after expenses before taxes.

**William Peare** [01:09:29]: You could have a lower multiple just off revenue.

**William Peare** [01:09:32]: So the four to seven, five to seven for us would be off profit.

**William Peare** [01:09:35]: I think he'll likely get four to 5 million and I'll get a 5% stake of that.

**William Peare** [01:09:41]: So not bad.

**William Peare** [01:09:43]: Not bad at all.

**William Peare** [01:09:44]: A couple of years.

**Daniel Kalinin** [01:09:45]: like, 250?

**Daniel Kalinin** [01:09:47]: Yeah, two, probably two to 300.

**William Peare** [01:09:49]: That's not cool.

**William Peare** [01:09:50]: Yeah, sure.

**William Peare** [01:09:51]: It doesn't, it doesn't suck.

**William Peare** [01:09:52]: So I'm probably, I was like really ready to just like super start ramping up.

**William Peare** [01:09:58]: Um, yeah.

**William Peare** [01:10:01]: And kind of just call it a day.

**William Peare** [01:10:03]: And he's like, no, please, God, just I'll give you a raise and you can sit at home and do your own thing.

**William Peare** [01:10:08]: And I was like, that's pretty  hard to argue with.

**William Peare** [01:10:10]: Stay on full benefits insurance and get paid.

**Daniel Kalinin** [01:10:13]: How's the acquisition going for you?

**Daniel Kalinin** [01:10:16]: Are you still getting people through Upwork or are you getting people through LinkedIn now?

**Daniel Kalinin** [01:10:20]: I honestly have not.

**William Peare** [01:10:22]: I'm just posting on LinkedIn.

**William Peare** [01:10:23]: I haven't done any cold outreach because I was so busy.

**William Peare** [01:10:26]: That's why I was kind of like at the point where I was like, hey, man, just start scaling this.

**William Peare** [01:10:29]: I need my time.

**William Peare** [01:10:32]: And then if he wants to sell, like, I mean, it'd probably be as early as like September.

**William Peare** [01:10:36]: Like we're in a valuation process right now.

**William Peare** [01:10:38]: We should have the valuation next week and then be looking for a buyer.

**William Peare** [01:10:43]: I realistically will probably just keep organically posting.

**William Peare** [01:10:46]: I'll probably get into this AI video thing.

**William Peare** [01:10:48]: I'll probably just start building a LinkedIn following and, you know, work with you until you're done and then maybe find one more smaller person.

**William Peare** [01:10:55]: But I might honestly just wait until I get that payout and then just.

**William Peare** [01:10:59]: just.

**William Peare** [01:11:00]: Use that to live off of for six months while I start.

**William Peare** [01:11:02]: Because if I start pushing acquisition heavy right now, you know how it goes.

**William Peare** [01:11:09]: Like if I brought in two or three clients, then I'm just going to be  slammed.

**William Peare** [01:11:12]: I think I would rather take the next like three to six months and really start deep diving into like AI courses, automation courses, and really just like learn as much as I possibly can.

**William Peare** [01:11:23]: Because just like you, like I've learned a lot of it through many, many late nights.

**William Peare** [01:11:28]: But you only know what you know.

**William Peare** [01:11:30]: Like even when you showed me that, like you're doing it through PowerShell, like I've definitely, a lot of the stuff you have to do through, I mean, PowerShell on your end, Terminal on Mac, a lot of the stuff has to be done that way.

**William Peare** [01:11:41]: But it, you can't have a conversation with PowerShell or Terminal.

**William Peare** [01:11:45]: Like it, you put in the prompts that you get from somewhere and it goes there and then you get back an output.

**William Peare** [01:11:49]: So like if you're trying to iterate and stuff like that, I guess you were doing it through Madness, which may achieve the same thing.

**William Peare** [01:11:55]: I don't know.

**William Peare** [01:11:56]: I keep it all in one place generally.

**William Peare** [01:11:58]: Like I don't go to chat.

**William Peare** [01:12:00]: Claude, describe what I'm trying to do.

**William Peare** [01:12:02]: Like if I'm working with chat or co-work and it starts giving me something that's code-based, I immediately tell it like, hey, cool, just give me a breakdown and a prompt to this.

**William Peare** [01:12:11]: I'm going to take this over to code.

**William Peare** [01:12:14]: I find it a lot easier to iterate and go through my changes that way.

**William Peare** [01:12:18]: So I want to learn.

**William Peare** [01:12:20]: I mean, now I got this AI video thing.

**William Peare** [01:12:22]: I probably want to spend the next like three to six months just like really sharpening my pencil on like everything I can do and working with a couple smaller clients who it's more of like, you know, working with them, helping them grow through stuff they have and also kind of just getting industry feedback.

**William Peare** [01:12:37]: Like I've learned a lot, like even just dealing with you on them.

**William Peare** [01:12:40]: AI video things, how you're doing outreach.

**William Peare** [01:12:42]: Like I'm just bringing in a ton of information for myself.

**William Peare** [01:12:45]: And if finances aren't really the worry, I mean, I get paid pretty well.

**William Peare** [01:12:49]: So if he's willing for me to just sit at my house and I mean, like the estimating thing, I'm good at it at this point.

**William Peare** [01:12:57]: It's like you doing the copywriting thing.

**William Peare** [01:12:59]: It'd be like having

**William Peare** [01:13:00]: Two clients you're copywriting for.

**William Peare** [01:13:01]: Like it probably chews up 15 hours of my week for a hundred plus thousand a year.

**William Peare** [01:13:06]: So if I can just sit around and get paid and learn for a few months, I think that way I can start my acquisition at a higher price point.

**William Peare** [01:13:14]: Instead of having to start at that $1,500 a month, I think I could easily start, you know, 25 to 4,000.

**William Peare** [01:13:21]: And when I'm actually taking on these clients, getting better return to my time instead of working a bunch for less money.

**William Peare** [01:13:27]: Yeah.

**William Peare** [01:13:29]: Yeah.

**William Peare** [01:13:29]: So I've shifted my strategy a bit because he pretty sweetheart offer.

**William Peare** [01:13:34]: mean, what the hell are supposed to say?

**William Peare** [01:13:35]: I was like, yeah, I'm trying to quit.

**William Peare** [01:13:37]: Like I'm quitting.

**Daniel Kalinin** [01:13:38]: He's like, yeah, I think long, long-term too.

**Daniel Kalinin** [01:13:40]: don't know if you know Eddie Maloof, but he has an agency.

**Daniel Kalinin** [01:13:44]: They, they, they print really well, but they kind of ended up building a really good team.

**Daniel Kalinin** [01:13:51]: And now what he just does is, um, he buys into companies whenever they have like, um, um,

**Daniel Kalinin** [01:14:00]: Whenever they go public for like, hey, we need to raise a million dollars for whatever, X amount of money or X percentage, he just does that, plugs his team in, and then helps them with the buyout to get acquired, and he multiplies his money very fast like that.

**Daniel Kalinin** [01:14:18]: So the whole acquire and sell thing, that's also something pretty sick.

**Daniel Kalinin** [01:14:24]: So yeah, I want to get some of those equity deals where it could be like, cool, I get like, you know, I put in half a million, company sells for 50 million, and whenever I bought in, it had like, I don't know, 10 million valuation, so I like 5X my money, 4X spread, and just, yeah, that's pretty sick.

**William Peare** [01:14:45]: It doesn't suck.

**William Peare** [01:14:46]: mean, mine wasn't that big, but I mean, I started with this company when it was really small, and my uncle ran, I mean, like Horizon Airlines, Thousand Trails came to the ground, he was the CEO.

**William Peare** [01:15:00]: for like three or four different very, very large companies where he had equity shares.

**William Peare** [01:15:03]: So like as soon as I started, he's like, yeah, take a lower salary and tell them you own equity.

**William Peare** [01:15:08]: And I mean, I made great money and bonuses and now I'll get a pretty chunky payout for two years of work.

**William Peare** [01:15:15]: So it almost double or triples my salary.

**William Peare** [01:15:19]: It's definitely good, but good.

**William Peare** [01:15:21]: I mean, it's just like the rev share kind of deal.

**William Peare** [01:15:23]: Like if you can get in and tie yourself to them, A, it's lower risk for them.

**William Peare** [01:15:26]: So it's a lot easier to sell to be like, hey man, you can pay me 80 grand a year for $150,000 job, but I want X percent.

**William Peare** [01:15:34]: It's kind of no skin off their back until they get a huge payout.

**William Peare** [01:15:37]: Because if this guy's getting 4 million, he's like, yeah, 200,000,,000, like just take it.

**William Peare** [01:15:41]: It's pocket change.

**William Peare** [01:15:42]: No problem.

**William Peare** [01:15:43]: Whereas if I would have asked for that up front, he would tell me to screw myself.

**William Peare** [01:15:46]: So yeah.

**William Peare** [01:15:48]: Yeah.

**William Peare** [01:15:49]: I think it's good.

**William Peare** [01:15:50]: And I mean, I, especially because you're already really ramping up quickly and learning a lot of this stuff, I think how I can provide good value to

**William Peare** [01:16:00]: Why you're still on the program is I think if you want to pick a couple of these that you don't really want to dump the time into, I'm happy to build them out on my end because I've built that stuff for me and general stuff, but stuff that's going into like, this is a different, you are in a different industry than what I'm doing.

**William Peare** [01:16:20]: So I'll learn from that and then it could go into a GitHub and then you can just go and access that code with your Claude, launch it where you want and tweak it.

**William Peare** [01:16:28]: But that way you're getting real value quickly, so to speak.

**William Peare** [01:16:31]: I know you want quick deliverable stuff you can actually act on.

**William Peare** [01:16:34]: So if you want to think of a couple of things that I'm just working on off meeting to get built out for you, that way you have them.

**William Peare** [01:16:40]: I want to make sure I'm providing good value to you.

**William Peare** [01:16:43]: Okay, cool.

**Daniel Kalinin** [01:16:46]: Okay, let's see this.

**Daniel Kalinin** [01:16:50]: Yeah, want to see what you got going on.

**Daniel Kalinin** [01:16:52]: Okay, so set up a path.

**Daniel Kalinin** [01:16:54]: me check the home directory.

**Daniel Kalinin** [01:16:55]: File created.

**Daniel Kalinin** [01:16:56]: So yeah, lead scraper was created.

**Daniel Kalinin** [01:16:58]: Next steps, drop.

**Daniel Kalinin** [01:17:00]: Google Places API key and build the scraper.

**Daniel Kalinin** [01:17:02]: Tell me your target locations.

**Daniel Kalinin** [01:17:04]: Yep.

**Daniel Kalinin** [01:17:05]: So if I get it, the Google Places API key, I don't know, this  just confuses me because I guess I'm more caveman when it comes to this stuff.

**Daniel Kalinin** [01:17:18]: So I give it an API key and it just starts scraping away.

**Daniel Kalinin** [01:17:25]: Where do I need to give it in-depth instructions?

**Daniel Kalinin** [01:17:28]: I probably do.

**Daniel Kalinin** [01:17:29]: Where is it going to then house all the leads then?

**Daniel Kalinin** [01:17:32]: That's what I was talking to you about.

**William Peare** [01:17:34]: was like, when it's just saying, I'll build the scraper, it sure as  isn't just going to be like, I'm scraping.

**William Peare** [01:17:42]: It's going to go from here to, I mean, then we need to decide like, we're going to have to do a couple of things for this to even be functional at all.

**William Peare** [01:17:49]: One, it's going to need a hosting path.

**William Peare** [01:17:53]: I mean, you could run it likely through the Cloud API.

**William Peare** [01:17:56]: I like to host all my stuff because hosting is cheap and then it lives somewhere and it's easy.

**William Peare** [01:18:00]: To tweak.

**William Peare** [01:18:00]: So I mean, bare minimum, you're going to need to get this off the ground and it realistically, like we could probably knock it out before we're even done with this call.

**William Peare** [01:18:07]: We're going to need an API key from go high level.

**William Peare** [01:18:11]: We would need to build out either an opportunity path or once you have the API key, you can probably tell it to  build out an API.

**William Peare** [01:18:19]: I haven't dealt with the go high level API enough to know if it can build it out itself or if it needs you to build it out.

**William Peare** [01:18:25]: But it's going to need an API key.

**William Peare** [01:18:27]: You're going to have to tell it, hey, I want these to live in, you know, the lead statement opportunity path.

**William Peare** [01:18:32]: That's where they're going to go.

**William Peare** [01:18:33]: You'll have to get the Google API key.

**William Peare** [01:18:36]: And then if you want it to be intelligent, which you do likely, you're going to want to get a cloud console API key.

**William Peare** [01:18:43]: And then you can tell cloud like, hey, this is what you do with this raw data.

**William Peare** [01:18:48]: Because if it's just scraping, it's just going to pull it.

**William Peare** [01:18:50]: But if you actually run it through an LLM and it's actually thinking on its own, you can tell it, hey, these are the base instructions for this API You're, you're, know, it's going to pull in this data.

**William Peare** [01:18:59]: You're.

**William Peare** [01:19:00]: going to receive this data.

**William Peare** [01:19:01]: I want you to parse it, automatically remove these people.

**William Peare** [01:19:04]: These are my super target people.

**William Peare** [01:19:06]: And then it's going to put it wherever you told it to put it.

**William Peare** [01:19:09]: But you're, you're good.

**William Peare** [01:19:10]: There's a few steps here.

**William Peare** [01:19:12]: Okay.

**William Peare** [01:19:12]: So let's just go to the console first off.

**Daniel Kalinin** [01:19:16]: Oh, not this console.

**William Peare** [01:19:18]: Cloud console, cloud.console.google or something like that.

**William Peare** [01:19:22]: You have to set it up separately.

**William Peare** [01:19:26]: Yeah.

**William Peare** [01:19:27]: You might have to just Google it.

**William Peare** [01:19:29]: Yeah.

**William Peare** [01:19:29]: So it's definitely different than your admin console.

**William Peare** [01:19:35]: You'll have to set it up.

**William Peare** [01:19:36]: I don't think I need a Gemini API key setup foundations.

**Daniel Kalinin** [01:19:49]: Okay.

**William Peare** [01:19:57]: Oh, you'll have to start a free trial.

**William Peare** [01:19:59]: So it'll pretty much.

**William Peare** [01:20:00]: Stay free with how much you're trying to use it, but you'll have to go all the way up to the top right and click start for free, first things first.

**William Peare** [01:20:04]: Okay.

**William Peare** [01:20:23]: Yeah, now for these API credits, the nice thing is things like this burn, like, very little.

**William Peare** [01:20:30]: I've set up , I don't know, 10 or a dozen, like, test things like this.

**William Peare** [01:20:36]: Same with Claude API, so that also you have to buy credits, but it burns them, like, really slowly, unless you're doing stuff that's pretty intensive.

**William Peare** [01:20:47]: Yeah, so you're working on your first project, you can name it whatever you want.

**William Peare** [01:20:59]: So if you click.

**William Peare** [01:20:59]: click.

**William Peare** [01:21:00]: Click into my first project.

**William Peare** [01:21:01]: Yeah.

**William Peare** [01:21:02]: If you click into my first project.

**William Peare** [01:21:05]: Oh, yeah.

**William Peare** [01:21:05]: Yeah.

**William Peare** [01:21:05]: You do this.

**William Peare** [01:21:07]: It's not a super UI.

**William Peare** [01:21:12]: Yeah.

**William Peare** [01:21:12]: Friendly UI.

**William Peare** [01:21:13]: There you go.

**William Peare** [01:21:15]: And I haven't made one with places, but yeah.

**William Peare** [01:21:18]: So you can enable it.

**William Peare** [01:21:20]: Places would be like Google Maps, I'm guessing.

**Daniel Kalinin** [01:21:22]: I'm guessing so.

**Daniel Kalinin** [01:21:23]: Yeah.

**William Peare** [01:21:24]: That's probably how it's getting the reviews because that's where it was.

**William Peare** [01:21:27]: Since that was like kind of your trigger, it probably needs that one.

**Daniel Kalinin** [01:21:31]: That tax firm, by the way, I love the lady, but they're a bit, a bit assholey.

**Daniel Kalinin** [01:21:39]: They didn't, uh, they didn't take the rev share.

**Daniel Kalinin** [01:21:43]: Really?

**Daniel Kalinin** [01:21:43]: make them.

**William Peare** [01:21:44]: Yeah.

**Daniel Kalinin** [01:21:44]: But I make them so much money.

**Daniel Kalinin** [01:21:45]: that kind of got me a bit upset.

**Daniel Kalinin** [01:21:48]: Didn't she pitch the rev share?

**William Peare** [01:21:50]: She did.

**Daniel Kalinin** [01:21:51]: Yeah.

**Daniel Kalinin** [01:21:51]: And then like, I guess she meant when she said like 20%, she meant including the sales team.

**Daniel Kalinin** [01:21:56]: But again, her English is like off.

**Daniel Kalinin** [01:21:57]: So I don't think she understood that.

**Daniel Kalinin** [01:22:00]: Like, if she's telling me, hey, like, I'll give you 20%, I'll be like, hell yeah, give me 20%.

**William Peare** [01:22:06]: What does she create a sales team?

**Daniel Kalinin** [01:22:08]: She doesn't have one yet, but she said, like, in the grand scheme of things, that, like, she wanted to be 20 or 25%.

**Daniel Kalinin** [01:22:13]: So I'm like, okay, like, I guess there's miscommunication there.

**Daniel Kalinin** [01:22:17]: I'm happy to do it at 10%.

**Daniel Kalinin** [01:22:18]: Like, I take 10% all day, too.

**Daniel Kalinin** [01:22:21]: Then she was like, her partner, like, her partner's an accountant, like, the one actually doing the fulfillment.

**Daniel Kalinin** [01:22:26]: And I guess she doesn't really understand marketing.

**Daniel Kalinin** [01:22:28]: She's like, why do we need to pay, like, people to do this stuff for us?

**Daniel Kalinin** [01:22:34]: And, you know, Sophie, that's her name.

**Daniel Kalinin** [01:22:36]: She was like, well, I mean, they're the reason why we have clients.

**Daniel Kalinin** [01:22:39]: And she's like, she didn't really get it.

**Daniel Kalinin** [01:22:41]: It's not trying to pitch a higher retainer.

**Daniel Kalinin** [01:22:43]: I'm like, okay, if you guys, like, don't want to give revenue, like, how about we just increase the retainer and, like, also say anything.

**Daniel Kalinin** [01:22:49]: So, yeah, I guess that partner's just getting in the way.

**Daniel Kalinin** [01:22:53]: but if I'm able to find, like, 100 tax firms like them, because they also have, like, 50 Google reviews, it's just like...

**Daniel Kalinin** [01:23:00]: One thing, I guess that, like the one thing that I linked up, if I saw on a few of them, I can run it up so easily.

**Daniel Kalinin** [01:23:08]: Totally.

**William Peare** [01:23:09]: Yeah.

**William Peare** [01:23:09]: Super scalable.

**William Peare** [01:23:12]: Yeah.

**Daniel Kalinin** [01:23:12]: Click places API, click enable.

**Daniel Kalinin** [01:23:14]: Okay.

**Daniel Kalinin** [01:23:14]: have the API key in left sidebar.

**Daniel Kalinin** [01:23:16]: Go to APIs.

**Daniel Kalinin** [01:23:19]: Okay.

**Daniel Kalinin** [01:23:25]: Okay.

**Daniel Kalinin** [01:23:25]: In the left sidebar, go to APIs and services credentials.

**Daniel Kalinin** [01:23:28]: I don't know what this is.

**Daniel Kalinin** [01:23:32]: APIs and services.

**William Peare** [01:23:35]: Yep.

**William Peare** [01:23:35]: And then you'll need a search.

**William Peare** [01:23:37]: Search the line.

**William Peare** [01:23:38]: There's so many.

**William Peare** [01:23:40]: Yeah.

**William Peare** [01:23:40]: Or if you go down to keys and credentials, it'll be in there as well.

**Daniel Kalinin** [01:23:45]: Places API.

**William Peare** [01:23:47]: Yep.

**William Peare** [01:23:48]: Okay.

**Daniel Kalinin** [01:23:50]: Keys.

**William Peare** [01:23:51]: Keys.

**William Peare** [01:23:56]: Whoa.

**William Peare** [01:23:57]: Oh my gosh.

**William Peare** [01:23:57]: That is annoying.

**William Peare** [01:24:00]: Yeah, and you can show that key, copy it into there.

**William Peare** [01:24:03]: It'll start placing it where it belongs.

**Daniel Kalinin** [01:24:06]: Show key, copy the key, optionally restrict key and limit it to the places API for security.

**Daniel Kalinin** [01:24:13]: I don't know what that means, but treat them like passwords, restricting this key.

**Daniel Kalinin** [01:24:24]: Mm-hmm, that's what I was telling you, Bab.

**Daniel Kalinin** [01:24:26]: Okay, so actions, would I just edit the key and restrict it?

**Daniel Kalinin** [01:24:34]: Yeah, right there.

**Daniel Kalinin** [01:24:35]: key restrictions, restrict to places.

**Daniel Kalinin** [01:24:38]: I guess websites.

**William Peare** [01:24:43]: Websites.

**Daniel Kalinin** [01:24:44]: Yeah.

**William Peare** [01:25:04]: I like how all their UIs look like exactly the same.

**William Peare** [01:25:08]: Yeah.

**Daniel Kalinin** [01:25:11]: List of 25.

**William Peare** [01:25:19]: It's fast.

**Daniel Kalinin** [01:25:21]: Dude, man, this is like insane.

**Daniel Kalinin** [01:25:27]: I love it.

**Daniel Kalinin** [01:25:28]: I love it so much.

**Daniel Kalinin** [01:25:30]: ChatGPT, I know they're trying to make a comeback right now.

**William Peare** [01:25:33]: don't even think I have chat.

**Daniel Kalinin** [01:25:34]: Yeah, they made images too, which I haven't really played with yet.

**Daniel Kalinin** [01:25:42]: ChatGPT.

**Daniel Kalinin** [01:25:43]: I know they made images too, showing his bank balance on the screen with text.

**Daniel Kalinin** [01:26:00]: From a bookkeeping offer, basically saying that checking your bank balance isn't a good way to understand the numbers in your business.

**Daniel Kalinin** [01:26:14]: I've never used this before, but I know a good chunk of people said it was pretty good.

**Daniel Kalinin** [01:26:22]: So I'll let that rip while I'm doing this.

**Daniel Kalinin** [01:26:38]: How many tokens do I have, by the way?

**Daniel Kalinin** [01:26:40]: Because it's kind of shredding tokens now.

**William Peare** [01:26:43]: What, Claude?

**William Peare** [01:26:44]: Code?

**William Peare** [01:26:44]: Code?

**William Peare** [01:26:45]: Yeah, mean, we're already at 350 tokens.

**Daniel Kalinin** [01:26:48]: Are you on Pro?

**William Peare** [01:26:51]: Yeah.

**William Peare** [01:26:52]: So click on, yeah, go to the settings, click usage.

**William Peare** [01:26:59]: Yeah.

**William Peare** [01:27:00]: Yeah, you've burned.

**William Peare** [01:27:01]: You barely even use this puppy.

**William Peare** [01:27:03]: resets on Wednesday.

**William Peare** [01:27:04]: Is there a higher tier?

**Daniel Kalinin** [01:27:07]: Yeah, there's max.

**William Peare** [01:27:10]: Max five times and ten times.

**William Peare** [01:27:12]: I run, so code, definitely choose it.

**William Peare** [01:27:19]: It's five-hour blocks with Claude.

**William Peare** [01:27:21]: It resets every five hours, and then you have your weekly limit.

**William Peare** [01:27:24]: Um, if I'm coding heavy, like, building out a  app, I might burn through, um, burn through my usage for the five-hour block in, like, two hours and have to wait.

**William Peare** [01:27:37]: So, I mean, if I keep doing heavy coding, I'll probably upgrade to the hundred a month, just so that I'm not bottlenecking out.

**William Peare** [01:27:43]: But I've never hit my weekly usage, um, ever.

**William Peare** [01:27:48]: And I've built, like, full  apps with it.

**William Peare** [01:27:52]: Um, so it's definitely, it chews through them decent, but I've never needed more than my $20 a month.

**William Peare** [01:27:59]: The biggest is I've

**William Peare** [01:28:00]: had to wait like two hours.

**William Peare** [01:28:01]: That's the worst thing that's happened.

**Daniel Kalinin** [01:28:11]: Request denied.

**Daniel Kalinin** [01:28:13]: Where is it saying that?

**William Peare** [01:28:14]: Right here.

**Daniel Kalinin** [01:28:16]: You're calling a legacy API, which is not enabled for your project.

**Daniel Kalinin** [01:28:25]: All right, I'll let that do.

**Daniel Kalinin** [01:28:26]: It's saying it just told me to run it, so I'm guessing I was supposed to run it.

**William Peare** [01:28:30]: Totally.

**William Peare** [01:28:31]: Yeah, yeah, yeah.

**William Peare** [01:28:32]: And then, mean, geez.

**William Peare** [01:28:35]: Not bad.

**William Peare** [01:28:36]: No.

**Daniel Kalinin** [01:28:37]: Not bad at all.

**William Peare** [01:28:40]: And I spun this up in two seconds.

**Daniel Kalinin** [01:28:42]: mean, like, yeah.

**William Peare** [01:28:46]: Damn.

**Daniel Kalinin** [01:28:47]: No, I think, I think ChatGPT is getting railed right now, so they're trying to figure all their stuff out ASAP, because Nanobananas shred them into pieces.

**Daniel Kalinin** [01:28:57]: What the  is Nanobanana?

**William Peare** [01:28:59]: It's...

**Daniel Kalinin** [01:29:00]: But, um, it's like a Gemini, but like its own separate thing.

**Daniel Kalinin** [01:29:04]: That's what Manus uses to create images, but yeah, they're trying to like bounce back, but they're just getting whooped in the eyes right now, so this is one of their ways to do it.

**Daniel Kalinin** [01:29:16]: Is Nano Banana pretty good for images?

**William Peare** [01:29:19]: I love it, yeah.

**Daniel Kalinin** [01:29:20]: All my image ads come through Manus, and Manus uses Nano Banana.

**Daniel Kalinin** [01:29:25]: Okay.

**Daniel Kalinin** [01:29:26]: Okay, so no, no leads were saved because access was denied, so let me.

**Daniel Kalinin** [01:29:33]: Yeah, you're going to want to copy that.

**William Peare** [01:29:35]: Yeah, exactly.

**William Peare** [01:29:36]: Yeah.

**William Peare** [01:29:37]: Yep.

**Daniel Kalinin** [01:29:39]: Why could we be having this issue?

**Daniel Kalinin** [01:29:42]: And where did it save that API key?

**William Peare** [01:29:46]: It did not, but you can access it at any time.

**William Peare** [01:29:49]: I mean, it may have put it into the ENV, but that could also be the issue is that it was telling you, hey, don't put that in here.

**William Peare** [01:29:55]: Oh my God, don't do that.

**William Peare** [01:29:58]: Is it enabled in your Google Cloud project?

**William Peare** [01:30:00]: Project, you luckily created it, or it didn't save it.

**William Peare** [01:30:04]: I would ask it really quickly to check if it's saved in the root, or if it didn't save it for you, because it would speed up.

**William Peare** [01:30:12]: If the API key is saved in the root folder?

**Daniel Kalinin** [01:30:16]: Yep.

**Daniel Kalinin** [01:30:25]: Unless we put the wrong engine.

**Daniel Kalinin** [01:30:27]: Yeah, it's created, it's, okay, good.

**William Peare** [01:30:30]: Could it be the restriction that we set?

**William Peare** [01:30:33]: Could be, yeah, take that off and see what it does.

**William Peare** [01:30:36]: Edit API key.

**Daniel Kalinin** [01:30:37]: No, mean, yeah.

**William Peare** [01:30:45]: Oh, click activate, top right?

**William Peare** [01:30:48]: Maybe that's it?

**William Peare** [01:30:49]: No, that's the free trial thing.

**Daniel Kalinin** [01:30:50]: Yeah, that's the free trial thing.

**William Peare** [01:30:53]: Remember to configure the OAuth consent screen with information about your application.

**William Peare** [01:30:57]: Okay, so go to the OAuth screen and...

**William Peare** [01:31:03]: What do I do here?

**Daniel Kalinin** [01:31:09]: You can just name it, web scraper, whatever you want to call it.

**William Peare** [01:31:16]: Scraper.

**William Peare** [01:31:17]: And then you're the support email, yep.

**William Peare** [01:31:19]: Next.

**William Peare** [01:31:20]: Internal.

**William Peare** [01:31:24]: That's you again.

**Daniel Kalinin** [01:31:32]: OAuth.

**Daniel Kalinin** [01:31:33]: You haven't configured.

**Daniel Kalinin** [01:31:35]: So I need to create an OAuth client?

**William Peare** [01:31:38]: Potentially, yeah, try that.

**Daniel Kalinin** [01:31:52]: Just enable the Places API on your console and do all the work.

**Daniel Kalinin** [01:31:58]: It's enabled.

**William Peare** [01:31:59]: Yeah,

**Daniel Kalinin** [01:32:00]: Yeah, let's do this.

**William Peare** [01:32:17]: Oh, looks like there's Places API and Places API new.

**William Peare** [01:32:21]: Which one did you use?

**William Peare** [01:32:22]: That might be the legacy thing they're talking about.

**William Peare** [01:32:24]: looks like there's two.

**Daniel Kalinin** [01:32:26]: I did new, so I assume that's not the legacy, but we shall see.

**William Peare** [01:32:30]: not.

**William Peare** [01:32:31]: Yeah.

**William Peare** [01:32:32]: Yes, that's exactly the issue.

**Daniel Kalinin** [01:32:33]: The code is using old.

**Daniel Kalinin** [01:32:35]: I'll update the scraper to...

**Daniel Kalinin** [01:32:38]: Okay.

**Daniel Kalinin** [01:32:39]: I don't know what that means, but okay.

**William Peare** [01:32:43]: Yeah, it's probably...

**William Peare** [01:32:44]: Is that a part of Claude, by the way?

**Daniel Kalinin** [01:32:46]: Like, just not knowing what the hell the problem is?

**William Peare** [01:32:49]: Yes, in my opinion.

**William Peare** [01:32:52]: mean, you're a coder.

**William Peare** [01:32:53]: Like, neither me nor you comes from, like, a coding background.

**William Peare** [01:32:57]: So that you just know what you know until you know it.

**William Peare** [01:33:00]: Like, I'm getting to the point now where I'm like, yeah, not surprised this broke.

**William Peare** [01:33:03]: This isn't going.

**William Peare** [01:33:07]: Ooh, we're cooking.

**William Peare** [01:33:09]: We are cooking.

**William Peare** [01:33:11]: Yeah.

**William Peare** [01:33:15]: Now, since we don't have a place where this lands, I'm not exactly  sure if it's just going to kick you out of file.

**William Peare** [01:33:22]: Like, oh, right there.

**Daniel Kalinin** [01:33:22]: I believe that it automatically made this.

**Daniel Kalinin** [01:33:24]: Yeah.

**Daniel Kalinin** [01:33:25]: Yeah.

**William Peare** [01:33:25]: So this will be its default until we tell it to do something else.

**William Peare** [01:33:32]: Yeah.

**William Peare** [01:33:33]: Got it.

**Daniel Kalinin** [01:33:33]: do you, whenever you do this stuff, do you notice that you have to kind of, like, baby step it across the way?

**Daniel Kalinin** [01:33:39]: So, like, hey, then send it to tax, tax firm leads or something like that?

**Daniel Kalinin** [01:33:43]: Or does it usually just know what the next steps are?

**William Peare** [01:33:47]: Um, there's a few, you know, like, once it gets to know you or you're working in a project that you're doing, um, it will come up with a lot of it to yourself, depending on how much context you give it and, like, how much age.

**William Peare** [01:34:00]: You know, you're like, hey, this is my goal.

**William Peare** [01:34:02]: This is what I want to happen.

**William Peare** [01:34:03]: This is the end result.

**William Peare** [01:34:04]: Pick me the path of least resistance with the lowest cost of use tools because a lot of the things will have a small subscription or use cost.

**William Peare** [01:34:12]: So I'll normally tell like, hey, you know, make this budget friendly.

**William Peare** [01:34:16]: This is my end use.

**William Peare** [01:34:17]: Get me there.

**William Peare** [01:34:18]: Ask me questions that are super relevant.

**William Peare** [01:34:20]: Yeah, bam.

**Daniel Kalinin** [01:34:21]: This is like, dude, a few years ago, this would require like a freaking VA to do this for you or like hours of.

**William Peare** [01:34:33]: Totally.

**William Peare** [01:34:34]: Bam.

**Daniel Kalinin** [01:34:36]: Okay.

**Daniel Kalinin** [01:34:36]: We got TurboTax in the mix, which we don't want, but that's fine.

**William Peare** [01:34:45]: Yeah.

**William Peare** [01:34:47]: That's sick.

**William Peare** [01:34:49]: Yeah.

**William Peare** [01:34:51]: And this is like super base level.

**William Peare** [01:34:53]: I mean, it's not even, you know, pulling their contact info or anything like that.

**William Peare** [01:34:58]: Bam.

**William Peare** [01:34:59]: Just like that.

**Daniel Kalinin** [01:35:03]: Yeah.

**William Peare** [01:35:07]: I mean, you could even have it to the point easily where it's clicking into their site, then going to their contact page, getting a contact email, updating your GoHighLevel with that and their phone number.

**William Peare** [01:35:18]: That way your VA can just go through, you know, or an auto email service, et cetera, et cetera, and just roll through there.

**Daniel Kalinin** [01:35:24]: I was going to say, I guess the next steps with this would be, I have the name of the businesses, but then I would actually want to, I would want that outreach personalized.

**Daniel Kalinin** [01:35:38]: Yes.

**William Peare** [01:35:39]: Yeah.

**Daniel Kalinin** [01:35:41]: So, yeah.

**William Peare** [01:35:42]: couple options.

**William Peare** [01:35:43]: I mean, for, to get further information, obviously, we would want to make like this was just a quick use taste test.

**William Peare** [01:35:50]: mean, that did, what did that take us, 20 minutes.

**William Peare** [01:35:52]: Yeah.

**William Peare** [01:35:54]: You're going to need to give it more API access so it can actually get into like Chrome or get into just, I think it's just called Google.

**William Peare** [01:36:00]: Google API for the internet.

**William Peare** [01:36:01]: So that way it can actually start clicking through their UI, getting into the backends, get the contact email, get the phone number, pull all that, update it, get it all into GoHighLevel.

**William Peare** [01:36:12]: And then you're likely going to have it, you could do another, I mean, yeah, I think kind of sky's the limit there.

**William Peare** [01:36:24]: It could either be done with code or even GoHighLevel with personalization tokens.

**William Peare** [01:36:27]: You could have an email template that's pre-built in there.

**William Peare** [01:36:31]: Like grab first name, last name.

**William Peare** [01:36:34]: How personalized do you want to go for this outreach?

**William Peare** [01:36:37]: Like, do you want to actually be referencing stuff or just like names?

**William Peare** [01:36:40]: How do you want to roll that?

**Daniel Kalinin** [01:36:43]: Mainly just name and the guy's personal email if possible.

**Daniel Kalinin** [01:36:47]: So it would probably have to find the person's name of the company and then also probably then like go and search them up on like a public fee to get their like personal email.

**Daniel Kalinin** [01:37:00]: Yes.

**William Peare** [01:37:00]: Yeah.

**Daniel Kalinin** [01:37:01]: I think that's the main thing.

**Daniel Kalinin** [01:37:03]: Yep.

**William Peare** [01:37:03]: Yeah.

**William Peare** [01:37:04]: And you're probably going to want to integrate like Apollo, which is free for most use cases, but that's like a directory for businesses and their emails, like their personal stuff.

**William Peare** [01:37:14]: That adds a ton of information, but you're going to want to compile as much of that as you can.

**William Peare** [01:37:18]: And then, I mean, we could either do it through a go high level where you have an email template where it's using the first name, last name tokens to personalize them.

**William Peare** [01:37:26]: And then you could have it on an automation, hey, when it hits Web Scraper next morning at the hours of eight to nine, send out this first email and then wait two days.

**William Peare** [01:37:35]: Like you could have it on pretty much running it through its own sequence there.

**Daniel Kalinin** [01:37:41]: So I can, I can do the outreach through Claude is what you're saying?

**Daniel Kalinin** [01:37:45]: You could.

**William Peare** [01:37:46]: So the downside to Claude and Gmail is Claude cannot automatically send emails.

**William Peare** [01:37:52]: So then you're either talking like integrating it with MailChimp or take your pick or go high level.

**William Peare** [01:38:00]: We'll do it automatically.

**William Peare** [01:38:01]: The most Google can do is put it as a draft.

**William Peare** [01:38:05]: It can't actually send emails by itself.

**William Peare** [01:38:08]: Okay.

**Daniel Kalinin** [01:38:09]: Yeah.

**Daniel Kalinin** [01:38:12]: Got it.

**William Peare** [01:38:12]: Yeah.

**William Peare** [01:38:13]: Sky's the  limit, though, with this.

**William Peare** [01:38:15]: Yeah, no, that's super cool.

**Daniel Kalinin** [01:38:18]: And whenever you structure projects, would you rather have it do, like, okay, so it just scraped a bunch of tax firms, from there, would you want it in the same kind of workflow to then find the people, like, the owners of those tax firms?

**Daniel Kalinin** [01:38:44]: Or would that be, like, its own separate kind of file slash project where then it takes that data and does that?

**William Peare** [01:38:55]: If it's one linear flow like that, I normally put it into one project.

**William Peare** [01:38:59]: Because if...

**William Peare** [01:39:00]: If not, you're going to have to trigger it off something, you know what mean?

**William Peare** [01:39:02]: Then you're going to like, you could easily do that.

**William Peare** [01:39:04]: Like a new opportunity is added in this stage to go high level, trigger  X, Y, and Z.

**William Peare** [01:39:10]: But then you just have more things you're working with and more things that can break.

**William Peare** [01:39:14]: Because at this point, when this is already built, you could just add that to the scope of this code.

**William Peare** [01:39:18]: Like, hey, once you found these leads, then I want you to do this.

**William Peare** [01:39:22]: And it's going to be like, oh, cool.

**William Peare** [01:39:23]: I need this API token.

**William Peare** [01:39:24]: I need this.

**William Peare** [01:39:25]: Where do you want it stored?

**William Peare** [01:39:29]: Yep.

**William Peare** [01:39:35]: But you can see what I mean.

**William Peare** [01:39:36]: If you're doing this, I guess you were doing it through Madness.

**William Peare** [01:39:38]: But if you're trying to do this through the  terminal, like good luck.

**William Peare** [01:39:42]: PowerShell is not offering much helpful insight into next steps.

**Daniel Kalinin** [01:39:46]: Although I would say someone needs to create a software that can make everything that you type, type out like this.

**Daniel Kalinin** [01:39:57]: Now, I used to type out a lot cooler.

**Daniel Kalinin** [01:39:59]: Do you know?

**Daniel Kalinin** [01:40:00]: If not, you're going to have to trigger it off something, you know what mean?

**Daniel Kalinin** [01:40:02]: Then you're going to like, you could easily do that.

**Daniel Kalinin** [01:40:04]: Like a new opportunity is added in this stage to go high level, trigger  X, Y, and Z.

**Daniel Kalinin** [01:40:10]: But then you just have more things you're working with and more things that can break.

**Daniel Kalinin** [01:40:14]: Because at this point, when this is already built, you could just add that to the scope of this code.

**Daniel Kalinin** [01:40:18]: Like, hey, once you found these leads, then I want you to do this.

**Daniel Kalinin** [01:40:22]: And it's going to be like, oh, cool.

**Daniel Kalinin** [01:40:23]: I need this API token.

**Daniel Kalinin** [01:40:24]: I need this.

**Daniel Kalinin** [01:40:25]: Where do you want it stored?

**William Peare** [01:40:29]: Yep.

**Daniel Kalinin** [01:40:35]: But you can see what I mean.

**Daniel Kalinin** [01:40:36]: If you're doing this, I guess you were doing it through Madness.

**Daniel Kalinin** [01:40:38]: But if you're trying to do this through the  terminal, like good luck.

**Daniel Kalinin** [01:40:42]: PowerShell is not offering much helpful insight into next steps.

**Daniel Kalinin** [01:40:46]: Although I would say someone needs to create a software that can make everything that you type, type out like this.

**Daniel Kalinin** [01:40:57]: Now, I used to type out a lot cooler.

**Daniel Kalinin** [01:40:59]: Do you know?

**Daniel Kalinin** [01:41:00]: I like Legacy used to type out, like where it'd be that white box and stuff like that.

**William Peare** [01:41:04]: Oh, yeah, yeah, yeah.

**Daniel Kalinin** [01:41:06]: That's like, it's so smooth for me.

**Daniel Kalinin** [01:41:08]: I love that.

**William Peare** [01:41:10]: Okay, so.

**William Peare** [01:41:11]: Yep, Apollo, yeah.

**William Peare** [01:41:14]: Uh-huh.

**Daniel Kalinin** [01:41:15]: 50 credits a month.

**Daniel Kalinin** [01:41:17]: Best match for what you're doing.

**Daniel Kalinin** [01:41:19]: Okay, cool.

**Daniel Kalinin** [01:41:20]: My recommendation, Apollo, it's because it, okay, it gives you any returns.

**Daniel Kalinin** [01:41:25]: Okay.

**Daniel Kalinin** [01:41:27]: Apollo's definitely the move for a cold, like, B2B outreach.

**Daniel Kalinin** [01:41:32]: It's the gold standard.

**Daniel Kalinin** [01:41:33]: I know those guys lose a lot of money, though.

**Daniel Kalinin** [01:41:38]: Apollo?

**Daniel Kalinin** [01:41:39]: Yeah, I believe they lose a lot, but I guess it's just a longer-term play that they have.

**William Peare** [01:41:46]: Hmm.

**William Peare** [01:41:46]: I haven't looked into it.

**William Peare** [01:41:48]: So it's not profitable.

**William Peare** [01:41:50]: I might be wrong, but I feel like I've spoken to somebody who goes cold email pretty heavily, so he always uses Apollo.

**William Peare** [01:42:00]: And they, how do it get me out of here?

**William Peare** [01:42:04]: Yeah, something about them just like not being profitable at all.

**William Peare** [01:42:11]: It doesn't, yeah.

**William Peare** [01:42:11]: I wonder how they get the information.

**William Peare** [01:42:15]: Probably like back-end transactions.

**Daniel Kalinin** [01:42:17]: That's the  that Facebook shut down a while ago where banks used to communicate with Facebook and route like transaction history over to Facebook.

**Daniel Kalinin** [01:42:28]: So Facebook would see what people are actually buying and then they would send them ads based on.

**Daniel Kalinin** [01:42:34]: Oh my Lord.

**Daniel Kalinin** [01:42:35]: Yeah, mean, that was a lawsuit and a half, but really cool concept.

**Daniel Kalinin** [01:42:40]: Yeah, great, great concept.

**Daniel Kalinin** [01:42:42]: I love that.

**Daniel Kalinin** [01:42:43]: I love that.

**Daniel Kalinin** [01:42:45]: I know when I first started dealing with the marketers and they were like, yeah, cool, we're going to get you on the geolocation.

**Daniel Kalinin** [01:42:50]: And I'm like, we're going to  do what?

**Daniel Kalinin** [01:42:52]: And it's like, well, it's just going to like ping their phone or device.

**Daniel Kalinin** [01:42:54]: And if they're in this radius of these nice houses you want and they earn X amount and they hit this demographic and I'm

**Daniel Kalinin** [01:43:00]: Like, it  knows all of this?

**Daniel Kalinin** [01:43:02]: What the ?

**Daniel Kalinin** [01:43:03]: Like, are you serious?

**Daniel Kalinin** [01:43:04]: It's like, yes, of course it does.

**Daniel Kalinin** [01:43:05]: I'm like, that is  up.

**Daniel Kalinin** [01:43:07]: So you're saying if they walk into this little circle I draw on the map, it's going to ping them with my ad.

**Daniel Kalinin** [01:43:12]: Wild.

**Daniel Kalinin** [01:43:14]: The information that is out there is just, yeah, pretty, pretty wild.

**Daniel Kalinin** [01:43:23]: Okay, so sign up.

**William Peare** [01:43:25]: Let me go to the API key.

**Daniel Kalinin** [01:43:29]: Mailbox linked, okay.

**Daniel Kalinin** [01:43:33]: Integrations.

**William Peare** [01:43:34]: Cloud.

**William Peare** [01:43:35]: No.

**William Peare** [01:43:36]: API.

**Daniel Kalinin** [01:43:36]: Search API, probably search API.

**Daniel Kalinin** [01:43:48]: Oh, since you already have the fine companies and people from scratch, enrichment.

**William Peare** [01:43:55]: Okay.

**William Peare** [01:44:02]: Not about to deal with this.

**William Peare** [01:44:05]: Grab your key.

**Daniel Kalinin** [01:44:15]: You're on the docs page.

**Daniel Kalinin** [01:44:17]: Account settings not here.

**Daniel Kalinin** [01:44:18]: Click the account avatar.

**Daniel Kalinin** [01:44:28]: Look for integrations are the API keys.

**Daniel Kalinin** [01:44:30]: Okay, so quad, code.

**Daniel Kalinin** [01:44:33]: See, by the time I'm ready to start this, I'm already going to have tested the concept completely with you, and I'm going to know exactly how it works.

**Daniel Kalinin** [01:44:40]: Log code, enrich leads.

**William Peare** [01:44:44]: Select an API.

**Daniel Kalinin** [01:44:50]: Which API to use?

**Daniel Kalinin** [01:44:52]: Oh, what scopes, yeah.

**William Peare** [01:44:55]: Select these two.

**William Peare** [01:45:00]: What the heck?

**William Peare** [01:45:02]: No, it's the one that I can't.

**Daniel Kalinin** [01:45:03]: Why can't you click it?

**William Peare** [01:45:07]: No clue.

**William Peare** [01:45:08]: Let's see this one.

**William Peare** [01:45:11]: Okay, that one I can click.

**William Peare** [01:45:13]: Also check this if it's available.

**Daniel Kalinin** [01:45:20]: Enrich.

**Daniel Kalinin** [01:45:21]: At the minimum, I just select match, but I can't do match.

**Daniel Kalinin** [01:45:29]: Let me press the plan.

**Daniel Kalinin** [01:45:30]: to be on an upgraded plan.

**Daniel Kalinin** [01:45:33]: Maybe.

**Daniel Kalinin** [01:45:34]: The other two I could.

**William Peare** [01:45:46]: It's likely a plan restriction.

**William Peare** [01:45:47]: No problem.

**William Peare** [01:45:48]: can use instead, which lets us search for people.

**William Peare** [01:45:50]: Okay.

**Daniel Kalinin** [01:45:55]: You need the contact search one, though.

**Daniel Kalinin** [01:46:00]: Did it just?

**Daniel Kalinin** [01:46:01]: I think so.

**Daniel Kalinin** [01:46:04]: What is the master key, by the way?

**Daniel Kalinin** [01:46:05]: Do you know what that is?

**Daniel Kalinin** [01:46:07]: No, I do not know what that is.

**Daniel Kalinin** [01:46:11]: I would assume that it's one that then can access multiple sub, dome, sub keys.

**Daniel Kalinin** [01:46:16]: Yeah.

**Daniel Kalinin** [01:46:18]: Okay.

**Daniel Kalinin** [01:46:19]: So select these two, create API key, copy, got it, step to the project.

**Daniel Kalinin** [01:46:40]: It stops warning you about it.

**Daniel Kalinin** [01:46:42]: It's like,  it.

**Daniel Kalinin** [01:46:42]: get it.

**Daniel Kalinin** [01:46:43]: You want me to put it in.

**Daniel Kalinin** [01:46:44]: You know how annoying it is to go and enter all these into a root file just so it can go.

**William Peare** [01:46:48]: You can view the root file.

**Daniel Kalinin** [01:46:50]: You are writing the code.

**Daniel Kalinin** [01:46:51]: You're seeing it anywhere.

**Daniel Kalinin** [01:46:53]: The whole thing.

**Daniel Kalinin** [01:46:56]: Okay.

**Daniel Kalinin** [01:46:56]: To scrape tax firms, then run in rich bets, look up.

**Daniel Kalinin** [01:47:00]: Owners, can I just run the runenrichment.bat if I already have leads inside of the Fathom, leads.csv?

**Daniel Kalinin** [01:47:19]: Yes, just run, okay.

**Daniel Kalinin** [01:47:21]: Damn, this is like...

**Daniel Kalinin** [01:47:22]: Yeah.

**Daniel Kalinin** [01:47:24]: .

**Daniel Kalinin** [01:47:25]: Okay.

**Daniel Kalinin** [01:47:26]: It's wild.

**Daniel Kalinin** [01:47:28]: Runenrich.bat, Windows batch file, okay.

**William Peare** [01:47:32]: It reads from, doesn't care how much data there is, okay.

**Daniel Kalinin** [01:47:40]: damn, if it cooks something up right now, that's just like, I don't know, because this is like, how many people are here?

**Daniel Kalinin** [01:47:48]: Oh, them all.

**Daniel Kalinin** [01:47:48]: Yeah.

**Daniel Kalinin** [01:47:49]: Yeah.

**Daniel Kalinin** [01:47:49]: There's like, I just got like 430 leads that I can probably end up booking a call with like, I don't

**William Peare** [01:48:00]: Yeah, a few of them, five or something.

**William Peare** [01:48:02]: you spent an hour and you might actually get a couple calls for like maybe two hours of, yeah.

**William Peare** [01:48:08]: I mean, that one might take a little longer, but it's pretty wild.

**William Peare** [01:48:11]: I want to automate Gamma too.

**William Peare** [01:48:12]: I'd be curious because with Gamma, if I just have a repeated structure like that I create for the tax firm one, it'd be pretty cool if Claude could just then recreate that structure for other niches.

**Daniel Kalinin** [01:48:32]: 100%.

**Daniel Kalinin** [01:48:32]: 100% will do that.

**Daniel Kalinin** [01:48:35]: Yeah, Gamma.

**Daniel Kalinin** [01:48:47]: I also need to make it nicer.

**Daniel Kalinin** [01:48:48]: Design's always been the thing that like I just don't get at all.

**Daniel Kalinin** [01:48:52]: Have you tried Claude design?

**William Peare** [01:48:55]: No.

**Daniel Kalinin** [01:48:57]: Probably worked what you have.

**Daniel Kalinin** [01:48:58]: You have to...

**Daniel Kalinin** [01:49:01]: Yeah, it's only on the web version, not the desktop, so you have to log in through your web one, but I think you get five free per month because it's in beta right now.

**William Peare** [01:49:11]: Yeah, and it will go through, it can either make stuff from scratch, obviously, but mostly what it's for is like you have things already you want refined and it'll help go through like colors, fonts, tones, stuff like that and do that  because I hate that.

**Daniel Kalinin** [01:49:24]: I think Gamma could 100% do this, by the way, because they got API keys, so I'm guessing Claude can just code whatever it needs to.

**Daniel Kalinin** [01:49:35]: Yeah, that's like disgusting.

**Daniel Kalinin** [01:49:38]: I know, isn't it?

**Daniel Kalinin** [01:49:40]: Pretty horrifying.

**Daniel Kalinin** [01:49:41]: Yeah.

**Daniel Kalinin** [01:49:43]: I think the more that I'm like more, the more I'm immersed into all this, the more that like Cameron England guy kind of speaks to me where it's like, if you don't figure this out, you are so cooked.

**William Peare** [01:49:52]: Yeah, there's going to be business owners in like two years that are still trying to

**William Peare** [01:50:00]: code outreach manually or whatever, they're just going to get killed through inefficiency.

**William Peare** [01:50:05]: That's probably the best way to put it.

**Daniel Kalinin** [01:50:07]: There's not even a chance of keeping up with it.

**Daniel Kalinin** [01:50:11]: Yeah.

**Daniel Kalinin** [01:50:15]: He also framed it from a profitability standpoint.

**Daniel Kalinin** [01:50:19]: It's like you could either automate your roles or what'd say?

**Daniel Kalinin** [01:50:28]: Or die, pretty much.

**Daniel Kalinin** [01:50:29]: Yeah, pretty much.

**William Peare** [01:50:31]: Yeah, because if you automate everything and you can give your employees more leverage, like a media buyer being able to take on 60 accounts instead of 40, your profitability goes up incrementally through every role that you pretty much just under-leverage in a sense, I guess.

**William Peare** [01:50:51]: I have 100%.

**Daniel Kalinin** [01:50:51]: You're just growing it to the moon, essentially.

**Daniel Kalinin** [01:50:55]: Yeah.

**Daniel Kalinin** [01:50:57]: No, like as soon as I started, because I'd done-

**Daniel Kalinin** [01:51:00]: I was huge on manual, and I did almost everything by myself.

**Daniel Kalinin** [01:51:03]: And then once I really started diving into it, I was like, are you  kidding me?

**Daniel Kalinin** [01:51:07]: Okay, so they cooked me here.

**Daniel Kalinin** [01:51:11]: Owners found for none.

**Daniel Kalinin** [01:51:13]: What's the problem?

**Daniel Kalinin** [01:51:15]: I might need to add that other scope in, huh?

**Daniel Kalinin** [01:51:19]: Potentially.

**Daniel Kalinin** [01:51:20]: The one that, yeah, comes with the subscription.

**Daniel Kalinin** [01:51:25]: Most likely the domain parameter needs to be sent as an array.

**Daniel Kalinin** [01:51:28]: Let me debug output to see exactly what Apollo is returning.

**Daniel Kalinin** [01:51:32]: Yeah, I know.

**Daniel Kalinin** [01:51:33]: And share the first two lines of the output, okay.

**Daniel Kalinin** [01:51:36]: Half the time when it's talking to me, I'm like, , of course that was the problem.

**Daniel Kalinin** [01:51:40]: Yeah, you didn't  sort the array.

**Daniel Kalinin** [01:51:42]: Like, I would have known that had I looked.

**William Peare** [01:51:44]: Like, just, thanks for helping.

**Daniel Kalinin** [01:51:46]: Some of this  it says, I'm like, totally.

**Daniel Kalinin** [01:51:48]: That's great.

**Daniel Kalinin** [01:51:49]: I'm glad that we're going through this.

**Daniel Kalinin** [01:51:53]: Run enrichment bat, okay.

**Daniel Kalinin** [01:51:56]: Run enrichment bat again, and share the first two lines.

**Daniel Kalinin** [01:51:59]: lines.

**Daniel Kalinin** [01:51:59]: I

**Daniel Kalinin** [01:52:00]: API, oh man, this is the error.

**Daniel Kalinin** [01:52:14]: So let's see Apollo, if it's just like restricting me on usage and all that other stuff.

**Daniel Kalinin** [01:52:32]: Two problems, the rate limit, free plan, UF4 and zero contacts found doesn't have data on small local firms.

**Daniel Kalinin** [01:52:38]: The rate limit is fixable.

**Daniel Kalinin** [01:52:40]: The bigger issue is...

**Daniel Kalinin** [01:52:43]: They're too small?

**Daniel Kalinin** [01:52:46]: I wouldn't think they're too small, but...

**William Peare** [01:53:48]: Bigger issue, let me update the script, probably run with 300 at 18 seconds each.

**Daniel Kalinin** [01:54:00]: This will take about 130 minutes.

**William Peare** [01:54:01]: I don't care.

**William Peare** [01:54:02]: I'll let it run in the background.

**Daniel Kalinin** [01:54:03]: However, the big concern is that ZeroContext came back for the first five leads.

**William Peare** [01:54:08]: Most likely the reason is plan restrictions, not missing data.

**Daniel Kalinin** [01:54:11]: What I'm looking at is missing compared to, this is the key one, data almost certainly, the free plan just blocks access to it, unlock API, use Apollo's UI manually, upload your CSV enrichment.

**Daniel Kalinin** [01:54:37]: This is going to be great.

**Daniel Kalinin** [01:54:53]: I'm going to know exactly how worth it this is before I even pay for it.

**Daniel Kalinin** [01:54:58]: I appreciate it.

**Daniel Kalinin** [01:55:00]: So much.

**Daniel Kalinin** [01:55:01]: It's going to be great.

**Daniel Kalinin** [01:55:05]: Okay, now I don't even know.

**Daniel Kalinin** [01:55:07]: I can promise you Apollo works great though.

**Daniel Kalinin** [01:55:10]: I'm sure it does.

**Daniel Kalinin** [01:55:11]: know everybody uses it.

**Daniel Kalinin** [01:55:13]: Yeah.

**Daniel Kalinin** [01:55:14]: Plan overview, but why am I on the basic plan if I thought I just upgraded to the other one?

**Daniel Kalinin** [01:55:26]: 65 a month.

**Daniel Kalinin** [01:55:28]: Credits in your plan.

**Daniel Kalinin** [01:55:31]: I feel like this is the old one.

**Daniel Kalinin** [01:55:33]: I think I just upgraded Apollo to the $65 per month plan.

**Daniel Kalinin** [01:55:47]: And how can I, billing, plan overview, this is what I was at right now.

**Daniel Kalinin** [01:56:00]: So now, plan overview.

**Daniel Kalinin** [01:56:03]: Okay, that's the same thing.

**Daniel Kalinin** [01:56:07]: Whatever, let's just see.

**Daniel Kalinin** [01:56:21]: Great.

**Daniel Kalinin** [01:56:22]: The API enrichment should be unlocked.

**Daniel Kalinin** [01:56:24]: Running again on that note, you may need to re-generate key after upgrading since plan permissions sometimes don't apply.

**Daniel Kalinin** [01:56:30]: Okay, cool.

**Daniel Kalinin** [01:56:30]: So let's do that.

**William Peare** [01:56:39]: Integrations, API keys, create a new key.

**Daniel Kalinin** [01:56:48]: that you've upgraded, you have to make a new one?

**Daniel Kalinin** [01:56:50]: what's it?

**Daniel Kalinin** [01:56:51]: What's it?

**Daniel Kalinin** [01:56:51]: Rich leads B2.

**Daniel Kalinin** [01:56:57]: think so.

**Daniel Kalinin** [01:56:58]: Yeah.

**Daniel Kalinin** [01:57:02]: What APIs to associate the key with.

**Daniel Kalinin** [01:57:10]: Yeah, let's see if that works.

**Daniel Kalinin** [01:57:27]: Please be available.

**Daniel Kalinin** [01:57:28]: No, it's not available.

**Daniel Kalinin** [01:57:34]: Why do you think?

**Daniel Kalinin** [01:57:35]: Did it give you feedback on that?

**William Peare** [01:57:52]: Don't worry about it.

**William Peare** [01:57:54]: I hired to hear a waterfall enrichment feature.

**William Peare** [01:57:56]: We don't need it.

**Daniel Kalinin** [01:57:56]: Our script uses...

**Daniel Kalinin** [01:57:57]: Okay.

**Daniel Kalinin** [01:57:59]: No, I already...

**Daniel Kalinin** [01:58:00]: He set this as a master key.

**Daniel Kalinin** [01:58:01]: That's annoying.

**Daniel Kalinin** [01:58:13]: I set it.

**Daniel Kalinin** [01:58:13]: Okay.

**Daniel Kalinin** [01:58:15]: All right.

**Daniel Kalinin** [01:58:16]: We're just going to try it.

**Daniel Kalinin** [01:58:19]: Copy.

**Daniel Kalinin** [01:58:19]: Let me speed up delay so it doesn't take two hours.

**Daniel Kalinin** [01:58:31]: Run it now.

**Daniel Kalinin** [01:58:32]: But now it's just saying not found.

**Daniel Kalinin** [01:58:46]: That's sweet.

**Daniel Kalinin** [01:58:52]: Still not found.

**Daniel Kalinin** [01:58:53]: It's doing something now.

**William Peare** [01:58:56]: Yeah.

**William Peare** [01:59:24]: Small local firms.

**William Peare** [01:59:25]: Let me update the script.

**William Peare** [01:59:27]: My company name is a fallback.

**William Peare** [01:59:46]: If I just exit out, it's going to stop the script, right?

**William Peare** [01:59:50]: Where?

**William Peare** [01:59:51]: I just exited it out.

**William Peare** [01:59:53]: Yeah.

**William Peare** [01:59:55]: No, it's not.

**William Peare** [01:59:57]: Yeah, I don't think so.

**William Peare** [01:59:58]: Okay.

**William Peare** [02:00:00]: All right.

**William Peare** [02:00:01]: I'll play around with this.

**William Peare** [02:00:02]: What do you think the next steps are for me?

**William Peare** [02:00:06]: I think, I mean, you're really cracking on this pretty good.

**William Peare** [02:00:09]: So I think you keep questions, comments, concerns open on bottlenecks you're running into.

**William Peare** [02:00:13]: And I mean, feel free to, what's your preference?

**William Peare** [02:00:16]: Text, email, Slack.

**William Peare** [02:00:17]: We have all three now.

**William Peare** [02:00:18]: What is your preference?

**William Peare** [02:00:20]: You can just talk to Yeah.

**William Peare** [02:00:22]: So feel free to just text back and forth.

**William Peare** [02:00:25]: I'm on retainer.

**William Peare** [02:00:26]: Shoot me a text anytime you're running into something.

**William Peare** [02:00:28]: So I can either check on my end and see what I run into, or we can just have a dialogue on it.

**William Peare** [02:00:33]: And then I'll put together a whole financial model document.

**William Peare** [02:00:37]: And next time we do the breakeven analysis and we do the financial model, that way you can kind of, as the people are coming in, we already know what you want to do with the VA and the hiring.

**William Peare** [02:00:46]: Then we can really look at like, what's the next step in terms of price point?

**William Peare** [02:00:49]: Do I like bring on a VA and automate a bunch of  and try and hit huge volume quick at a slightly lower price point to kind of get foot in the door?

**William Peare** [02:00:56]: Or do I want to go for higher end products, lower?

**William Peare** [02:01:00]: Closing rate, potentially, but less work for actual deliverables.

**William Peare** [02:01:04]: I'd like to run through that.

**William Peare** [02:01:06]: And at that point, I think our next meeting after that is we actually go on about onboarding and training employees and how you actually run employees, because that's probably going to be one of the biggest...

**William Peare** [02:01:19]: It's a super  hard skill to learn, first off.

**William Peare** [02:01:24]: It's very, very hard to do.

**William Peare** [02:01:25]: You're easy to talk to.

**William Peare** [02:01:27]: You're not going to have any issue with it in terms of your people skills.

**William Peare** [02:01:30]: It just is something that, like, it's hard to do.

**William Peare** [02:01:34]: You don't do it until you do it.

**William Peare** [02:01:35]: And you've kind of always, it seems like potentially, except for doing like internships, pretty much always run your own business and work for yourself.

**William Peare** [02:01:43]: Yeah.

**William Peare** [02:01:44]: Yeah.

**Daniel Kalinin** [02:01:44]: So that's probably going to be the biggest stepping stone is actually taking that next leap to actually like running teams under you.

**William Peare** [02:01:51]: So I think we go through financial models, we go through breakeven analysis.

**William Peare** [02:01:54]: And then after that, we go through kind of like the hiring plan, what onboarding looks...

**William Peare** [02:02:00]: Like what support you should be planned on giving, what's a realistic timeline, and someone actually getting to the point where they're useful and not feeling like it's lost money for two months when they suck.

**William Peare** [02:02:09]: Just making sure you have realistic expectations, how much input it's going to be.

**William Peare** [02:02:13]: It's not going to make your workload easier for probably 90 days.

**William Peare** [02:02:16]: They'll take some low-hanging fruit off your plate, but it's really going to be the three to six-month mark where you're really like, , cool.

**William Peare** [02:02:23]: Those guys are confident.

**William Peare** [02:02:24]: They're running.

**William Peare** [02:02:25]: I'm actually to the point now where I can put a lot of energy into something else.

**William Peare** [02:02:28]: Because on the front end, you're probably going to get busier, man.

**William Peare** [02:02:31]: Like it's probably going to be harder because you're going to not only have to be doing what you do, but you're also going to have to babysit their work and train them.

**William Peare** [02:02:38]: And that's just like it's a cost of getting to that point, in my opinion.

**William Peare** [02:02:43]: I'm guessing I can't just threaten to fire them if they don't learn it in a week, right?

**William Peare** [02:02:47]: You can.

**William Peare** [02:02:48]: You're just going to have to train someone else.

**William Peare** [02:02:50]: Like you could potentially, like, you know, do it until you get a hire that just learns faster than others.

**William Peare** [02:02:54]: But we also go through the interview process.

**William Peare** [02:02:59]: can.

**William Peare** [02:02:59]: can.

**William Peare** [02:02:59]: can.

**William Peare** [02:02:59]: You You You

**William Peare** [02:03:00]: And kind of like how you're vetting the culture fit.

**Daniel Kalinin** [02:03:03]: And I'm even happy to hop on, like if you want me to hop on as like a partner or this is my tech consultant, like bring me in onto the interviews as some phantom role, just so that after the interviews, like I could ask some pointed questions and I can also offer you on feedback on like things I saw, how I would structure it and stuff of that nature.

**Daniel Kalinin** [02:03:23]: I think that is your next two big steps for our next couple of meetings.

**Daniel Kalinin** [02:03:27]: And then I'd be super stoked, especially with me going remote.

**William Peare** [02:03:30]: If you want to like, you're going to learn a lot by doing it.

**William Peare** [02:03:33]: And I find it to be kind of fun.

**William Peare** [02:03:35]: But if you have some stuff that you're like, Hey, this is just something like the go high level integration or something.

**William Peare** [02:03:40]: If you want to just be like, Hey, this is something I want to work on.

**Daniel Kalinin** [02:03:42]: Can you build this out and store it online?

**Daniel Kalinin** [02:03:44]: Because we can just share a GitHub.

**Daniel Kalinin** [02:03:46]: They're free.

**Daniel Kalinin** [02:03:47]: Like we could just have a shared GitHub folder and I could upload the code into there.

**Daniel Kalinin** [02:03:52]: And then you can just sync it.

**Daniel Kalinin** [02:03:55]: I'm happy to start knocking out some project work for you on the retainer.

**Daniel Kalinin** [02:03:58]: gives me great experience on working with.

**Daniel Kalinin** [02:04:00]: Different programs.

**Daniel Kalinin** [02:04:00]: Gets you quick deliverables you can actually use.

**William Peare** [02:04:03]: So those are my next couple steps.

**William Peare** [02:04:05]: I think you're learning too fast.

**William Peare** [02:04:08]: I hope so.

**William Peare** [02:04:09]: Yeah.

**William Peare** [02:04:09]: I need to make more money.

**William Peare** [02:04:11]: But I was watching this guy, same guy, by the way, that exits companies, Eddie.

**William Peare** [02:04:15]: He says that with his company, what they do is they make the, what's the thing that people do whenever they want to work with a company?

**William Peare** [02:04:25]: Like they have to like submit something.

**William Peare** [02:04:27]: What is that called?

**William Peare** [02:04:28]: When they want to work with a company?

**William Peare** [02:04:30]: submit, submit a resume.

**William Peare** [02:04:32]: Oh, a resume.

**William Peare** [02:04:34]: Yeah.

**William Peare** [02:04:34]: Resume form.

**William Peare** [02:04:35]: job application.

**William Peare** [02:04:36]: Yeah.

**William Peare** [02:04:37]: you, dude.

**William Peare** [02:04:39]: Wow.

**William Peare** [02:04:39]: Must be nice.

**William Peare** [02:04:42]: Yeah.

**William Peare** [02:04:43]: He, he basically says that, uh, he makes the job application so like long, like 40, 50 minutes.

**William Peare** [02:04:52]: Oh, I mean, I wouldn't do it to that extent.

**William Peare** [02:04:54]: He just, he needs to hire players, but he makes it really annoying or really long.

**William Peare** [02:04:58]: He to get through because, you know.

**William Peare** [02:05:00]: Doesn't want to, like, fill it up with garbage, if that makes sense.

**William Peare** [02:05:03]: Yeah, no, 100%.

**William Peare** [02:05:04]: We, when I hire, I mean, if it's a field role, like if I'm hiring a  reefer, I'm like, cool, you've got a set of tool belts, you're not afraid of heights, you can be here at 6 a.m.

**William Peare** [02:05:12]: every morning, sold.

**William Peare** [02:05:15]: That's kind of the qualifications.

**William Peare** [02:05:16]: And then I have a two-week, we have a two-week period.

**William Peare** [02:05:21]: Everyone, at least field workers, goes through a two-week probation period.

**William Peare** [02:05:24]: So they show up.

**William Peare** [02:05:25]: If they  sneeze wrong, if they're late one minute, like if they do anything at all in that two weeks, they're cut.

**William Peare** [02:05:31]: And then at the end of the two weeks, I pull together every single member on their crew, and every single person gets a thumbs up, thumbs down.

**William Peare** [02:05:38]: Like if you just, like, some of the guys thought you're a dick, and they didn't like you, or you didn't jive with the whole team, those guys are out there doing miserable- work all day.

**William Peare** [02:05:46]: So, like, they have to at least be able to have fun and have a good relationship.

**Daniel Kalinin** [02:05:50]: So if it's not, if they don't fit with the team, they're out just for that.

**Daniel Kalinin** [02:05:53]: For office roles and, like, higher paid admin roles, I normally do, like, two to three interviews.

**Daniel Kalinin** [02:06:00]: Like, I'll normally interview, then I'll normally do an interview with, like, me and their lead, and then I'll normally do an interview with, like, me and the owner or the leadership group.

**Daniel Kalinin** [02:06:07]: So, like, we grill the  out of them.

**Daniel Kalinin** [02:06:10]: We'll do, like, personality tests or disk assessments, so we'll have stuff we have to do beforehand.

**Daniel Kalinin** [02:06:16]: Yeah, like, that's pretty critical, I think.

**Daniel Kalinin** [02:06:18]: And then, yeah, the application process, we'll normally have, like, either video submittals or, like, a huge long list of questions, some of which might not even be super relevant to the role, just to see if they're willing to take the time and actually put thought and energy into answering them.

**Daniel Kalinin** [02:06:33]: So, like, I make it pretty difficult because I run my people pretty hard.

**William Peare** [02:06:37]: Like, we pay good, but I also expect a lot.

**Daniel Kalinin** [02:06:39]: So, like, if they're not willing to, like, put in a lot for the application when they should be trying their hardest almost, you're probably going to have them for two months and they're going to immediately start.

**Daniel Kalinin** [02:06:49]: Yeah, that guy's logic and he had a debate with one of his, like, recruiters where it was, like, the recruiter wanted to ask, like, dumb questions like Sally had two apples.

**Daniel Kalinin** [02:07:00]: John took one of them away.

**Daniel Kalinin** [02:07:02]: Yeah, and he was like, Eddie, was like, this is retarded.

**Daniel Kalinin** [02:07:06]: It has nothing to do with the business.

**Daniel Kalinin** [02:07:08]: And the recruiter was like, yeah, but if they can't even answer a simple Sally and John question, like, you know, what does that say about them?

**William Peare** [02:07:14]: So they purposely try to make it so that nobody gets through the form.

**Daniel Kalinin** [02:07:19]: And if someone does get through the form, that's when they kind of like start analyzing everything.

**Daniel Kalinin** [02:07:25]: Yeah, think you really got to do a ton of vetting on the front end.

**William Peare** [02:07:29]: Yeah.

**William Peare** [02:07:31]: And I think I can, I can just run ads to like Columbia or something.

**William Peare** [02:07:35]: Same time zone, speak English, all that kind of stuff.

**William Peare** [02:07:41]: Yeah.

**Daniel Kalinin** [02:07:41]: I think the one of my VAs for BizBooster, she's one hour behind me.

**Daniel Kalinin** [02:07:47]: She's in Columbia, but yeah, they really good experience with them.

**Daniel Kalinin** [02:07:53]: So I might just run ads there and just make it also like a bit difficult to get through.

**Daniel Kalinin** [02:07:57]: And I mean, if somebody wants a job and they're willing to go through.

**William Peare** [02:08:00]: A good amount of questions, then, you know, I want quality, I guess is what I'm trying to say, and I'm happy to pay.

**William Peare** [02:08:05]: I just need to get a few more clients, that way it kind of like spreads easier across like the expenses.

**William Peare** [02:08:14]: Sure, that makes sense.

**William Peare** [02:08:16]: Okay, cool.

**William Peare** [02:08:17]: I'm going to ram through everything.

**William Peare** [02:08:18]: If you have any next steps for me, feel free to email it.

**William Peare** [02:08:21]: I hope the weekend goes well for you and happy belated birthday again.

**William Peare** [02:08:26]: Oh, thanks, bud.

**William Peare** [02:08:27]: Yeah, no, it's, I'll send over the next steps.

**William Peare** [02:08:30]: What, when do you want to do the next one?

**William Peare** [02:08:31]: What's your schedule like?

**William Peare** [02:08:35]: I'm testing, I'm testing my AI agent right now.

**William Peare** [02:08:39]: So, Fathom, you better get this date and time and calendar.

**William Peare** [02:08:42]: Let's, you have his email already, so don't  it up.

**William Peare** [02:08:45]: We can do Monday.

**William Peare** [02:08:47]: Monday, what time do you want to do?

**William Peare** [02:08:48]: Traditional?

**William Peare** [02:08:49]: know you're doing, yeah, is that fine?

**William Peare** [02:08:52]: Because I know you said your wife wants you to be earlier now.

**William Peare** [02:08:55]: Yeah, I mean, I can do like two to four, three to five.

**William Peare** [02:08:59]: can right back.

**William Peare** [02:09:00]: Two to four, three to five, I'm trying to think.

**Daniel Kalinin** [02:09:03]: Your time.

**Daniel Kalinin** [02:09:05]: Yeah.

**William Peare** [02:09:09]: Monday, I'm still in the office.

**William Peare** [02:09:11]: I'll be in the office Monday, so I won't be back at my house until evenings.

**William Peare** [02:09:16]: Let's, for the sake of testing Fathom, let's say that I kick it off 5 p.m.

**William Peare** [02:09:24]: Pacific time, and then if I can move that forward so I'm not interacting with dinner, I will.

**Daniel Kalinin** [02:09:30]: But for this last week until I'm actually working full remote, you know, I'm going to get her there, and I respect that, and I want to spend time with the kids too, but this is the last week before I go remote.

**Daniel Kalinin** [02:09:41]: So I have one more week before I, and after that, my schedule will be pretty free because I can do the estimating at midnight.

**Daniel Kalinin** [02:09:48]: I can do it at five in the morning.

**Daniel Kalinin** [02:09:49]: It doesn't really matter when I do the quotes as long as they're done.