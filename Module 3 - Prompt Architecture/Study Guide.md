# Module 3: The Reasoning Engine
## Quick Reference Study Guide

---

## Core Concept

**Clear structure prevents context bleeding.** When you separate role, data, constraints and instructions—whether using XML tags, Markdown headers or simple labels—the AI produces consistent, high-quality outputs. The goal is **clarity, not a specific syntax**.

---

## Key Terms

| Term | Definition |
|------|------------|
| **Context Bleeding** | When different parts of a prompt contaminate each other (AI confuses instructions with data) |
| **XML Tags** | Explicit containers: `<tag>content</tag>` |
| **Markdown Headers** | Section dividers using `##` symbols |
| **Clear Sections** | Simple labels like `ROLE:` or `TASK:` |
| **Meta-Prompting** | Using AI to analyze and improve your prompts |
| **Lost in the Middle** | AI pays less attention to middle sections; place instructions at the end |

---

## The Structure Spectrum

| Format | Syntax | Best For |
|--------|--------|----------|
| **XML Tags** | `<tag>content</tag>` | Complex prompts, nested data, templates, structured outputs |
| **Markdown Headers** | `## Section` | Narrative prompts, documentation-style, XML-uncomfortable users |
| **Clear Sections** | `LABEL: content` | Simple tasks, beginners, when formal structure feels like overkill |

**All three work.** Choose based on comfort level and task complexity.

---

## When XML Is Superior

Use XML specifically when you need:

1. **Nested data** - Tags inside tags (client_info, metrics, communications all inside user_data)
2. **Structured output** - Requesting Claude return data in specific format
3. **Reusable templates** - Clear placeholders like `[CLIENT_NAME]`
4. **Edge cases** - When your data contains Markdown that might confuse structure

---

## When You Don't Need Structure

**Skip formal structure when:**
- Task is simple and single-purpose
- Back-and-forth conversation
- Your natural writing is already clear
- Quick questions

**Use structure when:**
- Multiple data sources
- Several distinct requirements
- Getting inconsistent results
- Creating reusable templates

**The goal is clarity, not ceremony.**

---

## The Same Prompt, Three Ways

**XML:**
```xml
<system_role>CSM at ActivTrak</system_role>
<task_context>Client productivity dropped 15%</task_context>
<constraints>Avoid surveillance language</constraints>
<output_format>Three hypotheses</output_format>
```

**Markdown:**
```markdown
## Role
CSM at ActivTrak

## Context
Client productivity dropped 15%

## Constraints
Avoid surveillance language

## Output
Three hypotheses
```

**Clear Sections:**
```
ROLE: CSM at ActivTrak
SITUATION: Client productivity dropped 15%
AVOID: Surveillance language
TASK: Three hypotheses
```

---

## Pro Tip: Ask Claude to Structure Data

When you have messy notes, ask Claude to organize them:

> "Here are my rough notes from the client call. Convert them into structured sections: Client Goals, Concerns, Action Items, Next Steps."

Use Claude's structured output as clean input for your next prompt.

---

## Standard ActivTrak Constraints

Include in every ActivTrak-related prompt:

```
AVOID:
- Words: tracking, monitoring, surveillance, spying
- Suggesting punitive actions based on data
- Focusing on individual blame

USE:
- Words: analytics, insights, visibility, patterns
- Supportive, consultative framing
```

---

## Quick Diagnostic

| If Output Is... | The Problem | The Fix |
|-----------------|-------------|---------|
| **Mixing instructions into response** | Context bleeding | Add structure (any format) |
| **Wrong tone or persona** | Missing/weak role | Add role section at top |
| **Using forbidden language** | Missing constraints | Add constraints section |
| **Ignoring key instructions** | Buried instructions | Move instructions to END |
| **Inconsistent results** | Unclear structure | Add more formal structure |
| **Over-complicated for task** | Over-engineering | Simplify—match complexity to task |

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| **Overloading** (research + write + critique) | Separate tasks across conversations |
| **Vague outputs** ("make it better") | Specify exactly what "better" means |
| **Missing constraints** | Always include what to AVOID |
| **Buried instructions** | Place key instructions at the END |
| **Over-engineering** | Simple tasks need simple prompts |

---

## Prompt Order

```
┌─────────────────────────────────────┐
│        Role / Persona               │ ← Who the AI should be
├─────────────────────────────────────┤
│        Context / Background         │ ← The situation
├─────────────────────────────────────┤
│        Data / Content               │ ← Material to work with
├─────────────────────────────────────┤
│        Constraints                  │ ← What NOT to do
├─────────────────────────────────────┤
│        Output Format / Task         │ ← What you need (END)
└─────────────────────────────────────┘
```

**Why this order:** Role primes the persona. Data goes in the middle. Instructions at the end get highest attention (Lost in the Middle effect).

---

## Module 2 → Module 3 → Module 4 Bridge

| Module | You Learned | Applied To |
|--------|-------------|------------|
| Module 2 | Select the right model tier | Choose Haiku/Sonnet/Opus |
| Module 3 | Structure prevents bleeding | Write clear prompts in any format |
| Module 4 | AI fails at math; use code | Data analysis with Python |

---

*Keep this guide handy when writing prompts. Remember: clarity over ceremony.*
