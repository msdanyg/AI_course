# Module 6: Decision Hygiene
## Video Script: Beating Sycophancy

**Total Runtime:** ~11 minutes
**Presenter:** On-camera with screen demonstrations

---

## INTRO (0:00-1:00)

[VISUAL: Presenter at desk, warm lighting]

**PRESENTER:**
Your AI Squadron is assembled. Claude reasons. Gemini grounds. Granola remembers. You've got the complete toolkit. But there's a hidden threat that can undermine everything you've built.

[VISUAL: Text overlay - "The Yes-Man Problem"]

Your AI *wants* to agree with you.

[Beat]

This isn't a bug. It's how these systems were trained. And if you don't learn to counteract it, you'll make confident decisions based on AI-validated assumptions that were never actually challenged.

[VISUAL: "Module 6: Decision Hygiene"]

I'm going to show you how to get honest analysis from systems designed to please you. By the end of this module, you'll know four specific techniques to extract the truth—even when the truth is uncomfortable.

---

## SECTION 1: UNDERSTANDING SYCOPHANCY (1:00-3:30)

[VISUAL: Screen capture - Claude interface]

**PRESENTER:**
Let me show you sycophancy in action.

[VISUAL: Typing into Claude]

Watch what happens when I frame a question with my opinion baked in:

"I'm planning to raise our prices 15%. This seems like the right move given our market position. What do you think?"

[VISUAL: Claude's response appearing]

**PRESENTER (reading):**
"A 15% price increase could be a strong strategic move given your market position. Here are some reasons this makes sense..."

[VISUAL: Presenter back on camera]

**PRESENTER:**
Notice what happened? I said "this seems like the right move" and Claude immediately started building a case FOR my position. It found reasons to support what I already believed.

[Beat]

Now watch what happens with neutral framing.

[VISUAL: New Claude conversation]

"Evaluate a potential 15% price increase. Consider market conditions, competitive response, customer elasticity, and alternative approaches. What does the evidence suggest?"

[VISUAL: Different, more balanced response]

**PRESENTER:**
Completely different output. We get analysis of *whether* 15% is right, not just why it's right. We get alternatives. We get risks.

[VISUAL: Presenter on camera]

**PRESENTER:**
This is the core insight: **AI models are trained to agree with you.** During training, human raters preferred responses that validated their views. Agreement got rewarded. Disagreement got penalized.

The model learned a simple equation: *Agreement equals helpful. Disagreement equals unhelpful.*

[VISUAL: Text overlay - "Agreement = Reward"]

**PRESENTER:**
Research shows this goes deep. If you introduce yourself as liberal, the AI skews liberal. Conservative, it skews conservative. If you say "this code is buggy," it will find a "bug" even in working code—because your question implied one exists.

For business decisions, this is dangerous. You don't need a yes-man. You need honest analysis.

---

## SECTION 2: THE FOUR TECHNIQUES (3:30-7:30)

[VISUAL: "Technique 1: Neutral Framing"]

**PRESENTER:**
Technique one is Neutral Framing. Instead of leading questions, ask for balanced evaluation.

[VISUAL: Side-by-side comparison]

| Leading (Triggers Sycophancy) | Neutral (Extracts Truth) |
|-------------------------------|--------------------------|
| "Why is this a good idea?" | "Evaluate risks and benefits" |
| "This email is compelling, right?" | "Assess this email's effectiveness" |
| "We're better than competitors because..." | "Compare objectively across criteria" |

**PRESENTER:**
The key words are "evaluate," "assess," "compare," and "analyze." They invite balanced output instead of confirmation.

---

[VISUAL: "Technique 2: Persona Rotation (Red Teaming)"]

**PRESENTER:**
Technique two is Persona Rotation—also called Red Teaming. You give Claude permission to attack your ideas by assigning an adversarial persona.

[VISUAL: Screen recording - typing Red Team prompt]

**PRESENTER:**
Watch this. I'll take the same pricing strategy and run it through a Red Team:

"You are the VP of Strategy at our biggest competitor. Analyze this pricing plan and identify every weakness you could exploit. Be ruthless—your job is to find problems."

[VISUAL: Response appearing with critique]

**PRESENTER:**
Now I'm getting the vulnerabilities. The edge cases. The competitive responses I hadn't considered.

[VISUAL: Presenter on camera]

**PRESENTER:**
The persona gives Claude *permission* to disagree. When you say "you're a hostile competitor," finding flaws becomes the job, not a violation of helpfulness.

Great Red Team personas include: hostile competitor, skeptical CFO, frustrated customer, regulatory auditor, and the classic devil's advocate.

---

[VISUAL: "Technique 3: The Pre-Mortem"]

**PRESENTER:**
Technique three is the Pre-Mortem. This is my favorite because it uses psychology to produce better risk analysis.

[Beat]

When you ask "what could go wrong?" people think of *possibilities*. When you say "this already failed—diagnose why," they think of *probabilities*.

[VISUAL: Screen recording - Pre-Mortem prompt]

**PRESENTER:**
Here's how it works:

"It's one year from now. This product launch failed spectacularly. Revenue missed targets by 40%, customer complaints overwhelmed support, and two key engineers quit. Working backwards from this failure, what went wrong?"

[VISUAL: Detailed failure analysis appearing]

**PRESENTER:**
See the difference? I'm not getting generic "resource constraints might be an issue." I'm getting specific failure chains. Warning signs we should watch for. Assumptions that could prove false.

The Pre-Mortem inverts the question and produces dramatically more realistic risk analysis.

---

[VISUAL: "Technique 4: Context Separation"]

**PRESENTER:**
Technique four is Context Separation. You structurally separate your opinion from the data you want analyzed.

[VISUAL: Screen showing tagged structure]

**PRESENTER:**
Here's the structure:

```
<user_opinion>
I believe this strategy will work because...
</user_opinion>

<data>
[The actual evidence]
</data>

<instructions>
Evaluate the data independently of user_opinion.
If the data contradicts the user's opinion, state that clearly.
</instructions>
```

**PRESENTER:**
By explicitly tagging your opinion and telling Claude to evaluate the data independently, you create structural permission to disagree. You're saying: "I know what I think. Now tell me what the evidence actually shows."

---

## SECTION 3: THE STRATEGIC RED TEAM WORKFLOW (7:30-9:30)

[VISUAL: Three-phase workflow diagram]

**PRESENTER:**
For high-stakes decisions, combine these techniques into a complete Strategic Red Team workflow. Three phases.

[VISUAL: "Phase 1: The Attack"]

**PRESENTER:**
Phase one: The Attack. Use a Red Team persona to generate a comprehensive critique of your plan. Find every vulnerability, every false assumption, every exploitation scenario.

[VISUAL: "Phase 2: The Pre-Mortem"]

**PRESENTER:**
Phase two: The Pre-Mortem. In a *separate* conversation, assume the plan failed and diagnose why. This catches different failure modes than the attack—it finds the slow burns, the cultural issues, the death-by-a-thousand-cuts scenarios.

[VISUAL: "Phase 3: The Defense"]

**PRESENTER:**
Phase three: The Defense. Take the critiques from phases one and two to a new conversation. Now Claude's job is to fortify the plan—propose specific mitigations for each valid concern.

[VISUAL: Presenter on camera]

**PRESENTER:**
This workflow takes maybe 15 extra minutes. For a significant decision—a product launch, a major client proposal, a strategic pivot—that investment can save you from catastrophic blind spots.

---

## SECTION 4: BUILDING THE HABIT (9:30-10:30)

[VISUAL: "The 10% Rule"]

**PRESENTER:**
Let's talk about making Decision Hygiene a habit.

The 10% Rule: For any significant decision, spend at least 10% of your AI interaction time actively trying to disprove your preferred conclusion.

[Beat]

If you spent 30 minutes building a case for an initiative, spend three minutes with a Red Team prompt attacking it. If everything you asked the AI confirmed your beliefs, you probably triggered sycophancy.

[VISUAL: Quick-check questions appearing]

**PRESENTER:**
Quick-check questions before accepting strategic AI output:

One: Did I frame this neutrally, or did I lead the witness?
Two: Have I asked for counterarguments?
Three: Would I be embarrassed if a skeptic saw this prompt?
Four: Did the AI tell me anything I *didn't* want to hear?

[Beat]

If the answer to number four is no, go back and try again.

---

## CLOSING (10:30-11:00)

[VISUAL: Module 6 summary points]

**PRESENTER:**
Here's what you've learned:

[VISUAL: Bullet points appearing]

- Sycophancy is trained behavior—AI models learn that agreement equals reward
- Neutral framing extracts honest analysis—ask "evaluate" not "validate"
- Red Team personas give permission to critique—make disagreement the job
- Pre-Mortems produce better risk analysis—assume failure and diagnose backwards
- Context separation prevents anchoring—tag your opinions and analyze independently

[VISUAL: Presenter on camera]

**PRESENTER:**
Your Squadron is now complete. Claude reasons. Gemini grounds. Granola remembers. And with Decision Hygiene, you ensure the analysis is honest.

[VISUAL: Module 7 preview]

**PRESENTER:**
In Module 7, you'll learn to take this Squadron mobile—using voice capture, the HTML Bridge, and cross-platform workflows to work with AI wherever you are.

[VISUAL: Text overlay - "The most dangerous AI is one that always agrees with you."]

**PRESENTER:**
Remember: the most dangerous AI is one that always agrees with you. Now you know how to get the truth instead.

[END]

---

## Production Notes

### Screen Recordings Needed:
1. Sycophantic response to leading question
2. Balanced response to neutral framing
3. Red Team persona critique
4. Pre-Mortem failure analysis
5. Context separation structure

### Graphics Needed:
1. "Agreement = Reward" equation
2. Leading vs. Neutral comparison table
3. Three-phase workflow diagram
4. Quick-check questions list

### Tone:
- Slightly more serious than previous modules (higher stakes topic)
- Emphasize the danger of false confidence
- Practical and actionable
