# Module 10 Lab Exercise
## Designing for the Agentic Future

**Objective:** Practice converting task-based workflows into goal-based, agent-ready designs.

**Time:** 25-30 minutes (Core Lab) | +15 minutes (Advanced Credit)

**Prerequisites:**
- Completed Modules 1-9
- Claude account
- Understanding of Skills framework from Module 8

**Note:** This lab focuses on **design thinking** for agents, not executing actual agent workflows (which require advanced setup). You'll practice the mindset and structural patterns that make workflows agent-compatible.

> **Advanced Module Notice:** If you're not yet comfortable with the concepts in Modules 1-9, feel free to skim this lab and return later. The exercises here prepare you for future capabilities but aren't required for day-to-day AI usage.

---

## Part 1: Task-to-Goal Conversion (8 minutes)

### Scenario

You currently perform these tasks manually:

**Task Set A: Meeting Action Items to Monday.com**
1. Review meeting notes for action items
2. Identify who is responsible for each item
3. Determine priority and due dates
4. Open Monday.com
5. Create tasks for each action item
6. Assign to appropriate team members

**Task Set B: Customer QBR Preparation**
1. Export customer usage data from ActivTrak
2. Analyze trends in productivity metrics
3. Identify wins to highlight
4. Flag areas needing attention
5. Create presentation slides
6. Draft talking points for each slide

### Task 1A: Convert to Goal Statements

Rewrite each task set as a single **goal statement** that an agent could execute.

**Template:**
```
GOAL: [Outcome description]

SUCCESS CRITERIA:
- [Measurable outcome 1]
- [Measurable outcome 2]
- [Measurable outcome 3]

HUMAN CHECKPOINTS:
- [Where human review is required]
```

**Your Goal Statement for Task Set A:**
```
[Write your goal statement here]
```

**Your Goal Statement for Task Set B:**
```
[Write your goal statement here]
```

### Task 1B: Evaluate Your Goals

Review your goal statements against these criteria:

| Criterion | Task Set A | Task Set B |
|-----------|------------|------------|
| Outcome-focused (not action-focused)? | | |
| Clear success criteria defined? | | |
| Human checkpoint included? | | |
| Could an agent know when it's "done"? | | |

**Deliverable:** Two goal statements and self-evaluation table

---

## Part 2: Structured Agent Prompts (10 minutes)

### Scenario

You need to design prompts that include conditional logic—the kind agents can navigate.

### Task 2A: If/Then Prompt Design

Create an agent-style prompt with conditional logic for this scenario:

**Scenario:** Monthly account health check

The agent should:
- Analyze account usage data
- Categorize accounts as Healthy (>80% engagement), At-Risk (50-80%), or Critical (<50%)
- Take different actions based on category

**Write your If/Then prompt:**

```
GOAL: Monthly account health assessment

INPUT:
<account_data>[Usage CSV will be provided]</account_data>

PROCESS:
1. Analyze engagement metrics for each account
2. Categorize by engagement level

CONDITIONAL ACTIONS:

IF engagement >= 80% (Healthy):
  [What should the agent do?]

IF engagement 50-80% (At-Risk):
  [What should the agent do?]

IF engagement < 50% (Critical):
  [What should the agent do?]

OUTPUT FORMAT:
[Specify the structure]

HUMAN CHECKPOINT:
[When should a human review before action?]
```

### Task 2B: Test Your Logic

Enter your prompt into Claude (without actual data) and ask:

```
Review this agent-style prompt. Identify:
1. Any ambiguous instructions
2. Missing edge cases
3. Unclear success criteria
4. Suggestions for improvement
```

**Record Claude's feedback:**
```
[Paste feedback here]
```

**Revised prompt based on feedback:**
```
[Your improved version]
```

**Deliverable:** Original prompt, Claude's feedback, and revised version

---

## Part 3: Modular Workflow Design (7 minutes)

### Scenario

You want to design a workflow that chains multiple Skills together—the modular approach that enables agentic orchestration.

### Task 3A: Identify Component Skills

For this workflow goal, identify the discrete Skills (modules) needed:

**Goal:** "Generate a competitive battle card for [COMPETITOR] based on current market intelligence"

**List the component Skills:**

| Skill Name | Input | Output | Purpose |
|------------|-------|--------|---------|
| Example: RESEARCH_COMPETITOR | Competitor name | Fact brief with citations | Gather current intelligence |
| | | | |
| | | | |
| | | | |
| | | | |

### Task 3B: Define the Chain

Draw the workflow showing how Skills connect:

```
[Skill 1] → Output feeds → [Skill 2] → Output feeds → [Skill 3] → Final Deliverable
     ↓                          ↓                          ↓
[Checkpoint?]             [Checkpoint?]              [Checkpoint?]
```

**Your workflow chain:**
```
[Draw your chain here]
```

### Task 3C: Identify Dependencies

Answer these questions:
1. Which Skills could run in parallel (no dependencies)?
2. Which Skills must run sequentially?
3. Where are the critical human checkpoints?

**Deliverable:** Component Skills table, workflow chain, and dependency analysis

---

## Part 4: Governance Framework (5 minutes)

### Scenario

You're designing agent permissions for a Customer Success workflow that handles client data.

### Task 4A: Permission Matrix

Define what the agent should and should not be able to do:

| Action | Allowed? | Requires Approval? | Reasoning |
|--------|----------|-------------------|-----------|
| Read client usage data | | | |
| Write to internal database | | | |
| Send email to client | | | |
| Post to internal Slack | | | |
| Create presentation file | | | |
| Access client PII | | | |
| Share data externally | | | |

### Task 4B: Escalation Triggers

Define situations that should automatically stop the agent and escalate to human:

```
ESCALATION TRIGGERS:
1. [Situation that requires human intervention]
2. [Situation that requires human intervention]
3. [Situation that requires human intervention]
```

**Deliverable:** Permission matrix and escalation triggers

---

## Lab Completion Checklist

Core deliverables:

- [ ] Two goal statements with success criteria (Part 1)
- [ ] If/Then agent prompt with Claude feedback (Part 2)
- [ ] Modular workflow design with component Skills (Part 3)
- [ ] Permission matrix and escalation triggers (Part 4)

---

## Advanced Credit: Future Workflow Design (+15 minutes)

### The Challenge

Design a complete agent-ready workflow for one of these ActivTrak scenarios:

**Option A: Proactive Churn Prevention**
Goal: Monitor account health signals and automatically initiate intervention workflows when risk indicators appear.

**Option B: Competitive Intelligence Automation**
Goal: Continuously monitor competitor activities and automatically generate alerts and analysis when significant changes occur.

**Option C: Sales Enablement Pipeline**
Goal: Automatically prepare deal intelligence packages when opportunities reach specific stages.

### Your Design Document

```
WORKFLOW NAME: [Name]

GOAL STATEMENT:
[Outcome-focused description]

SUCCESS CRITERIA:
-
-
-

COMPONENT SKILLS:
| Skill | Purpose | Input | Output |
|-------|---------|-------|--------|
| | | | |
| | | | |
| | | | |

WORKFLOW LOGIC:
[If/Then structure with conditional paths]

PERMISSION BOUNDARIES:
| Action | Policy |
|--------|--------|
| | |
| | |

HUMAN CHECKPOINTS:
1. [When and why]
2. [When and why]

ESCALATION TRIGGERS:
1.
2.
3.

AUDIT REQUIREMENTS:
[What should be logged]

ESTIMATED AUTONOMY LEVEL:
[ ] Fully autonomous (human reviews output only)
[ ] Semi-autonomous (human approves key decisions)
[ ] Assisted (human triggers each phase)
```

### Advanced Deliverable

- [ ] Complete workflow design document
- [ ] Justification for autonomy level chosen
- [ ] Risk assessment for the workflow

---

## Reflection Questions

After completing the lab:

1. What was hardest about converting tasks to goals?
2. Where did your If/Then logic have gaps that Claude identified?
3. How does modular Skill design enable agentic workflows?
4. What governance considerations surprised you?

**Save your reflections—they demonstrate readiness for autonomous AI operations.**

---

## Troubleshooting

**Problem:** My goal statements still sound like tasks
- **Solution:** Focus on outcomes, not activities. Ask "What state do I want to achieve?" not "What steps do I take?"

**Problem:** My If/Then logic has too many branches
- **Solution:** Start with 2-3 main paths. Add complexity only where business logic requires it.

**Problem:** I can't identify where humans should review
- **Solution:** Ask: "What would go wrong if the agent made the wrong choice here? How bad would it be?" High-consequence decisions need human checkpoints.

**Problem:** My Skills have too many dependencies
- **Solution:** Break larger Skills into smaller, single-purpose modules. Each Skill should do one thing well.

---

**Lab Complete. Proceed to Quiz when ready.**
