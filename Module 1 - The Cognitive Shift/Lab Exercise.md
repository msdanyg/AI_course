# Module 1: The Cognitive Shift
## Lab Exercise: The Water Glass Challenge

**Duration:** 25-30 minutes
**Tools Required:** Claude (claude.ai) or ChatGPT

---

## Objective

Experience the Water Glass Effect firsthand, then practice restructuring prompts to focus AI attention. By the end of this lab, you'll have concrete evidence of how context structure affects output quality using real ActivTrak scenarios.

---

## Scenario

You're a Customer Success Manager at ActivTrak preparing for a monthly check-in with TalentBridge Staffing, a mid-market recruiting firm with 450 deployed licenses. They've been customers for nearly 3 years and renewal is coming up in Q4. The account has had some friction around HRIS integration and Potential False Activity (PFA) alerts.

You have the following information (provided below):
- A messy internal Slack thread discussing the account
- Recent account notes from Salesforce
- Data from their ActivTrak dashboard

Your task: Generate three talking points for the call that demonstrate value and address their concerns proactively.

---

## Part 1: The Solo Pilot Approach (10 minutes)

### Step 1: Copy the Cluttered Context

Copy the entire block below and paste it into a new Claude conversation:

```
Here's everything I have on the TalentBridge Staffing account. Can you help me prep for my call with them?

Slack thread from yesterday:
---
@leslie.thompson: Hey team - heads up on TalentBridge. Marcus (their IT admin) pinged me about the UKG integration again. Said he's getting frustrated that we promised it months ago and it's still not working right for them. Their renewal is coming up and I'm a little worried.

@tom.jackson: Yeah I've been working with Marcus on this. The sync was supposed to happen over the weekend. I think we're close but no confirmation yet that the PTO data is flowing correctly.

@leslie.thompson: Also unrelated but did anyone submit their expense reports? Finance is on my case about the Austin trip receipts.

@zach.pierce: I just took over this account from Leslie. What's the deal with the PFA alerts? Marcus mentioned something about wanting to scrub historical data?

@tom.jackson: Oh that's a whole thing. They have like a dozen repeat offenders showing false activity - probably hardware jigglers - and they want us to retroactively remove that data from their reports. I told them we'd need to go through product for that.

@leslie.thompson: @zach.pierce - the calendar integration is also still on hold. They have security concerns about the Azure AD permissions we need. It's been tabled twice now. Also can someone cover my Thursday meeting? Doctor appointment.
---

Account Notes (from Salesforce):
- 3-year customer, ~450 licenses (down from 520 after RIF last year)
- They built custom Power BI reports using ActivConnect - their frontline managers use these instead of the portal
- Key contacts: Marcus (IT Admin), Dean (Director of IT), Shaneen (VP Technology)
- Renewal coming Q4, last year required executive intervention from Gabriela to save
- Main pain points: UKG integration for PTO tracking, PFA alert handling, calendar integration on hold
- Wins: Identified employees not working, found underutilized staff, hybrid work compliance tracking

Their Dashboard Metrics (last 6 months):
- Avg Productive Hours/Day: trending slightly down (-4%)
- Active Users: 447
- PFA Alerts: 12 recurring users flagged
- Schedule Adherence: 78% (was 82%)
- Top Apps: Microsoft Teams, Outlook, their internal recruiting platform
- ActivConnect: Heavily used for Power BI integration

Dean mentioned in the last call that they're always comparing us to competitors during renewal to make sure they're "getting good value." Also said he can't tie ActivTrak productivity metrics to actual business outcomes like placements made.

What should I talk about in my call?
```

### Step 2: Review Claude's Response

Note what Claude focuses on:
- [ ] Did it understand the task correctly?
- [ ] Did it clearly separate hypotheses from other commentary?
- [ ] Could you use this response directly in your call prep?
- [ ] Was it concise and to the point?
- [ ] Was it actionable and what you would need for the call?

**Write down your observations:**

```
What worked:


What didn't work:


What did Claude focus on that wasn't helpful:


```

---

## Part 2: The Squadron Leader Approach (10 minutes)

### Step 3: Start a New Conversation

Open a fresh Claude conversation. This time, you'll structure the context like a mission briefing.

### Step 4: Paste the Structured Prompt

```
[ROLE]
You are a Customer Success Manager at ActivTrak, a workforce analytics platform. Your approach follows "Insights, Not Oversight" - you help customers understand work patterns to improve productivity, not to surveil employees.

[CONTEXT]
Account: TalentBridge Staffing (recruiting firm, 450 licenses)
Situation: Monthly check-in call, renewal coming in Q4
Relationship History: 3-year customer, required executive save at last renewal
Key Stakeholder: Dean (Director of IT) - reports to Shaneen (VP Technology)
Account Health: Amber - they provide good feedback but have ongoing friction points

[CURRENT PAIN POINTS]
1. UKG Integration: PTO data not syncing properly; customer frustrated with delays
2. PFA Alerts: 12 users with recurring false activity alerts; customer wants historical data scrubbed but this requires product involvement
3. Calendar Integration: On hold due to Azure AD permission concerns; security team won't approve broad access

[WINS TO REFERENCE]
- Successfully using ActivConnect with custom Power BI dashboards
- Identified employees not working expected hours
- Found underutilized staff and gave them more work
- Tracking hybrid work policy compliance

[METRICS]
- Avg Productive Hours/Day: -4% (6-month trend)
- Schedule Adherence: 78% (down from 82%)
- PFA Alerts: 12 recurring users
- Active Users: 447

[TASK]
Generate exactly three talking points for this call that:
1. Acknowledge a current pain point and provide a status update or path forward
2. Reinforce value they're already getting from ActivTrak
3. Position ActivTrak favorably for the upcoming renewal conversation

[CONSTRAINTS]
- Do not promise features or timelines you cannot confirm
- Frame productivity insights supportively, not as surveillance
- Reference specific data points from their account
- Keep each talking point concise enough to say in 30 seconds

[FORMAT]
### Talking Point [1/2/3]: [Title]
**Key Message:** [1-2 sentences]
**Supporting Data/Context:** [specific reference]
**Transition to Next Topic:** [optional bridge sentence]
```

### Step 5: Compare the Responses

Evaluate the structured response:
- [ ] Are talking points clearly separated and prioritized?
- [ ] Does each reference specific account data?
- [ ] Is the framing consultative ("Insights, Not Oversight")?
- [ ] Could you use these talking points in the actual call?

**Side-by-side comparison:**

| Criteria | Solo Pilot Response | Squadron Leader Response |
|----------|--------------------|-----------------------|
| Stayed on topic | | |
| Used account-specific data | | |
| Addressed pain points appropriately | | |
| Reinforced existing value | | |
| Ready to use in the call | | |

---

## Part 3: Reflection & Stretch Challenge (5-10 minutes)

### Reflection Questions

1. What specific differences did you notice between the two responses?

2. What information from the cluttered prompt did Claude fixate on that wasn't relevant to your call prep?

3. How did the [CONSTRAINTS] section shape Claude's recommendations?

4. Which response could you actually use without significant editing?

### Stretch Challenge: The Renewal Prep

Dean mentioned they compare ActivTrak to competitors at every renewal to ensure "good value." Create a structured prompt to:

1. Generate a value summary that ties ActivTrak usage to business outcomes
2. Prepare responses to likely objections about the integration issues
3. Draft a "why renew" message for Shaneen (VP Technology)

Use the same mission briefing structure:
- [ROLE]
- [CONTEXT]
- [DATA]
- [TASK]
- [CONSTRAINTS]
- [FORMAT]

**Bonus:** Include a [DO NOT INCLUDE] section that explicitly tells Claude what to ignore (like internal team chatter, expense reports, or meeting coverage requests).

---

## Real-World Application

### Your Turn: Apply This to Your Work

Think of a recent situation where you needed AI help with an account or project. Structure a prompt using this framework:

```
[ROLE]
Who should Claude act as?

[CONTEXT]
Account/Project name:
Current situation:
Key stakeholders:
Relationship history:

[DATA]
Relevant metrics or facts:

[TASK]
What specific output do you need?

[CONSTRAINTS]
What should Claude avoid or be careful about?

[FORMAT]
How should the output be structured?
```

---

## Success Criteria

You've completed this lab successfully if you can:

- [ ] Articulate why the first prompt produced scattered results
- [ ] Explain how the structured prompt concentrated Claude's attention
- [ ] Identify at least two specific improvements in the second response
- [ ] Apply the mission briefing structure to an account or project you're working on

---

## Key Takeaway

The same AI, given the same underlying information, produces dramatically different results based on how you structure the context. Squadron Leaders don't have better AI access—they have better prompts.

**ActivTrak Application:** When preparing for customer calls, QBRs, or internal analysis, structure your prompts the way you want the conversation to go. Tell the AI what role to play, what data matters, and what constraints to follow. Your prep time drops and your output quality increases.

---

## Troubleshooting

**If Claude's responses are similar in both cases:**
- Make sure you started a completely new conversation for Part 2
- Check that you copied the full structured prompt including all sections
- Try adding "Follow the format exactly" at the end of the structured prompt

**If Claude asks clarifying questions:**
- This is actually good behavior—it means the AI is trying to focus
- Provide the clarification and note how it improves the output

**If you're short on time:**
- Skip the stretch challenge
- Focus on completing Parts 1 and 2 and the comparison table

**If you work in a non-customer-facing role:**
- The same principles apply to any complex task
- Substitute "customer call" with "project update," "analysis request," or "stakeholder presentation"

---

*Lab complete. Proceed to the Module 1 Quiz when ready.*
