# Module 8 Video Script
## The Squadron Playbook: Building, Sharing, and Mastering Claude Skills

**Duration:** ~10 minutes
**Format:** Talking head with screen demonstrations

---

## SCENE 1: COLD OPEN (0:00 – 0:45)

**[SCREEN: Squadron Leader badge animation, then fade to a Claude conversation showing the same long context block being pasted three times in three different chats]**

**NARRATOR:**

How many times have you re-pasted the same context into Claude this week?

How many times have you re-explained that you work at ActivTrak, that you prefer bullet points, that competitive analysis should always include Teramind, Hubstaff, and Insightful?

If you are answering "more than zero," you are paying the **repetition tax**. And in this module, you are going to stop paying it.

**[SCREEN: Title card — "Module 8: The Squadron Playbook"]**

I am going to teach you Skills. Not as a feature you can list on a resume, but as the operational system that turns you from a Solo Pilot who types every prompt by hand into a Squadron Architect who builds Mission Cards once and runs them forever.

Let's go.

---

## SCENE 2: WHAT SKILLS ACTUALLY ARE (0:45 – 2:30)

**[SCREEN: Side-by-side diagram. Left: "PROJECT — persistent context, bound to one workspace." Right: "SKILL — portable methodology, available everywhere."]**

A Skill is a packaged capability. Mechanically, it is a folder with one file inside called `SKILL.md`. That file has a name, a description, and a set of instructions. That is the whole shape.

The single most important thing to understand is this. Claude reads the description. Claude decides on its own whether to fire the skill. **You do not have to remember the skill exists.**

**[SCREEN: Demo — type "what do I owe people from this week" and watch Claude auto-invoke a Gmail skill]**

Watch this. I type a normal sentence. I do not type a slash command. I do not say "use the Gmail skill." I just ask the question. Claude scans every installed skill description, sees a match, and fires the skill before drafting a response.

That is the magic. Skills work because Claude is reading the description, not because you memorized the catalog.

**[SCREEN: Comparison table — Project vs Skill]**

Now compare this to a Project. A Project stores documents and conversation history. It is bound to one workspace. You enter the project to use it.

A Skill is the opposite. A Skill stores methodology, steps, and output templates. It is available in every conversation, every project, every chat. Install it once. Use it everywhere.

Projects fight contextual amnesia inside one mission. Skills fight contextual amnesia across every mission you fly.

---

## SCENE 3: ANATOMY OF A SKILL (2:30 – 4:00)

**[SCREEN: Annotated SKILL.md file with callouts pointing at each section]**

Let me show you the anatomy.

Top of the file is YAML frontmatter. Two fields matter: `name` and `description`.

**[SCREEN: Highlight the name field]**

The name is gerund-form, lowercase, hyphenated. `extracting-gmail-action-items`. Not `Gmail_TodoExtractor`. Not `email-stuff`. The convention exists for a reason. Claude reads thousands of skill names, and the gerund pattern signals "this is a skill, not a noun."

**[SCREEN: Highlight the description field, zoom in on it]**

The description is the trigger. This is where most skills succeed or die. Write it in third person. List the actual phrases the user says. "Use when the user asks to summarize their inbox, find action items in recent emails..."

The description is **not a summary** of what the skill does. It is a recognition pattern. Write it for the model asking "should I fire here?"

**[SCREEN: Scroll down to the markdown body, highlight each section as narrator names it]**

The body has four near-mandatory parts. Steps. Output format. Gotchas. Constraints.

Steps are numbered, not prose. Output format is a literal template, not a description of a template. Gotchas are the failure patterns you have actually seen.

Hard rule: keep `SKILL.md` under 500 lines. Past that, Claude starts losing the plot. Move depth into companion files in the skill folder.

---

## SCENE 4: TWO TYPES OF SKILLS (4:00 – 5:00)

**[SCREEN: Two-column visual. Left: "Capability Uplift" with a downward-trending chart. Right: "Encoded Preference" with an upward-trending chart.]**

There are two types of skills, and they age differently.

**Capability uplift** skills add functions Claude does not do well alone. Useful, but they live on borrowed time. Every time the model upgrades, capability skills get partially obsoleted. The thing your skill teaches Claude to do, Claude eventually learns to do natively.

**Encoded preference** skills capture YOUR way of working. Your competitive analysis structure. Your meeting prep format. Your customer success rubric. These skills do not make Claude smarter. They make Claude consistent **with you**. And these get more valuable over time.

**[SCREEN: Squadron Leader investment rule — 80% preference / 20% capability]**

The Squadron Leader investment rule: spend 80 percent of your skill-building effort on encoded preference. Your competitive advantage is your methodology. Let Anthropic worry about capability uplift.

---

## SCENE 5: FINDING AND CREATING SKILLS (5:00 – 6:30)

**[SCREEN: Skill catalog browser inside Claude]**

You do not have to build every skill from scratch. Anthropic maintains an official skill catalog. The plugin ecosystem has thousands more.

**[SCREEN: Click install on a skill]**

Browse. Install. The skill becomes available in every conversation from that point forward. No per-project setup.

The first skill you should install is **Skill Builder** itself. The official name is `skill-creator`. It is the skill that helps you build skills.

**[SCREEN: Demo conversation — narrator says "I want to build a skill that helps me prep for QBRs"]**

Watch how this works. I describe the job in plain English. Skill Builder fires. It asks me clarifying questions about triggers, inputs, outputs, and edge cases. It scaffolds the SKILL.md file. I review and refine.

Where Skill Builder helps most is the structure. New authors consistently underweight the description and overweight the steps. They write a beautiful seven-step procedure with no clear trigger. The skill never fires.

Where Skill Builder needs your help is the gotcha section. Claude has not lived your work. **You** have to tell it what failure modes to avoid.

---

## SCENE 6: THE FIVE SKILL KILLERS (6:30 – 8:30)

**[SCREEN: Title card — "The 5 Skill Killers"]**

When skills fail, they fail in five recognizable ways. Memorize this list.

**[SCREEN: Killer 1 callout]**

**Killer one. Vague descriptions.** Symptom: the skill never auto-fires. Fix: write the description in specific, loud, third person. List actual phrases the user says.

**[SCREEN: Killer 2 callout]**

**Killer two. Over-defined processes.** Symptom: works on simple cases, robotic on edge cases. Fix: match degrees of freedom to the task. Tight for fragile operations. Loose for creative work.

**[SCREEN: Killer 3 callout]**

**Killer three. Stating the obvious.** Symptom: bloated skill, behavior does not match the file length. Fix: cut anything Claude already does well. The skill should contain only what is unique to YOUR way of working.

**[SCREEN: Killer 4 callout]**

**Killer four. Missing gotcha section.** Symptom: works on the cases you tested, fails on edge cases anyone could have predicted. Fix: every skill needs a gotcha section. This is the highest-signal content in the entire skill.

**[SCREEN: Killer 5 callout]**

**Killer five. Monolithic structure.** Symptom: the file is 1,500 lines and Claude starts skipping sections. Fix: 500-line cap. Move detail into companion files.

**[SCREEN: All five killers on one slide]**

Print this slide. Pin it next to your monitor. The next time a skill misbehaves, this list tells you which knob to turn.

---

## SCENE 7: THE LITMUS TEST (8:30 – 9:00)

**[SCREEN: Quote card — "If you find yourself iterating on the output AFTER the skill runs, the skill itself needs improvement."]**

There is one test that tells you whether a skill is done.

If you find yourself cleaning up Claude's output **after** the skill runs, the skill is incomplete. The fix is not to write a better follow-up prompt. The fix is to upgrade the skill.

Move the cleanup logic into the skill itself. The whole point of a skill is that you do **not** have to remember to ask for the cleanup. Encode it once, get it forever.

---

## SCENE 8: WHAT YOU ARE ABOUT TO BUILD (9:00 – 10:00)

**[SCREEN: Lab preview — Gmail Action Item Extractor wireframe]**

Your lab is to build your first preference skill. The Gmail Action Item Extractor.

It reads your inbox. It isolates messages from internal teammates and from ActivTrak. It extracts the action items. It returns a prioritized to-do list.

You will install a shared skill first to feel the loop. Then you will design your Gmail skill on paper. Then you will build it with Skill Builder. Then you will test it against real messages. Then you will use the Five Killers framework to debug what does not work the first time.

**[SCREEN: Squadron Leader badge with "Playbook" overlay]**

When you finish the lab, you will have your first Mission Card. And once you have one, you will see opportunities for the next one everywhere.

The Solo Pilot types every prompt by hand. The Squadron Architect builds the Playbook.

**AI drafts. Humans send. The Playbook makes the drafts predictable.**

Mission Control out.

---

**End of Module 8 Video Script**
