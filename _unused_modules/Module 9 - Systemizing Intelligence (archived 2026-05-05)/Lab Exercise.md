# Module 8 Lab Exercise
## Building Your Squadron Playbook

**Objective:** Create a complete set of persistent AI infrastructure tailored to your role—Projects, Skills, and Gems that will serve as your personal Squadron Playbook.

**Time:** 30-40 minutes

**Prerequisites:**
- Claude account with Projects access
- Gemini account with Gems access
- Understanding of your key workflows and pain points

---

## Part 1: The Infrastructure Audit (5 minutes)

Before building, let's identify what you need.

### Task 1A: Workflow Inventory

List your **top 5 recurring work tasks** where you currently use AI (or could use AI):

| Task | Frequency | Current Pain Point |
|------|-----------|-------------------|
| Example: Competitive analysis | Weekly | Rebuilding context every time |
| 1. | | |
| 2. | | |
| 3. | | |
| 4. | | |
| 5. | | |

### Task 1B: Context Mapping

For each task above, identify:
- What **background context** do you repeatedly explain?
- What **documents** do you frequently reference?
- What **output format** do you always want?

This becomes the blueprint for your infrastructure.

**Deliverable:** Completed workflow inventory table (keep for reference throughout lab)

---

## Part 2: Build Your First Project (10 minutes)

### Task 2A: Choose Your Mission

Select one workflow from your inventory that would benefit most from persistent context. Good candidates:
- Requires 5+ conversations per month
- Uses reference documents
- Needs consistent terminology/formatting

**Your chosen workflow:** _________________

### Task 2B: Write Custom Instructions

Create a new Claude Project and write your Custom Instructions using this template:

```
You are my [ROLE DESCRIPTION] for [DOMAIN/COMPANY].

CONTEXT:
- My role: [Your job title and responsibilities]
- Key focus areas: [What you work on]
- Important relationships/accounts: [Key stakeholders]

BEHAVIOR:
- [How Claude should approach tasks in this domain]
- [What to prioritize]
- [What to avoid or flag]

TERMINOLOGY:
- [Industry or company-specific language rules]
- [Terms to use or avoid]

OUTPUT PREFERENCES:
- [Preferred format: bullets, tables, prose]
- [Desired length and structure]
- [Any standard sections to include]
```

**Your Custom Instructions:**
```
[Write yours here before entering into Claude]


```

### Task 2C: Upload Knowledge Files

Identify 3-5 documents to upload to your Project:

| Document | Purpose |
|----------|---------|
| 1. | |
| 2. | |
| 3. | |
| 4. | |
| 5. | |

Upload these to your Project's knowledge base.

### Task 2D: Test Your Project

Start a conversation in your new Project with a realistic request:

```
[Write a test prompt that you would actually use]
```

**Evaluation checklist:**
- [ ] Did Claude demonstrate awareness of your context?
- [ ] Did the output match your format preferences?
- [ ] Did it use your terminology correctly?
- [ ] Did it reference your uploaded documents (if relevant)?

**Deliverable:** Screenshot or copy of your Project's Custom Instructions

---

## Part 3: Create Two Skills (10 minutes)

### Task 3A: The "Quick Analysis" Skill

Create a Skill for rapid analysis tasks. Start with this template, then customize:

```
SKILL NAME: Quick [Analysis Type]

TRIGGER: When I say "Quick [trigger word] on [SUBJECT]"

INSTRUCTIONS:
1. [First analysis step]
2. [Second analysis step]
3. [Third analysis step]
4. [Summary or recommendation]

OUTPUT FORMAT:
[Describe structure: table, bullets, sections]

EXAMPLE:
"Quick [trigger] on [sample subject]" produces:
[Show expected output structure]
```

**Your Quick Analysis Skill:**
```
SKILL NAME:

TRIGGER:

INSTRUCTIONS:


OUTPUT FORMAT:


```

### Task 3B: The "Prep Brief" Skill

Create a Skill for preparation/planning tasks:

```
SKILL NAME: [Meeting/Task] Prep

TRIGGER: When I say "Prep me for [EVENT/TASK]"

INSTRUCTIONS:
1. Context refresh on the subject
2. Recent relevant history
3. Key priorities or objectives
4. Potential challenges or watch-outs
5. Recommended questions or actions

OUTPUT FORMAT:
- Keep to one page
- Use bullet points
- Include "Next Steps" section
```

**Your Prep Brief Skill:**
```
SKILL NAME:

TRIGGER:

INSTRUCTIONS:


OUTPUT FORMAT:


```

### Task 3C: Test Your Skills

In a Claude conversation (can be inside your Project), test both Skills:

**Test 1:** `[Your quick analysis trigger]`
- Did it follow the structure?
- Was the output useful?

**Test 2:** `[Your prep brief trigger]`
- Did it cover all sections?
- Was it actionable?

**Deliverable:** Both Skill definitions (text format)

---

## Part 4: Build a Gemini Gem (8 minutes)

### Task 4A: Identify Your Research Specialty

Select a research domain where you need current, grounded information:
- Market/competitive intelligence
- Industry news and trends
- Customer/account research
- Technical documentation research

**Your research focus:** _________________

### Task 4B: Configure Your Gem

Go to [gemini.google.com](https://gemini.google.com) and create a new Gem.

**Name:** [Descriptive, role-based name]

**Instructions:**
```
You are a [specialty] researcher for [domain/company].

YOUR FOCUS:
- [Primary topic area]
- [Key subjects to track]
- [Relevant competitors/entities]

WHEN RESEARCHING:
- [Verification requirements]
- [Date/recency standards]
- [Source preferences]

OUTPUT FORMAT:
- [Structure for findings]
- [Required sections]
- [Confidence/verification notes]
```

**Your Gem Configuration:**
```
Name:

Instructions:




```

### Task 4C: Test Your Gem

Use your Gem for a realistic research request:

```
[Write a test research query]
```

**Evaluation checklist:**
- [ ] Did it focus on your specified domain?
- [ ] Did it cite sources appropriately?
- [ ] Did it follow your output format?
- [ ] Did it flag any confidence concerns?

**Deliverable:** Screenshot of your Gem configuration

---

## Part 5: The Integration Test (7 minutes)

### Task 5A: Multi-Tool Workflow

Now let's test your infrastructure working together. Choose a realistic scenario from your work.

**Scenario:** _________________

**Workflow:**

1. **Start with Gem** (research phase):
   Query: _________________

2. **Move to Project** (synthesis phase):
   Take Gem's output and ask your Project to synthesize/analyze it.
   Prompt: _________________

3. **Apply Skill** (formatting phase):
   Use one of your Skills to structure the final output.
   Trigger: _________________

### Task 5B: Document the Workflow

```
WORKFLOW NAME: [Descriptive name]

PURPOSE: [What this workflow produces]

STEPS:
1. Gem "[Name]": [What it does]
2. Project "[Name]": [What it does]
3. Skill "[Name]": [What it does]

OUTPUT: [Final deliverable description]

TIME SAVED: [Estimated vs. manual approach]
```

**Deliverable:** Documented workflow with all three tools

---

## Part 6: Maintenance Plan (5 minutes)

### Task 6A: Set Your Review Schedule

Based on your infrastructure, commit to a maintenance schedule:

**Weekly Review (15 min):**
- [ ] Check: _________________
- [ ] Update: _________________

**Monthly Refresh (30 min):**
- [ ] Review: _________________
- [ ] Update: _________________
- [ ] Archive: _________________

**Quarterly Audit (1 hour):**
- [ ] Evaluate: _________________
- [ ] Expand: _________________
- [ ] Share: _________________

### Task 6B: Knowledge File Tracker

Create a simple tracker for your uploaded documents:

| Document | Project | Last Updated | Next Review |
|----------|---------|--------------|-------------|
| | | | |
| | | | |
| | | | |

**Deliverable:** Maintenance schedule commitment

---

## Lab Completion Checklist

Submit or save these deliverables:

- [ ] Workflow inventory table (Part 1)
- [ ] Claude Project with Custom Instructions (Part 2)
- [ ] Two Claude Skills defined and tested (Part 3)
- [ ] Gemini Gem configured and tested (Part 4)
- [ ] Multi-tool workflow documented (Part 5)
- [ ] Maintenance schedule committed (Part 6)

---

## Stretch Goals (Optional, +15 minutes)

### Stretch 1: Build a Second Project

Create a Project for a different workflow from your inventory. Compare how the Custom Instructions differ based on the use case.

### Stretch 2: Skill Library Expansion

Create three more Skills targeting your most common tasks:
- Data formatting Skill
- Communication drafting Skill
- Decision analysis Skill

### Stretch 3: Custom GPT (If You Have ChatGPT Plus)

Build a Custom GPT that could be shared with teammates:
- Choose a workflow others do similarly
- Write instructions for team-wide use
- Upload shared knowledge files
- Test with a colleague if possible

---

## Troubleshooting

**Problem:** Custom Instructions seem ignored
- **Solution:** Keep under 500 words. Be specific, not exhaustive. Test with explicit references to your instructions.

**Problem:** Knowledge files not being referenced
- **Solution:** Explicitly ask Claude to "check the uploaded documents" or "reference the [filename]"

**Problem:** Skills produce inconsistent outputs
- **Solution:** Add more specific output format instructions. Include an example output structure.

**Problem:** Gem not finding relevant information
- **Solution:** Refine focus areas. Add specific entities/competitors to track. Adjust recency requirements.

---

## Reflection Questions (Post-Lab)

1. Which piece of infrastructure (Project, Skill, Gem) do you think will save you the most time?
2. What workflow that you didn't build would benefit most from this approach?
3. How might you share these systems with teammates?
4. What maintenance challenge do you anticipate?

**Save your reflections—they inform your ongoing infrastructure development.**

---

**Lab Complete. Proceed to Quiz when ready.**
