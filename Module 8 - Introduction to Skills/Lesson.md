# Module 8: The Squadron Playbook
## Building, Sharing, and Mastering Claude Skills

---

## The Repetition Tax

Every conversation you start with Claude begins from zero.

You re-explain your role. You re-state how you want output formatted. You re-paste the same context document for the third time this week. You re-invoke the same five-step methodology you use for every competitive analysis. Multiply that across a year and you are paying a tax measured in hours: the **repetition tax** for not having a system.

You already learned, in Module 4, how Claude Projects fix part of this problem. Projects give you a persistent workspace where Claude remembers the documents, the custom instructions, and the conversation history. That is the right answer when you have one ongoing mission with one body of context.

But Projects have a ceiling. They are bound to one workspace. The methodology you build inside your Competitive Intelligence project does not travel with you when you open a fresh chat to draft a customer email. The careful brand-voice instructions you wrote inside your Marketing Content project do not show up when you switch over to your Customer Success project. Each project is an island.

A **Skill** is the bridge between islands.

If a Project is a mission archive, a Skill is a Mission Card. A standardized procedure, written once, that any pilot in your squadron can pull from the playbook and run on any mission. Skills are how you stop paying the repetition tax permanently, because they are how you encode YOUR way of working into something Claude can recognize and execute on demand, in any conversation, in any project.

This module is your transition from Squadron Leader to Squadron Architect. You are about to build the Playbook.

---

## What Skills Actually Are

A Skill is a packaged capability. Mechanically, it is a folder containing a `SKILL.md` file with structured instructions, optionally bundled with companion files such as scripts, templates, or reference documents.

The `SKILL.md` file has two halves. The top is **YAML frontmatter** that names the skill and describes when it should fire. The bottom is **Markdown** that tells Claude what to do once it fires.

The single most important thing to understand about Skills is this: **Claude reads the description and decides on its own whether to fire the skill.**

When you ask Claude something, Claude scans the descriptions of every installed skill. If your message matches a description, Claude invokes that skill automatically before it even drafts a response. You do not need to remember the skill exists. You do not need to type a special command. The trigger is your natural language, and the description is the gate.

This makes the description the most important line in the entire skill.

### Skills versus Projects

The distinction confuses people, so it is worth setting cleanly. Both Skills and Projects fight contextual amnesia, but they fight different parts of it.

| Dimension | Project | Skill |
|-----------|---------|-------|
| What it stores | Documents, conversation history, custom instructions | Methodology, steps, output templates, gotchas |
| Where it lives | Bound to one workspace | Available in every conversation, every project |
| How it activates | You enter the project to use it | Claude auto-fires it when your message matches the description |
| What it remembers | Specific facts about a domain | A repeatable way of working |
| Best metaphor | A dedicated office for one mission | A Mission Card in the squadron Playbook |

The cleanest way to think about it: a Project is **persistent context**. A Skill is **portable methodology**. You use them together. A Project holds the briefing material; a Skill defines how you read briefings. The same Skill works inside your Customer Success project, your Competitive Intelligence project, and a brand new chat with no project at all.

This is the cross-project superpower. Install a Skill once. Use it everywhere.

---

## Anatomy of a Skill

Every skill, no matter how complex, follows the same shape. Understanding the shape is the difference between writing a skill that works and writing one that quietly fails.

```yaml
---
name: extracting-gmail-action-items
description: Use when the user asks to summarize their inbox, find action items in
  recent emails, identify what they owe people, or pull the to-do list from this
  week's messages. Searches Gmail via the connector and returns a prioritized list.
---

# Extracting Gmail Action Items

## When to use this skill
[Trigger phrases the user typically says]

## Steps
1. Determine the time range (default: last 7 days unless user specifies)
2. Search Gmail using the connector
3. Filter for messages from internal teammates and ActivTrak senders
4. Extract action items, deadlines, and priority signals
5. Return a structured to-do list

## Output format
| Sender | Subject | Action | Due | Priority |

## Gotchas
- Marketing emails often contain false action verbs; ignore them
- Calendar invites are not action items
- Automated notifications (Jira, Monday) are usually not actionable
```

Read that example carefully. Every component does specific work.

**The `name`** is gerund-form, lowercase, hyphenated. `extracting-gmail-action-items`, not `Gmail_TodoExtractor` or `email-stuff`. The convention exists because Claude reads thousands of skill names and the gerund pattern signals "this is a skill, not a noun."

**The `description`** is the trigger. This is where most skills succeed or die. The description is written in third person, lists actual phrases the user might say, and explains what the skill does after it fires. The description is not a summary of the skill. It is a recognition pattern. Write it for the model asking "should I fire here?"

**The Markdown body** has four near-mandatory components:

- **Steps**: numbered, specific, actionable. Not prose. Numbered lists make execution order unambiguous.
- **Output format**: a literal template, not a description of a template. Show Claude what the output looks like, do not describe it.
- **Gotchas**: failure patterns you have observed in practice. This is the highest-signal section in the entire skill.
- **Constraints** (optional): rules specific to this skill. "Never include emails older than 30 days." "Always exclude marketing senders."

A few skills require companion files. A skill that processes Excel spreadsheets might include a Python script. A skill that drafts customer outreach might include a templates folder. The rule is simple: if the asset is **about the skill**, it lives in the skill folder. If it is **about you or your organization** in general, it lives outside and the skill references it.

There is a 500-line ceiling for `SKILL.md`. Past that line count, Claude starts losing the plot. Move detail into reference files.

---

## Two Types of Skills, and Where to Invest

Not all skills age the same way. Some skills compound in value over time. Others quietly become obsolete as Claude gets smarter. Knowing the difference tells you where to spend your skill-building budget.

**Capability uplift skills** add functions that Claude does not do well on its own. A skill that runs a complex statistical analysis. A skill that orchestrates a long agentic workflow. A skill that handles a tricky file format. These are valuable, but they live on borrowed time. Every time the underlying model upgrades, capability skills get partially or fully obsoleted. The thing your skill teaches Claude to do, Claude eventually learns to do natively.

**Encoded preference skills** capture YOUR way of working. Your competitive analysis structure. Your meeting prep format. Your customer success scoring rubric. Your brand voice. These skills are not making Claude smarter. They are making Claude consistent with you. And critically, these get **more** valuable over time, not less, because the underlying model gets better at executing your preferences cleanly while still respecting them.

The Squadron Leader investment rule: spend roughly 80 percent of your skill-building effort on encoded preference. Build skills that say "this is how WE work." Let Anthropic worry about capability uplift. Your competitive advantage is your methodology, not your ability to invent capability.

---

## Finding and Activating Shared Skills

You do not have to build every skill from scratch. Anthropic maintains an official skill catalog, and the broader plugin ecosystem includes thousands of community-built skills. Before building, look.

The activation flow has three steps:

**Browse.** Open the skill catalog inside Claude (or your Claude Code or API integration, depending on where you work). Skills are listed by name and description. Read the descriptions, not the names. The description is what controls behavior.

**Install.** Click install or run the install command, depending on your environment. The skill becomes available in every conversation and every project from that point forward. There is no per-project setup.

**Invoke.** Two ways. The default is **auto-invocation**: when you say something that matches the skill's description, Claude fires it without you asking. The fallback is **manual invocation**: type a slash command or explicitly tell Claude to use a specific skill. Auto is the goal. Manual is the safety net while you tune the description.

A useful first skill to install is `skill-creator` itself. It is the Skill Builder. Once installed, you can build new skills inside any Claude conversation by saying something like "I want to build a skill that helps me prep for QBRs." Claude will recognize the request, fire `skill-creator`, and walk you through the design conversation.

Once `skill-creator` is in your playbook, every other skill becomes easier to build.

---

## Creating Skills with the Skill Builder

The fastest way to write a good skill is to let Claude write the first draft.

The conversation goes like this: you describe the job in plain English. Skill Builder asks clarifying questions about triggers, inputs, outputs, and edge cases. Claude scaffolds the `SKILL.md` file. You review, refine, and ship.

Where Skill Builder helps most is the structure. New skill authors consistently underweight the description and overweight the steps. They write a beautiful seven-step procedure with no clear trigger. The skill never fires. Skill Builder catches this by asking, early, "what does the user say to make this fire?"

Where Skill Builder needs your help is the gotcha section. Claude has not lived your work. It does not know that your last skill failed because it kept including marketing emails in the action items list. It does not know that calendar invites masquerade as action items. You have to tell it. The gotcha section is where your real expertise lands.

There is a single litmus test that tells you when a skill is done versus when it is not yet ready. If you find yourself iterating on the output **after** the skill runs, the skill itself needs improvement. The fix is not to write a better follow-up prompt. The fix is to upgrade the skill. Move the cleanup logic into the skill itself. The whole point of a skill is that you do not have to remember to ask for the cleanup. Encode it once, get it forever.

---

## The 5 Skill Killers

When skills fail, they fail in five recognizable ways. Memorize this list. It is the most useful diagnostic in the entire module.

### Killer 1: Vague descriptions

**Symptom**: the skill never auto-fires. You always end up invoking it manually.

**Why it happens**: the description is written as a summary instead of a trigger. "This skill helps with email" tells Claude what the skill is. It does not tell Claude when to fire.

**Fix**: write the description in **specific, loud, third person**. List the actual phrases the user says. "Use when the user asks to summarize their inbox, find action items in recent emails, identify what they owe people from this week..." Loud means concrete. Specific means you can imagine the exact sentence a user would type.

### Killer 2: Over-defined processes

**Symptom**: the skill works on simple cases but produces stilted, robotic output on anything off-script.

**Why it happens**: too many steps, too tightly specified. The skill straitjackets Claude when the task needed flexibility.

**Fix**: match degrees of freedom to the task type. **Tight instructions** for fragile operations where every step matters (filing a Jira ticket with the right project, label, and assignee). **Loose guidance** for creative work where the structure should breathe (drafting an email response). One skill should not try to govern both.

### Killer 3: Stating the obvious

**Symptom**: the skill is bloated, hard to maintain, and the behavior does not match the length of the file.

**Why it happens**: the author wrote down everything Claude already does well. "Be polite. Use proper grammar. Format the output cleanly." Claude already does these things. Saying them adds noise without adding signal.

**Fix**: challenge every paragraph. Does Claude really need this instruction? Or is this something the model handles natively? Cut anything Claude already does. The skill should contain only what is unique to YOUR way of working.

### Killer 4: Missing gotcha section

**Symptom**: the skill works for the cases the author tested, but fails consistently on edge cases that any experienced user would have anticipated.

**Why it happens**: the author shipped the skill without writing down what could go wrong. The model never gets a chance to avoid the predictable mistakes.

**Fix**: every skill needs a gotcha section listing failure patterns you have actually seen. This is the highest-signal content in the entire skill. "Marketing emails often contain false action verbs; ignore them" is worth more than ten more lines of process steps.

### Killer 5: Monolithic structure

**Symptom**: the `SKILL.md` is 1,500 lines long, hard to navigate, and Claude starts skipping sections.

**Why it happens**: the author kept adding to the same file instead of splitting it.

**Fix**: hard cap at 500 lines. Past that, move detail into companion files in the skill folder. Reference the companion files from `SKILL.md` with one-line summaries. The main file should be a map. The reference files are the territory.

---

## The Debugging and Improvement Loop

Skills are not a write-once artifact. They evolve with your work, with model upgrades, and with the failure modes you discover in practice. Build a habit of improving them.

**If the skill is not firing when it should**, the description is the first place to look. Add more trigger phrases. Make the description louder and more specific about when to fire. Test by saying the trigger phrases out loud and watching whether the skill fires.

**If the output is wrong but the skill is firing**, the steps or the output format are the issue. Tighten the relevant step. Add a concrete output example showing exactly what good looks like. Examples beat descriptions every time.

**If you keep finding yourself cleaning up Claude's output after the skill runs**, the skill is incomplete. The cleanup logic belongs in the skill. Move it.

**Quarterly review** is the maintenance cadence. Every 90 days, review your installed skills. Re-evaluate skills when models upgrade (some capability skills will be obsolete) and when your workflow shifts (some preference skills may need new steps). Even functional skills benefit from a fresh read; you will spot bloat and outdated examples.

---

## Best Practices, Compressed

Before you build your first skill in the lab, internalize these:

- **One job per skill.** If you cannot describe the skill's purpose in one sentence, it is probably two skills. Split it.
- **The description is a trigger, not a summary.** Write for the model asking "should I fire here?" Not for the human reading the catalog.
- **Show, do not describe, the output.** A literal template is worth ten paragraphs of structural description.
- **Document gotchas explicitly.** Failure patterns are the highest-signal content you can write.
- **Match degrees of freedom to the task.** Tight for fragile operations. Loose for creative work.
- **Respect the context binding rule.** Assets about the skill live with the skill. Assets about you or your organization live outside and get referenced.
- **Keep it under 500 lines.** Move depth into companion files.
- **Ship preference skills, not capability skills.** Your competitive advantage is your methodology.

---

## Your First Mission Card

You are about to build your first preference skill: a Gmail Action Item Extractor. It reads your inbox, isolates messages from internal teammates and from ActivTrak, extracts the action items, and returns a structured to-do list. It encodes how YOU read email. Once it is in your playbook, you will trigger it with a phrase as natural as "what do I owe people from this week," and Claude will quietly do the work before you finish the question.

The lab walks you through five phases: install a shared skill so you experience the loop end-to-end, design your Gmail skill on paper, build it with Skill Builder, test it against real messages, and apply the 5-Killers framework to debug what does not work the first time.

Skills are how you stop being a Solo Pilot who types every prompt by hand. Skills are how the squadron flies in formation. Build the playbook, and the playbook flies you.

**AI drafts. Humans send. The Playbook makes the drafts predictable.**

---

**End of Module 8 Lesson**
