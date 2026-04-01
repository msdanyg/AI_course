# Module 5: The Sensory System
## Lab Exercise: The Complete Sensor Array

**Duration:** 30-35 minutes
**Tools Required:** Claude (claude.ai), Gemini (gemini.google.com), Slack

---

## Objective

Practice the complete Squadron sensor workflow: set up data connectors, gather intelligence with Gemini (including Deep Research), process meeting context, leverage Slack AI and synthesize with Claude. You'll build and exercise the full intelligence pipeline.

---

## Scenario

You're an ActivTrak team member preparing for an important cross-functional meeting. Leadership has asked your team to evaluate and recommend a new project management tool, and you need to present a well-researched recommendation. You need to:
1. Check what your team already knows (Slack AI + Connectors)
2. Gather current research on the options (Gemini)
3. Process context from previous discussions (Flight Recorder)
4. Synthesize everything into a recommendation brief (Claude)

---

## Part 0: Supply Lines & Comms Network (8 minutes)

### Step 0A: Explore Data Connectors in Claude

Navigate to [claude.ai](https://claude.ai) and open your settings:

1. Click your profile icon → **Settings** → **Connected Apps**
2. Review which connectors are available (Google Drive, Slack, Gmail, etc.)
3. If not already connected, enable **Google Drive** as your first connector
4. Note which other connectors are available in your workspace

**Record your observations:**
```
Connectors currently enabled:


Connectors available but not enabled:


```

### Step 0B: Test a Connector-Powered Prompt

With Google Drive connected, try this prompt in a new Claude conversation:

```
I'd like to find any documents in my Google Drive related to project management
tools or tool evaluations. What can you find?
```

**Observe:** Does Claude pull relevant documents? Note how this differs from manually uploading a file.

> [!tip] If Google Drive isn't available in your workspace, skip this step and note it as a gap. The concept still applies: connectors eliminate manual copy-pasting.

### Step 0C: Slack AI Morning Briefing

Open Slack and find the AI feature (sparkle icon or search bar):

1. Ask Slack AI: "Summarize the key discussions in #general from this week"
2. Then try: "What decisions were made in [your team channel] recently?"

**Record your observations:**
```
What Slack AI surfaced that you would have missed:


How long would it have taken to find this manually?


```

> [!tip] If Slack AI isn't enabled in your workspace, simulate by manually checking a channel and noting how long it takes to find 3 key points. This illustrates the problem Slack AI solves.

**Before moving on:** Disable any connectors you don't need for the rest of this lab. This preserves context window for the upcoming exercises.

---

## Part 1: Gemini Research Mission (10 minutes)

### Step 1: Open Gemini

Navigate to [gemini.google.com](https://gemini.google.com) and ensure you're using Gemini Advanced if available.

### Step 2: Conduct Research

Paste this research prompt:

```
I'm evaluating project management tools for a mid-size team. Please research and provide:

1. Current pricing tiers for Asana, Monday.com and ClickUp - what's included in each
2. Their most recent product updates or feature announcements (last 6 months)
3. Key strengths customers mention in reviews for each tool
4. Common complaints or weaknesses from customer feedback
5. How each tool positions itself for team collaboration

For each fact, note the source. Format as a structured fact brief with clear sections.
```

### Step 3: Verify with Double Check

After receiving the response:
- Click the **Double Check** button (if available in your Gemini version)
- Note which claims are grounded in sources
- Identify any statements without strong source support

**Record your observations:**
```
Claims with strong source support:


Claims needing verification:


Information gaps (couldn't find):


```

### Step 4A: (Optional) Try Deep Research

If you have access to Gemini Advanced or ChatGPT Plus, try the same topic with Deep Research mode:

1. Select "Deep Research" in Gemini (or the Deep Research model in ChatGPT)
2. Enter: "Conduct a comprehensive comparison of Asana, Monday.com and ClickUp including pricing, features, integrations, user sentiment and recent developments"
3. Let it run (5-10 minutes)
4. Compare the depth and breadth of results vs. your standard query

**Record your observations:**
```
Key differences between standard query and Deep Research:


Additional insights Deep Research found:


Was the extra time worth it for this use case? Why/why not?


```

### Step 4B: Create Your Fact Brief

Using Gemini's response (standard or Deep Research), create a structured Fact Brief in this format:

```markdown
# Fact Brief: Project Management Tool Evaluation
**Research Date:** [Today's date]
**Source Tool:** Gemini Advanced

## Verified Facts

### Pricing Comparison
- [Fact from research] — Source: [URL if provided]
- [Fact from research] — Source: [URL if provided]

### Recent Updates
- [Fact from research] — Source: [URL if provided]

### Strengths (from customer feedback)
- [Strength per tool] — Source: [Review site/URL]

### Weaknesses (from customer feedback)
- [Weakness per tool] — Source: [Review site/URL]

## Needs Verification
- [Any claims that weren't well-sourced]

## Research Gaps
- [Information you couldn't find]
```

---

## Part 2: Processing Meeting Context (10 minutes)

Since you may not have a Flight Recorder (Granola, Zoom AI or Chorus) installed, we'll simulate meeting notes. In a real workflow, these would come from your Flight Recorder's exports.

### Step 5: Review Simulated Meeting Notes

Here are "Granola-style" notes from previous meetings about the tool evaluation:

**Initial Requirements Meeting (3 weeks ago):**
```markdown
## Tool Evaluation Kickoff
**Date:** [3 weeks ago]
**Attendees:** Dana Park (Director of Operations), Raj Patel (IT Manager), You

### Key Points
- Currently using a mix of spreadsheets and email to manage projects
- Pain point: No centralized visibility into project status across teams
- IT concerned about integration complexity with existing systems
- Dana mentioned the team tried Trello previously but found it "too simple for our needs"
- Budget: Approved for Q2, looking for solution under $20/user/month

### Requirements Discussed
- Must integrate with Google Workspace and Slack
- Want customizable dashboards for department leads
- Need both Kanban and timeline views
- Data privacy and SOC 2 compliance required

### My Notes During Meeting
- Dana is the executive sponsor and ultimate decision maker
- Raj will evaluate security and integration requirements
- They want to pilot with one department first (30 users)

### Next Steps
- Research top 3 tool options
- Schedule demos with shortlisted vendors
```

**Demo Review Meeting (2 weeks ago):**
```markdown
## Post-Demo Debrief
**Date:** [2 weeks ago]
**Attendees:** Dana Park, Raj Patel, Lisa Nguyen (Team Lead), You

### Reactions After Vendor Demos
- Strong positive reaction to Monday.com's dashboard customization
- Dana specifically liked the automated status reporting
- Raj asked detailed questions about API access and SSO support
- Lisa concerned about learning curve for her team

### Questions Raised
- "Can we create custom workflows for different departments?"
- "How easy is it to migrate our existing data from spreadsheets?"
- "What does the onboarding and training process look like?"

### Concerns
- Lisa worried about adoption: "If it's too complex, people won't use it"
- Raj wants to understand data residency and backup policies
- Dana asked about ROI: "How do we measure if this actually improves efficiency?"

### Tool Preferences So Far
- Dana: "Monday.com felt the most polished. ClickUp has more features but seemed overwhelming."

### My Notes During Meeting
- Ease of adoption is the top priority for Lisa's team
- Need to prepare a migration plan to address Raj's concerns
- ROI framework for Dana would help move the decision forward

### Next Steps
- Compile final comparison with pricing
- Prepare recommendation presentation
- Address outstanding security questions
```

### Step 6: Extract Context with Claude

Open a **new Claude conversation** and paste:

```
ROLE: Analyst helping prepare a tool recommendation for leadership

MEETING HISTORY:
Here are notes from our previous discussions about the project management tool evaluation:

KICKOFF MEETING:
"""
[Paste the Initial Requirements Meeting notes above]
"""

POST-DEMO DEBRIEF:
"""
[Paste the Demo Review Meeting notes above]
"""

TASK: Analyze these meeting notes and extract:

1. **Stakeholder Priorities**: Who are the key decision makers and what does each care about most?

2. **Requirements Consensus**: Where do stakeholders agree? Where do they differ?

3. **Concerns to Address**: What objections or worries need to be resolved before a decision?

4. **Tool Preferences**: What did stakeholders respond to positively or negatively?

5. **Recommended Focus**: Based on this history, what should our final recommendation emphasize?

Base your analysis ONLY on evidence from these meeting notes.
```

**Save Claude's analysis**—you'll use it in Part 3.

---

## Part 3: Squadron Synthesis (10 minutes)

Now combine your Gemini research with your Claude-analyzed meeting context.

### Step 7: Create a Combined Brief

Open a **new Claude conversation** and paste:

```
ROLE: ActivTrak team member preparing a tool recommendation for leadership

TOOL RESEARCH (from Gemini research):
"""
[Paste your Fact Brief from Part 1]
"""

STAKEHOLDER CONTEXT (from meeting history analysis):
"""
[Paste Claude's analysis from Step 6]
"""

TASK: Create a recommendation brief that includes:

1. **SITUATION SUMMARY** (2-3 sentences)
   - Where we are in the evaluation process
   - Key dynamics to be aware of

2. **TOOL COMPARISON** (3-4 bullets per tool)
   - Compare the shortlisted tools based on our team's specific requirements
   - Use verified research, not assumptions

3. **STAKEHOLDER ALIGNMENT**
   - For Dana (Director of Ops): How recommendation addresses her priorities
   - For Raj (IT Manager): How recommendation addresses his concerns
   - For Lisa (Team Lead): How recommendation addresses adoption worries

4. **RISK MITIGATION**
   - Address the concerns raised in previous meetings
   - Include specific points about ease of adoption and migration

5. **RECOMMENDED NEXT STEPS**
   - What should we propose at the decision meeting?
   - What questions remain open?

CONSTRAINTS:
- Base tool comparisons on the Fact Brief only
- Reference specific moments from the meeting history to show alignment
- Present a clear recommendation with rationale
```

### Step 8: Review Your Output

Evaluate the recommendation brief:

- [ ] Does it reference specific moments from the meeting history?
- [ ] Are tool comparisons based on the Fact Brief (not invented)?
- [ ] Does it address each stakeholder's specific concerns?
- [ ] Would you feel confident presenting this in a real meeting?

---

## Part 4: Reflection

### Questions to Consider

1. **Connector Impact:** How did data connectors (or the concept of them) change how you think about providing context to Claude?

```


```

2. **The Fact Brief Impact:** How did having verified research change Claude's output compared to if you had just asked "compare project management tools for me"?

```


```

3. **Deep Research Value:** If you tried Deep Research, how did the depth compare to a standard query? When would the extra time be worth it?

```


```

4. **Context Value:** What insights emerged from the meeting history that you might have forgotten or missed without structured notes?

```


```

5. **Slack AI Potential:** How could Slack AI change your morning routine or meeting prep workflow?

```


```

6. **Application:** What recurring task in your work would benefit from the full sensor array (Connectors + Gemini + Meeting AI + Slack AI → Claude)?

```


```

---

## Success Criteria

You've completed this lab successfully if you can:

- [ ] Navigate connector settings and understand when to enable/disable them
- [ ] Conduct research in Gemini and create a structured Fact Brief
- [ ] Identify which claims are grounded and which need verification
- [ ] Understand when to use Deep Research vs. standard queries
- [ ] Process meeting context to extract strategic insights
- [ ] Use Slack AI (or understand the workflow) for team intelligence
- [ ] Execute the verified handoff (all sensor inputs → Claude)
- [ ] Produce polished deliverables based on verified information

---

## Bonus Challenge

### Create a Reusable Sensor Array Template

Design a prompt template for a task you do regularly that would benefit from the full Squadron sensor workflow. Include:

1. **Pre-check (Slack AI + Connectors):** What should you check first to avoid duplicating effort?
2. **Gemini Research Prompt:** What intelligence do you need to gather? Standard query or Deep Research?
3. **Meeting Context Prompt:** What Flight Recorder output should inform the result?
4. **Synthesis Prompt:** How should Claude combine all sensor inputs?

Test your template with a real scenario and refine until it produces consistent results.

---

## Key Takeaways

1. **Connectors eliminate friction.** Direct data feeds mean Claude can access your workspace without manual copy-pasting. Manage them intentionally.

2. **Verification prevents hallucination.** The Fact Brief constrains Claude to work with real information. Deep Research provides comprehensive depth when needed.

3. **Context creates relevance.** Meeting history transforms generic advice into tailored strategy. Any Flight Recorder works as long as you capture consistently.

4. **Team intelligence matters.** Slack AI surfaces decisions, discussions and context that would take 20+ minutes to find manually.

5. **The handoff is critical.** Structured transfer between sensors ensures nothing is lost.

6. **The sensor array multiplies capability.** Each sensor does what it's best at. Together they're more powerful than any single tool.

7. **This workflow scales.** Once you learn the pattern, apply it to any task requiring research + context + synthesis.

---

*Lab complete. Proceed to the Module 5 Quiz when ready.*
