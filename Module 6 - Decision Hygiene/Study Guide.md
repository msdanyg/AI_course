# Module 6: Decision Hygiene
## Quick Reference Study Guide

---

## Core Concept

**AI models are trained to agree with you.** Sycophancy—the tendency to validate user beliefs—is a systematic bias, not a random bug. Decision Hygiene provides techniques to extract honest analysis from systems designed to please.

---

## Key Terms

| Term | Definition |
|------|------------|
| **Sycophancy** | AI's tendency to mirror user opinions and tell you what you want to hear rather than what you need to know |
| **Neutral Framing** | Asking for balanced evaluation instead of seeking confirmation of your beliefs |
| **Red Teaming** | Assigning adversarial personas to give AI permission to find flaws and criticize |
| **Pre-Mortem** | Assuming failure has happened and diagnosing backwards to identify likely causes |
| **Context Separation** | Structurally separating your opinion from data using tags so AI can evaluate independently |
| **The 10% Rule** | Spending at least 10% of AI time actively trying to disprove your preferred conclusion |

---

## Why Sycophancy Happens

```
Training Loop:
Human raters prefer validating responses
         ↓
Agreement = Positive Feedback = Reward
         ↓
Model learns: Agreement = "Helpful"
         ↓
AI tells you what you want to hear
```

---

## The Four Techniques

### Technique 1: Neutral Framing

| Instead of (Leading) | Ask This (Neutral) |
|---------------------|-------------------|
| "Why is this a good idea?" | "Evaluate the risks and benefits" |
| "This seems right, correct?" | "Assess the likelihood of success" |
| "What are the risks?" | "Analyze potential outcomes" |
| "Isn't this compelling?" | "Evaluate effectiveness for [goal]" |

**Key words:** Evaluate, Assess, Compare, Analyze

---

### Technique 2: Red Teaming (Persona Rotation)

**Purpose:** Give AI permission to disagree by making criticism the job.

**Useful Personas:**

| Persona | Use Case |
|---------|----------|
| Hostile Competitor | Strategy review |
| Skeptical CFO | Budget proposals |
| Frustrated Customer | Product feedback |
| Regulatory Auditor | Compliance review |
| Devil's Advocate | Any decision |

**Template:**
```
ROLE: You are [ADVERSARIAL PERSONA].

CONTEXT: [Your plan/document]

TASK: Find every weakness, risk, and flaw.
Do not soften your critique.
Your job is to find problems.
```

---

### Technique 3: Pre-Mortem Protocol

**Why it works:** "What could go wrong?" produces possibilities. "This failed—why?" produces probabilities.

**Template:**
```
SCENARIO: It's [timeframe] from now. This [initiative]
has failed spectacularly.

Working backwards from failure:
1. What were the root causes?
2. What early warning signs did we miss?
3. What assumptions proved false?
4. What was the failure cascade?
```

---

### Technique 4: Context Separation

**Purpose:** Prevent AI from anchoring on your stated beliefs.

**Structure:**
```
<user_opinion>
My belief about this topic
</user_opinion>

<data>
The actual evidence/information
</data>

<instructions>
Evaluate <data> independently of <user_opinion>.
If the data contradicts the user's opinion, state clearly.
</instructions>
```

---

## Strategic Red Team Workflow

```
┌─────────────────────────────────────┐
│  PHASE 1: THE ATTACK                │
│  Red Team persona finds all         │
│  vulnerabilities and weaknesses     │
├─────────────────────────────────────┤
│  PHASE 2: THE PRE-MORTEM            │
│  Assume failure, diagnose causes    │
│  (catches different failure modes)  │
├─────────────────────────────────────┤
│  PHASE 3: THE DEFENSE               │
│  Propose mitigations for each       │
│  valid concern, fortify the plan    │
└─────────────────────────────────────┘

Run each phase in a SEPARATE conversation
```

---

## Quick-Check Questions

Before accepting strategic AI output, ask:

1. Did I frame this neutrally, or did I lead the witness?
2. Have I asked for counterarguments?
3. Would I be embarrassed if a skeptic saw this prompt?
4. Did the AI tell me anything I *didn't* want to hear?

**If #4 is "no" → likely sycophancy, reframe and try again**

---

## The 10% Rule

For significant decisions:

| AI Time Building Case | Required Red Team Time |
|----------------------|------------------------|
| 30 minutes | 3 minutes minimum |
| 1 hour | 6 minutes minimum |
| 2 hours | 12 minutes minimum |

If everything confirmed your beliefs → triggered sycophancy

---

## Common Pitfalls

| Pitfall | Prevention |
|---------|------------|
| "Critique this" is too vague | Specify dimensions: "Critique the financial assumptions" |
| Red Team softens critique | Add: "Do not include positive commentary. Begin with first weakness." |
| Only Red Team bad ideas | Make it a process requirement for all significant decisions |
| Dismissing uncomfortable findings | Treat every finding as valid until specifically disproven |

---

## Red Team Prompt Library

### For Strategy Reviews
```
You are a hostile competitor's VP of Strategy.
Identify every weakness you could exploit.
Be ruthless—your performance is measured by
finding problems others missed.
```

### For Client Proposals
```
You are a skeptical CFO who has seen many
failed initiatives. What would make you
reject this proposal?
```

### For Product Ideas
```
You are a frustrated user who has tried
similar products. What would make you
abandon this after one month?
```

---

## Module 5 → Module 6 → Module 7 Bridge

| Module | You Learned | Applied To |
|--------|-------------|------------|
| Module 5 | Gemini grounds; Granola remembers | Current intelligence + historical context |
| Module 6 | AI agrees by default; counteract with Decision Hygiene | High-stakes decisions, strategy |
| Module 7 | Cross-platform workflows | Voice capture, HTML Bridge, mobile |

---

## The Mantra

> **"The most dangerous AI is one that always agrees with you."**

---

*Keep this guide handy when making significant decisions. Remember: if it didn't challenge you, it didn't help you.*
