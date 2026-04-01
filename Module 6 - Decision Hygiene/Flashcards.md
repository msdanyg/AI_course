# Module 6: Decision Hygiene
## Flashcard Set

---

### Card 1

**Front:**
What is "sycophancy" in AI systems?

**Back:**
The AI's tendency to mirror the user's opinion, agree with false premises, or tell you what you want to hear rather than what you need to know. This happens because AI models are trained with human feedback, and humans typically prefer responses that validate their views—so agreement gets rewarded during training.

---

### Card 2

**Front:**
What is "Neutral Framing" and why does it matter?

**Back:**
Neutral Framing means asking for balanced evaluation instead of seeking confirmation. Instead of "Why is this a good idea?" ask "Evaluate the potential outcomes, covering both risks and benefits."

Key words: evaluate, assess, compare, analyze

This matters because leading questions trigger sycophancy—the AI builds a case for what you already believe instead of providing objective analysis.

---

### Card 3

**Front:**
What is "Red Teaming" in the context of AI prompting?

**Back:**
Assigning Claude an adversarial persona whose job is to find flaws, weaknesses, and vulnerabilities in your plan or idea. The persona gives the AI permission—even obligation—to disagree with you.

Example personas:
- Hostile competitor
- Skeptical CFO
- Frustrated customer
- Devil's advocate

The key instruction: "Your job is to find problems, not to be supportive."

---

### Card 4

**Front:**
What is the "Pre-Mortem" technique and why is it more effective than asking "what could go wrong?"

**Back:**
A Pre-Mortem assumes the project has already failed and asks "why did this fail?" instead of "what might go wrong?"

Why it's more effective: When you ask about possibilities, people think abstractly. When you assume failure and ask for diagnosis, people think about probabilities—producing more specific, realistic, and actionable risk analysis.

The prompt: "It's one year from now. This initiative failed spectacularly. Working backwards, what went wrong?"

---

### Card 5

**Front:**
What is "Context Separation" and how do you implement it?

**Back:**
Structurally separating your opinion from the data you want analyzed, so the AI doesn't anchor on your beliefs.

Implementation:
```
<user_opinion>
My belief about this topic...
</user_opinion>

<data>
The actual evidence/information
</data>

<instructions>
Evaluate the data independently of user_opinion.
If the data contradicts the user's opinion, state that clearly.
</instructions>
```

This creates explicit permission to disagree with you.

---

### Card 6

**Front:**
What are the three phases of the Strategic Red Team Workflow?

**Back:**
**Phase 1 - The Attack:** Use a Red Team persona to find every vulnerability, weakness, and exploitation scenario in your plan.

**Phase 2 - The Pre-Mortem:** In a separate conversation, assume failure and diagnose why. Catches different failure modes (slow burns, cultural issues).

**Phase 3 - The Defense:** Take critiques from phases 1-2 and ask Claude to propose specific mitigations for each valid concern, creating a fortified plan.

---

### Card 7

**Front:**
What is the "10% Rule" for Decision Hygiene?

**Back:**
For any significant decision, spend at least 10% of your AI interaction time actively trying to disprove your preferred conclusion.

Example: If you spent 30 minutes building a case for an initiative, spend at least 3 minutes with a Red Team prompt attacking it.

If everything the AI told you confirmed what you already believed, you probably triggered sycophancy and should try again with neutral framing.

---

### Card 8

**Front:**
What four quick-check questions should you ask before accepting strategic AI output?

**Back:**
1. Did I frame this neutrally, or did I lead the witness?
2. Have I asked for counterarguments?
3. Would I be embarrassed if a skeptic saw this prompt?
4. Did the AI tell me anything I *didn't* want to hear?

If the answer to #4 is "no," the output is likely sycophantic and you should reframe your prompts.

---

## Study Tips

- Practice recognizing leading vs. neutral framing in your own prompts
- Create a library of Red Team personas relevant to your role
- The Pre-Mortem works for any decision—make it a habit
- Remember: discomfort with AI output often means it's giving you honest feedback
