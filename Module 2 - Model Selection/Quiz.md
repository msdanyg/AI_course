# Module 2: Model Selection & The "Thinking" Protocol
## Knowledge Check Quiz

**Instructions:** Answer all questions. Review feedback after each answer to reinforce learning.

---

### Question 1 (Multiple Choice)

Which Claude model tier should you use for categorizing 500 customer support tickets into "Technical," "Billing," or "Feature Request"?

A) Opus with Extended Thinking for maximum accuracy
B) Sonnet for balanced performance
C) Haiku for speed and cost efficiency
D) It doesn't matter—all models perform the same on this task

**Correct Answer:** C

**Feedback:**
- **Why C is correct:** This is a simple classification task with high volume. Haiku excels here—it's fast enough to process 500 tickets efficiently and costs roughly 1/60th of Opus. The task doesn't require deep reasoning, just pattern recognition.
- **Why A is wrong:** Opus with Extended Thinking is massive overkill. You'd spend 60x more and wait much longer for no quality improvement on this simple task.
- **Why B is wrong:** Sonnet would work, but it's more expensive than necessary. Save Sonnet for tasks that actually benefit from its capabilities.
- **Why D is wrong:** All models would produce similar quality on this task, but the cost and speed differences are significant. Model selection matters even when quality doesn't differ.

---

### Question 2 (True/False with Explanation)

**Statement:** Extended Thinking is primarily useful because it makes Claude respond faster.

A) True
B) False

**Correct Answer:** B (False)

**Feedback:**
Extended Thinking actually makes responses *slower*, not faster. Its value is *accuracy*, not speed. Extended Thinking gives Claude a "scratchpad" to reason through problems before committing to an answer. This deliberate processing catches errors that fast pattern-matching (System 1) would miss—especially on mathematical and logical reasoning tasks. You're trading latency for intelligence.

---

### Question 3 (Multiple Choice)

You need to analyze a complex customer situation with conflicting signals and prepare a strategic recommendation for an executive presentation. The output goes directly to leadership. Which model/mode combination is most appropriate?

A) Haiku (standard mode)
B) Sonnet (standard mode)
C) Sonnet with Extended Thinking
D) Opus with Extended Thinking

**Correct Answer:** D

**Feedback:**
- **Why D is correct:** This task has two critical factors: (1) Complex with ambiguous inputs requiring strategic judgment—that's Opus territory. (2) Low error tolerance since it goes directly to executives—that calls for Extended Thinking. The combination ensures deep reasoning with self-verification.
- **Why A is wrong:** Haiku lacks the reasoning depth for strategic analysis with conflicting information.
- **Why B is wrong:** Sonnet might handle this adequately, but for executive-facing strategic work, you want the nuance Opus provides.
- **Why C is wrong:** Extended Thinking with Sonnet would help, but for truly complex strategic analysis, Opus's deeper reasoning capability is worth the additional cost.

---

### Question 4 (Scenario-Based)

A colleague says: "I always use Opus because I want the best results." What's wrong with this approach? Select all that apply.

A) Opus costs significantly more per token than other models
B) Opus is slower, which breaks iteration flow on simple tasks
C) Simple tasks don't benefit from Opus's deep reasoning
D) Opus actually produces worse results on simple tasks

**Correct Answers:** A, B, C

**Feedback:**
- **A is correct:** Opus costs roughly 60x more per token than Haiku. For simple tasks, this cost provides no benefit.
- **B is correct:** Opus's slower response time interrupts the rapid iteration that simple tasks benefit from.
- **C is correct:** Deep reasoning capabilities are wasted on tasks like translations or simple lookups—the output quality is identical.
- **D is incorrect:** Opus doesn't produce *worse* results on simple tasks; it just doesn't produce *better* results. The issue is waste, not degradation.

The principle: Match resources to requirements. Don't default to the most expensive option.

---

### Question 5 (Multiple Choice)

What are the two axes of the model selection decision matrix?

A) Speed and Cost
B) Task Complexity and Error Tolerance
C) Model Size and Response Time
D) Accuracy and Creativity

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** The decision matrix uses Task Complexity (Simple → Standard → Complex) and Error Tolerance (High → Low) to guide model selection. Simple tasks with high tolerance → Haiku. Complex tasks with low tolerance → Opus with Extended Thinking.
- **Why A is wrong:** Speed and cost are *outcomes* of model choice, not decision inputs.
- **Why C is wrong:** These are technical characteristics, not task-assessment criteria.
- **Why D is wrong:** While relevant to outputs, these aren't the axes we use for systematic model selection.

---

### Question 6 (Multiple Choice)

What should you look for in the Thinking Block to verify Claude's reasoning is sound?

A) The response should be short to show efficiency
B) Problem decomposition, checking work, and self-correction
C) Complex vocabulary and technical jargon
D) Agreement with your initial hypothesis

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** Good thinking blocks show: breaking problems into steps, considering multiple approaches, checking intermediate results, and self-correction ("Wait, that's not right..."). These indicate genuine reasoning rather than pattern-matching.
- **Why A is wrong:** Length isn't the indicator—thoroughness is. A good thinking block for a complex problem should be detailed.
- **Why C is wrong:** Jargon doesn't indicate quality reasoning. Clear step-by-step logic does.
- **Why D is wrong:** Actually, if the thinking block only confirms your hypothesis without considering alternatives, that's a warning sign of potential sycophancy or shallow analysis.

---

### Question 7 (Scenario-Based)

You need to verify that a revenue calculation is correct: "Q1 ($2.3M) + Q2 ($1.8M) + Q3 ($2.1M) = $6.2M total." Which approach is best?

A) Ask Haiku to confirm—it's a simple lookup
B) Ask Sonnet in standard mode—it's basic math
C) Use any model with Extended Thinking—math needs verification
D) No AI needed—just use a calculator

**Correct Answer:** C (or D)

**Feedback:**
- **Why C is correct:** Mathematical reasoning benefits from Extended Thinking regardless of how "simple" it looks. Standard mode pattern-matches numbers rather than calculating, which leads to confident wrong answers. Extended Thinking forces step-by-step verification.
- **Why D is also acceptable:** For straightforward arithmetic, a calculator is actually the right tool. The point is that if you *are* using AI for math, Extended Thinking is essential.
- **Why A is wrong:** Haiku pattern-matches. It might output "Yes, that's correct" without actually checking.
- **Why B is wrong:** Standard mode on any model is prone to math errors because it predicts plausible-looking numbers rather than calculating.

**The correct answer:** 2.3 + 1.8 + 2.1 = 6.2 ✓ (but always verify with calculation, not pattern-matching)

---

## Scoring Guide

- **7/7 correct:** Excellent! You understand model selection and the thinking protocol. Ready for Module 3.
- **5-6 correct:** Good foundation. Review the concepts you missed before continuing.
- **3-4 correct:** Rewatch the video and review flashcards, then retake the quiz.
- **0-2 correct:** Schedule time to review the module content before proceeding.

---

*Quiz complete. Proceed to the Study Guide for a quick reference summary.*
