# Module 4: Agentic Data Analysis
## Knowledge Check Quiz

**Instructions:** Answer all questions. Review feedback after each answer to reinforce learning.

---

### Question 1 (Multiple Choice)

What is "The Calculator Problem" in AI?

A) AI models run out of memory when processing large numbers
B) AI predicts numbers rather than calculating them, leading to confident but potentially wrong answers
C) AI can only do basic arithmetic, not complex calculations
D) AI calculators are slower than traditional calculators

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** LLMs are probabilistic reasoning engines. When asked to multiply 847 × 293, they don't perform the calculation—they predict what digits would most likely follow that prompt based on training patterns. This can result in plausible-looking but incorrect answers.
- **Why A is wrong:** Memory limits exist but aren't "The Calculator Problem."
- **Why C is wrong:** AI can attempt any calculation; the issue is reliability, not capability.
- **Why D is wrong:** Speed isn't the problem—accuracy is.

---

### Question 2 (Multiple Choice)

What is the difference between probabilistic and deterministic output?

A) Probabilistic outputs are always wrong; deterministic outputs are always right
B) Probabilistic outputs are faster; deterministic outputs are slower
C) Probabilistic outputs are AI predictions; deterministic outputs are code-calculated results
D) There is no practical difference for data analysis

**Correct Answer:** C

**Feedback:**
- **Why C is correct:** Probabilistic output is the AI predicting likely text/numbers based on patterns. Deterministic output comes from executing actual code—Python calculates the math precisely. Same AI, different reliability depending on approach.
- **Why A is wrong:** Probabilistic outputs can be correct (especially for common calculations), but they're unreliable.
- **Why B is wrong:** Speed isn't the distinguishing characteristic.
- **Why D is wrong:** The difference is critical for data accuracy.

---

### Question 3 (True/False with Explanation)

**Statement:** If Claude's Analysis Tool shows Python code alongside numerical results, you can trust those numbers are calculated rather than predicted.

A) True
B) False

**Correct Answer:** A (True)

**Feedback:**
When Claude writes and executes Python code, the Python interpreter performs the actual calculation. The code creates a deterministic output—the computer computes rather than predicts. This is why the rule is "no numbers without code."

**However:** You should still spot-check critical figures, as the code itself could have errors in logic (though the math execution will be precise).

---

### Question 4 (Multiple Choice)

How can you ensure Claude uses Code Execution for data analysis?

A) Use Claude Opus instead of Sonnet
B) Upload data files and explicitly request "use Python" or "show me the code"
C) Ask Claude to think step by step
D) Use longer, more detailed prompts

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** Three reliable triggers: (1) Upload CSV/Excel files—Claude recognizes data work, (2) Explicitly request code: "Use Python to calculate..." or "Show me the code," (3) Request specific numerical precision: "Calculate the exact percentage..."
- **Why A is wrong:** Model tier doesn't determine code execution; prompting approach does.
- **Why C is wrong:** Chain-of-thought helps reasoning but doesn't guarantee code execution.
- **Why D is wrong:** Length doesn't trigger code execution—specific requests do.

---

### Question 5 (Multiple Choice)

What is "Vibe Coding"?

A) Writing code while listening to music
B) Describing desired outcomes in natural language and letting AI handle technical implementation
C) A specific Python library for visualizations
D) Coding that focuses on emotional user experiences

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** Vibe Coding lets non-technical users create professional visualizations by describing what they want ("make it clean and professional, dark background, soft colors") while AI translates those descriptions into actual code parameters.
- **Example:** "Create a scatter plot that looks presentation-ready with a trend line" → Claude interprets and writes matplotlib code with appropriate styling.
- **The workflow:** Describe → Review → Refine → Verify data accuracy

---

### Question 6 (Scenario-Based)

A CSM receives this response from Claude: "Based on the uploaded data, productive hours decreased by 18.7% quarter-over-quarter. The largest decline was in the Nursing department at 24.3%."

No code is shown in the response. What should the CSM do?

A) Use these numbers in the QBR presentation—Claude is reliable
B) Ask Claude to recalculate using Python and show the code
C) Manually calculate all the numbers from scratch
D) Assume the numbers are close enough for client discussions

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** Without visible code, these numbers are predictions, not calculations. The CSM should follow up: "Please recalculate these figures using Python and show me the code you're using." This converts probabilistic output to deterministic output.
- **Why A is wrong:** Numbers without code should never be trusted for client-facing work.
- **Why C is wrong:** Manual calculation defeats the purpose of AI assistance—just request code execution.
- **Why D is wrong:** "Close enough" isn't acceptable for professional analysis that affects client decisions.

---

### Question 7 (Multiple Choice)

What are the three rules of the Verification Protocol?

A) Check spelling, verify format, confirm length
B) No numbers without code, spot-check critical figures, document methodology
C) Run three times, average results, use the median
D) Compare to Google, compare to Excel, compare to calculator

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** The three rules ensure reliable AI-generated analysis:
  1. **No numbers without code:** If there's no code block, the number is a guess
  2. **Spot-check critical figures:** Verify 1-2 key calculations manually
  3. **Document methodology:** Note how analysis was produced for credibility and verification
- These rules apply to all AI-generated quantitative work at ActivTrak.

---

### Question 8 (Multiple Choice)

When generating visualizations for an ActivTrak client QBR, which prompt approach is best?

A) "Make a chart of the data"
B) "Create a professional bar chart showing productivity changes by department, sorted by change amount, with positive changes in green and negative in red. Show the code."
C) "Write Python code using matplotlib with figure size 10,8, bar width 0.8..."
D) "Chart this like you would for a Fortune 500 presentation"

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** This prompt uses Vibe Coding effectively—describing the desired outcome in natural language (professional, sorted, color-coded) while requesting code verification. It's specific enough for consistent results without requiring technical knowledge.
- **Why A is wrong:** Too vague—results will vary.
- **Why C is wrong:** Over-specifies technical details most users don't know; let AI handle implementation.
- **Why D is wrong:** "Fortune 500" is vague and doesn't specify the actual requirements.

---

### Question 9 (True/False with Explanation)

**Statement:** Once you've verified that Claude's Analysis Tool calculated a number correctly, you can trust all other numbers in that response without additional verification.

A) True
B) False

**Correct Answer:** B (False)

**Feedback:**
You should spot-check multiple critical figures, not just one. Different calculations might use different code logic, and errors can exist in some calculations but not others. The verification protocol recommends checking 1-2 key figures, not just one.

**Best practice:** Focus verification on the numbers that will be most visible or impactful in your deliverable.

---

### Question 10 (Scenario-Based)

You need to analyze quarterly account data and create a presentation for a client. Order these steps according to the Squadron Leader workflow:

1. Upload CSV to Claude
2. Request executive summary with supportive framing
3. Ask Claude to show first 5 rows to verify data loaded correctly
4. Request percentage calculations with code verification
5. Generate professional visualization using Vibe Coding

A) 1 → 2 → 3 → 4 → 5
B) 1 → 3 → 4 → 5 → 2
C) 3 → 1 → 4 → 2 → 5
D) 1 → 4 → 3 → 5 → 2

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** The proper workflow is:
  1. **Upload data** (1) - Get data into Claude
  2. **Verify load** (3) - Confirm data parsed correctly before analysis
  3. **Calculate with code** (4) - Get verified numbers
  4. **Create visualizations** (5) - Build charts from verified data
  5. **Generate summary** (2) - Synthesize insights last, incorporating all verified analysis
- This ensures each step builds on verified work from the previous step.

---

## Scoring Guide

- **10/10 correct:** Excellent! You've mastered agentic data analysis. Ready for Module 5.
- **8-9 correct:** Strong understanding. Review the concepts you missed before proceeding.
- **6-7 correct:** Good foundation. Rewatch the video section on verification protocol.
- **4-5 correct:** Review the lesson content and repeat the lab exercise.
- **0-3 correct:** Schedule time to thoroughly review Module 4 before proceeding.

---

*Quiz complete. Review the Study Guide for a quick reference summary.*
