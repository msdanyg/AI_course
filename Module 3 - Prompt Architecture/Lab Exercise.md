# Module 3: Prompt Architecture
## Lab Exercise: The POC Closeout Challenge

**Duration:** 20-25 minutes
**Tools Required:** Claude (claude.ai), the Forever New POC deck (provided)

---

## Objective

By the end of this lab, you will be able to:
- Transform an unstructured email into a reusable markdown template with placeholders
- Structure complex multi-asset prompts using XML tags, markdown headers or clear labels
- Apply the ActivTrak standard prompt components (Role → Context → Data → Constraints → Output Format)
- Prevent context bleeding when working with multiple data sources
- Create prompts that produce consistent, professional POC closeout communications

---

## The Challenge: POC Closeout Communication

You're a Customer Success Manager who just completed a successful POC with Forever New, a retail company. You need to create:

**Part A:** A reusable POC closeout email template (for future POCs)
**Part B:** A comprehensive executive summary using multiple data sources
**Bonus Challenge:** Do both in a single, well-structured prompt

This is a real ActivTrak workflow. The templates you create today can be used for actual POCs.

---

## Part A: Email to Template (10 minutes)

### The Assignment

**Your Goal:** Convert the Forever New POC closeout email into a reusable markdown template with placeholders.

### Data Source: The POC Closeout Email

```
Subject: Forever New POC Results - Ready to Discuss Next Steps

Hi Ben and team,

I wanted to share the results from your ActivTrak POC. The data is really compelling.

Your team showed 0.3 hours more productivity when working remotely (6.8 hrs) compared to in-office (6.5 hrs). The Buying Apparel team especially benefited from remote work. Interestingly, hybrid days where people split locations had the lowest productivity at 6.4 hours - likely due to transition time.

We also identified significant capacity opportunities. 68.6% of users (105 of 153) are currently below productivity goals, representing about $104K in monthly financial loss or 25 FTE worth of untapped capacity. The IT Department spends 27% of their time in chat and messaging - nearly double other departments - suggesting focus time optimization opportunities.

We detected 3 users with potential time theft issues using input simulation tools, which validates your concerns about activity authenticity.

Based on these findings, I recommend we focus on three immediate actions: addressing the IT productivity gap, coaching the bottom 36 users averaging under 5 productive hours daily, and investigating the input simulation cases.

The ROI potential is substantial - even a conservative 10% improvement would recover $125K annually and gain 2.5 FTE capacity without hiring.

I'd love to schedule a call this week to discuss moving forward with Essentials Plus. Are you available Thursday or Friday afternoon?

Best regards,
Sarah Mitchell
Customer Success Manager, ActivTrak
```

### Your Instructions

Create a prompt that tells Claude to:
1. **Replace specific details** with placeholders in [BRACKETS]
2. **Organize into clear sections** with markdown headers (##)
3. **Preserve the tone and flow** but make it generic enough for any POC
4. **Make it flexible** - some POCs might have 2 findings, others might have 5

**Before you start:** Analyze the email:
- What information is **specific to Forever New** and needs to become a placeholder?
- What structure is **universal** to all POC closeouts?
- What are the **logical sections**?

### Try It Yourself First

Open Claude and write your own prompt. See if you can get it to produce a good template!

---

<details>
<summary><strong>💡 Show Me How</strong> (Click to reveal example prompt)</summary>

Here's an example using the ActivTrak standard prompt components:

```
ROLE: You are a Solutions Consultant at ActivTrak creating reusable templates for POC closeout communications.

CONTEXT: This template will be used by the Solutions team for future POC closeouts with different clients. It needs to be flexible enough to work for various findings while maintaining a consistent professional structure.

DATA: [Paste the POC closeout email above]

CONSTRAINTS:
- Replace all client-specific details with placeholders in [BRACKETS]
- Use descriptive placeholder names (e.g., [CLIENT_NAME], [PRODUCTIVITY_METRIC], [ROI_FIGURE])
- Preserve the supportive, consultative tone
- Keep the email structure flexible for 2-5 key findings
- Maintain professional closing format

OUTPUT FORMAT:
Create a markdown template with these sections:
## Subject Line
## Greeting
## Key Findings (flexible number)
## Recommendations
## ROI Summary
## Next Steps
## Closing
```

**What makes this work:**
- **Role** establishes who Claude is and their purpose
- **Context** explains why this template matters and how it will be used
- **Data** clearly separates the source material
- **Constraints** prevent common errors (vague placeholders, rigid structure)
- **Output Format** specifies exactly what sections to create

</details>

---

### Refine Your Template

Review Claude's output. Does it have:
- [ ] Clear section headers (## Greeting, ## Key Findings, ## Recommendations, etc.)
- [ ] Placeholders for customizable data: [CLIENT_NAME], [PRODUCTIVITY_METRIC], [ROI_FIGURE]
- [ ] Flexibility for different findings (some POCs might have 2 findings, others might have 5)
- [ ] A professional closing with [YOUR_NAME], [YOUR_TITLE]

If not, ask Claude to revise with specific instructions.

### Reflection

**Did you need structured prompting for this simple task, or was a casual request sufficient?**

```


```

---

## Part B: Multi-Asset Executive Summary (10-15 minutes)

### The Assignment

**Your Goal:** Create a structured prompt that synthesizes THREE data sources into a board-ready executive summary for Forever New's CIO.

**The Challenge:** How do you structure a prompt with multiple data sources without context bleeding?

**Important:** Notice that each data source uses a **different format** (free text, Markdown, bullet list). This is intentional! Real-world data rarely comes in a single format, and your prompt structure must handle this variety.

### Data Source 1: POC Closeout Email (FREE TEXT FORMAT)

```
[Use the Forever New email from Part A above]
```

### Data Source 2: POC Findings Deck (MARKDOWN FORMAT)

```markdown
# Forever New POC Results Summary

## Success Criteria Validation

| Criterion | Status | Metric |
|-----------|--------|--------|
| Remote work productivity | ✅ VALIDATED | 0.3 hrs more productive (6.8 vs 6.5 hrs) |
| After-hours work verification | ✅ VALIDATED | Schedule adherence tracking implemented |
| Comprehensive visibility | ✅ VALIDATED | Application usage beyond AD logs achieved |
| Capacity opportunities | ✅ VALIDATED | 25 FTE untapped capacity identified |
| License optimization | ✅ VALIDATED | Usage patterns tracked for cost savings |
| False activity detection | ✅ VALIDATED | 3 users detected using input simulation |
| Meeting time visibility | ✅ VALIDATED | Offline meeting integration successful |

## Workforce Utilization

**Critical Finding**: 105 of 153 users (68.6%) currently below productivity goal

- **Monthly financial loss**: $104,292
- **Annualized impact**: $1,251,500
- **Equivalent untapped capacity**: 25.03 FTE

## Time Allocation by Department

| Department | Office Apps | Business Systems | Chat/Messaging | Other |
|------------|-------------|------------------|----------------|-------|
| Buying Apparel | 65.7% | — | 14.1% | 20.2% |
| Finance | 40.7% | 24.5% | — | 34.8% |
| IT Department | 15.4% | — | **27.1%** ⚠️ | 57.5% |
| People & Culture | 33.1% | — | 13.8% | 53.1% |

*⚠️ IT Department chat time is double other departments*

## False Activity Detection

- **2 confirmed cases**: Input simulation detected (movemouse.exe, screenshot evidence)
- **1 highly suspected case**: Productivity theater identified through pattern analysis

## Immediate Action Recommendations

1. **Address IT productivity gap**: 0.8-hour gap vs other departments
2. **Target bottom performers**: 36 users (24%) averaging under 5 hrs/day
3. **Investigate input simulation**: Follow up on 3 flagged accounts

## ROI Projections

| Scenario | Improvement | Annual Recovery | FTE Capacity Gained |
|----------|-------------|-----------------|---------------------|
| Conservative | 10% | $125,150 | 2.5 FTE |
| Target | 20% | $250,300 | 5 FTE |
| Full Potential | 100% | $1,251,500 | 25 FTE |
```

### Data Source 3: POC Kickoff Meeting Notes (BULLET LIST FORMAT)

```
POC Kickoff Meeting - Forever New
Date: October 15, 2024
Attendees: Ben (IT Lead), Efstratios (CIO), Sarah Mitchell (ActivTrak CSM)

• New CIO Efstratios joined 3 months ago with mandate to cut costs and improve efficiency
• Board pressuring leadership for data-driven RTO (return-to-office) policy decisions
• Employees claiming high productivity while WFH but no objective data to validate
• Current monitoring limited to Azure AD logs - very fragmented visibility
• IT team suspects some employees using mouse jigglers or similar tools
• Recent productivity decline coincides with WFH policy expansion
• IT controls all software licensing, looking for opportunities to optimize spend
• Employee council raised privacy concerns about "surveillance"
• Need solution that provides insights without being perceived as Big Brother
• Timeline: 30-day POC, decision needed before Q1 budget planning
• Success criteria: validate/refute WFH productivity claims, identify capacity gaps, detect anomalous activity
```

### Your Instructions

Structure a prompt that includes:

1. **Role:** Who is Claude? (CSM preparing executive summary for C-suite)
2. **Context:** What's the purpose and audience? (Board-ready POC results, non-technical executives)
3. **Data Sources:** All three sources above - **clearly separated**
4. **Constraints:**
   - Use "users" or "accounts" (never "customers" for end users)
   - Use "analytics" and "insights" (never "monitoring" or "tracking")
   - Frame findings supportively using "Insights, Not Oversight" philosophy
   - No technical jargon - audience is C-suite
   - Keep summary to 400 words maximum
   - Do NOT include individual names from false activity detection
5. **Output Format:**
   - POC Overview (2 sentences)
   - Key Findings (3-4 bullet points with quantified impact)
   - Strategic Recommendations (3 priorities with business rationale)
   - Expected ROI (conservative and target scenarios)
   - Proposed Next Steps (specific action with timeline)

**Critical question before you start:** If you paste all three data sources into a single paragraph with vague instructions, what could go wrong?

```


```

### Choose Your Format

You have three options for structuring this prompt:
- **XML Tags** - Most precise, best for nested data
- **Markdown Headers** - Balanced, familiar syntax
- **Clear Labels** - Simplest, fastest

**Try writing your prompt now** using your preferred format!

---

<details>
<summary><strong>💡 Show Me How - Option A: XML Tags</strong> (Click to reveal)</summary>

```xml
<system_role>
You are a Customer Success Manager at ActivTrak preparing an executive summary for a retail company's C-suite following a successful POC.
</system_role>

<task_context>
The CIO needs a concise executive summary for the board meeting that synthesizes POC results into business impact and next steps. The audience is non-technical executives focused on ROI and strategic recommendations.
</task_context>

<data_source_1>
<source_type>POC Closeout Email</source_type>
<content>
[Paste the Forever New email here]
</content>
</data_source_1>

<data_source_2>
<source_type>POC Findings Deck</source_type>
<content>
[Paste the deck summary above]
</content>
</data_source_2>

<data_source_3>
<source_type>POC Kickoff Meeting Notes</source_type>
<content>
[Paste the meeting notes above]
</content>
</data_source_3>

<constraints>
- Use "users" or "accounts" (never "customers" for end users)
- Use "analytics" and "insights" (never "monitoring" or "tracking")
- Frame findings supportively using "Insights, Not Oversight" philosophy
- No technical jargon - audience is C-suite
- Keep summary to 400 words maximum
- Do NOT include individual names from false activity detection
</constraints>

<output_format>
Provide an executive summary with these sections:
1. POC Overview (2 sentences: what we tested, timeframe)
2. Key Findings (3-4 bullet points with quantified impact)
3. Strategic Recommendations (3 priorities with business rationale)
4. Expected ROI (conservative and target scenarios)
5. Proposed Next Steps (specific action with timeline)
</output_format>
```

**Why this works:**
- Each data source is clearly labeled and separated
- Role and context set expectations upfront
- Constraints prevent common errors (surveillance language)
- Output format ensures consistency

</details>

---

<details>
<summary><strong>💡 Show Me How - Option B: Markdown Headers</strong> (Click to reveal)</summary>

```markdown
## Role
You are a Customer Success Manager at ActivTrak preparing an executive summary for a retail company's C-suite following a successful POC.

## Context
The CIO needs a concise executive summary for the board meeting that synthesizes POC results into business impact and next steps. The audience is non-technical executives focused on ROI and strategic recommendations.

## Data Source 1: POC Closeout Email
[Paste the Forever New email here]

## Data Source 2: POC Findings Deck
[Paste the deck summary above]

## Data Source 3: POC Kickoff Meeting Notes
[Paste the meeting notes above]

## Constraints
- Use "users" or "accounts" (never "customers" for end users)
- Use "analytics" and "insights" (never "monitoring" or "tracking")
- Frame findings supportively using "Insights, Not Oversight" philosophy
- No technical jargon - audience is C-suite
- Keep summary to 400 words maximum
- Do NOT include individual names from false activity detection

## Output Format
Provide an executive summary with these sections:
1. POC Overview (2 sentences)
2. Key Findings (3-4 bullet points with quantified impact)
3. Strategic Recommendations (3 priorities with business rationale)
4. Expected ROI (conservative and target scenarios)
5. Proposed Next Steps (specific action with timeline)
```

**Why this works:**
- Familiar markdown syntax (##)
- Clear visual separation between sections
- Readable and easy to modify
- Less intimidating than XML for beginners

</details>

---

<details>
<summary><strong>💡 Show Me How - Option C: Clear Labels</strong> (Click to reveal)</summary>

```
ROLE: Customer Success Manager at ActivTrak preparing executive summary for retail company C-suite

CONTEXT: CIO needs board-ready summary of POC results focused on ROI and strategic recommendations. Non-technical audience.

DATA SOURCE 1 - POC CLOSEOUT EMAIL:
[Paste email]

DATA SOURCE 2 - POC FINDINGS DECK:
[Paste deck summary]

DATA SOURCE 3 - MEETING NOTES:
[Paste notes]

AVOID:
- Words: monitoring, tracking, surveillance, customers (use: analytics, insights, users)
- Technical jargon
- Individual names from time theft cases
- Exceeding 400 words

OUTPUT STRUCTURE:
1. POC Overview (2 sentences)
2. Key Findings (3-4 quantified bullets)
3. Strategic Recommendations (3 priorities with rationale)
4. Expected ROI (conservative and target)
5. Proposed Next Steps (action + timeline)
```

**Why this works:**
- No special syntax required
- Simple, direct labels
- Easy to scan and modify
- Fastest option for straightforward tasks

</details>

---

### Test Your Prompt

1. Choose ONE of the three formats above (or use your own)
2. Paste it into a new Claude conversation
3. Review the output

### Evaluate Your Results

| Criteria | Your Result |
|----------|-------------|
| Used appropriate ActivTrak terminology | ☐ Yes ☐ No |
| Stayed within 400-word limit | ☐ Yes ☐ No |
| Included all 5 required sections | ☐ Yes ☐ No |
| Avoided surveillance language | ☐ Yes ☐ No |
| Synthesized all three data sources | ☐ Yes ☐ No |
| Ready to send without editing | ☐ Yes ☐ No |

**Reflection:** Where did structure make the biggest difference?

```


```

---

## Bonus Challenge: One Prompt, Two Outputs (Advanced)

### The Assignment

Can you create a single structured prompt that produces BOTH:
1. The reusable email template (Part A)
2. The executive summary (Part B)

**Why this is hard:**
- Different output formats (template vs. finished content)
- Different audiences (CSM future use vs. CIO board presentation)
- Risk of context bleeding between template creation and summary writing

**Hint:** You'll need **nested structure** - perhaps a parent `<task>` tag with two child `<deliverable>` tags, each with their own constraints and output formats.

### Try It Yourself

Design your combined prompt below:

```
[Your combined prompt structure here]


```

---

<details>
<summary><strong>💡 Show Me How</strong> (Click to reveal example approach)</summary>

Here's one way to structure a combined prompt using nested XML:

```xml
<task_overview>
You are a Customer Success Manager at ActivTrak. You need to create TWO deliverables from POC closeout materials.
</task_overview>

<deliverable_1>
<type>Reusable Template</type>
<goal>Convert the POC email into a markdown template for future use</goal>
<source_data>
[Forever New email]
</source_data>
<instructions>
Replace specific details with [PLACEHOLDERS], organize with ## headers, preserve tone
</instructions>
</deliverable_1>

<deliverable_2>
<type>Executive Summary</type>
<goal>Create board-ready summary synthesizing all three data sources</goal>
<source_data>
[Email + POC Deck + Meeting Notes]
</source_data>
<constraints>
[All ActivTrak terminology constraints]
</constraints>
<output_format>
[5 required sections]
</output_format>
</deliverable_2>
```

**Key insight:** Nested tags prevent context bleeding between the two tasks. Each deliverable has its own clear scope.

</details>

---

**Reflection:** Was this bonus worth the complexity, or would two separate prompts be better?

```


```

---

## Reflection Questions

1. **Which structure format felt most natural to you?** (XML / Markdown / Clear Labels)

   **Why?**

2. **What happened when you didn't separate data sources clearly?**

3. **How did placing instructions at the END affect Claude's focus?**

4. **Which part of the prompt had the biggest impact on quality:**
   - Role definition?
   - Context setting?
   - Data separation?
   - Constraints list?
   - Output format specification?

5. **Could you reuse your structured prompt from Part B for other POC closeouts by just swapping the data?**

6. **What would you add to your prompt template library after this lab?**

---

## Key Takeaways

1. **Structure prevents context bleeding** - Multiple data sources need clear separation or the AI confuses which information belongs to what context

2. **Templates need placeholders and flexibility** - A good template balances specificity (clear structure) with adaptability (works for different scenarios)

3. **All three formats work for multi-asset prompts** - XML is most precise for complex nesting, Markdown is readable and familiar, Clear Labels are fastest for simple tasks

4. **Constraints prevent post-generation editing** - Spending 30 seconds listing what NOT to do saves 5 minutes of fixing surveillance language

5. **Output format specifications ensure consistency** - When you define the structure upfront, every POC closeout email follows the same professional pattern

6. **Real work deserves structured prompts** - The POC closeout you just created could go to an actual client. That's when structure matters most.

---

## Success Criteria

You've completed this lab successfully if you can:

- [ ] Identify when structure is needed vs. when a casual prompt is sufficient
- [ ] Convert unstructured communications into reusable markdown templates
- [ ] Structure prompts that use 2+ data sources without context bleeding
- [ ] Apply all five ActivTrak prompt components (Role → Context → Data → Constraints → Output)
- [ ] Choose the appropriate format (XML/Markdown/Labels) for your task complexity
- [ ] Explain why separating data from instructions prevents AI confusion
- [ ] Create a prompt template you would actually use in your ActivTrak role

---

## What to Do With Your Templates

1. **Save your email template** - You'll use it in Module 8 when we build reusable Skills
2. **Save your structured prompt from Part B** - This becomes a "Mission Card" you can deploy for every POC
3. **Share with your team** - If your template works well, others can adapt it for their POCs

**Pro tip:** The best templates evolve. After each use, refine your constraints and output format based on what needed editing.

---

## Connection to Module 4 Preview

In the next module, you'll learn why AI fails at math and how to use **Code Execution** to get accurate calculations. Notice that the Forever New POC has lots of numbers - ROI projections, productivity percentages, FTE calculations.

In Module 4, you'll learn to structure prompts that ask Claude to *show its work* by writing and running Python code. The structured prompting you learned today becomes even more powerful when combined with verifiable calculations.

The Squadron Leader's rule: **Structure the mission. Verify the math. Own the output.**

---

*Lab complete. Proceed to Module 3 Quiz when ready.*
