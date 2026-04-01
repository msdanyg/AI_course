# Module 0 Lab Exercise
## Cockpit Configuration & Data Safety Verification

**Objective:** Configure your complete AI toolchain and verify your understanding of data safety protocols.

**Time:** 20-25 minutes

**Prerequisites:**
- ActivTrak enterprise credentials
- Mac computer with admin permissions (for desktop apps)
- Google Workspace account
- Granola account

---

## Part 1: Tool Inventory & Configuration (12 minutes)

### Task 1A: Inventory Your Tools (4 minutes)

Different ActivTrak employees have access to different AI tools. First, identify what you have in each Squadron role:

**Mission Control (Reasoning & Writing):**
- [ ] Claude.ai or Claude Desktop
- [ ] Claude Code (IDE integration)
- [ ] ChatGPT
- [ ] Cursor or GitHub Copilot
- [ ] Other: _____________

**Recon & Radar (Research & Grounding):**
- [ ] Gemini (web or Workspace)
- [ ] Bing AI
- [ ] Google NotebookLM
- [ ] Other: _____________

**Flight Recorder (Meeting Capture):**
- [ ] Granola
- [ ] Chorus.ai
- [ ] Zoom AI summaries
- [ ] Other: _____________

**Specialized Units (your team's tools):**
- [ ] _____________
- [ ] _____________

### Task 1B: Configure Your Mission Control Tool (4 minutes)

Choose your primary reasoning tool (Claude, ChatGPT, etc.) and verify it's working:

1. Log in to your Mission Control tool
2. Verify your account is active and you see any enterprise features
3. Test with this prompt:

```
"Summarize what you can help me with in 3 bullet points."
```

4. Test file upload (if available):
   - Create a simple text file
   - Upload or drag it into the tool
   - [ ] File upload works

Record which tool you're using: ________________

### Task 1C: Configure Your Recon & Radar Tool (2 minutes)

Gemini is available company-wide. Verify it's working:

1. Navigate to [gemini.google.com](https://gemini.google.com)
2. Sign in with your ActivTrak Google Workspace account
3. Test real-time search:

```
"What is ActivTrak's current pricing as shown on their website?"
```

- [ ] Gemini returned current information with web sources

### Task 1D: Identify Your Flight Recorder (2 minutes)

What meeting capture tool do you use? (Granola, Chorus, Zoom AI, etc.)

My Flight Recorder: ________________

Verify:
- [ ] It's connected to your calendar/meetings
- [ ] You can access a recent meeting's transcript or summary
- [ ] You know how to copy/export notes

---

## Part 2: Data Safety Classification (8 minutes)

### Task 2A: Traffic Light Exercise

For each data type below, classify it as **Green**, **Yellow**, or **Red** and explain why.

| Data Type | Zone | Reasoning |
|-----------|------|-----------|
| A customer's email address from Salesforce | | |
| Screenshot of competitor's pricing page | | |
| Your AWS admin password | | |
| Meeting notes from a client call | | |
| A case study draft with customer quotes | | |
| Account usage CSV from ActivTrak analytics | | |
| Internal strategy document about Q1 goals | | |
| API key for a third-party integration | | |

**Answer Key (check after completing):**

<details>
<summary>Click to reveal answers</summary>

| Data Type | Zone | Reasoning |
|-----------|------|-----------|
| Customer email from Salesforce | **Green** | Internal data for analysis; review outputs before external use |
| Competitor pricing screenshot | **Green** | Publicly available; safe to analyze |
| AWS admin password | **Red** | Security credential; never share with any AI |
| Meeting notes from client call | **Green** | Internal documentation; useful for synthesis |
| Case study draft with customer quotes | **Yellow** | Contains customer PII; may need PR review before distribution |
| Account usage CSV | **Green** | Internal analytics; standard analysis use case |
| Internal strategy document | **Green** | Internal documentation; safe for AI analysis |
| API key for integration | **Red** | Security credential; never share with any AI |

</details>

### Task 2B: Scenario Decision

Read each scenario and decide: **Proceed**, **Proceed with Review**, or **Stop**.

**Scenario 1:**
You want to upload a spreadsheet of account names and ARR values to Claude and ask for expansion opportunity analysis.

Your decision: ________________

**Scenario 2:**
You want to paste your Slack bot's API token into Claude to ask for help debugging an integration.

Your decision: ________________

**Scenario 3:**
You want to feed Granola meeting notes into Claude and generate a QBR email draft for a specific customer.

Your decision: ________________

**Scenario 4:**
You want to upload a competitor battle card (internal document) and ask Claude to identify weaknesses in our positioning.

Your decision: ________________

**Answer Key:**

<details>
<summary>Click to reveal answers</summary>

1. **Proceed** - Account names and ARR are Green zone data. Review the output before sharing externally.

2. **Stop** - API tokens are Red zone. Never share credentials with AI tools.

3. **Proceed** - Meeting notes are Green. Just review the email before sending to the customer.

4. **Proceed** - Internal competitive docs are Green. Analysis stays internal unless you share it.

</details>

---

## Part 3: First Squadron Exercise (5 minutes)

Now let's practice using your tools together—a Recon & Radar → Mission Control handoff.

### The Workflow:

1. **In your Recon tool (Gemini, Bing AI, etc.)**, search for:
```
"What are the top 3 workforce analytics competitors to ActivTrak in 2024?"
```

Record the names: ________________

2. **Copy the response** and paste it into your Mission Control tool (Claude, ChatGPT, etc.) with this prompt:

```
<context>
[Paste the research here]
</context>

Based on this competitive research, write 3 bullet points I could use to differentiate ActivTrak in a sales conversation. Focus on our "Insights, Not Oversight" positioning.
```

3. **Review the output** before you would ever use it externally.

Ask yourself:
- Is the information accurate based on what you know?
- Would you send this as-is, or would you edit it?
- Did the AI make any assumptions you'd want to verify?

- [ ] Completed the Recon → Mission Control handoff
- [ ] Reviewed output before hypothetical use

---

## Lab Completion Checklist

**Tool Inventory:**
- [ ] Identified my Mission Control tool(s)
- [ ] Identified my Recon & Radar tool(s)
- [ ] Identified my Flight Recorder tool
- [ ] Primary tools are configured and working

**Data Safety Understanding:**
- [ ] Can classify data into Green/Yellow/Red zones
- [ ] Understand when to proceed vs. stop vs. review
- [ ] Know the "AI drafts, humans send" principle

**Squadron Workflow:**
- [ ] Successfully completed a Recon → Mission Control handoff
- [ ] Reviewed AI output before hypothetical use

---

## Troubleshooting

**Problem:** My Mission Control tool doesn't show enterprise features
- **Solution:** Verify you're signed in with your @activtrak.com email. Check with IT if enterprise access isn't provisioned.

**Problem:** I don't have access to a Mission Control tool
- **Solution:** Request access to Claude or ChatGPT from IT. In the meantime, you can use Gemini for basic tasks.

**Problem:** Gemini doesn't show Workspace integration
- **Solution:** Ensure you're signed into Gemini with your Workspace account, not a personal Google account.

**Problem:** I'm not sure which Flight Recorder my team uses
- **Solution:** Check with your manager. Common options: Granola, Chorus.ai, Zoom AI summaries. All Zoom meetings have AI summaries available.

---

## Reflection Questions

After completing the lab:

1. Which of the three tools do you think you'll use most frequently? Why?

2. What types of data do you work with regularly that fall into the Yellow zone?

3. How does the "AI drafts, humans send" principle change how you might use AI outputs in your role?

**Save your reflections—they'll help contextualize future modules.**

---

**Lab Complete. Proceed to Quiz when ready.**
