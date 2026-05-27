---
title: Impromptu Google Meet Meeting
date: 2026-05-11
participants: [William Peare]
source: fathom
type: meeting
url: https://fathom.video/calls/669946850
tags: [fathom, meeting]
---

# Impromptu Google Meet Meeting
**Date:** May 11, 2026
**Participants:** William Peare
**Recording:** [View on Fathom](https://fathom.video/calls/669946850)

---

## Summary

### [Audio setup and technical troubleshooting @ 0:00](https://fathom.video/share/CA1GhzGvZPvnh4FFEDs4xd2QhWX56vKe?tab=summary&timestamp=0)

The team tested audio connectivity and resolved an echo issue that was affecting call quality. Once resolved, they confirmed all participants could hear each other clearly and proceeded with screen sharing.

### [Commission system architecture and reporting @ 2:17](https://fathom.video/share/CA1GhzGvZPvnh4FFEDs4xd2QhWX56vKe?tab=summary&timestamp=137)

William reviewed the commission functionality in the system, confirming that:

  - Reports can be built on commissions to track unpaid commissions per person
  - Commissions are automatically generated when jobs are sold (2% for self-gen, with other tiers for front-end and wash-out)
  - Commissions can be assigned either to the sales rep automatically or left unassigned
  - The system has no automation capability for conditional commission generation—commissions are not triggered by properties or conditions, only generated as flat percentages of planned revenue
  - Commissions are reportable but not automatable, requiring manual payroll review

### [Self-generated commission workflow and controls @ 5:00](https://fathom.video/share/CA1GhzGvZPvnh4FFEDs4xd2QhWX56vKe?tab=summary&timestamp=300)

The team established the process for handling self-generated (self-gen) commissions:

  - Self-gen commissions are flat 2% and cannot be automatically generated based on a property flag
  - When a sales rep sells a self-gen job, they must manually add a commission entry in the system (e.g., "Pete self-gen") and set the amount
  - The commission then appears as unpaid in the system
  - During payroll, William and Chance will spot-check self-gen claims by reviewing the Slack list and verifying the lead source
  - Tiered commissions are handled separately via quarterly reviews of sales numbers and paid out in bulk
  - Risk mitigation: While sales reps could theoretically mark all jobs as self-gen, this is no different from the previous system where they could check a box in HubSpot; the safeguard is the payroll team's spot-checking process
  - **Action item**: Contact JobNimbus support to ask about (1) how to track commissions for regular payroll processing and (2) whether specific commissions can be created for inside sales (Quincy) automatically

### [Job creation and contact workflow @ 15:03](https://fathom.video/share/CA1GhzGvZPvnh4FFEDs4xd2QhWX56vKe?tab=summary&timestamp=903)

The team clarified the proper workflow for creating new jobs:

  - Jobs must be created from the job level (not the contact level) to trigger the lead intake questions
  - The system requires a contact to exist before a job can be created; clicking "add job" forces users to either create a new contact or match to an existing one
  - Once a contact is created/matched and "save and continue" is clicked, the system immediately opens the job playbook with intake questions
  - For existing contacts (e.g., Standcraft), users can type the contact name when creating a job and the system will show matching contacts to select from, avoiding duplicate contact creation
  - Job name field exists in the playbook but has display limitations (see next chapter)

### [Job naming and display issues @ 18:04](https://fathom.video/share/CA1GhzGvZPvnh4FFEDs4xd2QhWX56vKe?tab=summary&timestamp=1084)

The team identified a significant issue with job naming:

  - When creating a job, the system defaults the job name to contact name + job number (e.g., "Jorn Reger \#123")
  - Users can enter a custom job name in the job name field during creation (e.g., "Jorn's Chicken Coop"), but this override does not stick
  - After job creation, the job card displays the contact name instead of the custom job name entered
  - The only current workaround is to manually edit the job after creation to change the display name
  - The team suspects the job name may be stored as a property in the system but the display name on the job board uses the contact's primary display name, creating confusion
  - Example: A job entered as "Calgary Court Construction" displays as "Zachary Bolt" (the contact) on the board
  - **Next step**: Further testing needed to understand whether the job name field is purely a property or if there's a way to make it the display name; team to investigate tomorrow

### [Zapier integration status and phone recordings @ 22:00](https://fathom.video/share/CA1GhzGvZPvnh4FFEDs4xd2QhWX56vKe?tab=summary&timestamp=1320)

William reviewed the current Zapier integrations:

  - **Call answer to create contact**: Working properly, no failures
  - **Job to air call contact**: Occasionally triggering failures; needs investigation to determine the cause
  - **Signed estimate**: Currently turned off; it works but won't provide useful data until a required amount field is added to the form
  - **Phone recordings**: Peter requested the ability to have call recordings available in JobNimbus (to review customer conversations before arriving at jobs); William is working on this via Zapier but encountered issues with the integration creating duplicate or triplicate records

### [Meeting conclusion and next steps @ 29:12](https://fathom.video/share/CA1GhzGvZPvnh4FFEDs4xd2QhWX56vKe?tab=summary&timestamp=1752)

Due to personal circumstances, the team decided to reconvene the following day to continue troubleshooting. William committed to addressing action items as notes are compiled, with key pending items including: contacting JobNimbus support about commission tracking and inside sales automation, further testing of job naming behavior, and investigating the Zapier integration failures.


---

## Action Items

- [ ] **William Peare** — Review Peter's Slack list; log job complaints in Fathom `[00:02:44]` [▶](https://fathom.video/calls/669946850?timestamp=164.9999)
- [ ] **William Peare** — Add Self-Gen Yes/No to commissions; delete 'Profit Tracker Commissions' calc; remove 'Unassigned' `[00:03:27]` [▶](https://fathom.video/calls/669946850?timestamp=207.9999)
- [ ] **William Peare** — Define payroll process: unpaid commissions report; mark paid; spot-check self-gen; pay tiered quarterly `[00:03:52]` [▶](https://fathom.video/calls/669946850?timestamp=232.9999)
- [ ] **Jorn Reger** — Define payroll process: unpaid commissions report; mark paid; spot-check self-gen; pay tiered quarterly `[00:03:52]` [▶](https://fathom.video/calls/669946850?timestamp=232.9999)
- [ ] **William Peare** — Call JobNimbus support re: commissions reporting/dashboards; inside sales commissions (Quincy) `[00:11:56]` [▶](https://fathom.video/calls/669946850?timestamp=716.9999)
- [ ] **William Peare** — Create 'Inside Sales Commission' (Unassigned) for Quincy; pay at payroll `[00:13:39]` [▶](https://fathom.video/calls/669946850?timestamp=819.9999)
- [ ] **Jorn Reger** — Enforce intake workflow: create jobs from JobNimbus; override default job name `[00:17:43]` [▶](https://fathom.video/calls/669946850?timestamp=1063.9999)
- [ ] **William Peare** — Fix Zapier 'Job to Aircall Contact' failure `[00:22:49]` [▶](https://fathom.video/calls/669946850?timestamp=1369.9999)
- [ ] **William Peare** — Schedule follow-up meeting for May 12 `[00:29:01]` [▶](https://fathom.video/calls/669946850?timestamp=1741.9999)
- [ ] **Jorn Reger** — Compile notes on JobNimbus issues for follow-up `[00:29:08]` [▶](https://fathom.video/calls/669946850?timestamp=1748.9999)

---

## Transcript

**William Peare** [00:00:00]: Because then in theory, you should be able to hear me.

**Jorn Reger** [00:00:03]: you in there?

**William Peare** [00:00:04]: Yeah.

**William Peare** [00:00:05]: I'm sorry, what they're doing right now, but just know that you might not have the time to go to me.

**William Peare** [00:00:09]: Okay.

**William Peare** [00:00:10]: Just kidding.

**William Peare** [00:00:11]: Can you guys hear me?

**William Peare** [00:00:13]: Okay.

**Kaitlyn Wilkinson** [00:00:17]: All right.

**Kaitlyn Wilkinson** [00:00:17]: Chance, can you hear me?

**Kaitlyn Wilkinson** [00:00:19]: Because I'm on my computer, but I muted myself.

**Kaitlyn Wilkinson** [00:00:22]: I can hear you.

**Kaitlyn Wilkinson** [00:00:25]: Okay.

**Kaitlyn Wilkinson** [00:00:27]: And you can share the screen.

**Kaitlyn Wilkinson** [00:00:30]: Yeah.

**Kaitlyn Wilkinson** [00:00:32]: All right.

**Kaitlyn Wilkinson** [00:00:32]: can share.

**Kaitlyn Wilkinson** [00:00:33]: Let me share.

**Kaitlyn Wilkinson** [00:00:33]: Okay.

**Kaitlyn Wilkinson** [00:00:34]: I'll boot out.

**Kaitlyn Wilkinson** [00:00:38]: You have to come over here.

**William Peare** [00:00:43]: Come around.

**Jorn Reger** [00:00:49]: Come on.

**William Peare** [00:00:54]: Come It's okay.

**William Peare** [00:00:57]: Come over here.

**William Peare** [00:00:58]: Come on.

**William Peare** [00:00:59]: All right.

**William Peare** [00:01:01]: No, around.

**William Peare** [00:01:02]: Come on, please.

**William Peare** [00:01:05]: Are you guys with me?

**Kaitlyn Wilkinson** [00:01:14]: Yeah.

**William Peare** [00:01:15]: Oh, I was like, it's all silent.

**William Peare** [00:01:18]: Okay, it looks like the report builder.

**William Peare** [00:01:21]: One sec.

**William Peare** [00:01:22]: This is like three times that.

**Jorn Reger** [00:01:26]: Yeah, that's bad.

**William Peare** [00:01:28]: It's not bad.

**Jorn Reger** [00:01:31]: Who's in here?

**Jorn Reger** [00:01:31]: Are you in the meeting?

**Jorn Reger** [00:01:36]: Oh, I get it.

**Jorn Reger** [00:01:37]: get it.

**Jorn Reger** [00:01:38]: one sec.

**Jorn Reger** [00:01:40]: Just leave the meeting.

**Jorn Reger** [00:01:45]: Okay, let's, one sec, let me get to...

**Jorn Reger** [00:01:47]: Have you guys tried that thing?

**Jorn Reger** [00:01:51]: No, it's not currently being tried.

**Jorn Reger** [00:01:56]: Okay, is that better?

**William Peare** [00:01:58]: Yes.

**William Peare** [00:01:59]: No echo.

**William Peare** [00:01:59]: Yeah.

**William Peare** [00:02:00]: Okay.

**William Peare** [00:02:00]: Much, much better.

**Jorn Reger** [00:02:03]: Okay.

**Jorn Reger** [00:02:04]: All right.

**Jorn Reger** [00:02:05]: I'm screen sharing to the TV.

**Jorn Reger** [00:02:09]: Can I screen share in here as well?

**Jorn Reger** [00:02:11]: I guess you're looking at your own thing.

**Jorn Reger** [00:02:13]: So, okay.

**Jorn Reger** [00:02:14]: What do we, what do we want to look at?

**William Peare** [00:02:17]: I don't really need to look at anything.

**William Peare** [00:02:19]: I just need to review.

**William Peare** [00:02:20]: Okay.

**William Peare** [00:02:21]: What I have.

**William Peare** [00:02:22]: So it does look like I can build reports on commission.

**William Peare** [00:02:27]: So I'll play with that and see what I can get in terms of like, does each one of them get a dashboard?

**William Peare** [00:02:31]: How does that work?

**William Peare** [00:02:35]: Um, just for our viewability, seems like there, there is some functionality there.

**William Peare** [00:02:42]: I don't know how great it's going be, but I will play with it and I will, I will get that figured out.

**William Peare** [00:02:49]: Um, on the job level, do I have Quincy with me?

**Jorn Reger** [00:02:54]: No, he wouldn't answer the phone.

**William Peare** [00:02:55]: But what have we got so far for job complaints?

**William Peare** [00:03:00]: So I'm going to go through Peter's Slack list.

**William Peare** [00:03:02]: That way Fathom can note them down.

**William Peare** [00:03:03]: I got self-generated being a thing.

**William Peare** [00:03:06]: Okay.

**William Peare** [00:03:06]: I'll have to look at the commissions thing and see if there's any way to stop them.

**William Peare** [00:03:11]: But essentially how it works is you make a commission.

**William Peare** [00:03:13]: There's not really like commissions that are dependent on other things.

**William Peare** [00:03:18]: I can see if there's a workflow that removes the commissions, but they're pretty limited.

**William Peare** [00:03:24]: Essentially what's going to happen is I'll share this really quick so you guys can see it.

**William Peare** [00:03:35]: You guys can see me.

**William Peare** [00:03:36]: Yeah.

**William Peare** [00:03:38]: So every job automatically has the commissions in there like so.

**William Peare** [00:03:49]: Profit tracker commissions.

**William Peare** [00:03:52]: That one needs to get deleted.

**William Peare** [00:03:55]: Okay.

**William Peare** [00:03:56]: Self-gen washout front end.

**William Peare** [00:03:57]: We market as paid once we pay it.

**William Peare** [00:04:00]: How much we paid the day we paid, centrally.

**William Peare** [00:04:03]: So I can do a report that shows ones that need to be paid, pay them, mark them as paid.

**William Peare** [00:04:09]: That's kind of the process.

**William Peare** [00:04:11]: So self-gen, we could have a property that is yes or no, and when you're paying commissions, you just check the property.

**William Peare** [00:04:18]: I do not think this is going to have any kind of ability to make that commission generate based on that property, though.

**William Peare** [00:04:30]: I would do that, then.

**William Peare** [00:04:32]: Yeah, so I think it's just going to be part of the payroll process is when you're paying, you check its status, where it came from.

**William Peare** [00:04:38]: If it's self-gen, you apply it.

**William Peare** [00:04:40]: I think that's probably kind of what we're at.

**William Peare** [00:04:43]: And then we need to look, because we had kind of a tiered system.

**William Peare** [00:04:46]: So self-gen being a flat 2%, yeah.

**William Peare** [00:04:56]: mean, there's a couple of ways we could broach the The tiered system just gets paid out.

**Jorn Reger** [00:05:00]: When it gets hit, so it doesn't need to be.

**William Peare** [00:05:02]: Right, so that's just kind of, we do like a quarterly review, look at their numbers, and it gets paid out, right?

**William Peare** [00:05:09]: Yeah.

**Jorn Reger** [00:05:10]: Okay, then that's kind of a non-issue.

**William Peare** [00:05:11]: We can just run their sales numbers.

**William Peare** [00:05:13]: But we'll put that field in there so they can mark self-gen, yes or no.

**William Peare** [00:05:18]: I want.

**Jorn Reger** [00:05:18]: Can we make it, is this maybe a problem?

**Jorn Reger** [00:05:23]: Could they make themselves a self-gen commission?

**Jorn Reger** [00:05:27]: I am Pete, I've sold a self-gen job.

**William Peare** [00:05:29]: are always in there.

**William Peare** [00:05:31]: Always.

**William Peare** [00:05:33]: So all they could do technically is mark it as paid, but that doesn't actually pay them.

**William Peare** [00:05:37]: So, I mean, they could mark it as paid, but the commission's always there.

**Jorn Reger** [00:05:42]: Yeah, but, so, I sell a job, I get a commission, or I get a commission generated based on your calculation, but you're saying the self-gen, commission, that's all separate?

**William Peare** [00:05:55]: It...

**William Peare** [00:05:56]: The commission just generates, like, I just...

**William Peare** [00:06:00]: put in the rules, like the commission is 2%, it's called front-end.

**William Peare** [00:06:04]: The commission is, it doesn't really get triggered by anything.

**William Peare** [00:06:08]: There's not, it doesn't, you know, like it doesn't really.

**William Peare** [00:06:12]: But how does it know the amount?

**William Peare** [00:06:14]: I tell it it's 2% of the planned revenue.

**William Peare** [00:06:17]: Like you tell it that portion.

**William Peare** [00:06:19]: Okay, sure.

**Jorn Reger** [00:06:20]: I mean, let's look at the same deal, one of the test ones.

**Jorn Reger** [00:06:25]: You're saying that there's like an unassigned commission before the job gets sold?

**William Peare** [00:06:28]: No, so contract sent, no commissions.

**William Peare** [00:06:32]: The trigger where I make it turn on, oh, so I guess maybe depending on that, let me see really quick.

**William Peare** [00:06:40]: My automations, automations.

**William Peare** [00:06:51]: Okay, commission, commission, commission, commission, commission, commission, send production.

**William Peare** [00:07:03]: Yeah, I think it's default.

**William Peare** [00:07:05]: It's just when it's sold.

**William Peare** [00:07:06]: I don't think I had to make one decision.

**Jorn Reger** [00:07:08]: You're saying that it defaults and builds a 2% because you put the calculation in there.

**Jorn Reger** [00:07:13]: So my name is Pete.

**Jorn Reger** [00:07:15]: I have sold a job and the commission then assigns itself to me.

**William Peare** [00:07:21]: It says this job has a Well, you can pick if it goes unassigned and you have to assign it or if it goes to the sales rep.

**William Peare** [00:07:26]: Those are your two options.

**Jorn Reger** [00:07:27]: Okay, so you've assigned it to Pete.

**Jorn Reger** [00:07:30]: So now Pete sees his commission.

**Jorn Reger** [00:07:32]: Can Pete manually add another commission?

**William Peare** [00:07:38]: It would probably depend on his privileges.

**William Peare** [00:07:40]: Let's go look.

**William Peare** [00:07:41]: I have admin privileges, so I would assume I'm able to.

**William Peare** [00:07:44]: I don't know.

**William Peare** [00:07:45]: Yeah, so what would that look like if you could?

**William Peare** [00:07:47]: Let me go.

**William Peare** [00:07:49]: Test, test, profit tracker, commissions, add commission.

**William Peare** [00:07:55]: Yeah, I can.

**William Peare** [00:07:57]: You're going to have to check it from your end and see.

**William Peare** [00:08:00]: You know, I'm also all admin, but you could, in theory, you'd have to name it.

**William Peare** [00:08:07]: So, I mean, it would have a duplicate name to one of the others.

**William Peare** [00:08:11]: You can see, like, front-end, wash-out, self-gen, live there, this unassigned, I must have accidentally clicked save on that.

**William Peare** [00:08:16]: So that needs to get deleted from the calculation.

**William Peare** [00:08:19]: These are unassigned because there wasn't a salesperson when it was made or because test-test doesn't have a salesperson.

**William Peare** [00:08:24]: But he'd have to label what it is.

**William Peare** [00:08:26]: So it'd be a duplicate of one of the things.

**Jorn Reger** [00:08:27]: So type in, like, chance self-gen.

**William Peare** [00:08:34]: Oh, you're saying that they would go and put this in when it applied?

**William Peare** [00:08:39]: Yeah.

**Jorn Reger** [00:08:40]: Yes, I think they would be able to do that if they had the proper privileges.

**Jorn Reger** [00:08:45]: But then we'd potentially have, but I guess, I'm thinking, like, someone could basically just say, hey, this was a self-gen job.

**Jorn Reger** [00:08:52]: Who reviews that it was a self-gen job, but.

**William Peare** [00:08:57]: I mean, really not much different than them marking.

**William Peare** [00:09:00]: The self-gen property, realistically, it kind of ends up as the same thing.

**William Peare** [00:09:03]: Yeah, exactly.

**Jorn Reger** [00:09:04]: So basically, if you self-gen a job, it's your responsibility to put your self-gen commission in.

**Jorn Reger** [00:09:12]: Which was the same as before.

**William Peare** [00:09:13]: I mean, before they just marked the property.

**William Peare** [00:09:15]: But yeah, I think that's pretty reasonable.

**William Peare** [00:09:18]: They just go in there and type self-gen.

**William Peare** [00:09:22]: Can you save that and then go to it?

**Jorn Reger** [00:09:24]: Can you create another commission and write in the same thing just to make sure that it doesn't like, Oh, that commission already exists.

**William Peare** [00:09:39]: It doesn't care.

**Jorn Reger** [00:09:41]: it doesn't tell you that you can't add it because it already exists.

**Jorn Reger** [00:09:45]: Okay.

**William Peare** [00:09:48]: It doesn't like that nature.

**William Peare** [00:09:50]: And then it just lives there.

**William Peare** [00:09:52]: And then it's up to us as much.

**William Peare** [00:09:54]: And then it's marked.

**Jorn Reger** [00:09:55]: So your screen is like tiny in a sense.

**Jorn Reger** [00:09:57]: So then it just marks it as unpaid.

**Jorn Reger** [00:10:00]: Yeah, it just puts it in there, it's unpaid, and then we have to.

**Jorn Reger** [00:10:03]: And you were saying that you can probably build a report off of commissions unpaid per person.

**William Peare** [00:10:10]: Yes, it appeared like commissions were reportable.

**William Peare** [00:10:14]: They're not automatable.

**William Peare** [00:10:15]: There's no automation.

**William Peare** [00:10:16]: But it does appear like when I go to insights, it does look like I could, so far the screen shows nothing, but I just assigned two to myself.

**William Peare** [00:10:26]: now maybe it'll, wow, if this could just load.

**William Peare** [00:10:32]: Insights.

**Jorn Reger** [00:10:35]: No, but I'll you in.

**Jorn Reger** [00:10:37]: There's no way to make a self-gen commission automatically.

**Jorn Reger** [00:10:42]: So what we're going to have to do is when they sell a self-gen, they have to go to the commissions and say, Pete self-gen, 2% and put it in basically themselves.

**Jorn Reger** [00:10:54]: And then it'll show unpaid.

**Jorn Reger** [00:10:55]: And I guess we could put that as a payroll thing that you and Chance will.

**Jorn Reger** [00:11:00]: Look at it to be like, let's just every once in a while spot check and make sure they were self-gen.

**Jorn Reger** [00:11:06]: Because in theory, Peter could just type in every single job and call it self-gen.

**Jorn Reger** [00:11:11]: But they could also check the box and hubspot, so there really wasn't a safeguard against that anyway.

**William Peare** [00:11:17]: No, there's really not much of way to deal with it unless you're going and checking where the lead came from.

**William Peare** [00:11:24]: So these are just kind of their default board.

**William Peare** [00:11:27]: But if I go to classic reports, that's where you actually build reports.

**Jorn Reger** [00:11:34]: Yeah.

**Jorn Reger** [00:11:35]: One of them is commission paid.

**William Peare** [00:11:37]: Let's create a report, create one.

**William Peare** [00:11:43]: I want to create one based off commissions.

**William Peare** [00:11:47]: This is just me.

**William Peare** [00:11:51]: You know, I'm going to have to play with this because I don't.

**Jorn Reger** [00:11:58]: Sure.

**Jorn Reger** [00:11:58]: It's not.

**William Peare** [00:12:00]: It's an amazing, amazing system, in a sense.

**Jorn Reger** [00:12:07]: I would call them, because they might have something set up for that already that we're just not seeing.

**William Peare** [00:12:12]: Yeah, because this is only for paid commissions, not to be paid.

**Jorn Reger** [00:12:19]: Yeah, there's got to be something for that, because they have thousands of roofers that work on how do you know?

**William Peare** [00:12:24]: Yeah, exactly.

**Jorn Reger** [00:12:25]: They can't annually be paying every certain, every literal commission every time it comes through.

**William Peare** [00:12:31]: Unless they're going to me back recently and let me know his time slots so I can, he's got time as of Wednesday.

**William Peare** [00:12:38]: I have a doctor's appointment with Ariel on Wednesday.

**William Peare** [00:12:42]: Ariel, what time is your appointment Wednesday?

**William Peare** [00:12:45]: Oh, she's canceling it.

**William Peare** [00:12:47]: Yeah, so I can do a morning.

**William Peare** [00:12:48]: What time is Ben coming with his, you won't know until Wednesday morning.

**William Peare** [00:12:55]: Wednesday.

**William Peare** [00:12:57]: Okay.

**William Peare** [00:12:59]: All those take a $650.

**William Peare** [00:13:00]: 15, crack of dawn, that should be safe.

**William Peare** [00:13:06]: I'll follow up with him on the commission stuff.

**William Peare** [00:13:10]: Wednesday morning.

**Jorn Reger** [00:13:11]: The inside sales, the inside sales property in the playbook, can we make that tie to the commissions?

**William Peare** [00:13:19]: We don't even need to really, it would just have to be a little clunky, because the best we can really do is put it to unassigned.

**William Peare** [00:13:31]: You can't, you can't assign them to anyone except for the salesperson or, hold on, let me look what the other option was.

**William Peare** [00:13:42]: It's pretty limited.

**William Peare** [00:13:45]: It's unassigned or salesperson.

**William Peare** [00:13:49]: That's it.

**William Peare** [00:13:50]: So we can put one that's unassigned all the time and just call it inside sales commission.

**William Peare** [00:13:55]: And then we need to check every time we're doing payroll who the inside sales was and if it applies.

**William Peare** [00:14:00]: Kind of annoying, but sort of.

**William Peare** [00:14:04]: It's always going to be Quincy.

**William Peare** [00:14:05]: There is no other inside sales.

**William Peare** [00:14:08]: Yeah.

**Jorn Reger** [00:14:08]: It's just then, does it generate commissions for every single deal that's sold, including yours?

**Jorn Reger** [00:14:15]: It generates them.

**William Peare** [00:14:16]: You don't have to pay them.

**William Peare** [00:14:18]: And that being said, I think if I get this just off the ground and we're happy with it, I think we need to build out a coded scaffolding that's doing this stuff for us.

**William Peare** [00:14:27]: Because through webhooks, it could definitely come in and like, it will do that stuff off properties that way.

**William Peare** [00:14:34]: It just natively does not have really any ability to do.

**Jorn Reger** [00:14:38]: So why don't you, for your note taker, ask JobMembus about how to track commissions for regular people and how to make, if possible, specific commissions for, in this case, Quincy for inside sales.

**Jorn Reger** [00:14:56]: Got it.

**Jorn Reger** [00:14:57]: I'm sure it caught that.

**William Peare** [00:14:58]: does very well.

**William Peare** [00:14:58]: Yeah, I'm sure it got that.

**Jorn Reger** [00:15:00]: So ask about those two things.

**Jorn Reger** [00:15:02]: Okay.

**William Peare** [00:15:03]: I am going to the other thing I noticed when I'm bringing in jobs is a lot of the stuff in the job playbook is pretty redundant because it doesn't actually do anything.

**William Peare** [00:15:14]: They're just fields that go in there for notes.

**William Peare** [00:15:16]: Like the first name, last name, field I put in, they just, they don't do anything besides put it in the field.

**William Peare** [00:15:23]: They don't name the job that it doesn't do anything.

**William Peare** [00:15:25]: And there's not any, this has no ability to like copy properties.

**William Peare** [00:15:29]: I can't copy that to make it the job name.

**William Peare** [00:15:31]: It just doesn't work like that.

**William Peare** [00:15:35]: Yeah.

**William Peare** [00:15:36]: So.

**William Peare** [00:15:37]: Okay.

**Jorn Reger** [00:15:37]: One, one thing kind of on that, that Quincy and I noticed, like if you press that white plus button and add a job, it doesn't have the like lead intake questions, basically.

**Jorn Reger** [00:15:48]: Not until I'm going to like contact.

**William Peare** [00:15:51]: So if I went here.

**William Peare** [00:15:52]: having to make a contact before they have to do You cannot have a deal or job without a contact.

**William Peare** [00:15:57]: You can't.

**William Peare** [00:15:58]: It won't allow it.

**William Peare** [00:15:59]: There's no way.

**William Peare** [00:16:00]: Do to combine those two?

**Jorn Reger** [00:16:01]: Because he has to go to like two different spots to do a phone call now.

**Jorn Reger** [00:16:06]: This is how you have to do it.

**William Peare** [00:16:07]: You have to run through this part first.

**William Peare** [00:16:09]: Unless they already have a contact, you can make it from the contact level and get straight to that.

**William Peare** [00:16:13]: But unless they have a contact, you have to make a contact first, and then it opens the playbook immediately.

**William Peare** [00:16:19]: So like it was that quick.

**William Peare** [00:16:22]: So you fill out that form that you're on, and then what?

**William Peare** [00:16:25]: You create a job?

**William Peare** [00:16:26]: right here.

**William Peare** [00:16:27]: Like where are the job follow playbook questions?

**Jorn Reger** [00:16:28]: Right here.

**Jorn Reger** [00:16:31]: Can I not see them?

**Jorn Reger** [00:16:32]: Once I can go to my screen.

**William Peare** [00:16:34]: Here, I'll go back.

**William Peare** [00:16:35]: So once you push click, add a job, as soon as you fill out the customer stuff, it will open up the next part.

**William Peare** [00:16:48]: Save and continue.

**William Peare** [00:16:49]: Instead of trying it.

**William Peare** [00:16:51]: And then you're there.

**William Peare** [00:16:54]: I'm not seeing it.

**Jorn Reger** [00:16:56]: Can I see?

**Jorn Reger** [00:16:56]: Maybe you have to put an address too?

**Jorn Reger** [00:16:58]: I can't see what you're

**William Peare** [00:17:00]: Seeing, Jorn, you want to share your screen?

**William Peare** [00:17:01]: Yeah.

**Jorn Reger** [00:17:02]: Let me share this.

**Jorn Reger** [00:17:07]: This one.

**Jorn Reger** [00:17:11]: So if I'm, let me cancel out this.

**Jorn Reger** [00:17:14]: If I press on this button here and I say create a job or add a job, you're saying when I fill out this info, it should come up with the questions?

**William Peare** [00:17:24]: As soon as you push save and continue, yes.

**William Peare** [00:17:27]: It doesn't make you leave the screen.

**William Peare** [00:17:29]: Oh, so the save and continue gets you to the second That makes the contact, which is then linked to the job you're making.

**William Peare** [00:17:36]: There's no workaround.

**Jorn Reger** [00:17:39]: Okay, so I think what they were doing.

**William Peare** [00:17:41]: file playbook questions in the contact, but this has no ability to copy properties.

**William Peare** [00:17:46]: I think what they were doing is they were here at contact.

**Jorn Reger** [00:17:49]: They were creating a contact and then trying to create a Yes, yeah, don't do that.

**William Peare** [00:17:54]: Just click create a job and make it always from the job level and then it'll force you to make the contact.

**William Peare** [00:18:00]: can ask the contact questions, and then it'll immediately push you into the jobs, like the playbook.

**William Peare** [00:18:04]: So do that for all homeowners.

**Jorn Reger** [00:18:07]: If we have a Standcraft job, go to the contact for Standcraft to add a job.

**William Peare** [00:18:12]: Yes, or you can do it from the, if you go click on the job thing, as soon as you type in Standcraft, you wouldn't have to make a new contact.

**William Peare** [00:18:18]: It would show you a list of contacts you match, and you can just add that to existing contact.

**William Peare** [00:18:22]: Yeah, okay.

**William Peare** [00:18:23]: Yep.

**William Peare** [00:18:24]: Okay, that's great.

**Jorn Reger** [00:18:26]: And then we're going to make sure that our syntax for jobs is the job name, not the, not the customer's name, basically, unless it's a homeowner.

**Jorn Reger** [00:18:34]: Yes.

**William Peare** [00:18:37]: And then, so right here, we need to essentially override, override this.

**William Peare** [00:18:48]: So on job details, it's automatically going to try and make the job name contact plus job number.

**William Peare** [00:18:54]: You need to override that and write in whatever you want.

**William Peare** [00:18:57]: Dusty, you have to do that, or it's going to be called the contact.

**William Peare** [00:19:01]: Yeah, sorry.

**Jorn Reger** [00:19:02]: Let me try to do that on my end because it's so small I can't really see yours.

**Jorn Reger** [00:19:05]: So you're saying, oh, there's a display name.

**Jorn Reger** [00:19:07]: So I'm going to say the first name, last name is Jorn Reger, but I want the display name to Jorn.

**William Peare** [00:19:17]: Nope, nope, nope, nope, nope, nope.

**William Peare** [00:19:20]: I mean, yes, you can do that, but that's for the contact's display name.

**William Peare** [00:19:23]: yeah, that's for the contact.

**William Peare** [00:19:24]: Okay.

**William Peare** [00:19:24]: Yeah, so you haven't even got to the job.

**William Peare** [00:19:27]: Okay.

**William Peare** [00:19:28]: So if you clicked Jorn, yeah, there you are.

**William Peare** [00:19:30]: Now on the job name, the top thing, you have to override it because it's automatically going to default to your name.

**William Peare** [00:19:36]: Okay, so this is where I would say I want this actually to be called Jorn's Chicken.

**Jorn Reger** [00:19:41]: Correct.

**Jorn Reger** [00:19:42]: Okay.

**William Peare** [00:19:44]: So that's easy.

**William Peare** [00:19:45]: Then you would scroll down into the playbook.

**William Peare** [00:19:48]: Yeah, now I'm seeing it.

**Jorn Reger** [00:19:49]: Yeah, okay, great.

**Jorn Reger** [00:19:52]: Okay.

**William Peare** [00:19:54]: That's good.

**William Peare** [00:19:55]: Okay.

**Jorn Reger** [00:19:57]: All right.

**Jorn Reger** [00:19:57]: And then Quincy's coming back.

**Jorn Reger** [00:19:58]: I'll tell him.

**Jorn Reger** [00:20:02]: Okay, so what you do for a new job to make them work is you do press on this white button, and it'll force you, I think you figured this out already, it'll force you to make a contact or match to an existing contact, and then you get to the questions for job-specific stuff.

**Jorn Reger** [00:20:23]: That's not what I figured out.

**Jorn Reger** [00:20:24]: Oh, what?

**Jorn Reger** [00:20:25]: Save and continue, and then I'll say So here, I'll just do it again.

**Jorn Reger** [00:20:28]: So I add a job, and it's me.

**William Peare** [00:20:32]: Yeah.

**William Peare** [00:20:33]: And then- yeah.

**Jorn Reger** [00:20:34]: You can just put in the name and the number, and then it will- Yeah.

**Jorn Reger** [00:20:37]: And then I'm going to- with this.

**Jorn Reger** [00:20:39]: Correct.

**Jorn Reger** [00:20:40]: But if you make a contact now- You can click save and continue, it takes you- Or honestly, I didn't have to press save and continue, I just made it match this customer, or then you would press save and continue.

**Jorn Reger** [00:20:52]: Now it's going to ask you all the intake questions.

**Jorn Reger** [00:20:57]: Yeah.

**Jorn Reger** [00:20:58]: Yeah.

**Jorn Reger** [00:20:58]: Okay.

**Jorn Reger** [00:20:59]: Sorry, what did you-

**Jorn Reger** [00:21:15]: So then is it saving the email and stuff that you put in later in the address to the contact and just go back and put them in.

**Jorn Reger** [00:21:33]: But it's just, as far as workflow goes, when you're intaping someone, that's just what I think is.

**Jorn Reger** [00:21:37]: Okay, that's great.

**Jorn Reger** [00:21:41]: Okay, sweet.

**Jorn Reger** [00:21:44]: That's good.

**Jorn Reger** [00:21:48]: Yeah, sure.

**Jorn Reger** [00:21:49]: Okay.

**Jorn Reger** [00:21:51]: That's working.

**William Peare** [00:21:52]: You're going to get on the commissions thing.

**William Peare** [00:21:55]: Hold on, Clover.

**William Peare** [00:21:56]: I can hear you guys with my AirPod.

**Jorn Reger** [00:22:00]: Um, what were some of the other questions that like Peter had?

**Jorn Reger** [00:22:03]: So where are we at with phone recordings?

**Jorn Reger** [00:22:10]: Yeah, he was doing something, I think you've been inside now.

**Jorn Reger** [00:22:15]: You probably hear us.

**Jorn Reger** [00:22:16]: He was doing something with Zapier to bring them in, but I think he's still working on it because I think it was like giving him, it was like trying to do it three times or like making disagreements of stuff.

**Jorn Reger** [00:22:28]: Um, but yeah, Peter definitely asked about having call recordings in JobNimbus because he likes to know the heat on the way to a job.

**Jorn Reger** [00:22:37]: Yes.

**William Peare** [00:22:37]: And that one, let me pull up Zapier.

**William Peare** [00:22:43]: Okay.

**William Peare** [00:22:44]: I have four things in Zap right now.

**William Peare** [00:22:49]: Let's test these Zappies.

**William Peare** [00:22:52]: Okay.

**William Peare** [00:22:52]: So we have the call answer to create contact that's on.

**William Peare** [00:22:57]: It hasn't failed.

**William Peare** [00:22:58]: Uh, JobNimbus.

**William Peare** [00:23:00]: Job to air call contact on, sometimes triggering a failure, so I need to figure out what that is.

**William Peare** [00:23:05]: The signed estimate I turned off, it works perfectly well, but until we make the field that is an amount and make them put it in, it's not going to tell us the amount.

**William Peare** [00:23:18]: What's going on, Errol?

**William Peare** [00:23:22]: Do you want me to go check on her?

**William Peare** [00:23:25]: I'll be back, guys.

**William Peare** [00:23:27]: Okay.

**William Peare** [00:23:28]: I'll be back.

**William Peare** [00:23:29]: Be strong.

**Jorn Reger** [00:23:29]: What other, what other issues or sort of fixes have you run into that you'd like, you know, you've probably done the most amount of intakes and stuff?

**Jorn Reger** [00:23:40]: Yeah.

**Jorn Reger** [00:23:42]: Are you seeing things?

**Jorn Reger** [00:23:42]: that sucks is, for new con, it always puts the contact's name as the name of the team, which is going to get...

**Jorn Reger** [00:23:54]: You can't override that?

**Jorn Reger** [00:23:56]: Maybe you can.

**Jorn Reger** [00:23:58]: But...

**Jorn Reger** [00:23:58]: I tried a couple of the...

**Jorn Reger** [00:24:00]: things to override it, like different fields, but you couldn't, like when you were in here, then like, you only get us the option to read that too.

**Jorn Reger** [00:24:08]: You can override it once it's made.

**Jorn Reger** [00:24:10]: You can do that.

**Jorn Reger** [00:24:12]: But look right here.

**Jorn Reger** [00:24:12]: So I've made it the job name.

**Jorn Reger** [00:24:15]: Can you not change this?

**Jorn Reger** [00:24:17]: I typed the job name is what I wanted to say.

**Jorn Reger** [00:24:20]: Like a good example of this is go to the search bar and search Calgary Court, like C-A-L-G-A-R-Y.

**Jorn Reger** [00:24:31]: Zachary Bolt's recult, because it's the contact, that's the contact for that job.

**Jorn Reger** [00:24:37]: So the only way to change this that I've found is you go into it and edit it once it's made.

**Jorn Reger** [00:24:44]: So you can make it and then you can edit it and change it to Calgary Court paper or something.

**Jorn Reger** [00:24:50]: But I put that one, when I filled it out, I filled out the job name as Calgary Court construction and yeah.

**Jorn Reger** [00:25:00]: Didn't do that.

**Jorn Reger** [00:25:01]: annoying.

**Jorn Reger** [00:25:01]: That's the role as the name.

**Jorn Reger** [00:25:07]: That's the engine part for the content.

**Jorn Reger** [00:25:10]: Yeah, right.

**Jorn Reger** [00:25:11]: So then, so if I match this, you're saying that when you fill out the job name, it doesn't, the job name will automatically use the primary context display name combined with the job number.

**Jorn Reger** [00:25:25]: So you're saying that when I say this is Jorn's Chicken Coop, it does not actually call this Jorn's Chicken Coop, because it probably won't let me.

**Jorn Reger** [00:25:36]: It will continue to say Jorn Reger.

**William Peare** [00:25:40]: That's really annoying.

**Jorn Reger** [00:25:42]: So you're saying it won't override?

**Jorn Reger** [00:25:45]: No, he's saying, he's saying he tricks it, but manually.

**Jorn Reger** [00:25:51]: Yeah.

**Jorn Reger** [00:25:51]: Like he was saying Calgary Court just is in there as job 1673, Zachary Bolt.

**Jorn Reger** [00:25:59]: about Herock was-28 didn't fixed wants

**Jorn Reger** [00:26:04]: So that's annoying.

**William Peare** [00:26:08]: But if you override the job name when you're making it, does the override not stick?

**Jorn Reger** [00:26:14]: That's what he's saying, yeah.

**Jorn Reger** [00:26:16]: It happened for a Sandcraft one as well.

**Jorn Reger** [00:26:19]: Try it.

**Jorn Reger** [00:26:20]: Create another job.

**Jorn Reger** [00:26:21]: Yeah, I'm going through it now.

**William Peare** [00:26:23]: Hopefully I'm doing something wrong.

**William Peare** [00:26:25]: Okay, I'm looking.

**William Peare** [00:26:27]: Job name, chance pair, or contact, chance pair, testee, chancerson.

**William Peare** [00:26:36]: All right, now I'm to spread all these details.

**William Peare** [00:26:40]: My name, my name, my address.

**William Peare** [00:26:44]: So you're saying like here at Dolores Depot, you just, you renamed it.

**William Peare** [00:26:50]: Those are the ones that we moved into when we did the question.

**Jorn Reger** [00:26:55]: All right, this is your 620.

**Jorn Reger** [00:27:00]: I know, Mom, I know.

**Jorn Reger** [00:27:02]: Some of those ones that came over, a lot of them were drafted.

**Jorn Reger** [00:27:06]: Dad, get over here.

**William Peare** [00:27:10]: What do you need?

**William Peare** [00:27:11]: throwing up.

**William Peare** [00:27:11]: Mom's throwing up?

**William Peare** [00:27:12]: What do you, I can't do anything for her, but did ask for me to help?

**William Peare** [00:27:16]: Yes, she's asking me to help.

**William Peare** [00:27:19]: Okay, okay.

**William Peare** [00:27:22]: Good, this is going so good.

**William Peare** [00:27:26]: This is going well on my end.

**William Peare** [00:27:28]: Uh, Testy, Chanceerson, let me see.

**William Peare** [00:27:33]: Testy, Chanceerson, Chance, uh, we can't find it yet, but, yeah, I don't know.

**William Peare** [00:27:47]: I'm going to have to do some more testing on that.

**William Peare** [00:27:49]: I would assume that I'm writing the job name.

**William Peare** [00:27:51]: Testy, Chanceerson, Chance, would it have a job name field if it's just going to use first name last time?

**Jorn Reger** [00:28:00]: Unless it is for it is naming a property job name something but it's not what the like the job on the board is displaying as.

**Jorn Reger** [00:28:12]: That's what I feel like is going on.

**Jorn Reger** [00:28:15]: So we're somewhere in there it's called Calgary Court but it's not the job name that gets displayed on the card.

**Jorn Reger** [00:28:23]: Yeah.

**Jorn Reger** [00:28:24]: Just somewhere.

**Jorn Reger** [00:28:26]: Yeah.

**Jorn Reger** [00:28:27]: So for all of like chances.

**Jorn Reger** [00:28:29]: Yeah.

**Jorn Reger** [00:28:30]: In job business.

**Jorn Reger** [00:28:31]: Are we having to click on to new construction and then create a job from there?

**Jorn Reger** [00:28:35]: I think you can pick what pipeline to put it in.

**Jorn Reger** [00:28:38]: Because it only gives us retail.

**Jorn Reger** [00:28:45]: So if we did create a job from here then we'd put it into this pipeline.

**Jorn Reger** [00:28:50]: I'm not sure.

**Jorn Reger** [00:28:52]: Try it.

**Jorn Reger** [00:28:52]: Yeah.

**Jorn Reger** [00:28:53]: Yeah.

**Jorn Reger** [00:28:53]: That's right.

**Jorn Reger** [00:28:54]: Yeah.

**Jorn Reger** [00:28:54]: Can I set up an appointment for you?

**Jorn Reger** [00:28:56]: Yeah.

**Jorn Reger** [00:28:57]: Yeah.

**Jorn Reger** [00:28:58]: Yeah.

**Jorn Reger** [00:29:12]: Okay, kids, I'm going to have to reconvene on this tomorrow.

**William Peare** [00:29:14]: Things are going really south here.

**William Peare** [00:29:16]: Okay, sounds good.

**Jorn Reger** [00:29:17]: We're going to go look and see what we can figure out.

**William Peare** [00:29:19]: Yeah, if you guys could make some notes on anything you have, I'll start knocking it out.

**Jorn Reger** [00:29:25]: Thanks, guys.