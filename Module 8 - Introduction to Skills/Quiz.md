# Module 8 Quiz
## The Squadron Playbook: Skills Mastery Check

**Instructions:** 7 questions. Mix of multiple choice, true/false with explanation, and scenario-based diagnostics. Detailed feedback provided for every answer. Pass threshold: 70% (5 of 7 correct).

---

### Question 1 (Multiple Choice — Retrieval)

**Which of the following correctly identifies the YAML frontmatter fields that every SKILL.md file should contain?**

A) `title` and `body`
B) `name` and `description`
C) `prompt` and `output`
D) `trigger` and `instructions`

**Correct Answer:** B

**Feedback for B (Correct):**
Mission Control confirms. Every SKILL.md file has YAML frontmatter at the top with two essential fields:

- `name`: gerund-form, lowercase, hyphenated identifier (e.g., `extracting-gmail-action-items`)
- `description`: third-person trigger phrase that tells Claude when to fire the skill

The Markdown body below the frontmatter contains the steps, output format, gotchas, and constraints. But the frontmatter is where Claude looks first to decide whether the skill applies.

**Feedback for other answers:**
- A (`title` and `body`): Generic markdown thinking, not Skills-specific. SKILL.md uses a structured format with required field names.
- C (`prompt` and `output`): These are conceptually relevant but not the actual frontmatter field names.
- D (`trigger` and `instructions`): Close conceptually — the description IS the trigger and the body IS instructions — but the literal field names are `name` and `description`.

---

### Question 2 (Multiple Choice — Comprehension)

**What is the key difference between a Claude Project and a Claude Skill?**

A) Skills cost money; Projects are free
B) Projects provide persistent context bound to one workspace; Skills provide portable methodology available across all conversations
C) Skills can access the internet; Projects cannot
D) Projects are for teams; Skills are for individuals

**Correct Answer:** B

**Feedback for B (Correct):**
Recon confirms. The cleanest distinction:

- **Project = persistent CONTEXT.** Documents, conversation history, and custom instructions bound to one workspace. You enter the project to use it.
- **Skill = portable METHODOLOGY.** Steps, output templates, and gotchas that travel across every conversation, every project, every chat. Install once, available everywhere.

Best practice is to use them together. A Project holds the briefing material for a domain; Skills define how you process briefings regardless of domain. The same skill works inside your Customer Success project, your Competitive Intelligence project, and a brand-new chat with no project at all.

**Feedback for other answers:**
- A: Both are available at the same subscription tier. Cost is not the differentiator.
- C: Neither has internet access by default. Connectors enable that for both.
- D: Both are primarily individual tools. Sharing mechanisms exist for both.

---

### Question 3 (Scenario — Analysis)

**Scenario:** You built a skill called `competitive-quick-look`. The description reads: "This powerful skill helps with competitive analysis tasks." When you type "give me a quick comp on Teramind," the skill does not auto-fire. You have to type `/competitive-quick-look` manually every time. Which Skill Killer is at work?**

A) Killer 1: Vague description
B) Killer 2: Over-defined process
C) Killer 4: Missing gotcha section
D) Killer 5: Monolithic structure

**Correct Answer:** A

**Feedback for A (Correct):**
Recon flags it correctly. This is Killer 1 in textbook form.

The description "This powerful skill helps with competitive analysis tasks" is written as a SUMMARY of what the skill does, not as a TRIGGER. Claude scans descriptions looking for matches to the user's actual phrasing. "Quick comp on Teramind" does not match "helps with competitive analysis tasks" closely enough to auto-fire.

**The fix:** rewrite the description in specific, loud, third-person language that lists the actual phrases users say:

> "Use when the user says 'quick comp on [company]', 'give me a comp brief on [company]', 'positioning analysis on [company]', or asks for a fast competitive overview. Returns structured strengths, weaknesses, and ActivTrak counter-positioning."

**Feedback for other answers:**
- B (Over-defined process): Would manifest as robotic output on edge cases, not failure to trigger.
- C (Missing gotcha): Would manifest as the skill failing on predictable edge cases, not failing to fire.
- D (Monolithic): Would manifest as Claude skipping sections of a long file, not failing to fire.

---

### Question 4 (Multiple Choice — Comprehension)

**You have 10 hours to invest in skill-building this quarter. According to the Squadron Leader investment rule, how should you allocate that time between capability uplift skills and encoded preference skills?**

A) 50/50 — both are equally valuable
B) 80% on capability uplift, 20% on encoded preference
C) 80% on encoded preference, 20% on capability uplift
D) 100% on capability uplift — Anthropic will eventually deprecate preference skills

**Correct Answer:** C

**Feedback for C (Correct):**
Mission Control confirms. The Squadron Leader investment rule: roughly 80% on encoded preference, 20% on capability uplift.

The reasoning matters more than the ratio:

- **Capability uplift skills** (teaching Claude to do something it does not do well alone) live on borrowed time. Every model upgrade obsoletes some of them.
- **Encoded preference skills** (capturing YOUR way of working) compound in value. Better models execute your preferences more cleanly while still respecting them.

Your competitive advantage is your methodology, not your ability to invent capability. Let Anthropic worry about capability uplift. You worry about encoding the way YOU and your team work.

**Feedback for other answers:**
- A (50/50): Misses the asymmetric ROI. Capability skills depreciate; preference skills appreciate.
- B (80% capability): Inverts the rule. You will spend most of your time rebuilding skills as models improve.
- D (100% capability): Wrong direction entirely. Preference skills are the durable investment.

---

### Question 5 (Scenario — Knowledge Utilization)

**Scenario:** You want to build a skill that summarizes Granola meeting transcripts into a structured action-items list for the meeting owner. You are about to write the description. Which of the following is the BEST description for auto-triggering?**

A) "This skill summarizes Granola meeting transcripts."
B) "A skill for processing Granola transcripts and extracting structured action items with owners and due dates."
C) "Use when the user says 'summarize that meeting,' 'pull the action items from [meeting name],' 'who owns what from the [day] sync,' or asks for follow-ups from a Granola transcript. Returns a structured table with action, owner, and due date."
D) "Use this skill to be more productive with your Granola meetings."

**Correct Answer:** C

**Feedback for C (Correct):**
Squadron Leader thinking. C is the only option that follows all three description rules:

1. **Specific** — lists actual phrases the user types
2. **Loud** — uses concrete words, not abstract concepts
3. **Third-person** — "Use when the user says..." (written for the model deciding whether to fire)

It also tells Claude what the skill RETURNS, which helps disambiguate from other meeting-related skills.

**Feedback for other answers:**
- A (summary, not trigger): Tells Claude WHAT the skill does, not WHEN to fire. Claude will not match natural user phrasings against it.
- B (still a summary): Better than A but still abstract. "Processing transcripts" is not how a user phrases a request.
- D (vague and aspirational): Marketing copy. Useless for triggering.

The pattern: open with "Use when the user says..." or "Use when the user asks to..." Then list the actual sentences they say. Then briefly state what the skill returns.

---

### Question 6 (True/False with Explanation — Retrieval)

**TRUE or FALSE: Once a Skill is installed, it works in every conversation and every project — you do not need to install it separately for each project.**

**Correct Answer:** TRUE

**Feedback if TRUE (Correct):**
Confirmed. This is one of the defining characteristics of Skills versus Projects:

- **Projects** are bound to one workspace. The custom instructions and knowledge files inside Project A do not apply when you open Project B.
- **Skills** install at the user level. Once installed, the skill is available in every conversation, every project, and every fresh chat. Auto-invocation works everywhere the description matches.

This is why Skills are called "portable methodology." Methodology that does not travel between contexts is not really methodology — it is just instructions trapped in one folder. Skills solve that.

**Feedback if FALSE (Incorrect):**
This is the cross-project superpower of Skills. Unlike Projects, which scope custom instructions and documents to one workspace, Skills install at the user level. Once installed, the skill is available in every conversation, every project, every chat. You do not re-install per project. This is precisely why Skills are described as "portable methodology" — the methodology travels with you.

---

### Question 7 (Scenario — Analysis)

**Scenario:** You built a Gmail action-item skill. It auto-fires correctly. The output table is well-formatted. But every time it runs, you find yourself manually deleting calendar invites from the list and adding the priority labels (High/Medium/Low) that the skill did not include. What does this tell you about the state of the skill?**

A) The skill is working correctly — manual cleanup is normal
B) The skill needs improvement — the cleanup logic should be encoded into the skill itself
C) The skill is over-engineered — you should remove the gotcha section
D) Claude is the wrong tool for this task

**Correct Answer:** B

**Feedback for B (Correct):**
This is the litmus test in action.

> "If you find yourself iterating on the output AFTER the skill runs, the skill itself needs improvement."

You are doing manual work that should not be manual. Two specific failures:

1. **Calendar invites in the output** = Killer 4 (missing gotcha). Add: "Calendar invites are not action items unless the body explicitly asks the user to do something." Update the skill's gotcha section.

2. **Missing priority labels** = the output format spec is incomplete. Add a Priority column to the output template with explicit High/Medium/Low criteria.

Then re-run. The whole point of a skill is that you do NOT have to remember to ask for the cleanup. Encode it once, get it forever. Manual post-processing is a signal that your skill is unfinished, not a signal that it is working.

**Feedback for other answers:**
- A (manual cleanup is normal): The opposite of true. Manual cleanup is the diagnostic that tells you the skill needs an upgrade.
- C (remove the gotcha section): Backwards — the gotcha section should be EXPANDED to cover the calendar-invite case, not removed.
- D (Claude is wrong tool): Premature. The skill is fixable. Reach for "wrong tool" only after upgrade attempts have actually failed.

---

## Quiz Complete

**Score Interpretation:**

- **6–7 correct (Squadron Architect level):** You understand Skills as portable methodology, can diagnose failures via the 5 Killers framework, and apply the litmus test. You are ready to build your full Playbook.
- **5 correct (Pass — 70% threshold):** Solid foundational understanding. Re-read the sections on the 5 Killers and the litmus test before building production skills.
- **3–4 correct:** Revisit the lesson with focus on description-writing patterns, the Skills-vs-Projects distinction, and the capability-vs-preference investment rule. The lab will reinforce all of these in practice.
- **0–2 correct:** Re-read the full lesson and re-watch the video before proceeding. Skills are foundational to the rest of the course.

**Key Concepts Mastered (if 70%+):**

1. SKILL.md anatomy — `name` and `description` frontmatter, plus structured Markdown body
2. Skills vs. Projects — portable methodology vs. persistent context
3. The 5 Skill Killers — vague descriptions, over-defined processes, stating the obvious, missing gotchas, monolithic structure
4. Description writing — specific, loud, third person, with literal user phrases
5. Capability vs. Preference — invest 80% in encoded preference
6. Cross-project availability — install once, available everywhere
7. The Litmus Test — manual cleanup after a skill runs means the skill is incomplete

---

**Proceed to the Study Guide to consolidate your learning, then to the Lab to build your first Mission Card.**
