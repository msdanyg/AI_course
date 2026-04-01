# Module 3: Prompt Architecture
## Video Script

**Target Duration:** 6-7 minutes (~1,000 words)

---

### INTRO [0:00-0:30]

**[VISUAL: Split screen — messy prompt left, structured prompt right]**

"Here's my email, make it better and remember we don't say tracking, and the client is worried about renewal."

Versus this structured version.

Same information. Dramatically different results. The difference is structure — and you have options for how to achieve it.

Welcome to Module 3: Prompt Architecture.

---

### SECTION 1: CONTEXT BLEEDING [0:30-1:30]

**[VISUAL: Words from different prompt parts mixing together]**

When you write "Here's my email. Make it professional. Don't use the word tracking" — you're mixing data, instructions and constraints in one stream.

**[VISUAL: Example output with "don't use tracking" included in the email]**

I've seen Claude literally include "remember not to use tracking" in its output because it couldn't tell that was an instruction, not content.

This is **context bleeding**. The solution is clear separation.

---

### SECTION 2: THREE FORMATS [1:30-3:30]

**[VISUAL: Spectrum from formal to casual]**

You have three options.

**[VISUAL: XML example]**

**XML Tags** — Most precise. Opening tag, content, closing tag.

```
<context>Background info</context>
<data>Content to process</data>
<instructions>What to do</instructions>
```

Best for complex prompts and reusable templates.

**[VISUAL: Markdown example]**

**Markdown Headers** — Friendlier syntax.

```
## Role
Workforce analytics consultant

## Data
Productivity report here

## Constraints
- No surveillance language
```

Best for people who find XML uncomfortable.

**[VISUAL: Labels example]**

**Clear Labels** — Simplest approach.

```
ROLE: Customer Success Manager
DATA: Productivity down 15%
AVOID: Tracking language
TASK: Write three hypotheses
```

No special syntax. Just clear separation.

**[VISUAL: All three side by side with equals sign]**

All three work. Pick what feels natural.

---

### SECTION 3: WHEN TO USE WHAT [3:30-4:30]

**[VISUAL: Two-column comparison]**

**Use formal structure when:**
- Multiple data sources
- Creating reusable templates
- Getting inconsistent results
- Data contains Markdown formatting

**Skip it when:**
- Simple, single-purpose task
- Quick questions
- Back-and-forth conversation

The goal is clarity, not ceremony.

---

### SECTION 4: PRO TIP [4:30-5:15]

**[VISUAL: Messy notes transforming into structured format]**

Here's a technique most people don't know: ask Claude to structure messy data for you.

"Here are my rough meeting notes. Convert them into sections: Client Goals, Concerns, Action Items, Next Steps."

Claude organizes it. Now you have clean data for your next prompt.

---

### SECTION 5: COMMON MISTAKES [5:15-6:00]

**[VISUAL: Quick icons for each]**

**Vague outputs.** "Make this better" means nothing. Be specific.

**Burying instructions.** Put key instructions at the END — AI pays most attention to beginnings and endings.

**Forgetting constraints.** Every ActivTrak prompt should specify what to avoid.

**Over-engineering.** Don't write XML prompts for "fix this typo."

---

### OUTRO [6:00-6:30]

**[VISUAL: Preview of Module 4]**

Structure beats length. Clear separation beats specific syntax.

In Module 4, we tackle AI's math problem. When Claude calculates, it's guessing — predicting what the answer probably looks like. You'll learn to use Code Execution for accurate calculations every time.

See you there.

---

**[END]**

---

## Production Notes

**Key Visuals:**
1. Structure spectrum (XML → Markdown → Labels)
2. Side-by-side format comparison
3. "Messy notes → Structured output" transformation

**Tone:** Quick and practical. The message is "you have options" — we're not forcing anyone into XML.
