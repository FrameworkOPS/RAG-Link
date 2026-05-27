---
title: Framework OPS W/ Daniel
date: 2026-05-18
participants: [William Peare, daniel@leadstatement.com]
source: fathom
type: meeting
url: https://fathom.video/calls/676495588
tags: [fathom, meeting]
---

# Framework OPS W/ Daniel
**Date:** May 18, 2026
**Participants:** William Peare, daniel@leadstatement.com
**Recording:** [View on Fathom](https://fathom.video/calls/676495588)

---

## Summary

## Meeting Purpose

[Review Daniel's automation roadmap and plan for cloud deployment.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=133.0)

## Key Takeaways

  - [**New MRR Stream:** A new $97/mo website service for home service pros, validated by 4 calls from a $20/lead ad test, will fund a full-time copywriter for the core B2B business.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=271.0)
  - [**Cloud Deployment:** The local lead-gen automation will move to GitHub/Railway for 24/7 reliability and remote access, solving its current dependency on a local PC.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=470.0)
  - [**AI Refinement:** The Claude-based copywriting agent needs "skills" (structured SOPs) to improve output quality and consistency, as it currently fails to reference the Obsidian knowledge base.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=178.0)
  - [**VA Onboarding:** A new VA, to be hired this week, will manage both the lead-gen outreach workflow and fulfillment for the new home service clients.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=3576.0)

## Topics

### Problem: Local Automation Bottlenecks

  - [The lead-gen automation (scrape → enrich → GammaDoc → ClickUp) is bottlenecked by two key issues:](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=178.0)
      - [**Unreliable Execution:** The workflow runs only when the local PC is on, creating a single point of failure.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=490.0)
      - [**Low-Quality AI Output:** Claude's copywriting is inconsistent and fails to reference the Obsidian knowledge base, requiring significant manual iteration.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=178.0)

### Solution: Cloud Deployment for Reliability

  - [The workflow will be moved to a cloud environment for 24/7 reliability and remote access.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=490.0)
  - [**Architecture:**](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=1164.0)
      - [**GitHub:** Cloud storage for the code base.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=1164.0)
      - [**Railway:** Hosting platform that automatically deploys from GitHub.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=1872.0)
  - [**Process:**](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=1872.0)
    1.  [Code changes are pushed to GitHub.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=1872.0)
    2.  [Railway auto-deploys the updated code.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=1872.0)
    3.  [API keys and sensitive data are stored as secure "environmental variables" in Railway, keeping them out of the public code base.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=1525.0)
  - [**Benefit:** This provides detailed build/deploy logs for efficient troubleshooting, which can be fed directly to Claude for analysis.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=1132.0)

### Solution: AI Skills for Quality Output

  - [To improve Claude's output, the agent will be trained with "skills"—structured, on-demand SOPs that provide a consistent execution path.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=184.0)
  - [**Workflow vs. Agent:**](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=2052.0)
      - [**Workflow:** A fixed sequence of steps (e.g., scrape → enrich). If a step fails, the workflow stops.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=2052.0)
      - [**Agent:** An autonomous entity that makes decisions and uses tools to achieve a goal. If a tool fails (e.g., Hunter.io), it will try others (e.g., Clay) to complete the task.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=2074.0)

### New MRR Stream: Website Service

  - [A new service will generate recurring revenue to fund the core B2B business.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=271.0)
  - [**Offer:** A "free website" build for home service pros.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=285.0)
  - [**Pricing:** $97/month for hosting and GoHighLevel (GHL) features (review automation, missed-call text-back).](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=285.0)
  - [**Execution:**](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=2600.0)
      - [**Lead Gen:** A Facebook ad test ($20/lead) generated 4 booked calls overnight.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=2600.0)
      - [**Fulfillment:** Websites are built in GHL using AI templates; a VA will manage this process.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=333.0)
      - [**Stickiness:** The service is designed to be indispensable, making clients dependent on the platform for operations.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=2897.0)
      - [**LTV:** Projected at \~$2,400 (24 months @ $97/mo), creating a high-margin business model.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=3257.0)

## Next Steps

  - [**Daniel:**](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=3559.0)
      - [Finalize the GammaDoc template to standardize formatting.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=452.0)
      - [Hire a VA this week to manage lead-gen outreach and new client fulfillment.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=3576.0)
      - [Test the new website service with the 4 booked calls.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=2859.0)
      - [Upgrade from Hunter.io to Clay for higher-quality lead enrichment.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=2120.0)
  - [**William:**](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=3349.0)
      - [Create Loom tutorials for the GitHub/Railway deployment process.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=3349.0)
      - [Build a test AI artifact (e.g., a Meta Ads dashboard) to demonstrate the concept.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=3373.0)
  - [**Both:**](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=3634.0)
      - [Meet Wednesday morning to review progress.](https://fathom.video/share/tAXJhvmJ3SsiC4LCA9cdyTuTBaHqAmhb?tab=summary&timestamp=3634.0)


---

## Action Items

_No action items._

---

## Transcript

**Daniel Kalinin** [00:00:00]: I am doing good.

**Daniel Kalinin** [00:00:00]: Let me just fix my audio.

**Daniel Kalinin** [00:00:11]: All right.

**Daniel Kalinin** [00:00:11]: I am good.

**Daniel Kalinin** [00:00:12]: All right.

**Daniel Kalinin** [00:00:13]: What's up?

**Daniel Kalinin** [00:00:14]: Okay.

**Daniel Kalinin** [00:00:16]: Let's ride.

**Daniel Kalinin** [00:00:17]: Yeah.

**William Peare** [00:00:19]: You okay?

**William Peare** [00:00:19]: You tired?

**William Peare** [00:00:20]: You've been working 40 hours a day?

**William Peare** [00:00:22]: No.

**Daniel Kalinin** [00:00:22]: Well, I actually got a, I don't know.

**Daniel Kalinin** [00:00:25]: I got some sort of disease or whatever.

**Daniel Kalinin** [00:00:27]: So I've been feeling pretty  lately.

**Daniel Kalinin** [00:00:31]: But I think it's like last night.

**William Peare** [00:00:34]: actually have like a disease.

**William Peare** [00:00:36]: No, I got a disease or a cold.

**Daniel Kalinin** [00:00:38]: Yeah.

**Daniel Kalinin** [00:00:39]: was like, oh, okay.

**Daniel Kalinin** [00:00:40]: Well, there's two different things.

**Daniel Kalinin** [00:00:42]: If you have AIDS, no big deal, bud.

**Daniel Kalinin** [00:00:44]: It's okay.

**Daniel Kalinin** [00:00:47]: Great.

**Daniel Kalinin** [00:00:47]: Great.

**William Peare** [00:00:48]: Yeah.

**William Peare** [00:00:48]: Probably because you're working yourself to death, Daniel.

**William Peare** [00:00:51]: No.

**Daniel Kalinin** [00:00:51]: My fiance caught something that transferred over to me.

**Daniel Kalinin** [00:00:56]: But I think today is the last day.

**Daniel Kalinin** [00:00:57]: But I've been dead for the past few days.

**Daniel Kalinin** [00:00:59]: Nice.

**William Peare** [00:01:00]: Nice.

**William Peare** [00:01:01]: Yeah.

**Daniel Kalinin** [00:01:02]: All right.

**Daniel Kalinin** [00:01:02]: Where shall we begin?

**William Peare** [00:01:05]: Did you get the PDF?

**Daniel Kalinin** [00:01:09]: Was it like three separate roadmaps or something?

**Daniel Kalinin** [00:01:12]: Yes.

**Daniel Kalinin** [00:01:13]: I thought I answered that.

**Daniel Kalinin** [00:01:14]: I think it was number two that I wanted to go with.

**William Peare** [00:01:19]: You probably did answer because you're a professional.

**William Peare** [00:01:22]: Let's look here.

**William Peare** [00:01:23]: Mr.

**William Peare** [00:01:24]: Framework Ops.

**William Peare** [00:01:25]: Boom, boom, boom.

**William Peare** [00:01:26]: Google Calendar.

**William Peare** [00:01:29]: Gmail.

**William Peare** [00:01:29]: Gmail.

**William Peare** [00:01:31]: Okay.

**William Peare** [00:01:33]: Boom, boom, boom, boom, boom, boom.

**William Peare** [00:01:38]: Okay.

**William Peare** [00:01:38]: Let's find you.

**William Peare** [00:01:41]: You are Daniel.

**William Peare** [00:01:45]: Daniel.

**William Peare** [00:01:50]: Okay.

**William Peare** [00:01:51]: Bam, bam, bam.

**William Peare** [00:01:52]: Wow.

**William Peare** [00:01:53]: That could zoom in a little bit.

**William Peare** [00:01:55]: Okay.

**William Peare** [00:01:55]: built it.

**William Peare** [00:01:56]: Yeah.

**William Peare** [00:01:56]: Yeah.

**William Peare** [00:01:56]: Good.

**William Peare** [00:01:57]: Good.

**William Peare** [00:01:58]: Okay.

**William Peare** [00:01:59]: Hot deployment.

**William Peare** [00:02:00]: Mm-hmm.

**William Peare** [00:02:00]: Mm-hmm.-hmm.

**William Peare** [00:02:02]: Yep.

**William Peare** [00:02:03]: Yep.

**William Peare** [00:02:06]: Dun, dun, dun, dun, dun.

**William Peare** [00:02:08]: Bam, bam, bam.

**William Peare** [00:02:10]: Okay.

**William Peare** [00:02:10]: I like that.

**William Peare** [00:02:13]: So first things first, the step to all of them kind of is that I get, is that I do a, let's go through the actual roadmap of exactly what you built so I understand how it's all tied together.

**William Peare** [00:02:35]: That way we can do the flop.

**William Peare** [00:02:36]: I'm going to refresh my coffee too.

**William Peare** [00:02:38]: I'll be able to hear you though.

**William Peare** [00:02:39]: Feel free to talk.

**William Peare** [00:02:40]: Yeah.

**William Peare** [00:02:40]: I'm just going to take my notes.

**William Peare** [00:02:43]: air call, on, or my AirPods.

**William Peare** [00:02:45]: A couple clicks here.

**William Peare** [00:02:49]: Fly like an eagle, Daniel.

**William Peare** [00:02:51]: Yeah.

**Daniel Kalinin** [00:02:53]: just been building out more of the ad format stuff.

**Daniel Kalinin** [00:02:56]: Uh, that's pretty much done at this point.

**Daniel Kalinin** [00:02:58]: What I noticed.

**Daniel Kalinin** [00:03:00]: First was Claude.

**Daniel Kalinin** [00:03:04]: I have everything in Obsidian, but Claude doesn't necessarily reference all the wiki links and tags that I set.

**Daniel Kalinin** [00:03:10]: So I was looking into that and it looks like I need to build out skills, which I'm not too familiar with, but I guess just like on-demand SOPs, that way it looks at everything it needs to.

**Daniel Kalinin** [00:03:21]: Because the copywriting is not necessarily there.

**Daniel Kalinin** [00:03:24]: There's a lot of iterations that I need to make, and that's still kind of like a time suck, I guess.

**Daniel Kalinin** [00:03:28]: So, yeah, I need to, I need to build skills around that, I believe.

**Daniel Kalinin** [00:03:38]: What else did I do?

**Daniel Kalinin** [00:03:43]: Did some more ClickUp stuff.

**Daniel Kalinin** [00:03:44]: mean, I think that, that stuff's pretty much done.

**Daniel Kalinin** [00:03:47]: Today, I kind of want to just focus on the GammaDoc and just finish that up.

**Daniel Kalinin** [00:03:51]: That way I can start outreaching.

**Daniel Kalinin** [00:03:58]: Yeah, and I was thinking about like what else.

**Daniel Kalinin** [00:04:00]: So I can pass off to my VA and I guess kind of like coincidence.

**Daniel Kalinin** [00:04:03]: So I told you that my fiance's brother, he was like trying to start his own thing, blah, blah.

**Daniel Kalinin** [00:04:09]: And I'm like, okay, cool.

**Daniel Kalinin** [00:04:10]: Just like sell websites.

**Daniel Kalinin** [00:04:11]: That's such an easy service to do, stack recurring revenue, blah, blah, blah.

**Daniel Kalinin** [00:04:16]: And that got me thinking like, you know, one way that I can expand on my B2B offer would be just selling websites to like new B2B businesses and then nurturing them, moving down the line.

**Daniel Kalinin** [00:04:31]: My biggest issue right now is that like, I am time sucked in this copywriting thing.

**Daniel Kalinin** [00:04:36]: And if I want to get a decent copywriter, that's going to cost me, I mean, at minimum, like five grand to 10 grand a month.

**Daniel Kalinin** [00:04:43]: So I need more recurring revenue.

**Daniel Kalinin** [00:04:45]: What I can probably do is just push ads for like, hey, we'll build you a free website.

**Daniel Kalinin** [00:04:52]: And then sell them on like a $97 a month hosting fee plus like review automation, miscalled text back.

**Daniel Kalinin** [00:04:58]: So I just played around.

**Daniel Kalinin** [00:05:00]: I found it for  and giggles.

**Daniel Kalinin** [00:05:01]: Last night, I just put up some ads.

**Daniel Kalinin** [00:05:03]: It was for home service, just to test that out.

**Daniel Kalinin** [00:05:06]: And I have four book calls today.

**Daniel Kalinin** [00:05:07]: No .

**Daniel Kalinin** [00:05:08]: So, yeah, that should be a good way to expand my MRR.

**Daniel Kalinin** [00:05:13]: Like, if I can get a couple hundred clients at $97 a month, I mean, that's effectively like 20K in MRR, which is super simple to do.

**Daniel Kalinin** [00:05:23]: I can probably troop that out in the next few.

**Daniel Kalinin** [00:05:25]: That's a big- bug.

**Daniel Kalinin** [00:05:27]: I'm closing my window.

**Daniel Kalinin** [00:05:32]: Which I can probably do pretty fast.

**Daniel Kalinin** [00:05:33]: And I was just thinking, like, okay, if I'm getting a VA, I don't want that VA working for, like, two, three hours a day or, like, whatever.

**Daniel Kalinin** [00:05:40]: So, on top of just helping me with outreach, I can basically just have a VA plug in a GoHighLevel and just build those websites out.

**Daniel Kalinin** [00:05:47]: It should be super simple because GoHighLevel can, like, auto-do it with, like, AI now.

**Daniel Kalinin** [00:05:53]: Yeah, so that's kind of where I'm at right now.

**Daniel Kalinin** [00:05:56]: Next steps that I need to do is get my outreach.

**Daniel Kalinin** [00:06:00]: Figure this claw  out that way it actually kind of like works and yeah.

**William Peare** [00:06:06]: Yeah okay now number two building the machine so you have the outreach portion of it like I'm gonna go over how I understood it last time you let me know if I'm incorrect and if any parts of this are broken so we scrape it's scraping it's then enriching it's then automatically creating the gamma doc.

**Daniel Kalinin** [00:06:31]: Yeah um at that point it's putting it into ClickUp for you to review before shipping it um yeah it puts it into ClickUp the VA reviews it um once they review and approve um I create looms personalized outreach um that gets shared over to them if there's no reply within like a few days or something like that then it'll be a outbound code email sequence.

**Daniel Kalinin** [00:07:00]: Okay.

**William Peare** [00:07:02]: What kicks off the cold email sequence?

**William Peare** [00:07:05]: Do you mark it as like replied or not replied?

**Daniel Kalinin** [00:07:08]: I guess so.

**Daniel Kalinin** [00:07:09]: I think, I don't know if it's going to have to be manual or it can be automated, but like I can just set a countdown timer inside of the click-up task.

**Daniel Kalinin** [00:07:17]: And once that timer goes to zero, I can just get pushed to like smart leader instantly.

**William Peare** [00:07:22]: Okay.

**William Peare** [00:07:25]: Okay.

**William Peare** [00:07:26]: Good.

**William Peare** [00:07:27]: And then you've tested that.

**William Peare** [00:07:31]: That's working consistently.

**Daniel Kalinin** [00:07:32]: Yeah.

**Daniel Kalinin** [00:07:33]: I need it.

**Daniel Kalinin** [00:07:34]: I just need to templatize the GammaDoc.

**Daniel Kalinin** [00:07:37]: That way it just has an easy reference all the time.

**Daniel Kalinin** [00:07:39]: Because sometimes when it's API generated, like it butchers some things like the formatting or whatever.

**Daniel Kalinin** [00:07:45]: So I just need that to be linear.

**William Peare** [00:07:49]: Okay.

**William Peare** [00:07:50]: And then where is this living?

**William Peare** [00:07:54]: Is this all running local on your desktop?

**William Peare** [00:07:57]: Yeah.

**William Peare** [00:07:57]: I still didn't understand that like GitHub stuff.

**Daniel Kalinin** [00:08:00]: If have an account, yeah, I guess I said I don't understand why I need it and all that stuff.

**Daniel Kalinin** [00:08:08]: Yeah, totally.

**William Peare** [00:08:10]: GitHub is not necessarily, so, I mean, my biggest thing, that's why picking Path 2 is good, if we don't have some type of cloud deployment, I mean, I guess potentially if you leave your desktop on all the time and it's just constantly running, it's not really an issue.

**William Peare** [00:08:25]: It's actually better in terms of security, but these workflows will only run if your desktop is on.

**William Peare** [00:08:33]: like, if your desktop is not running, these automations will not run because it needs to call the code that's local on your desktop.

**William Peare** [00:08:41]: So even if it goes through this app or whatever it's going through, unless it can actually get to those source files on your computer, it'll bounce.

**Daniel Kalinin** [00:08:49]: Okay.

**William Peare** [00:08:50]: So that's kind of on the bulletproofing part of it.

**William Peare** [00:08:52]: Like, if you want something that'll run 24-7 no matter what, we need to have some place that's living and hosted.

**William Peare** [00:08:59]: living, that that that that you can you you Thank you.

**William Peare** [00:09:00]: Yeah, and I guess that's part of it.

**Daniel Kalinin** [00:09:01]: Like, how do I just get  to run 24-7 and, like, actually produce good quality stuff?

**Daniel Kalinin** [00:09:06]: Like, that's where skills came in.

**Daniel Kalinin** [00:09:08]: Yeah.

**Daniel Kalinin** [00:09:08]: Because, again, I guess, like, I thought Cloud would be, like, a super genius, but it's just as retarded as, like, Cloud Chat or something like that, like, where you have to sell it everything.

**Daniel Kalinin** [00:09:17]: I'd like it to just be, like, be a copywriter and do XYZ.

**William Peare** [00:09:21]: Yeah, and so that's where you're getting not necessarily, like, the workflow versus agent.

**William Peare** [00:09:27]: Everyone is, like, using the word agent, which is relevant.

**William Peare** [00:09:30]: But, I mean, a lot of these are just workflows.

**William Peare** [00:09:35]: There's some semi-agentic in the way that, like, based on the enrichment or scraping data it gets, it might do it slightly differently.

**William Peare** [00:09:41]: But it's doing the same consistent output you've trained it to do consistently.

**William Peare** [00:09:46]: Yeah, so you're really programming different skills and they're teaching it different skills and then telling it automatically through the API to run these skills.

**William Peare** [00:09:56]: So you can make it completely automated, but you do have to build out.

**William Peare** [00:10:00]: Build out the skill as to what it's doing, which isn't very hard to do, but you will need that because if not, it's always going to bottleneck on that.

**William Peare** [00:10:10]: You're really just telling, you know, the, well, just Claude.

**William Peare** [00:10:16]: The API is going to give it its, like, prompts, so to speak, automatically, but unless it has, like, a structured sequence to go through or unless it's been trained as, like, a fully autonomous agent and has a list of tools it can call, it doesn't really know what it's supposed to be doing.

**William Peare** [00:10:32]: Like, it can go search Obsidian for the context, but unless it knows, like, its path of what it's supposed to be doing each time.

**William Peare** [00:10:38]: And then what I would recommend is almost, like, you were talking about from Cameron, like, you should have your own personal Slack channel to you, like, where it hits this step and then it's almost like a go, no go.

**William Peare** [00:10:50]: It's like, oh, cool, proceed, and you'll just, you know, click proceed, and then it knows to automatically go to the next step.

**William Peare** [00:10:56]: So it's got some kind of trigger that you can handle anywhere.

**William Peare** [00:11:00]: Yeah.

**William Peare** [00:11:01]: Yeah.

**Daniel Kalinin** [00:11:02]: Yeah.

**Daniel Kalinin** [00:11:02]: just need to automate as much of it as possible, honestly.

**William Peare** [00:11:06]: Yeah, absolutely.

**William Peare** [00:11:07]: Okay.

**William Peare** [00:11:08]: The skills building out, that's, yeah, that's a good thing.

**William Peare** [00:11:12]: We have the onboarding and SOP pretty well done.

**William Peare** [00:11:16]: The thing is, we're just going to need to make sure this machine is bulletproof and consistent, that you can run through it 10, 15, 20 times, and it's super clear to you.

**William Peare** [00:11:24]: That way, when you're bringing someone onto it, it's easy for you to train them on it.

**William Peare** [00:11:28]: Because if you're not comfortable with it yet, and we're trying to bring someone on to run that system, the chance of it getting  up is...

**William Peare** [00:11:34]: Yeah, pretty high.

**Daniel Kalinin** [00:11:36]: Pretty high, yeah.

**William Peare** [00:11:37]: I mean, it makes sense to you, because you built the whole thing through dozens of hours if you're sleepless nights, but it may not be as clear to them.

**William Peare** [00:11:43]: They're going to be like, where the hell do these GammaDocs come from, and how is it getting this information?

**William Peare** [00:11:47]: Where do I look if something's not right?

**William Peare** [00:11:49]: They'll have no idea what's going on.

**Daniel Kalinin** [00:11:51]: Okay.

**William Peare** [00:11:58]: Like, 20 plus.

**William Peare** [00:11:59]: Like,

**Daniel Kalinin** [00:12:00]: The concept is, I can iterate on it for sure, but it's just like, even some things like, wherever the book a call button is, it's formatted weirdly or inside of a card when I'd want it to be a separate card, or maybe it says some inaccurate stuff, so on and so forth.

**Daniel Kalinin** [00:12:19]: So, I kind of just want to make it so that, like, basically just one specific GammaDoc with, like, custom values being, like, their review count, their name, so on and so forth.

**Daniel Kalinin** [00:12:31]: That's pretty much it.

**Daniel Kalinin** [00:12:33]: Sure.

**William Peare** [00:12:35]: Okay.

**William Peare** [00:12:35]: Seems pretty easy-peasy.

**William Peare** [00:12:38]: Do you want to run through the cloud deployment now?

**William Peare** [00:12:41]: Cloud deployment would be GitHub.

**William Peare** [00:12:44]: GitHub, Railway, whatever you want to pick, however you want to roll that.

**William Peare** [00:12:49]: Those are two easy starting points.

**William Peare** [00:12:51]: But that's somewhere it could live.

**William Peare** [00:12:54]: Do you want to kick that off now?

**Daniel Kalinin** [00:12:56]: you want more of...

**Daniel Kalinin** [00:12:57]: Yeah, let's kick that off now.

**Daniel Kalinin** [00:12:58]: Okay.

**Daniel Kalinin** [00:12:59]: Okay.

**Daniel Kalinin** [00:13:00]: I probably have to one because I need to fulfill for these four calls.

**Daniel Kalinin** [00:13:07]: I need to create them, websites and stuff.

**Daniel Kalinin** [00:13:11]: You're all good.

**William Peare** [00:13:11]: You just let me know what your next availability is.

**William Peare** [00:13:14]: We'll book from there.

**William Peare** [00:13:14]: This is my first week fully remote.

**William Peare** [00:13:17]: I did that one tiny podcast, and then the guy was like, oh, you should try and apply for this other podcast.

**William Peare** [00:13:22]: And like I did, and they were like, oh, cool.

**William Peare** [00:13:24]: We'd love to have you on there.

**William Peare** [00:13:25]: I looked him up.

**William Peare** [00:13:26]: I was like, , this is actually like a big podcast.

**William Peare** [00:13:29]: like a real  podcast.

**William Peare** [00:13:31]: So now I have a meeting with those people at noon for like roofing success network.

**William Peare** [00:13:35]: It's cool.

**Daniel Kalinin** [00:13:36]: Yeah.

**Daniel Kalinin** [00:13:36]: Cool.

**Daniel Kalinin** [00:13:37]: Apparently a bigger one.

**William Peare** [00:13:38]: So I'm pretty excited about that.

**William Peare** [00:13:39]: Hopefully that gives me maybe some inbound leads than calling me.

**Daniel Kalinin** [00:13:43]: Yeah, well.

**Daniel Kalinin** [00:13:44]: Yeah.

**William Peare** [00:13:45]: So that was my plan.

**William Peare** [00:13:47]: Okay.

**William Peare** [00:13:48]: What is this the only workflow you have built out right now?

**Daniel Kalinin** [00:13:53]: The GammaDot creation.

**Daniel Kalinin** [00:13:56]: Yes.

**Daniel Kalinin** [00:13:58]: There's also the like lead.

**Daniel Kalinin** [00:14:00]: Beatscraper?

**Daniel Kalinin** [00:14:01]: Yep.

**Daniel Kalinin** [00:14:01]: I guess that's part of it, yeah.

**Daniel Kalinin** [00:14:03]: So yeah, it'd be the only workflow.

**Daniel Kalinin** [00:14:05]: Okay.

**William Peare** [00:14:07]: Let me close this out right away.

**William Peare** [00:14:18]: Okay.

**William Peare** [00:14:23]: Have you linked your Claude to GitHub through MCP or anything like that?

**William Peare** [00:14:29]: Do you have any of that set up?

**Daniel Kalinin** [00:14:30]: I don't think so.

**Daniel Kalinin** [00:14:31]: I think I just set up an account.

**Daniel Kalinin** [00:14:33]: Okay.

**William Peare** [00:14:33]: Okay.

**William Peare** [00:14:36]: When you're running Claude, are you running it local or are you running it cloud?

**William Peare** [00:14:43]: Local.

**Daniel Kalinin** [00:14:44]: Like it's on my PC download as an app.

**Daniel Kalinin** [00:14:48]: Oh yeah, definitely.

**William Peare** [00:14:49]: But within that, at the bottom of the little bar when you're like starting a prompt, you'll kind of like get to pick the work tree and if it's local or if it's cloud, you know.

**William Peare** [00:14:59]: Okay.

**William Peare** [00:14:59]: Okay.

**William Peare** [00:14:59]: Thank Thank you.

**William Peare** [00:14:59]: Thank you.

**William Peare** [00:14:59]: you.

**William Peare** [00:15:00]: Let me check right now.

**Daniel Kalinin** [00:15:04]: I want to say everything's local.

**Daniel Kalinin** [00:15:07]: Okay.

**William Peare** [00:15:11]: Pull up my cloud.

**William Peare** [00:15:12]: Ask it to just make me a simple one so we can test this.

**William Peare** [00:15:16]: Okay.

**William Peare** [00:15:22]: Okay, so right here, local, cloud.

**William Peare** [00:15:24]: We'll go to framework.

**William Peare** [00:15:27]: We're on local.

**William Peare** [00:15:28]: Good.

**William Peare** [00:15:29]: Daniel, click up replicator.

**William Peare** [00:15:57]: Yeah, I'll see if it can give me some...

**William Peare** [00:16:00]: Random variables, so I can show you entering that and testing it.

**William Peare** [00:16:14]: Yeah, you're going to need to set up, and you could ask that on your end.

**William Peare** [00:16:18]: You could go into chat now and ask it to set up the MCP, the remote access to Git and Railway, and it'll start getting that for you.

**William Peare** [00:16:26]: You'll need that.

**William Peare** [00:16:27]: If not, you have to manually, it's a pain mask.

**Daniel Kalinin** [00:16:32]: It's like, gosh, my nose itches so much.

**Daniel Kalinin** [00:17:00]: I want to cry all the time.

**Daniel Kalinin** [00:17:03]: It's just because you're sad.

**Daniel Kalinin** [00:17:05]: Probably.

**William Peare** [00:17:11]: Okay.

**William Peare** [00:17:13]: So I have it pushing.

**William Peare** [00:17:16]: Let me see if I can pull up this deploy if it's happening in a lot of time.

**William Peare** [00:17:21]: Okay.

**William Peare** [00:17:22]: So from GitHub, show more.

**William Peare** [00:17:25]: I have this Daniel ClickUp replicator, one I made just for this.

**William Peare** [00:17:31]: One commit.

**William Peare** [00:17:32]: Good.

**William Peare** [00:17:32]: Four days ago.

**William Peare** [00:17:33]: So I don't have a fresh commit coming in here yet.

**William Peare** [00:17:41]: Deployed.

**William Peare** [00:17:47]: Can you see my screen?

**William Peare** [00:17:48]: Yeah.

**Daniel Kalinin** [00:17:52]: Okay.

**William Peare** [00:17:53]: So in my, you know, I'm in my GitHub.

**William Peare** [00:17:57]: I can see all my projects.

**William Peare** [00:18:00]: This isn't even all of them.

**William Peare** [00:18:01]: So repositories up here.

**William Peare** [00:18:03]: Click on them.

**William Peare** [00:18:05]: Messing around with this one.

**William Peare** [00:18:06]: can see it hasn't been updated for four days.

**Daniel Kalinin** [00:18:09]: That's fine.

**William Peare** [00:18:10]: I haven't really changed anything here.

**William Peare** [00:18:13]: So I can see all the files that it's put in here.

**William Peare** [00:18:19]: That way we have them all.

**William Peare** [00:18:21]: These are all coming from your local, but it pushes them here to live here.

**William Peare** [00:18:24]: I can see if it has attached.

**William Peare** [00:18:28]: Doesn't look like it hasn't attached railway yet.

**William Peare** [00:18:31]: We'll go over to railway.

**William Peare** [00:18:33]: Is that connected to my local?

**Daniel Kalinin** [00:18:35]: No.

**Daniel Kalinin** [00:18:36]: I was about to say, how the hell did you get that?

**Daniel Kalinin** [00:18:38]: It's amazing.

**Daniel Kalinin** [00:18:39]: You're welcome.

**William Peare** [00:18:41]: I'm assuming it's this one, innovative ambition.

**William Peare** [00:18:44]: They'll pick random names.

**William Peare** [00:18:45]: It crashed.

**William Peare** [00:18:47]: So there's a few things we can look at here.

**William Peare** [00:18:50]: We can click on this.

**William Peare** [00:18:52]: This is pretty much where you're going to do your troubleshooting.

**William Peare** [00:18:54]: So you have the build logs.

**William Peare** [00:18:56]: You know, you could just copy those down as plain text, throw it into Claude.

**William Peare** [00:19:00]: Like, what the , Claude?

**Daniel Kalinin** [00:19:02]: Okay, so I guess this is Railway.

**Daniel Kalinin** [00:19:05]: So Railway is connected to GitHub, and you're using Railway to troubleshoot any problems that I have with the scripts or something like that?

**William Peare** [00:19:15]: No, this will more...

**William Peare** [00:19:17]: That you're going to have to iterate on yourself.

**William Peare** [00:19:20]: Then you'll tell Claude to make the changes.

**William Peare** [00:19:22]: It'll push...

**William Peare** [00:19:24]: Assume GitHub is just like a cloud storage of your local coding files, the scaffolding for the code.

**William Peare** [00:19:33]: So it's going to go to GitHub where it's safely hosted online for it to be accessed by these webhooks at any time, instead of if your computer's off.

**William Peare** [00:19:42]: Then Railway is going to be like the backend setup.

**William Peare** [00:19:44]: So that's where you're going to put in like your API keys, things of that nature, so they can live safely online.

**William Peare** [00:19:49]: And then it'll also produce the URL, so you actually have a place to access this.

**William Peare** [00:19:54]: You know, you can put that in the GoHigh level, you can share it with clients, however you need to do that.

**William Peare** [00:19:59]: Okay.

**William Peare** [00:20:00]: But the build log is going to show when it went through a build, the steps of it, what happened.

**William Peare** [00:20:08]: Oh, it looks like it all is good here.

**William Peare** [00:20:10]: This all happened nicely, except for that one red line.

**William Peare** [00:20:14]: And then we look at the deploy logs, and I can see like, hey, wow, there's all these issues, a bunch of red stuff, and it crashed.

**William Peare** [00:20:21]: So I could just take this, download it as plain text, go back to Claude.

**William Peare** [00:20:27]: And I can tell you already, this is because we don't have the variables put in.

**William Peare** [00:20:30]: But like, if you're messing with it, and you don't know what's going on, I can go here, paste it, what happened.

**William Peare** [00:20:42]: And then it'll kick me back some smart  answers about how I have to put in the variables.

**William Peare** [00:20:46]: And we'll go through putting in, putting in the variables.

**Daniel Kalinin** [00:20:49]: So this is just a cleaner way to build out programs and scripts, right?

**William Peare** [00:20:54]: Yeah, this will just make sure it can, it's bulletproofing it so it can run continuously.

**William Peare** [00:20:59]: It's not living on your computer.

**William Peare** [00:21:00]: I mean, you'll have your computer, but it'll also have a place that it can run online.

**Daniel Kalinin** [00:21:05]: Okay, and that's going to help if I need to use it on, like, my MacBook or something or, like, whatever, right?

**Daniel Kalinin** [00:21:09]: I can just download it off Railway and GitHub and just import it or something?

**Daniel Kalinin** [00:21:13]: Correct.

**Daniel Kalinin** [00:21:14]: The scripts themselves?

**William Peare** [00:21:15]: Mm-hmm.

**Daniel Kalinin** [00:21:16]: They'll live.

**William Peare** [00:21:17]: This will have nothing to do with where they actually live.

**William Peare** [00:21:20]: This is more bulletproofing the actual process itself so that it's not dependent on your computer.

**William Peare** [00:21:25]: Like, if you had a power outage or your computer got turned off or that computer, like, and died, this program will still run continuously.

**William Peare** [00:21:32]: You can also edit it from anywhere.

**William Peare** [00:21:34]: So if you were somewhere else on a different computer and you're like, whoa, whoa, whoa, something is way wrong with this script, you could hop in, download the files off Git, edit them in code, push it back to Git, it'll automatically push it to Railway and update your whole system.

**William Peare** [00:21:49]: Whereas if it lives on your computer, it's pretty siloed.

**William Peare** [00:21:52]: It can only work on your computer.

**William Peare** [00:21:53]: So, like, if you are not at that computer or the computer is not up and running, you won't be able to run.

**William Peare** [00:22:00]: This program.

**William Peare** [00:22:04]: So it's saying it's crashing because the startup failed.

**William Peare** [00:22:07]: It needs the environmental variables.

**William Peare** [00:22:09]: Shocking.

**William Peare** [00:22:10]: Missing required is ClickUp API token.

**William Peare** [00:22:13]: So I'll just use mine for this.

**William Peare** [00:22:16]: But we're out of here now.

**William Peare** [00:22:19]: We're just on this main thing.

**William Peare** [00:22:20]: We have this variable screen.

**William Peare** [00:22:23]: There's no variable set.

**William Peare** [00:22:25]: So then let's see if I can actually make this medium-sized.

**William Peare** [00:22:30]: Okay.

**William Peare** [00:22:31]: We'll make this slightly larger, medium-sized.

**William Peare** [00:22:35]: We need, you know, the API token, the space ID, the template file you're choosing to use, the webhook secret, which you can just make something up unless it specifies.

**William Peare** [00:22:44]: And then the form vendor is type form.

**William Peare** [00:22:47]: So for you, you'll need to get your ClickUp API token.

**William Peare** [00:22:50]: Have you even made a ClickUp API token?

**William Peare** [00:22:52]: Yeah, yeah, yeah.

**Daniel Kalinin** [00:22:53]: Okay.

**William Peare** [00:22:54]: So if we went through, not this one, this is for SkyWrite.

**William Peare** [00:23:01]: Over here.

**William Peare** [00:23:05]: Oh, no.

**William Peare** [00:23:06]: Well, I'm not going to use mine because then I'd have to reset.

**William Peare** [00:23:09]: You can't copy it more than once, which is super annoying.

**William Peare** [00:23:12]: Yeah, I think you've got to regenerate it or something.

**Daniel Kalinin** [00:23:14]: Yeah, super annoying.

**William Peare** [00:23:15]: It messes with my whole flow.

**William Peare** [00:23:19]: Yeah.

**William Peare** [00:23:20]: Okay, we'll just put some random in there so you can see how it's done.

**William Peare** [00:23:23]: Okay, so the syntax is important, so I mean, we'll need to, you know, it's all caps, and then, you know, paste your token here.

**Daniel Kalinin** [00:23:44]: Claude was telling me, by the way, to delete a screenshot that had, like, my API key in the Claude chat.

**Daniel Kalinin** [00:23:51]: Is that that bad, or is it just kind of?

**William Peare** [00:23:54]: Depends on what it's for, you know, if it's, like, for, yeah, it's not great.

**William Peare** [00:24:00]: know, it could be used nefariously, but it's a matter of preference and how much you're going to be doing.

**William Peare** [00:24:07]: Obviously, if it's like a QuickBooks token or like maybe to your go high level where there's customer data, like for the  web scraper, like who gives a ?

**William Peare** [00:24:14]: You know, like when they're going to scrape the web and look at your leads, like it's just not super critical.

**William Peare** [00:24:20]: Some of the things, yeah, you should be pretty, pretty mindful of, and this is where you handle that.

**William Peare** [00:24:26]: So it'll just build you out of blank scaffolding and then you'll come in here and, know, the space ID, Daniel Space, go through and build these all out, secret.

**William Peare** [00:24:54]: So it'll give you this little like form of what you need.

**William Peare** [00:25:09]: Uh, you are using Typeform?

**William Peare** [00:25:12]: Uh, yeah.

**Daniel Kalinin** [00:25:25]: And this just saves it to the entire kind of project, right?

**William Peare** [00:25:29]: Um, no.

**William Peare** [00:25:30]: What this will do, so, you're coding that you do on your computer.

**William Peare** [00:25:36]: Obviously, on your computer, it's safe to just put all those things, so it doesn't really matter.

**William Peare** [00:25:39]: But when you're sending it out to Git, it's going to have, you know, all the code.

**William Peare** [00:25:44]: And in the code, it's going to say, you know, at this point, reference ClickUp API token.

**William Peare** [00:25:50]: And it's not going to say what it is, it's just going to say reference it.

**William Peare** [00:25:53]: So, this, setting the variables, is telling the code when it's running, you know, when you're referencing ClickUp API token.

**William Peare** [00:26:00]: Token, the value of that, the hidden value equals this so that your code doesn't have to have sensitive data and it can run through the whole code and then this is where it's going to store like the answer to the question like it's going to be asking a question what is ClickUp token and then if you need to update your whole token, you don't have to do anything with your code, you can literally just go in here and update the value of that token when you regenerate it and it will know what it's referring to.

**William Peare** [00:26:22]: Okay, we've added all these and once you've done some updates, you'll see up there, it says you applied six changes, deploy, we can deploy, it's probably still going to crash because it's got no real APIs, but let's see, then it'll go, you know, it's initializing, it'll go through its process, you will wait patiently while it does its building.

**William Peare** [00:27:00]: What if it's calling?

**William Peare** [00:27:01]: done.

**William Peare** [00:27:03]: Hello?

**William Peare** [00:28:27]: Okay, now I can see, hey, Troy, my wife is on the way over, so be froggy and ready to unload a pressure.

**William Peare** [00:28:37]: Did you just leave?

**William Peare** [00:28:46]: Okay, copy that.

**William Peare** [00:28:47]: I will call Jorn.

**William Peare** [00:28:51]: Sorry, Daniel.

**William Peare** [00:28:53]: It's always something.

**William Peare** [00:28:58]: That's awesome.

**William Peare** [00:29:00]: Okay.

**William Peare** [00:29:00]: So we can see now it's got the green checkmark.

**William Peare** [00:29:02]: It's active.

**William Peare** [00:29:02]: It passed all its checks.

**William Peare** [00:29:04]: It does not necessarily mean whatever you're building is working how you want it.

**William Peare** [00:29:07]: It just means that it didn't run into any issues that stop it from deploying.

**William Peare** [00:29:13]: Okay.

**William Peare** [00:29:14]: So now I can click on this.

**William Peare** [00:29:16]: Same thing.

**William Peare** [00:29:16]: I'm going to have my logs of how it went through its building, which is pretty much gibberish to me or you, but that's okay.

**William Peare** [00:29:23]: Code knows what it's looking at.

**William Peare** [00:29:25]: I'm sure a real coder would look at this and be like, you know, of course, I understand exactly what this is saying.

**William Peare** [00:29:29]: Yeah.

**William Peare** [00:29:32]: I don't, but that's okay.

**William Peare** [00:29:35]: Then I look at the deploy logs.

**William Peare** [00:29:37]: It went through, it started its container, which is like a little cloud storage thing that it lives in.

**William Peare** [00:29:41]: Great.

**William Peare** [00:29:44]: I click on this.

**William Peare** [00:29:47]: This, this, this.

**William Peare** [00:29:48]: This does not have a URL yet.

**William Peare** [00:29:52]: So let's close that out.

**William Peare** [00:29:55]: So variables, settings, public network.

**William Peare** [00:30:00]: Networking, private networking.

**William Peare** [00:30:01]: generate a domain.

**William Peare** [00:30:04]: We can just, if there's specified ports you'll need, code will tell you, but we're going to generate this domain.

**William Peare** [00:30:11]: And then we'll have a little URL we can click on.

**William Peare** [00:30:13]: There's probably nothing on here.

**William Peare** [00:30:15]: It's just saying the status of it.

**William Peare** [00:30:16]: But like I could go back here and say, add a nice UI to the code so we can show him as a happy face.

**William Peare** [00:30:35]: And then it should push that to GitHub and then push it here and we'll be able to watch it go through its rebuild cycle.

**William Peare** [00:30:42]: Now this is a pretty simple one, but the concept is exactly the same.

**William Peare** [00:30:48]: The key thing is the variables, making sure they match up all your API tokens, having the naming right.

**William Peare** [00:30:54]: And then it's feeding off your code, essentially.

**William Peare** [00:31:00]: If you went through here and you updated these with your real stuff, with that repo I gave you, and then walk it through it, it's going to do what you're hoping it'll do.

**Daniel Kalinin** [00:31:12]: So whatever code gets pushed inside of Claude, it'll get pushed to Railway.

**William Peare** [00:31:16]: Yes, it'll push it to GitHub, and then GitHub automatically deploys to Railway with any updates.

**William Peare** [00:31:22]: So it'll auto-opt itself whenever you adjust the code.

**Daniel Kalinin** [00:31:25]: And I know I'm being repetitive here, I'm just trying to ingrain it in my head.

**Daniel Kalinin** [00:31:28]: So, okay, it's pushing it as a Railway.

**Daniel Kalinin** [00:31:30]: Cool.

**Daniel Kalinin** [00:31:31]: Like, what do I do inside of Railway?

**Daniel Kalinin** [00:31:34]: Why do I care about it inside of Railway?

**Daniel Kalinin** [00:31:35]: Is it just a more convenient place to look at everything, or?

**William Peare** [00:31:37]: No, it has nothing to do with convenience or looking at anything.

**William Peare** [00:31:40]: It's less convenient, I would say.

**William Peare** [00:31:43]: What you're doing in here is it's purely just for assigning the variables for your code and giving it a backend URL.

**William Peare** [00:31:51]: So, like, if the webhooks need a URL to grab something, it can go there, grab the code with the API hooks and the live data instead of trying to jump to your machine and grab

**William Peare** [00:32:00]: Grab it.

**William Peare** [00:32:00]: If your machine is always on and there's never any rescue machine going off, technically this is unnecessary, but you don't want to build, you want to build this, especially if it's one of your main things.

**William Peare** [00:32:11]: You can see I did that push.

**William Peare** [00:32:12]: Now it's deploying again.

**William Peare** [00:32:14]: Now it's online.

**William Peare** [00:32:16]: So in theory, if that worked, I would check this and it's now going to have, see, it's now wham, bam.

**William Peare** [00:32:25]: Um, yeah, this is really just bulletproofing your system.

**William Peare** [00:32:31]: So that way it has somewhere else to run.

**William Peare** [00:32:32]: And then also it, with those deploy and build logs, it's going to have more troubleshooting information that you can feed into Claude.

**William Peare** [00:32:39]: Like right now, Claude can just troubleshoot itself, but you don't really have any outputs that you can check if things are going well.

**William Peare** [00:32:46]: So like if one specific API is failing, um, it's a lot more of a  to troubleshoot.

**William Peare** [00:32:53]: It also is just living on your computer.

**William Peare** [00:32:55]: That's the main thing.

**William Peare** [00:32:56]: Like you want to have some kind of way of hosting.

**Daniel Kalinin** [00:33:00]: So if it doesn't live on my computer and it lives in Railway, like, what, technically an agent can just work 24-7 or something like that?

**Daniel Kalinin** [00:33:09]: Yes.

**William Peare** [00:33:10]: Whereas if not, the agent would have to also live on your computer, which, depending on what you're running, running, like, even one or two solid agents  take some bandwidths.

**William Peare** [00:33:23]: Um, and if you made the one, like, an agent that's running off a virtual private network and it's tagging your computer, your computer still needs to always be on or it's not going to be to get that data.

**Daniel Kalinin** [00:33:34]: Got it.

**Daniel Kalinin** [00:33:35]: Do a lot of people connect Claw directly inside of the VPS?

**William Peare** [00:33:40]: I would think so.

**William Peare** [00:33:41]: Well, it calls it all through the API key for the agents.

**William Peare** [00:33:45]: So that's all calling it through a key and you're just giving it, like, tools that it can use.

**William Peare** [00:33:52]: Like, you'll give it permission and train it on all these tools and then it'll know how to, like, grab the tools and then based on, for a...

**William Peare** [00:34:00]: True agent, like if it gets, you know, it's scraped.

**William Peare** [00:34:03]: got three different clients and they had one didn't have an email.

**William Peare** [00:34:07]: It might then hop to their LinkedIn, see if it can find anything.

**William Peare** [00:34:10]: Oh, didn't find anything there.

**William Peare** [00:34:11]: I'm going to hop to Yelp.

**William Peare** [00:34:12]: And it'll like know how to go through different steps to get the end result, where if we train just a workflow, like the scraping and rich, it's going to go through, you know, the Google.

**William Peare** [00:34:22]: It's going to pull up all that stuff onto your spreadsheet.

**William Peare** [00:34:25]: Hunter.io is going to try and enrich it.

**William Peare** [00:34:27]: If Hunter.io failed to do its step, the workflow has done what it was trained to do.

**William Peare** [00:34:33]: It's just going to not give you that value.

**William Peare** [00:34:34]: Whereas like a true agent would be like, okay, well, we've went through these two tools.

**William Peare** [00:34:38]: I didn't find it.

**William Peare** [00:34:39]: I have these six other tools at my disposal and it's just going to start running through every tool until it gets the job done.

**William Peare** [00:34:45]: That's the biggest difference in like a workflow and an agent is that it'll make independent decisions without having to stop and ask you.

**William Peare** [00:34:53]: Okay.

**Daniel Kalinin** [00:34:55]: I know that's a lot.

**William Peare** [00:34:56]: Yeah.

**William Peare** [00:34:57]: It's a lot.

**Daniel Kalinin** [00:34:59]: Um, most, that's

**William Peare** [00:35:00]: So what you will need are just workflows, not agents.

**William Peare** [00:35:03]: Agents are a lot harder to build because they need to be able to figure out stuff on their own, which means you have to give them the list of tools or skills, whatever it might be, to do their job completely, and then the access to go figure these things out.

**William Peare** [00:35:18]: And then they'll learn and develop on their own.

**William Peare** [00:35:20]: Are you getting a lot of stuff from Hunter that doesn't have all the data you would need?

**William Peare** [00:35:25]: Hunter.io?

**William Peare** [00:35:26]: Yeah.

**Daniel Kalinin** [00:35:27]: I think I have everything that I need for now.

**Daniel Kalinin** [00:35:32]: I feel like I saw a place that scrapes better, so like Clay.

**Daniel Kalinin** [00:35:35]: I think it's a much better alternative than Hunter.

**Daniel Kalinin** [00:35:38]: Yeah, Clay is very good.

**Daniel Kalinin** [00:35:40]: Yeah, so I might upgrade to that.

**Daniel Kalinin** [00:35:41]: It's like five times more expensive, maybe $150 a month, but if it...

**Daniel Kalinin** [00:35:46]: Chris, are you at the shop?

**William Peare** [00:35:49]: Can you run down, my wife's going to be there in a second, and unload the pressure washer?

**William Peare** [00:35:53]: Troy was supposed to do it, but he forgot and he left for an emergency, apparently.

**William Peare** [00:35:56]: Emergency, tram emergency.

**William Peare** [00:35:58]: Thank you, buddy.

**William Peare** [00:36:00]: Yeah, Clay, I believe, is like the gold standard.

**Daniel Kalinin** [00:36:05]: Yeah.

**William Peare** [00:36:06]: But $150 a month, I mean, I guess you could test the theory and see how well it's working before you upgraded and built that out that much.

**William Peare** [00:36:13]: But what's your success rate, you think, on these scrapes on actually getting usable contact information?

**Daniel Kalinin** [00:36:19]: Hunter is probably like 15% to 25%.

**Daniel Kalinin** [00:36:23]: Okay.

**William Peare** [00:36:25]: So?

**Daniel Kalinin** [00:36:26]: So Clay can do it at like 60% or something.

**Daniel Kalinin** [00:36:29]: I mean, that makes a lot of sense.

**Daniel Kalinin** [00:36:30]: Price is not the issue, so like I'll probably just try Clay and see how that goes because, yeah, if I can get accurate data, that'd probably be the best move for me.

**William Peare** [00:36:40]: Yeah, you're going to have a way higher odds, especially if you're putting in all the time and effort to do it.

**William Peare** [00:36:44]: Now, my biggest concern with this whole process, but I also think it's the part that makes it close the highest, is each one having a loom video.

**William Peare** [00:36:51]: Like, how long are you going to test that before you go to some general loom video?

**William Peare** [00:36:55]: Because that could be a  time suck and a half.

**William Peare** [00:36:58]: It's going to be a time suck and a half.

**Daniel Kalinin** [00:37:00]: To be fair, spent the last like four to six months not even doing acquisitions.

**Daniel Kalinin** [00:37:03]: So I mean, you know, I could, I gotta get  somehow.

**Daniel Kalinin** [00:37:10]: Yeah, I don't know.

**Daniel Kalinin** [00:37:11]: mean, I'll play around with the scripts.

**Daniel Kalinin** [00:37:12]: Once I find something that works pretty good, just like, I'll generalize it, but I'm not going to know that until I put in manual input.

**Daniel Kalinin** [00:37:19]: So it is what it is.

**William Peare** [00:37:21]: Yeah, you think you got a month or two of just recording the  out of yourself?

**William Peare** [00:37:25]: Pretty much.

**Daniel Kalinin** [00:37:28]: Yeah, pretty much, which is fine with me.

**Daniel Kalinin** [00:37:30]: Like, whatever.

**Daniel Kalinin** [00:37:31]: I sign clients that I got to put in time, that's, that's fine with me.

**Daniel Kalinin** [00:37:35]: Yeah, it's called running a business.

**William Peare** [00:37:37]: Yeah.

**Daniel Kalinin** [00:37:39]: No .

**William Peare** [00:37:40]: Okay.

**William Peare** [00:37:41]: The railway one is gonna take a decent amount.

**William Peare** [00:37:45]: Give me, okay, so you saw very vaguely the variables, how it gets pushed over.

**William Peare** [00:37:51]: Give me what questions that immediately kicked off for you so that I know where I should dig in more.

**Daniel Kalinin** [00:37:55]: Yeah, I always assume that, like, if I...

**Daniel Kalinin** [00:38:00]: Connect, OpenClaw, Ermes, like the, it would know what to do through a Claude MCP.

**Daniel Kalinin** [00:38:05]: Yeah.

**Daniel Kalinin** [00:38:05]: So that's why I never understood, like, that people use Railway, if, why people use Railway if the Claude MCP can just be the connection, if that makes sense.

**Daniel Kalinin** [00:38:17]: Yes.

**William Peare** [00:38:18]: Well, yes, two different things, completely, because both OpenClaw, Ermes, and what you have, the system you have running on right now, they're all completely local.

**William Peare** [00:38:26]: You could set them up on a VPS, but right now, they're all isolated to your computer.

**William Peare** [00:38:33]: Railway is really just a back-end to actually, like, provide URLs and for something to live online that's accessible by any service, as opposed to living on your local computer.

**William Peare** [00:38:45]: Okay.

**William Peare** [00:38:45]: So I would say unrelated to it necessarily being agentic, it definitely makes it easier for the stuff to be accessed, but it's not really a bottleneck in that way.

**William Peare** [00:38:56]: It's just a more solid, scalable option, as opposed to you.

**William Peare** [00:39:00]: Having it live on your computer for all time.

**William Peare** [00:39:03]: Okay.

**Daniel Kalinin** [00:39:03]: Would it be different if I just got an ERMES on a VPS and then also downloaded Claude on that VPS and it had access to Claude there?

**William Peare** [00:39:22]: I think if you had your whole code base that it's running off of on there, then it would run just the same.

**William Peare** [00:39:27]: Okay.

**Daniel Kalinin** [00:39:28]: Just the same thing.

**William Peare** [00:39:28]: You'd have to have, like, you know, all the local files you have built out, the whole code base that runs this script, all the Python that's doing the scraping and all that would need to live on the VPS.

**William Peare** [00:39:38]: But I think, I mean, it would be exactly the same thing as your local computer, just virtually hosted.

**William Peare** [00:39:43]: Okay.

**William Peare** [00:39:44]: There's many ways to split this onion is kind of the thing.

**William Peare** [00:39:47]: Like, it can be local, it can be hosted by a hosting service.

**Daniel Kalinin** [00:39:51]: No, I I definitely know I shouldn't keep it local because, yeah, I mean, if this PC dies one day, everything dies, right?

**Daniel Kalinin** [00:39:58]: It would suck, big time.

**William Peare** [00:40:01]: Like you've probably noticed even that like if you're on a different computer you can't even really see most of your Claude stuff because it's completely tied to that.

**William Peare** [00:40:12]: Now there's a couple things there like you're doing it all local you could just do a leadstatement cloud folder within Claude and then access that from anything but that's not going to fix this coding thing that's just going to show you a view through Claude.

**William Peare** [00:40:28]: The VA onboarding SOPs, I feel really, really solid about that.

**William Peare** [00:40:32]: Obviously, like I said, we need to build out this workflow for you completely.

**William Peare** [00:40:36]: You need to iterate on it for a week or two to make sure you like what's happening.

**William Peare** [00:40:41]: You need to build out a Loom library and written SOPs so that it's like super clear and trainable on bringing someone on.

**William Peare** [00:40:46]: That way you don't have to dump immense time into training this person.

**William Peare** [00:40:50]: Yeah.

**William Peare** [00:40:51]: Yeah.

**William Peare** [00:40:51]: And then I think we get into getting you the genetic AI whether you want to go with Hermes or open claw.

**William Peare** [00:40:58]: I did some research there.

**William Peare** [00:41:00]: Some even newer, like Open Claw is so new that it still breaks frequently.

**William Peare** [00:41:04]: Hermes is older where it's getting a little bit more obsolete.

**William Peare** [00:41:07]: They have a bunch of new ones out now, so we can pretty much test whichever one you want.

**William Peare** [00:41:11]: I tested both just to see what it is.

**William Peare** [00:41:14]: And honestly, for me, I tested it just to see that it was workable.

**William Peare** [00:41:18]: But mostly with what I'm doing, it makes more sense for it to just be ran by like coworker Claude.

**William Peare** [00:41:25]: So for you, you'll have enough repeatable tasks with the copywriting and stuff where actually having a fully local one makes sense.

**William Peare** [00:41:34]: I don't have that many repeatable tasks that it's just cranking out constantly where it's worth the upkeep of the system because it's a little bit more work on that end.

**William Peare** [00:41:42]: But I think that's the next one we get rolling for you.

**William Peare** [00:41:49]: And then going through your GoHigh level and the Zapier, what you actually have built.

**William Peare** [00:41:54]: Because have you had to start paying for Zapier yet?

**William Peare** [00:41:57]: I think I've paid for it for a while.

**Daniel Kalinin** [00:41:59]: you'll see

**Daniel Kalinin** [00:42:02]: Yeah, I've been paying it for a while.

**Daniel Kalinin** [00:42:05]: What I'm thinking with like this website service stuff, I got another lead that I got to call right after.

**Daniel Kalinin** [00:42:11]: So it's like, I mean, it should be super simple.

**Daniel Kalinin** [00:42:12]: What I can probably do is I can train an agent on creating a sub, like agents act as co-work, right?

**Daniel Kalinin** [00:42:21]: Like they basically just have access to, okay, I can just train an agent, get it like, you know, I don't know, like not admin permissions to kill all my stuff, but what I can, and I can probably give it an email too.

**Daniel Kalinin** [00:42:36]: That way I can just invite it as a member, right?

**Daniel Kalinin** [00:42:38]: Yes.

**Daniel Kalinin** [00:42:39]: Yeah.

**Daniel Kalinin** [00:42:40]: I think I've heard of that service before, email for agents.

**Daniel Kalinin** [00:42:44]: Yeah.

**Daniel Kalinin** [00:42:45]: I mean, I can technically just, because what I do before these calls, I just spin up a professional website in Manus.

**Daniel Kalinin** [00:42:52]: You can also do it in GHL now with like, they have some AI studio thing that you basically can just copy the website.

**Daniel Kalinin** [00:43:00]: A website URL, and it'll build it out in GHL.

**Daniel Kalinin** [00:43:05]: So I can probably have the agent just literally do the pre-call fulfillment just to be like, hey, here's your website, blah, blah, blah.

**Daniel Kalinin** [00:43:13]: Yeah, I can run that  up if I automate it too.

**Daniel Kalinin** [00:43:18]: Yeah, just spitting out thoughts.

**William Peare** [00:43:20]: Yeah, and so you just ran a Facebook ad?

**William Peare** [00:43:23]: What was your path of?

**Daniel Kalinin** [00:43:25]: Yeah, I'll show you right now.

**Daniel Kalinin** [00:43:27]: I can't believe you got four calls in a night.

**Daniel Kalinin** [00:43:31]: Yeah, I mean, I've said all those calls today.

**Daniel Kalinin** [00:43:36]: I don't know, maybe I should have become like a sales rep for like a Fortune 500 company.

**Daniel Kalinin** [00:43:40]: I'd probably make a good amount of money.

**Daniel Kalinin** [00:43:42]: Yeah, seriously.

**Daniel Kalinin** [00:43:44]: See the entire screen.

**William Peare** [00:44:04]: Yes, sir, Mr.

**William Peare** [00:44:04]: John.

**Daniel Kalinin** [00:45:21]: Cool.

**Daniel Kalinin** [00:45:22]: Yeah.

**Daniel Kalinin** [00:45:24]: $20 per lead submission.

**Daniel Kalinin** [00:45:26]: I just spun up some few  ads.

**Daniel Kalinin** [00:45:35]: It's like, we'll build your free website, blah, blah, blah.

**Daniel Kalinin** [00:45:38]: They then tell me some info about them.

**Daniel Kalinin** [00:45:41]: This woman right here, I think her name's Lisa.

**Daniel Kalinin** [00:45:43]: Yeah, she's a .

**Daniel Kalinin** [00:45:44]: So I marked her as red.

**Daniel Kalinin** [00:45:46]: Um, but yeah, they just tell me like their, their trade or whatever, whatever service they provide, name, email.

**Daniel Kalinin** [00:45:53]: just call them up and then I set those appointments and I'm like, cool, I'll get you a website before that, blah, blah, blah.

**Daniel Kalinin** [00:45:58]: Probably put them on like a.

**Daniel Kalinin** [00:46:00]: Fenday free trial.

**Daniel Kalinin** [00:46:03]: I'm probably going to position it as like, if you give me a solid testimonial, blah, blah, blah, I'm going to take away like an activation fee of like $297.

**Daniel Kalinin** [00:46:12]: That way I can just get testimonials pretty fast.

**Daniel Kalinin** [00:46:16]: I don't know, charging like $97 a month or something like that.

**Daniel Kalinin** [00:46:20]: I built the website too.

**Daniel Kalinin** [00:46:21]: was pretty simple.

**Daniel Kalinin** [00:46:22]: Lead Trade Systems.

**Daniel Kalinin** [00:46:24]: Yeah.

**Daniel Kalinin** [00:46:25]: bang?

**Daniel Kalinin** [00:46:25]: Yeah.

**Daniel Kalinin** [00:46:26]: And it's just like, links to Calendly, see how it works, blah, blah, blah.

**Daniel Kalinin** [00:46:31]: I don't know, just like some simple stuff.

**Daniel Kalinin** [00:46:34]: But yeah, I mean, I'll just play around with it in the home service space.

**Daniel Kalinin** [00:46:42]: But realistically, like, I mean, two options.

**Daniel Kalinin** [00:46:44]: Either I run this up, like, I don't know, hopefully I'll close a call today.

**Daniel Kalinin** [00:46:47]: I mean, but I'll close one eventually, regardless.

**Daniel Kalinin** [00:46:50]: But I might run it up in home service, or I'll just do that for B2B and just start targeting like new firms that just like, you know, got launched like CPAs, bookkeepers, whatever.

**Daniel Kalinin** [00:47:00]: Whatever.

**Daniel Kalinin** [00:47:00]: And just nurture them down the line.

**Daniel Kalinin** [00:47:02]: That should probably be pretty simple.

**Daniel Kalinin** [00:47:05]: That is crazy.

**William Peare** [00:47:07]: Yeah.

**Daniel Kalinin** [00:47:08]: Yeah, just like that.

**William Peare** [00:47:10]: Yeah.

**William Peare** [00:47:10]: Pretty  cool what you can do nowadays.

**Daniel Kalinin** [00:47:13]: That's like, I think I probably think this has been about like every hour or every two hours.

**Daniel Kalinin** [00:47:17]: Like, if I don't stay on top of this , I am going to get  by the person at will.

**Daniel Kalinin** [00:47:23]: Oh, I know.

**Daniel Kalinin** [00:47:24]: It's such a ...

**Daniel Kalinin** [00:47:25]: Yeah.

**Daniel Kalinin** [00:47:25]: This used to be a design team, plus a funnel team, plus a website team, plus a whatever, blah, blah, blah.

**Daniel Kalinin** [00:47:32]: Now it's just like, my dumb  can do this in like two hours.

**Daniel Kalinin** [00:47:38]: Yeah.

**Daniel Kalinin** [00:47:38]: I'm curious.

**William Peare** [00:47:39]: You think you'd close one of them today?

**William Peare** [00:47:41]: Decent odds?

**William Peare** [00:47:42]: Yeah.

**William Peare** [00:47:43]: I mean, I'll see.

**Daniel Kalinin** [00:47:44]: I don't know.

**Daniel Kalinin** [00:47:45]: I think I'm fine with closing people.

**Daniel Kalinin** [00:47:47]: Like, it's honestly going to be funny because I don't know how nervous I'm going to be on closing.

**Daniel Kalinin** [00:47:53]: Like, for B2B, I can just be like six or nine, okay, whatever, blah, blah, like pay me.

**Daniel Kalinin** [00:47:57]: And I wouldn't really stutter, but...

**Daniel Kalinin** [00:48:00]: This is a new service.

**Daniel Kalinin** [00:48:01]: I might even set her at $97 just because, like, I don't know.

**Daniel Kalinin** [00:48:04]: $97.

**Daniel Kalinin** [00:48:06]: Yeah.

**Daniel Kalinin** [00:48:07]: This is a new, this is a different persona, too.

**Daniel Kalinin** [00:48:09]: I mean, these guys are more, like, price conscious, which is why, like, I was thinking about it and I just need to kind of over-deliver heavily and I need to get them to be really sticky with it.

**Daniel Kalinin** [00:48:17]: So there's, like, invoicing systems and GoHard level that I need to get them, like, to use, review automations, all that kind of stuff.

**Daniel Kalinin** [00:48:24]: It's basically just going to be, like, I need to position it to a point where they'd be, like, technically shutting down their business if they stop using this software, you know?

**Daniel Kalinin** [00:48:35]: Yeah.

**William Peare** [00:48:36]: So for $100 a month, they're going to get the website and automated review requests?

**William Peare** [00:48:40]: Yeah.

**William Peare** [00:48:41]: Miss called text back as well.

**Daniel Kalinin** [00:48:43]: GoHard level has an invoicing system.

**Daniel Kalinin** [00:48:45]: So that's probably going to, like, I'll try to cater that to my onboarding workflow where it's, like, hey, like, you can invoice people through here.

**Daniel Kalinin** [00:48:52]: You can add customers to this list right here, so on and so forth.

**Daniel Kalinin** [00:48:56]: And it's just, like, I mean, I think these guys use, like, Homes Pro or whatever.

**Daniel Kalinin** [00:49:00]: Jobber and QuickBooks, whatever, for customer data.

**Daniel Kalinin** [00:49:05]: If I can just get them to use this, it's just going to be so sticky.

**Daniel Kalinin** [00:49:09]: I think Hermosi calls it air.

**Daniel Kalinin** [00:49:11]: I'd literally just be selling air.

**Daniel Kalinin** [00:49:12]: I'm selling a templated system that I don't have to touch whatsoever.

**Daniel Kalinin** [00:49:18]: If I can get the websites to be auto-generated, mean, that's going to make my life super easy.

**Daniel Kalinin** [00:49:26]: If anything, like, I can build out a few templates and the VA can always just come in for every new sub-account that needs to be created and build that out.

**Daniel Kalinin** [00:49:36]: So, you know, even at, like, I don't know, a couple hundred clients, maybe just one CSM would be more than fine because I'm guessing, you know, not, these guys might only have, like, a support ticket once every, like, few weeks because it's mainly just going to be adding images or whatever.

**Daniel Kalinin** [00:49:52]: Yeah.

**Daniel Kalinin** [00:49:52]: So, I mean, it seems like a really easy, easy service to fulfill on.

**Daniel Kalinin** [00:49:58]: Super easy.

**William Peare** [00:49:59]: Yeah.

**William Peare** [00:50:00]: I'm changing my whole model.

**William Peare** [00:50:01]: In fact, this is what I'm going to do now.

**Daniel Kalinin** [00:50:03]: This is a cakewalk.

**Daniel Kalinin** [00:50:05]: Yeah, I was just thinking like, yeah, I mean, this would be super easy for me to do in B2B as well.

**Daniel Kalinin** [00:50:11]: So I can just get that like kind of, I guess my whole goal is have like a portfolio of companies, A, that I invest into that I own.

**Daniel Kalinin** [00:50:23]: If I can build something out on the B2B side, that's pretty big.

**Daniel Kalinin** [00:50:26]: And then also on the, I don't know, like home service side, that's pretty big because home service ads are pretty simple for me too.

**Daniel Kalinin** [00:50:35]: Yeah, that just made my life pretty, pretty easy financially.

**Daniel Kalinin** [00:50:39]: No .

**William Peare** [00:50:40]: Yeah, I'm excited to see if this just kicks off because at least it could feel like fuel the MMR to get the person in there to boost the  copywriting, which will then boost the bigger ticket item one.

**William Peare** [00:50:50]: But then you're not having to fund it out of pocket because that's definitely.

**Daniel Kalinin** [00:50:54]: Pretty much, yeah, if I can get this to like, I mean, I know some guys that like.

**Daniel Kalinin** [00:51:00]: This guy right here, he does a for-home service pros, and he does almost half a million a month with it, and it's just recurring as .

**Daniel Kalinin** [00:51:11]: So it's like, even if I get it to a point where it's like $30,000, my expenses are, I mean, extremely conservative 50%, even though it won't be.

**Daniel Kalinin** [00:51:23]: It'll mainly probably just be towards a payroll, like a CSM or whatever.

**Daniel Kalinin** [00:51:27]: Like, if I can get $10,000, $15,000 per month that I could just fuel on the B2B side of things and just get a really good employee, I mean, my life is pretty much set in stone in there.

**Daniel Kalinin** [00:51:37]: And at that point, I'd probably just scale this if I'm getting that MRR, to be honest.

**Daniel Kalinin** [00:51:41]: Yeah, no .

**William Peare** [00:51:42]: That would be crazy.

**William Peare** [00:51:44]: At $300,000 a month, he's pushing in this?

**William Peare** [00:51:47]: Yeah, like half a million, I think.

**Daniel Kalinin** [00:51:49]: That is insane.

**William Peare** [00:51:51]: Yeah.

**Daniel Kalinin** [00:51:53]: Yeah, so I just need to make it sticky.

**Daniel Kalinin** [00:51:55]: I need to build out the systems right now, but it should be super simple.

**Daniel Kalinin** [00:51:59]: And...

**Daniel Kalinin** [00:52:00]: I think I can whoop ads against all these guys because I just know sales processes.

**Daniel Kalinin** [00:52:05]: I just sent one of the guys that I have a book call with a video of hinting at the website and some pre-call framing, so on and so forth.

**Daniel Kalinin** [00:52:16]: This is a super beginner model, although it's a super good model too, but most people that do it are retarded when it comes to how to frame, pre-call stuff, all that.

**Daniel Kalinin** [00:52:29]: Right, right.

**William Peare** [00:52:30]: Yeah, it's just such a low price point to get in there and such a low-risk thing for them.

**William Peare** [00:52:34]: That's just that, like you said, like once you get in there, it's like, what the hell are they going to do?

**William Peare** [00:52:39]: Yeah.

**William Peare** [00:52:40]: Yeah.

**Daniel Kalinin** [00:52:40]: Do you own the website?

**Daniel Kalinin** [00:52:43]: Which website?

**William Peare** [00:52:45]: If you're building their website and go high level, do you own it or do they own it?

**Daniel Kalinin** [00:52:49]: I would buy it probably unless they have their own website, which is going to make it even more sticky.

**Daniel Kalinin** [00:52:54]: So that's kind of logic with that.

**William Peare** [00:52:56]: Yeah, that was my thought.

**William Peare** [00:52:58]: I'm like, if you own it, then they're really...

**William Peare** [00:52:59]: And great

**William Peare** [00:53:00]: .

**William Peare** [00:53:02]: They're pretty much trapped there unless they want to buy it back.

**Daniel Kalinin** [00:53:05]: Yeah, I guess this is like predatory marketing in a sense or predatory fulfillment.

**Daniel Kalinin** [00:53:10]: But no, I mean like I spoke to a lot of these guys and that's why I called my brother's or my fiance's brother retarded because I gave him like a whole sales script and he was like, I need to learn it.

**Daniel Kalinin** [00:53:20]: I need to learn about the industry.

**Daniel Kalinin** [00:53:21]: I don't know  about this industry.

**Daniel Kalinin** [00:53:24]: But I mean like, yeah, it's just like so fundamental.

**Daniel Kalinin** [00:53:28]: He's got like one guy that I have a call with at like 2.30.

**Daniel Kalinin** [00:53:30]: He's starting a pressure washing company.

**Daniel Kalinin** [00:53:32]: He's going to start door knocking.

**Daniel Kalinin** [00:53:33]: I just tell him like, dude, like, I mean, do you want to be the guy that's like a no-name on Google who seems sketchy as ?

**Daniel Kalinin** [00:53:39]: Or do you just want to have a good website, have reviews, make people actually trust you, go with you, so on and so forth?

**Daniel Kalinin** [00:53:43]: And like, that's literally all I'm selling.

**Daniel Kalinin** [00:53:46]: I'm framing it in a way that I'm not generating leads for them.

**Daniel Kalinin** [00:53:49]: I'm just kind of optimizing their traffic.

**Daniel Kalinin** [00:53:52]: Yeah, and giving them validity.

**William Peare** [00:53:55]: Pretty much.

**William Peare** [00:53:57]: Yeah.

**William Peare** [00:53:58]: And then you can pivot into leads.

**Daniel Kalinin** [00:54:00]: Yeah, work with a company right now, an SEO company, and they'd happily take on a shitload of clients, so I can just charge them either recurring monthly or a one-time payment just to buy the client.

**Daniel Kalinin** [00:54:17]: Yeah, I mean, if my LTV on these clients is like they stay for two years, which apparently isn't uncommon, especially at my lower price point.

**Daniel Kalinin** [00:54:28]: Like this guy right here, he charges like $2.97 a month.

**Daniel Kalinin** [00:54:31]: If do $2.97, those guys are staying for two years.

**Daniel Kalinin** [00:54:34]: I mean, this is the easiest system in the world.

**Daniel Kalinin** [00:54:36]: My LTV can be like, my CAC up to LTV can be like, I don't know what my CAC's going be, maybe like $200 or something like that, or $100.

**Daniel Kalinin** [00:54:44]: I can't, I haven't validated that yet.

**Daniel Kalinin** [00:54:47]: It's an LTV of 97 times 24 months, so like $2,400 plus back end upsells.

**Daniel Kalinin** [00:54:55]: Yeah, I mean, yeah, it's just like, yeah.

**Daniel Kalinin** [00:55:00]: Yeah, that's what I'm going to work on.

**Daniel Kalinin** [00:55:01]: Holy .

**William Peare** [00:55:03]: Yeah, if that kicks off, which, you know, that's crazy.

**William Peare** [00:55:06]: You're just thinking outside the box, my boy, thinking outside the box.

**William Peare** [00:55:10]: Yeah, and that's kind of what I need to do, too.

**Daniel Kalinin** [00:55:14]: Like, I need to have MRR.

**Daniel Kalinin** [00:55:16]: I got to call James Johnson, who has a property management company, but I need a, I definitely need a stack MRR.

**Daniel Kalinin** [00:55:22]: I don't, it's going to be hard to just scale if I continue relying on PIFs and all that stuff.

**Daniel Kalinin** [00:55:33]: And yeah, I can, I can stack MRR much easier like this.

**Daniel Kalinin** [00:55:36]: Right.

**Daniel Kalinin** [00:55:38]: Yeah.

**William Peare** [00:55:38]: I mean, at that point, you can be picky about the PIFs and really be pushing big ticket ones when you're not having to worry about the month to month.

**Daniel Kalinin** [00:55:44]: Yeah, pretty much.

**Daniel Kalinin** [00:55:46]: Yeah.

**Daniel Kalinin** [00:55:46]: Okay.

**William Peare** [00:55:49]: On my notes, I mean, Fathom will give me my notes, but the biggest thing that I got that I want to knock out today is just a couple of Loom videos for you on Railway in general, just so you have some stuff.

**William Peare** [00:56:00]: If you can reference and go back to a couple of times on that, what else do you, let me look at.

**William Peare** [00:56:06]: Skills is a big one.

**Daniel Kalinin** [00:56:08]: I need to, yeah, need to figure out the skills.

**Daniel Kalinin** [00:56:12]: Yep.

**Daniel Kalinin** [00:56:12]: Okay.

**William Peare** [00:56:13]: Have you built any live artifacts yet?

**William Peare** [00:56:17]: Like dashboards and something, right?

**Daniel Kalinin** [00:56:20]: They can be essentially anything.

**Daniel Kalinin** [00:56:21]: Dashboard's an easy example.

**William Peare** [00:56:22]: That would be huge.

**Daniel Kalinin** [00:56:24]: I don't know my use case, but I would like a centralized system where I can just view specific stuff.

**Daniel Kalinin** [00:56:31]: Yep.

**Daniel Kalinin** [00:56:32]: I actually believe I had Claude tell me exactly what I need to do next.

**Daniel Kalinin** [00:56:41]: If I can find it.

**Daniel Kalinin** [00:56:48]: So meta adds API connection.

**Daniel Kalinin** [00:57:01]: So that Claude can pull certain metrics without me opening the ads manager.

**Daniel Kalinin** [00:57:04]: This would probably be a good artifact.

**Daniel Kalinin** [00:57:06]: That way I can just see client-by-client.

**Daniel Kalinin** [00:57:09]: I need great Claude skills for ad batch generation, copywriting, all that good stuff.

**Daniel Kalinin** [00:57:18]: Scheduled routines for work that I do manually.

**William Peare** [00:57:23]: And that's pretty much the workflow slash agent, depending on how complex, but the, yep, routines, scheduled routines is important.

**Daniel Kalinin** [00:57:32]: And, um, blah, blah, blah, your own memory says process, not create, I don't know what this  means.

**Daniel Kalinin** [00:57:41]: Um, audit plus level up as, given how fast your memory and obesity have audit, 4C score per unit and level up next auto, so I guess it's like recurring audits to see what can be automated or whatever.

**Daniel Kalinin** [00:57:55]: Um, I mean, that's what it said so far.

**Daniel Kalinin** [00:57:58]: Um, but yeah, artifact.

**Daniel Kalinin** [00:58:00]: This would be good.

**Daniel Kalinin** [00:58:01]: I'm in a lot of ad accounts.

**Daniel Kalinin** [00:58:03]: So if I can see everything, you can look into like the MetaMCP.

**Daniel Kalinin** [00:58:07]: If I can somehow get, like I have such simple rules with like BizBooster, for example, where it's like if an ad hits 40 bucks without a conversion, turn it off and all that stuff.

**Daniel Kalinin** [00:58:18]: And like if it can just monitor that 24-7, I mean, and turn it off automatically, like that's just going to make my, that's going to take time off of my VA.

**Daniel Kalinin** [00:58:30]: And I can just put that VA, it's actually uploading ads and stuff.

**Daniel Kalinin** [00:58:34]: Right.

**Daniel Kalinin** [00:58:34]: And they could be on the go, no go.

**William Peare** [00:58:36]: Cause most of them, unless it's fully agentic, like with the live artifact, it's probably still going to have like a confirm.

**William Peare** [00:58:43]: So like it'll push it to Slack or wherever you have like a push to confirm, like you were talking about go, no go.

**William Peare** [00:58:48]: But even if you just had them doing that, as opposed to like going through and calculating it all, much better.

**William Peare** [00:58:56]: I think that's a pretty easy use case that I'm happy to test on.

**William Peare** [00:59:00]: I'll build that one so I can give you the full walkthrough on it.

**William Peare** [00:59:04]: I've done a couple on my end, but mine are a little different.

**William Peare** [00:59:06]: So I'll build out a couple and then we can go through building that and we can kind of start looking at the agentic AI primer.

**William Peare** [00:59:16]: I think the onboarding SOP is pretty solid for that one.

**William Peare** [00:59:19]: I really just want you to finish out what you're building on the lead gen thing.

**William Peare** [00:59:24]: That way we can really test it, run through, try and break it and then make sure you have good written SOPs and some Loom videos.

**William Peare** [00:59:32]: That way when you hire this person, we're ready to kick them off.

**William Peare** [00:59:34]: Yeah, I agree.

**Daniel Kalinin** [00:59:36]: And yeah, I want to make this hire like this week.

**Daniel Kalinin** [00:59:38]: So I just, I guess that's another good thing.

**Daniel Kalinin** [00:59:40]: Like outside of just having them handle my gamma outreach, I can also help use them to set up like new sub accounts from these home service clients.

**Daniel Kalinin** [00:59:49]: I mean, I should be able to close them.

**Daniel Kalinin** [00:59:51]: It's such a simple, simple service.

**Daniel Kalinin** [00:59:54]: So I'll just, uh, Is the ad still working?

**Daniel Kalinin** [00:59:59]: Yeah, yeah, yeah.

**Daniel Kalinin** [01:00:02]: What I want to say.

**Daniel Kalinin** [01:00:06]: Yeah, I have four calls today.

**Daniel Kalinin** [01:00:07]: I'll probably book a few more calls today and just start building out the onboarding thing.

**Daniel Kalinin** [01:00:13]: It should be super simple to do.

**Daniel Kalinin** [01:00:15]: I might probably just set it as a 10-day free trial with their payment on file.

**Daniel Kalinin** [01:00:24]: And after the 10 days, I can just call them in advance.

**Daniel Kalinin** [01:00:28]: And if they like it, then great.

**Daniel Kalinin** [01:00:30]: Great.

**Daniel Kalinin** [01:00:32]: Yeah, I like that.

**William Peare** [01:00:34]: What day do you want to link up this week?

**William Peare** [01:00:38]: What do I want to link up this week?

**Daniel Kalinin** [01:00:39]: Yeah, what works on your schedule?

**Daniel Kalinin** [01:00:42]: I think Wednesday is good.

**Daniel Kalinin** [01:00:44]: Okay, Wednesday.

**William Peare** [01:00:45]: What time are you thinking you want another morning slot?

**Daniel Kalinin** [01:00:48]: Let me double check.

**Daniel Kalinin** [01:00:49]: Yeah, Wednesday morning slot is good.

**Daniel Kalinin** [01:00:51]: Let me look, see what I have.

**William Peare** [01:00:55]: I got the coffees in.

**Daniel Kalinin** [01:00:56]: This one sucks as I thought it was the same thing as Expressino.

**Daniel Kalinin** [01:01:00]: But it's not.

**William Peare** [01:01:03]: Not the same.

**William Peare** [01:01:05]: Let me get back to you on Wednesday and see what my slot is on Wednesday.

**William Peare** [01:01:08]: It might have to be later in the day, but I'll confirm that today.

**Daniel Kalinin** [01:01:12]: Okay.

**Daniel Kalinin** [01:01:12]: If your gas station, by the way, has Redberry Fizz, the limited edition, I think you're going to love that one.

**William Peare** [01:01:17]: Redberry Fizz.

**William Peare** [01:01:19]: Yeah.

**Daniel Kalinin** [01:01:19]: They ran out at the deli downstairs, but it was like I should have stopped up on like 20 of them.

**Daniel Kalinin** [01:01:25]: Okay.

**Daniel Kalinin** [01:01:26]: I'm going to have to look.

**William Peare** [01:01:27]: Yeah.

**Daniel Kalinin** [01:01:28]: All right.

**Daniel Kalinin** [01:01:29]: I'm going start calling these people.

**Daniel Kalinin** [01:01:30]: sending more stuff.

**Daniel Kalinin** [01:01:31]: And then I'll just keep killing myself over and calling.

**Daniel Kalinin** [01:01:35]: Get it.

**Daniel Kalinin** [01:01:35]: Get it done, bud.

**William Peare** [01:01:36]: Shoot me a text.

**William Peare** [01:01:37]: Give me an update if you close one today.

**William Peare** [01:01:39]: Absolutely.

**Daniel Kalinin** [01:01:39]: See you.

**Daniel Kalinin** [01:01:40]: Bye.