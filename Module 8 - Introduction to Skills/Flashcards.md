# Module 8 Flashcards
## The Squadron Playbook: Skills Retrieval Practice

**How to use:** Read the front. Try to answer before flipping. Use these for spaced repetition — review one week, two weeks, and one month after completing the module.

---

## Card 1

**FRONT**
What is a Skill, mechanically?

**BACK**
A folder containing a `SKILL.md` file with YAML frontmatter (`name` and `description`) plus a Markdown body of structured instructions, optionally bundled with companion files (scripts, references, templates).

The single most important field is `description` — Claude reads it to decide whether to auto-fire the skill.

---

## Card 2

**FRONT**
What is the key difference between a Project and a Skill?

**BACK**
- **Project** = persistent CONTEXT (documents, history, custom instructions) bound to ONE workspace
- **Skill** = portable METHODOLOGY (steps, output templates, gotchas) available across EVERY conversation and EVERY project

Projects fight contextual amnesia inside one mission. Skills fight it across every mission.

---

## Card 3

**FRONT**
What are the four near-mandatory components of the Markdown body of a SKILL.md?

**BACK**
1. **Steps** — numbered, specific, actionable (not prose)
2. **Output format** — a literal template, not a description of one
3. **Gotchas** — failure patterns you have actually seen (highest-signal content)
4. **Constraints** — rules specific to this skill

Plus the hard rule: keep the file under 500 lines. Past that, move depth to companion files.

---

## Card 4

**FRONT**
What are Capability Uplift skills versus Encoded Preference skills, and where should you invest?

**BACK**
- **Capability Uplift**: teaching Claude to do something it does not do well alone. Live on borrowed time — model upgrades obsolete them.
- **Encoded Preference**: capturing YOUR way of working. Compound in value over time — better models execute your preferences more cleanly.

**Squadron Leader investment rule:** spend 80% on Encoded Preference. Your competitive advantage is your methodology.

---

## Card 5

**FRONT**
Name the 5 Skill Killers.

**BACK**
1. **Vague descriptions** → fix with specific, loud, third-person trigger language
2. **Over-defined processes** → match degrees of freedom to the task (tight for fragile, loose for creative)
3. **Stating the obvious** → cut anything Claude already does well
4. **Missing gotcha section** → document failure patterns you have actually seen
5. **Monolithic structure** → 500-line cap; move depth to companion files

---

## Card 6

**FRONT**
What does it mean to write a description that "auto-fires"?

**BACK**
The description is the trigger Claude reads to decide whether to invoke the skill. A good description:

- Is written in third person ("Use when the user asks to...")
- Lists the ACTUAL phrases users say
- Is specific and loud — concrete words, not abstract concepts
- Briefly states what the skill returns

A description that is a SUMMARY of the skill ("This powerful skill helps with...") is the #1 reason skills do not fire.

---

## Card 7

**FRONT**
What is the Litmus Test for whether a skill is done?

**BACK**
**"If you find yourself iterating on the output AFTER the skill runs, the skill itself needs improvement."**

Manual cleanup after a skill runs is a diagnostic signal that the skill is incomplete. The fix is NOT to write a better follow-up prompt. The fix is to upgrade the skill — move the cleanup logic INSIDE the skill so you do not have to remember to ask for it.

Encode it once. Get it forever.

---

## Card 8

**FRONT**
Where do skills install, and what does that mean for using them?

**BACK**
Skills install at the **user level**. Once installed:

- The skill is available in EVERY conversation
- It works in EVERY project
- It works in fresh chats with no project at all
- You do NOT install per project

This is the cross-project superpower. Install once, available everywhere. This is why Skills are called "portable methodology" — methodology that travels with you across every context.

---

**End of Module 8 Flashcards.** Next review: 7 days. Then 14 days. Then 30 days. Spaced repetition turns these from passing knowledge into permanent operating instructions.
