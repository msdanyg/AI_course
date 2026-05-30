# Module 8 Video Script - ElevenLabs Narration
## The Squadron Playbook: Building, Sharing, and Mastering Claude Skills

**TTS-optimized narration. Read straight through. Pauses encoded with break tags.**

---

How many times have you re-pasted the same context into Claude this week?

<break time="1s" />

How many times have you re-explained that you work at ActivTrak, that you prefer bullet points, that competitive analysis should always include Teramind, Hubstaff, and Insightful?

<break time="1s" />

If you are answering "more than zero," you are paying the REPETITION TAX. And in this module, you are going to stop paying it.

<break time="2s" />

Welcome to Module Eight. The Squadron Playbook.

I am going to teach you Skills. Not as a feature you can list on a resume, but as the operational system that turns you from a Solo Pilot who types every prompt by hand into a Squadron Architect who builds Mission Cards once and runs them forever.

<break time="1s" />

Let's go.

<break time="2s" />

A Skill is a packaged capability. Mechanically, it is a folder with one file inside called SKILL dot M D. That file has a name, a description, and a set of instructions. That is the whole shape.

The single most important thing to understand is this. Claude reads the description. Claude decides on its own whether to fire the skill. YOU DO NOT HAVE TO REMEMBER THE SKILL EXISTS.

<break time="1s" />

Picture this. You type a normal sentence into Claude. You do not type a slash command. You do not say "use the Gmail skill." You just ask the question. Claude scans every installed skill description, sees a match, and fires the skill before drafting a response.

That is the magic. Skills work because Claude is reading the description, not because you memorized the catalog.

<break time="2s" />

Now compare this to a Project. A Project stores documents and conversation history. It is bound to one workspace. You enter the project to use it.

A Skill is the opposite. A Skill stores methodology, steps, and output templates. It is available in every conversation, every project, every chat. Install it once. Use it everywhere.

Projects fight contextual amnesia INSIDE one mission. Skills fight contextual amnesia ACROSS every mission you fly.

<break time="2s" />

Let me show you the anatomy of a skill.

Top of the file is Y A M L frontmatter. Two fields matter. Name. And description.

<break time="1s" />

The name is gerund-form, lowercase, hyphenated. For example: extracting hyphen gmail hyphen action hyphen items. Not Gmail underscore Todo Extractor. Not email hyphen stuff. The convention exists for a reason. Claude reads thousands of skill names, and the gerund pattern signals "this is a skill, not a noun."

<break time="1s" />

The description is the trigger. This is where most skills succeed or die. Write it in third person. List the actual phrases the user says. For example: "Use when the user asks to summarize their inbox, find action items in recent emails."

The description is NOT a summary of what the skill does. It is a recognition pattern. Write it for the model asking "should I fire here?"

<break time="2s" />

The body of the skill has four near-mandatory parts. Steps. Output format. Gotchas. Constraints.

Steps are numbered, not prose. Output format is a literal template, not a description of a template. Gotchas are the failure patterns you have actually seen.

Hard rule. Keep your skill file under five hundred lines. Past that, Claude starts losing the plot. Move depth into companion files in the skill folder.

<break time="2s" />

There are two types of skills, and they age differently.

CAPABILITY UPLIFT skills add functions Claude does not do well alone. Useful, but they live on borrowed time. Every time the model upgrades, capability skills get partially obsoleted. The thing your skill teaches Claude to do, Claude eventually learns to do natively.

<break time="1s" />

ENCODED PREFERENCE skills capture YOUR way of working. Your competitive analysis structure. Your meeting prep format. Your customer success rubric. These skills do not make Claude smarter. They make Claude consistent WITH you. And these get more valuable over time.

<break time="1s" />

The Squadron Leader investment rule: spend eighty percent of your skill-building effort on encoded preference. Your competitive advantage is your methodology. Let Anthropic worry about capability uplift.

<break time="2s" />

You do not have to build every skill from scratch. Anthropic maintains an official skill catalog. The plugin ecosystem has thousands more.

Browse. Install. The skill becomes available in every conversation from that point forward. No per-project setup.

<break time="1s" />

The first skill you should install is SKILL BUILDER itself. The official name is skill hyphen creator. It is the skill that helps you build skills.

<break time="1s" />

Here is how it works. You describe the job in plain English. Skill Builder fires. It asks you clarifying questions about triggers, inputs, outputs, and edge cases. It scaffolds the skill file. You review and refine.

Where Skill Builder helps most is the structure. New authors consistently underweight the description and overweight the steps. They write a beautiful seven-step procedure with no clear trigger. The skill never fires.

Where Skill Builder needs your help is the gotcha section. Claude has not lived your work. YOU have to tell it what failure modes to avoid.

<break time="2s" />

When skills fail, they fail in five recognizable ways. Memorize this list.

<break time="1s" />

Killer one. VAGUE DESCRIPTIONS. Symptom: the skill never auto-fires. Fix: write the description in specific, loud, third person. List actual phrases the user says.

<break time="1s" />

Killer two. OVER-DEFINED PROCESSES. Symptom: works on simple cases, robotic on edge cases. Fix: match degrees of freedom to the task. Tight for fragile operations. Loose for creative work.

<break time="1s" />

Killer three. STATING THE OBVIOUS. Symptom: bloated skill, behavior does not match the file length. Fix: cut anything Claude already does well. The skill should contain only what is unique to YOUR way of working.

<break time="1s" />

Killer four. MISSING GOTCHA SECTION. Symptom: works on the cases you tested, fails on edge cases anyone could have predicted. Fix: every skill needs a gotcha section. This is the highest-signal content in the entire skill.

<break time="1s" />

Killer five. MONOLITHIC STRUCTURE. Symptom: the file is fifteen hundred lines and Claude starts skipping sections. Fix: five hundred line cap. Move detail into companion files.

<break time="2s" />

The next time a skill misbehaves, this list tells you which knob to turn.

<break time="2s" />

There is one test that tells you whether a skill is done.

If you find yourself cleaning up Claude's output AFTER the skill runs, the skill is incomplete. The fix is not to write a better follow-up prompt. The fix is to upgrade the skill.

Move the cleanup logic into the skill itself. The whole point of a skill is that you do NOT have to remember to ask for the cleanup. Encode it once, get it forever.

<break time="2s" />

Your lab is to build your first preference skill. The Gmail Action Item Extractor.

It reads your inbox. It isolates messages from internal teammates and from ActivTrak. It extracts the action items. It returns a prioritized to-do list.

<break time="1s" />

You will install a shared skill first to feel the loop. Then you will design your Gmail skill on paper. Then you will build it with Skill Builder. Then you will test it against real messages. Then you will use the Five Killers framework to debug what does not work the first time.

<break time="1s" />

When you finish the lab, you will have your first Mission Card. And once you have one, you will see opportunities for the next one everywhere.

The Solo Pilot types every prompt by hand. The Squadron Architect builds the Playbook.

<break time="1s" />

A I drafts. Humans send. The Playbook makes the drafts predictable.

<break time="1s" />

Now head to the lesson, then the lab. Build your first Mission Card.

<break time="2s" />

Mission Control out.

---

**End of Module 8 ElevenLabs Narration**
