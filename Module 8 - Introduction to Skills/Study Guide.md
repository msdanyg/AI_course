# Module 8 Study Guide
## The Squadron Playbook: Skills Synthesis

**One-page consolidation of Module 8.** Use this for review before the quiz, before the lab, and during your quarterly skill audits.

---

## Core Mental Model

**Project = persistent CONTEXT (one workspace).**
**Skill = portable METHODOLOGY (everywhere).**

A Project remembers facts about a domain. A Skill encodes a way of working that travels across every domain.

You use them together. The Project holds the briefing material. The Skill defines how you process briefings.

---

## Anatomy of a SKILL.md

```yaml
---
name: gerund-form-lowercase-hyphenated
description: Use when the user says "[trigger phrase 1]", "[trigger phrase 2]"...
  Returns [what the skill produces].
---
```

Body sections (in this order):
1. **When to use** (trigger phrases)
2. **Steps** (numbered, not prose)
3. **Output format** (literal template)
4. **Gotchas** (failure patterns you have seen)
5. **Constraints** (skill-specific rules)

Hard cap: **500 lines**. Move depth to companion files in the skill folder.

---

## The Description Recipe

The description is the trigger. Most skills succeed or die on this one field.

**Bad:** "This skill helps with email tasks."
**Good:** "Use when the user says 'summarize my inbox', 'what do I owe people', 'pull my action items from this week'. Returns a structured to-do list."

**Three rules:**
1. **Specific** — list actual phrases users type
2. **Loud** — concrete words, not abstract concepts
3. **Third person** — "Use when the user asks to..." (written for the model)

---

## The Investment Rule

| Type | What it does | How it ages | Invest |
|------|--------------|-------------|--------|
| Capability uplift | Teaches Claude something it does not do well | DEPRECIATES with model upgrades | 20% |
| Encoded preference | Captures YOUR way of working | APPRECIATES over time | 80% |

Your competitive advantage is methodology, not capability. Let Anthropic worry about capability uplift.

---

## The 5 Skill Killers (Diagnostic Cheatsheet)

| Symptom | Killer | Fix |
|---------|--------|-----|
| Skill never auto-fires | 1. Vague description | Write specific, loud, third-person triggers with actual user phrases |
| Robotic output on edge cases | 2. Over-defined process | Match degrees of freedom to task type (tight/loose) |
| Bloated skill, behavior does not match length | 3. Stating the obvious | Cut anything Claude already does well |
| Fails on predictable edge cases | 4. Missing gotcha | Add the failure pattern to the gotcha section |
| Claude skipping sections | 5. Monolithic structure | 500-line cap; move depth to companion files |

---

## The Litmus Test

> **If you find yourself iterating on the output AFTER the skill runs, the skill itself needs improvement.**

Manual cleanup is a diagnostic signal, not a normal part of using a skill. The fix is to upgrade the skill, not to write a better follow-up prompt. Encode the cleanup logic INSIDE the skill so you do not have to remember to ask.

---

## Decision Tree: Do I need a Skill or a Project?

```
Is the work bound to one specific domain with documents and history?
├── YES → Project
│   └── Do you also have a repeatable methodology that runs ON the project's content?
│       └── YES → Skill (used INSIDE the project)
└── NO → Is there a repeatable methodology you want available everywhere?
    └── YES → Skill
```

Best practice: combine them. Skills inside Projects is the high-leverage configuration.

---

## Maintenance Cadence

**Quarterly review** (every 90 days):
- Re-evaluate capability skills — did a model upgrade obsolete any?
- Re-read every preference skill — has your workflow shifted?
- Audit each skill against the 5 Killers
- Apply the litmus test to each skill's recent output

**When models upgrade:** assume some capability skills are now overkill. Test before assuming they still earn their place.

**When workflows shift:** preference skills need editing. The methodology you encoded six months ago may not be the methodology you use today.

---

## Self-Assessment Checklist

Before the quiz, you should be able to answer YES to all of these:

- [ ] I can name the two YAML frontmatter fields in a SKILL.md (name, description)
- [ ] I can explain the difference between a Project and a Skill in one sentence
- [ ] I can list all 5 Skill Killers and their fixes
- [ ] I can identify which Killer applies to a given symptom
- [ ] I can explain the capability vs. preference distinction and the 80/20 investment rule
- [ ] I know what the Litmus Test is and what it tells me
- [ ] I understand that skills install at the user level and work across all projects
- [ ] I can write a description that auto-fires (specific, loud, third person, with actual user phrases)

If any box is unchecked, re-read the relevant lesson section before taking the quiz.

---

## Connection to Your Work

Walk through your week. Find:

- **One task you do 3+ times per week** — that is your next preference skill
- **One context you re-paste regularly** — that is your next Project
- **One workflow where you clean up Claude's output afterward** — that cleanup belongs INSIDE a skill

These three observations are the seeds of your full Squadron Playbook.

---

**AI drafts. Humans send. The Playbook makes the drafts predictable.**

**End of Module 8 Study Guide.** Proceed to the Quiz, then the Lab.
