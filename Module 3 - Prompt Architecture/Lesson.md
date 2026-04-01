# Module 3: The Reasoning Engine
## Advanced Prompt Architecture

---

## Introduction: Programming in English

In Module 1, you learned that AI is a probabilistic reasoning engine. In Module 2, you learned to select the right model for the task. Now we address the most powerful lever you have: **how you structure your prompts**.

Here's the uncomfortable truth: most people write prompts like text messages. Short. Vague. Hoping the AI "gets it." Squadron Leaders write prompts like mission briefings—structured, explicit and unambiguous.

This module introduces you to **structured prompting**—techniques that transform casual prompting into precision engineering. You'll learn why structure matters, how to prevent "context bleeding" and how to choose the right format for your needs.

**The key insight:** It's not about XML specifically—it's about **clear separation of concerns**. You can achieve this with XML tags, Markdown formatting or even just well-organized plain text. The goal is making sure the AI knows exactly what's a role, what's data, what's a constraint and what's an instruction.

---

## The Problem: Context Bleeding

Let's start with a failure case. Here's a prompt a CSM might write:

> "Here's my email to the client. Can you make it more professional? Also remember that we never use the word 'tracking' and always say 'analytics' instead. The client is worried about their renewal and I want to reassure them."

What's wrong with this? Everything is mixed together:
- The instructions ("make it more professional")
- The constraints ("never use tracking")
- The context ("client is worried")
- The data (presumably the email, though it's not clearly separated)

When you mix instructions with data, the AI can confuse which is which. It might try to make your *instructions* more professional. It might include "never use tracking" in its response as if it were part of the email. This is **context bleeding**—when different parts of your prompt contaminate each other.

The solution? **Clear structure**—whether that's XML tags, Markdown headers or well-organized sections.

---

## The Structure Spectrum: Three Approaches

You have three main options for structuring prompts, progressing from simplest to most advanced. All three work—choose based on your comfort level and the complexity of the task.

### Option 1: Clear Labels (Simplest Approach)

Even without special syntax, you can use clear labels and line breaks:

```
ROLE: You are a Customer Success Manager at ActivTrak.

BACKGROUND: The client's productivity dropped 15% last quarter
during their EHR implementation.

THE DATA:
- Nursing: -18%
- Admin: +3%
- IT: -8%

WHAT TO AVOID:
- Don't use "tracking" or "monitoring"
- Don't blame employees

TASK: Write three hypotheses for the productivity drop.
Format as numbered list with one supporting data point each.
```

**Best for:**
- Simple, single-purpose prompts
- People new to structured prompting
- Quick tasks where formal structure feels like overkill
- When you just need "good enough" separation

### Option 2: Markdown Headers (Balanced)

Markdown uses # symbols and formatting to create clear sections:

```markdown
## Role
You are a workforce analytics consultant...

## Context
The client is preparing for a QBR...

## Data
Here's the productivity report:
- Metric 1: value
- Metric 2: value

## Constraints
- Do not use surveillance language
- Keep response under 200 words

## Output Format
Provide three bullet points summarizing...
```

**Best for:**
- People who find XML syntax uncomfortable
- Prompts that are more narrative in nature
- When you're already working in Markdown documents
- Quick structuring without memorizing tag names

---

## Markdown Quick Reference

If you're new to Markdown, here's a quick reference for the most useful formatting you'll use in prompts:

### Headers
```markdown
# Level 1 Header
## Level 2 Header
### Level 3 Header
```

### Text Formatting
```markdown
**Bold text**
*Italic text*
***Bold and italic***
```

### Lists
```markdown
Bullet list:
- Item one
- Item two
  - Nested item
  - Another nested item

Numbered list:
1. First item
2. Second item
3. Third item
```

### Code
```markdown
Inline code: `variable_name`

Code block:
```
code goes here
```

Code block with syntax highlighting:
```python
def function_name():
    return "value"
```
```

### Tables
```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data 1   | Data 2   | Data 3   |
| Data 4   | Data 5   | Data 6   |
```

### Links and Horizontal Rules
```markdown
[Link text](https://url.com)

Horizontal rule:
---
```

**Why this matters for prompting**: Markdown formatting helps you organize data within prompts (tables for metrics, lists for findings, code blocks for technical content) and helps Claude parse structured information more reliably.

---

### Option 3: XML Tags (Most Precise)

XML tags create explicit containers with opening and closing markers:

```xml
<context>
This is background information
</context>

<data>
This is the actual content to work with
</data>

<instructions>
This is what I want you to do
</instructions>
```

**Best for:**
- Complex prompts with multiple data sources
- Prompts you'll reuse repeatedly (templates)
- Situations where you need to nest information (data within data)
- When you want Claude to output structured data back to you
- Advanced users comfortable with structured syntax

---

## When XML Is Superior

While all three approaches work, XML has specific advantages in certain situations:

### 1. Nesting Complex Data

XML allows you to put tags inside tags, creating hierarchies:

```xml
<user_data>
  <client_info>
    Company: TechCorp
    Industry: Manufacturing
  </client_info>

  <metrics>
    Active Users: 1,847
    Productivity: 6.2 hrs/day
  </metrics>

  <communications>
    Last QBR: Positive
    NPS: 8
  </communications>
</user_data>
```

This nesting is harder to achieve cleanly with Markdown or plain sections.

### 2. Asking Claude to Output Structured Data

When you want Claude to return data in a specific format, XML in your prompt signals that you're comfortable with structured output:

```xml
<output_format>
Return your analysis as:
<recommendation>
  <action>What to do</action>
  <rationale>Why</rationale>
  <priority>High/Medium/Low</priority>
</recommendation>
</output_format>
```

### 3. Reusable Templates with Placeholders

XML makes it easy to create templates with clear insertion points:

```xml
<task_context>
Client: [CLIENT_NAME]
Industry: [INDUSTRY]
Tenure: [MONTHS] months
Health Status: [RED/YELLOW/GREEN]
</task_context>
```

### 4. Preventing Ambiguity in Edge Cases

When your data itself contains formatting (like Markdown text you're asking Claude to edit), XML tags prevent confusion:

```xml
<content_to_edit>
## Our Q3 Results

We achieved **15% growth** this quarter...
</content_to_edit>

<instructions>
Edit the content above to be more concise.
</instructions>
```

Without the XML tags, Claude might confuse the Markdown headers in your data with structural elements of your prompt.

---

## The ActivTrak Standard Components

Regardless of which format you choose, these are the components you should include:

| Component | Purpose | Example |
|-----------|---------|---------|
| **Role** | Defines who the AI should be | "You are a workforce analytics consultant..." |
| **Context** | Background situation and goals | "The client is preparing for a QBR..." |
| **Data** | The actual content to process | Email text, report data, transcript |
| **Constraints** | What NOT to do | "Do not use surveillance language..." |
| **Output Format** | Desired structure | "Respond with bullet points..." |
| **Examples** | (Optional) Sample outputs to emulate | "Here's a good example:..." |

### Same Prompt, Three Formats

Here's how the same prompt looks in each format:

**XML Version:**
```xml
<system_role>
You are a Customer Success Manager at ActivTrak, focused on
"Insights, Not Oversight."
</system_role>

<task_context>
I need to explain a 15% productivity drop to our client's VP.
The drop coincides with their Epic EHR implementation.
</task_context>

<user_data>
Productivity Metrics (Q3 vs Q2):
- Nursing/Clinical: -18%
- Administrative: +3%
- Focus Time: -22%
- Collaboration Time: +15%
</user_data>

<constraints>
- Frame analysis as supportive, not punitive
- Do not use words: tracking, monitoring, surveillance
</constraints>

<output_format>
Provide three hypotheses with supporting data points.
</output_format>
```

**Markdown Version:**
```markdown
## Role
You are a Customer Success Manager at ActivTrak, focused on
"Insights, Not Oversight."

## Context
I need to explain a 15% productivity drop to our client's VP.
The drop coincides with their Epic EHR implementation.

## Data
Productivity Metrics (Q3 vs Q2):
- Nursing/Clinical: -18%
- Administrative: +3%
- Focus Time: -22%
- Collaboration Time: +15%

## Constraints
- Frame analysis as supportive, not punitive
- Do not use words: tracking, monitoring, surveillance

## What I Need
Provide three hypotheses with supporting data points.
```

**Clear Sections Version:**
```
ROLE: You are a Customer Success Manager at ActivTrak, focused on "Insights, Not Oversight."

SITUATION: I need to explain a 15% productivity drop to our client's VP. The drop coincides with their Epic EHR implementation.

DATA:
Productivity Metrics (Q3 vs Q2):
- Nursing/Clinical: -18%
- Administrative: +3%
- Focus Time: -22%
- Collaboration Time: +15%

AVOID: Tracking/monitoring language. Don't be punitive.

TASK: Provide three hypotheses with supporting data points.
```

All three will produce similar quality results. Choose what feels natural to you.

---

## When Structure Isn't Needed

Here's an important truth: **you don't always need formal structure**.

For simple, single-purpose prompts, a well-written paragraph can work fine:

> "Review this email draft and make it more concise. Keep it under 100 words, maintain a professional but warm tone, and make sure the call-to-action is clear. Here's the draft: [email text]"

This works because:
- There's one clear task (make it concise)
- The constraints are simple (under 100 words, professional tone)
- The data is clearly separated ("Here's the draft:")
- There's no risk of confusing instructions with content

**Use formal structure when:**
- You have multiple data sources
- Your task has several distinct requirements
- You're getting inconsistent results
- You want to create a reusable template
- The prompt is complex enough that sections help organize your thinking

**Skip formal structure when:**
- The task is simple and single-purpose
- You're having a back-and-forth conversation
- Your natural writing is already clear and organized
- You're just asking a quick question

The goal is **clarity**, not ceremony. If your prompt is clear without XML or Markdown headers, that's fine.

---

## Pro Tip: Ask Claude to Structure Your Data

Here's a technique many people don't know: **you can ask Claude to convert messy data into structured format**.

If you have unstructured information—meeting notes, email threads, raw data dumps—you can ask Claude to organize it before using it in a structured prompt.

**Example:**

> "Here are my rough notes from the client call. Please convert them into a structured format with these sections: Client Goals, Concerns Raised, Action Items, and Next Steps. Use XML tags."

Claude will return something like:

```xml
<client_goals>
- Reduce overtime costs by Q2
- Improve visibility into remote team productivity
</client_goals>

<concerns_raised>
- Privacy worries from employee council
- Integration with existing HRIS
</concerns_raised>

<action_items>
- Send privacy documentation by Friday
- Schedule technical call with IT team
</action_items>

<next_steps>
- Follow-up meeting in two weeks
- Pilot program proposal due March 15
</next_steps>
```

You can then use this structured output as input for your next prompt. This is especially useful when:
- You're working with messy meeting transcripts
- You have data scattered across multiple sources
- You want to create a consistent format for recurring tasks

---

## Chain of Thought: Forcing Logic Before Output

Sometimes you need the AI to show its reasoning, not just give you an answer. You can request this in any format:

**XML:**
```xml
<output_format>
First, show your reasoning in a <thinking> section.
Then provide your final response.
</output_format>
```

**Markdown:**
```markdown
## Output Format
Start with a "Reasoning" section where you think through the problem.
Then provide your final answer under "Conclusion."
```

**Plain:**
```
Before giving your answer, explain your reasoning step by step.
Then provide your final recommendation.
```

**When to use explicit thinking requests:**
- Complex data interpretation
- Situations with multiple valid interpretations
- When you need to verify the AI's logic
- When the answer will be shared with stakeholders

---

## Meta-Prompting: AI Writing AI Instructions

Here's a power technique: use AI to improve your prompts.

**Meta-prompting** is asking the AI to act as a prompt engineer and refine your instructions. It's recursive—using the tool to sharpen the tool.

You can do this in whatever format you prefer:

**Simple version:**
> "I have a prompt that's giving me inconsistent results. Can you analyze it and suggest improvements? Here's my current prompt: [paste prompt]"

**Structured version:**
```markdown
## Your Role
You're an expert prompt engineer.

## Task
Analyze my prompt for weaknesses and suggest improvements.

## My Current Prompt
"""
[paste your underperforming prompt here]
"""

## What I Need
1. List specific weaknesses
2. Explain why each causes problems
3. Provide a revised version
```

### When to Use Meta-Prompting

- **Debugging poor outputs**: When results are inconsistent, the prompt is usually the problem
- **Creating templates**: When building reusable prompts for your team
- **Learning**: Understanding *why* a prompt works teaches you to write better ones

---

## Common Mistakes and Fixes

### Mistake 1: Overloading a Single Prompt

**Problem:** Asking for research, analysis, writing AND critique in one prompt.

**Fix:** Use the Squadron model. Research with Gemini, analyze with Claude, critique in a separate conversation.

### Mistake 2: Vague Output Requests

**Problem:** "Make this better" or "Write something good"

**Fix:** Specify exactly what "better" means:
```
Improve this email by:
- Shortening to under 100 words
- Adding one specific data point
- Ending with a clear call-to-action
```

### Mistake 3: Forgetting Constraints

**Problem:** Getting outputs that violate ActivTrak messaging guidelines.

**Fix:** Always include what to avoid:
```
AVOID:
- Words: tracking, monitoring, surveillance, spying
- Suggesting punitive actions based on data
- Focusing on individual blame
```

### Mistake 4: Burying Instructions

**Problem:** Putting the key task in the middle of a long prompt.

**Fix:** Put orientation at the top, data in the middle, instructions at the end. The AI pays most attention to the beginning and end.

### Mistake 5: Using Structure When Unnecessary

**Problem:** Writing 500-word XML prompts for simple tasks.

**Fix:** Match complexity to the task. A simple question deserves a simple prompt.

---

## The Prompt Architecture Checklist

Before sending any complex prompt, verify:

### Structure
- [ ] Clear separation between role, context, data and instructions
- [ ] Format chosen matches task complexity (XML/Markdown/sections)
- [ ] No mixing of instructions within data sections

### Clarity
- [ ] Single, clear primary objective
- [ ] Explicit constraints (what NOT to do)
- [ ] Defined output format

### Context Quality
- [ ] Only relevant data included (no Water Glass Effect)
- [ ] Data clearly labeled and organized
- [ ] Critical instructions at the end (Lost in the Middle prevention)

### Framing
- [ ] Passes the "Insight vs Oversight" test
- [ ] Uses appropriate ActivTrak terminology
- [ ] Role aligns with task requirements

---

## Module 1 → Module 2 → Module 3 Integration

You now have a complete foundation:

| Module | You Learned | You Can Now |
|--------|-------------|-------------|
| Module 1 | AI is probabilistic; context matters | Structure context like mission briefings |
| Module 2 | Different models for different tasks | Select the right model tier |
| Module 3 | Structure prevents context bleeding | Write precision prompts in any format |

**The Squadron Leader Prompt Process:**
1. Select the right model (Haiku/Sonnet/Opus)
2. Choose your structure format (XML/Markdown/sections)
3. Include explicit constraints
4. Define output format
5. Place instructions at the end
6. Use meta-prompting to refine when needed

---

## What's Next

In Module 4, you'll learn why AI fails at math and how to use **Code Execution** to get accurate calculations. You'll discover that when you need numbers, you need Python—and Claude can write and run that Python for you.

The prompt architecture you learned in this module becomes even more powerful when combined with code execution. You'll structure data analysis requests the same way—with clear sections, constraints and explicit output formats.

---

## Key Takeaways

1. **Structure prevents context bleeding**—keeping role, data, constraints and instructions clearly separated

2. **You have three format options**: XML tags (most precise), Markdown headers (balanced), or clear sections (simplest)

3. **XML is superior** for nested data, structured outputs, reusable templates and edge cases with formatting conflicts

4. **You don't always need formal structure**—simple tasks can use simple prompts

5. **Ask Claude to structure your data** when you have messy information that needs organizing

6. **Place instructions at the end** of prompts due to the "Lost in the Middle" effect

7. **Meta-prompting** lets you use AI to improve your prompts—leverage this for templates and debugging

8. **Structure beats length**—a well-organized 200-word prompt outperforms a rambling 500-word prompt

---

*You're now equipped to write prompts that produce consistent, high-quality results using whatever format feels natural to you. In the lab exercise, you'll practice transforming messy prompts into structured formats of your choice.*
