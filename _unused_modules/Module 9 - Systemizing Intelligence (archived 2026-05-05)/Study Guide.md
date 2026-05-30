# Module 8 Study Guide
## Systemizing Intelligence: Projects, Skills, Gems & Custom GPTs

**One-Page Quick Reference**

---

## Core Concept

**Squadron Architect Model**: Build persistent AI infrastructure that works for you even when you're not actively prompting. Move from giving instructions to building systems.

**The Problem It Solves**: Contextual amnesia—every AI conversation starts blank, creating repetition tax, consistency drift, and an expertise ceiling.

---

## Squadron Mapping for Module 8

| Concept | Squadron Term | Tool/Platform |
|---------|--------------|---------------|
| Persistent workspaces | Mission Archives | Claude Projects |
| Reusable templates | Mission Cards | Claude Skills |
| Research specialists | Recon Specialists | Gemini Gems |
| Shareable assistants | Deployable Specialists | Custom GPTs |
| Your infrastructure | Squadron Playbook | All combined |

---

## The Four Persistence Tools

### 1. Claude Projects

**What**: Persistent workspace with custom instructions, knowledge files, and conversation history

**Best For**: Deep work requiring extensive context, ongoing client/account work, analysis with documents

**Key Components:**
- Custom Instructions (behavior rules)
- Knowledge Files (reference documents)
- Conversation History (ongoing context)

**Create when**: 5+ conversations on same topic, need consistent context, have reference documents

---

### 2. Claude Skills

**What**: Reusable prompt templates invoked with trigger phrases

**Best For**: Repeatable tasks across different contexts, standardized methodologies

**Key Components:**
- Trigger phrase ("Quick comp on...")
- Structured instructions
- Input placeholders
- Output format

**Example Use Case**: Brand Guidelines Skill—ensures all AI-generated content follows ActivTrak terminology, tone and formatting standards. Build once, apply to any content.

**Create when**: Same analysis pattern used repeatedly, want consistent output structure

---

### 3. Gemini Gems

**What**: Custom AI assistants optimized for Google Workspace

**Best For**: Real-time research, Google Workspace integration, current data needs

**Key Strengths:**
- Web grounding (current information)
- Native Docs/Sheets/Slides integration
- Collaborative access

**Create when**: Need current data, want Workspace integration, research workflows

---

### 4. Custom GPTs

**What**: Shareable assistants in ChatGPT

**Best For**: Team distribution, consistent methodology across users

**Key Differentiator**: **Can be shared with others**

**Create when**: Others need same assistant, want organization-wide standardization

---

## Decision Matrix

| Need | Primary Tool | Why |
|------|-------------|-----|
| Deep client work | Claude Project | Context + documents + history |
| Quick repeated tasks | Claude Skill | Portable methodology |
| Real-time research | Gemini Gem | Grounded, current data |
| Team-shared assistant | Custom GPT | Distributable, consistent |

---

## Project Architecture Patterns

| Pattern | Structure | Use Case |
|---------|-----------|----------|
| Client Hub | One Project per account | Account-specific context |
| Workflow Station | One Project per workflow | Recurring process work |
| Knowledge Base | Centralized reference | Shared domain knowledge |

---

## Custom Instructions Template

```
You are my [ROLE] for [DOMAIN].

CONTEXT:
- My role: [title/responsibilities]
- Key focus: [areas of work]

BEHAVIOR:
- [How to approach tasks]
- [What to prioritize/avoid]

OUTPUT:
- [Format preferences]
- [Structure requirements]
```

Keep under 500 words. Be specific, not exhaustive.

---

## Maintenance Schedule

| Frequency | Actions |
|-----------|---------|
| Weekly | Review conversations, update Skills, check Gem accuracy |
| Monthly | Refresh knowledge files, audit instructions, archive inactive |
| Quarterly | Evaluate expansion, share patterns with team |

---

## Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| Mega-Project | Everything in one workspace | Create purpose-specific Projects |
| Instruction Overload | 2,000-word instructions | Keep under 500 words |
| Stale Knowledge | Outdated documents | Monthly refresh schedule |
| Tool Confusion | Wrong tool for task | Use decision matrix |

---

## Integration Workflow Example

**Competitive presentation workflow:**

1. **Gem** ("Market Intel"): Gather current competitor news
2. **Project** ("Competitive Intelligence"): Synthesize with historical analysis
3. **Skill** ("Presentation Outline"): Structure into slides
4. **Result**: Consistent, current, properly formatted deliverable

---

## Quick Reference: When to Use What

| Task Type | Tool | Reason |
|-----------|------|--------|
| Ongoing account work | Project | Persistent context |
| Format this analysis | Skill | Reusable methodology |
| What's the latest on...? | Gem | Current web data |
| Give this to my team | Custom GPT | Shareable |

---

## The Transformation

| Before (Solo Pilot) | After (Squadron Architect) |
|--------------------|---------------------------|
| Blank conversations | Persistent Projects |
| Re-explaining context | Custom Instructions |
| Inconsistent outputs | Standardized Skills |
| Manual research setup | Configured Gems |
| Personal use only | Team distribution |

---

## Bridge to Module 9

You've built the infrastructure. Now it's time to produce artifacts.

**Module 9: Code Execution** teaches you to generate:
- Excel spreadsheets
- PowerPoint presentations
- PDF reports
- Custom file outputs

Your Projects hold context. Your Skills define process. Code execution produces deliverables.

---

## The Architect's Creed

> **"Don't just use AI—build systems that use AI for you. Infrastructure scales. Individual prompts don't."**

---

## Self-Assessment

Can you:
- [ ] Explain the three components of a Claude Project?
- [ ] Describe when to use Skills vs. Projects?
- [ ] Identify scenarios where Gems outperform Projects?
- [ ] Name the key differentiator of Custom GPTs?
- [ ] Create a maintenance schedule for your infrastructure?

If yes to all: **Module 8 mastered. Proceed to Module 9.**
If no to any: **Review corresponding lesson section, re-attempt lab.**

---

**End of Module 8 Study Guide**
