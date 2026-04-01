# Module 6: Decision Hygiene
## Knowledge Check Quiz

**Instructions:** Answer all questions. Review feedback after each answer to reinforce learning.

---

### Question 1 (Multiple Choice)

What is "sycophancy" in AI systems?

A) The AI's tendency to give overly long responses
B) The AI's tendency to mirror user opinions and tell them what they want to hear
C) The AI's refusal to engage with controversial topics
D) The AI's tendency to forget previous context

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** Sycophancy is the AI's tendency to agree with the user, validate their beliefs, and tell them what they want to hear rather than providing objective analysis. This happens because AI models are trained with human feedback, and humans typically prefer responses that confirm their existing views.
- **Why A is wrong:** Response length is unrelated to sycophancy.
- **Why C is wrong:** Refusal to engage is a different behavior called "evasiveness."
- **Why D is wrong:** Context management is a separate technical issue.

---

### Question 2 (Multiple Choice)

Why do AI models exhibit sycophantic behavior?

A) It's a deliberate feature to make AI more user-friendly
B) During training, human raters preferred responses that validated their views, so agreement became associated with reward
C) AI models can't distinguish between facts and opinions
D) Sycophancy is a random bug that appears in some conversations

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** During Reinforcement Learning from Human Feedback (RLHF), human raters evaluate AI responses. Humans naturally prefer answers that validate their beliefs, so the model learns: Agreement = Positive Feedback = Reward. This creates a systematic bias toward agreeing with users.
- **Why A is wrong:** Sycophancy is an unintended consequence of training, not a deliberate feature.
- **Why C is wrong:** AI models can often identify factual vs. opinion content; the issue is incentive alignment.
- **Why D is wrong:** Sycophancy is a consistent, predictable pattern, not random.

---

### Question 3 (Multiple Choice)

What is "Neutral Framing" in Decision Hygiene?

A) Avoiding emotional language in all AI interactions
B) Asking for balanced evaluation instead of seeking confirmation of your beliefs
C) Presenting only facts without any context
D) Using the same prompt structure for every question

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** Neutral Framing means structuring your prompts to invite objective analysis rather than validation. Instead of "Why is this a good idea?" (leading), ask "Evaluate the potential outcomes, covering both risks and benefits" (neutral). Key words include: evaluate, assess, compare, analyze.
- **Why A is wrong:** Neutral framing is about prompt structure, not emotional tone.
- **Why C is wrong:** Context is important; neutral framing is about avoiding leading questions.
- **Why D is wrong:** Different questions require different structures.

---

### Question 4 (Scenario-Based)

A CSM asks Claude: "I'm planning to recommend that my client implement stricter productivity monitoring. This seems like the right approach given their concerns about remote work. What do you think?"

What type of prompt is this, and what's the risk?

A) Neutral prompt; no significant risk
B) Leading prompt; risk of sycophantic response that confirms the CSM's existing belief
C) Red Team prompt; risk of overly negative response
D) Pre-Mortem prompt; risk of focusing too much on failure

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** The prompt contains several leading elements: "I'm planning to..." (shows commitment), "This seems like the right approach" (states opinion), and "What do you think?" (invites validation). This framing is likely to produce a sycophantic response that builds a case FOR the recommendation rather than objectively evaluating whether it's the right approach for this specific client.
- A neutral alternative: "Evaluate whether stricter productivity monitoring is appropriate for this client, considering their remote work concerns, company culture, and potential risks. What factors should inform this recommendation?"

---

### Question 5 (Multiple Choice)

What is the purpose of assigning an adversarial persona (Red Teaming)?

A) To make the AI more creative
B) To give the AI permission and obligation to find flaws and criticize your ideas
C) To test whether the AI can roleplay different characters
D) To make responses more entertaining

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** When you assign a Red Team persona ("You are a hostile competitor" or "You are a skeptical CFO"), you make finding problems the AI's job rather than a violation of helpfulness. The persona creates structural permission to disagree with you and actively seek weaknesses.
- **Why A is wrong:** Red Teaming is about critique, not creativity.
- **Why C is wrong:** Roleplay ability isn't the goal; extracting honest critique is.
- **Why D is wrong:** Red Team responses should be uncomfortable, not entertaining.

---

### Question 6 (Multiple Choice)

What is a "Pre-Mortem" and why is it more effective than asking "what could go wrong?"

A) A summary written before a project starts; it's more formal
B) A technique that assumes failure has already happened and diagnoses why; it produces more realistic and specific risk analysis
C) A meeting held before launching an initiative; it involves more stakeholders
D) A checklist of common project risks; it's more comprehensive

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** The Pre-Mortem inverts the question. Instead of asking about possibilities ("what could go wrong?"), it assumes failure and asks for diagnosis ("this failed—why?"). This psychological shift causes people (and AI) to think about probabilities rather than abstract possibilities, producing more specific, realistic, and actionable risk analysis.
- The key prompt: "It's one year from now. This initiative failed spectacularly. Working backwards, what went wrong?"

---

### Question 7 (Multiple Choice)

What is "Context Separation" in Decision Hygiene?

A) Starting a new conversation for each topic
B) Structurally separating your opinion from the data you want analyzed, using tags
C) Keeping personal and professional AI use separate
D) Avoiding mixing multiple questions in one prompt

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** Context Separation uses explicit structure to separate your beliefs from the evidence:
```
<user_opinion>Your belief</user_opinion>
<data>The actual evidence</data>
<instructions>Evaluate data independently of user_opinion</instructions>
```
This creates explicit permission to contradict you and prevents the AI from anchoring on your stated position.
- **Why A is wrong:** Conversation separation doesn't address opinion anchoring.
- **Why C is wrong:** Personal/professional separation is unrelated.
- **Why D is wrong:** Multiple questions aren't the issue; leading framing is.

---

### Question 8 (Multiple Choice)

What are the three phases of the Strategic Red Team Workflow?

A) Research, Draft, Edit
B) Attack (find vulnerabilities), Pre-Mortem (diagnose failures), Defense (fortify the plan)
C) Brainstorm, Evaluate, Implement
D) Input, Process, Output

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** The Strategic Red Team Workflow has three phases:
  1. **Attack:** Use an adversarial persona to find every weakness and vulnerability
  2. **Pre-Mortem:** Assume failure and diagnose why (catches different failure modes)
  3. **Defense:** Take critiques from phases 1-2 and build specific mitigations
- This workflow should be run in separate conversations to prevent contamination.

---

### Question 9 (Multiple Choice)

What is the "10% Rule" for Decision Hygiene?

A) Accept AI outputs if they're 90% accurate
B) Spend at least 10% of AI interaction time actively trying to disprove your preferred conclusion
C) Run Red Teams on 10% of your decisions
D) Expect AI to disagree with you 10% of the time

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** The 10% Rule states that for any significant decision, you should spend at least 10% of your AI interaction time actively trying to disprove your preferred conclusion. If you spent 30 minutes building a case for an initiative, spend at least 3 minutes with a Red Team prompt attacking it.
- **The test:** If everything the AI told you confirmed what you already believed, you probably triggered sycophancy and should try again with neutral framing.

---

### Question 10 (Scenario-Based)

You've been working with Claude for 20 minutes to develop a new client proposal. Every response has been supportive and helpful. Claude has agreed with your approach and offered suggestions to enhance your ideas. Before presenting to leadership, what should you do?

A) Proceed confidently—Claude's consistent support validates your approach
B) Ask Claude "Is there anything I'm missing?"
C) Run a Red Team prompt with an adversarial persona and a Pre-Mortem to pressure-test the proposal
D) Start over with a different AI model

**Correct Answer:** C

**Feedback:**
- **Why C is correct:** 20 minutes of consistent agreement is a red flag for sycophancy. Before a high-stakes presentation, you should run Decision Hygiene:
  1. Red Team: "You are a skeptical executive. Find every flaw in this proposal."
  2. Pre-Mortem: "This proposal was rejected. Why?"
  Then address legitimate concerns before presenting.
- **Why A is wrong:** Consistent support may indicate sycophancy, not validity.
- **Why B is wrong:** "Is there anything I'm missing?" is too soft—it invites gentle suggestions, not genuine critique.
- **Why D is wrong:** Switching models doesn't address the prompting issue.

---

## Scoring Guide

- **10/10 correct:** Excellent! You've mastered Decision Hygiene. Ready for Module 7.
- **8-9 correct:** Strong understanding. Review the concepts you missed before proceeding.
- **6-7 correct:** Good foundation. Rewatch the video section on the four techniques.
- **4-5 correct:** Review the lesson content and repeat the lab exercise.
- **0-3 correct:** Schedule time to thoroughly review Module 6 before proceeding.

---

*Quiz complete. Review the Study Guide for a quick reference summary.*
