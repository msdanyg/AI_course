# Module 4: Agentic Data Analysis
## Video Script: The "No Math" Rule

**Duration:** 10-12 minutes

---

## OPENING HOOK [0:00-0:45]

[SCREEN: Split view—Claude chat on left, calculator on right]

**NARRATOR:**
I want to show you something that might shake your confidence in AI. Watch this.

[DEMO: Type into Claude: "What is 847 times 293?"]

Claude responds... confidently. A number appears. Looks reasonable, right?

[SCREEN: Same calculation in calculator app]

Now let's check with an actual calculator. 847 times 293 equals... 248,171.

[SCREEN: Highlight the discrepancy if Claude got it wrong]

Different answer. And here's the thing—Claude didn't hesitate. It didn't say "let me think" or "I'm not sure." It just... guessed. And when AI guesses numbers, it can be confidently wrong.

This is the Calculator Problem. And in the next ten minutes, you're going to learn how to solve it—turning Claude from an unreliable calculator into a precision data analysis tool.

Welcome to Module 4: Agentic Data Analysis.

[TITLE CARD: Module 4 - The "No Math" Rule]

---

## SECTION 1: THE CALCULATOR PROBLEM [0:45-2:30]

[SCREEN: Visual showing "Probabilistic" vs "Deterministic"]

**NARRATOR:**
Let's understand why this happens. Remember from Module 1—Claude is a probabilistic reasoning engine. It doesn't retrieve answers from a database or calculate them in a logic circuit. It predicts the most likely sequence of characters that should follow your input.

For text, this works brilliantly. Claude can write in any style, explain complex concepts, generate creative content—because language has patterns it learned from billions of examples.

[SCREEN: Animation of token prediction with numbers]

But for math? When you ask "847 times 293," Claude is essentially predicting which digits would most likely appear after that prompt. For simple math like "2 plus 2," there are so many training examples that the prediction is reliable. But for unusual or complex calculations, it's making an educated guess about which digits "look right."

[SCREEN: ActivTrak QBR slide with metrics]

Why does this matter for your work? Think about a QBR presentation. You're showing a client their productivity metrics—percentage changes, trend calculations, ROI figures. Every number needs to be exact.

A confident-sounding wrong number is worse than no number at all. It erodes trust. It can lead to bad decisions. And it makes you look unprepared.

[SCREEN: Quote card]

Here's the rule: **Never trust AI to do math—but always trust it to write code that does math.**

Let me show you what that means.

---

## SECTION 2: THE CODE EXECUTION SOLUTION [2:30-4:30]

[SCREEN: Claude interface with Analysis Tool indicator]

**NARRATOR:**
Claude has a feature called the Analysis Tool—sometimes called Code Execution. This changes everything.

[DEMO: Same calculation with explicit code request]

Watch what happens when I ask differently: "Use Python to calculate 847 times 293 and show me the code."

[SCREEN: Claude generating and executing Python code]

Now Claude is writing actual Python code. And when that code runs, it's not predicting the answer—the computer is actually calculating it. 847 times 293 equals 248,171. Exactly right.

[SCREEN: Side-by-side comparison]

See the difference? Same AI, same question, completely different reliability.

- **Probabilistic output:** Claude predicts what numbers look right
- **Deterministic output:** Code executes and returns the actual calculation

[SCREEN: How to trigger code execution]

How do you ensure Claude uses code execution? A few approaches:

**Explicit requests:**
- "Write and run Python code to calculate..."
- "Use the Analysis Tool to analyze this data..."
- "Generate a chart using code..."

**Upload data files:**
When you drag a CSV or Excel file into Claude, it automatically recognizes this is data work and enables code processing.

**Specify numerical tasks:**
- "Calculate the exact percentage change..."
- "Perform statistical analysis on..."

The key phrase to remember: "Show me the code." If Claude can show you the code it ran, the numbers are reliable.

---

## SECTION 3: VIBE CODING FOR ANALYSTS [4:30-6:30]

[SCREEN: Complex Python visualization code]

**NARRATOR:**
Now you might be thinking—I'm not a programmer. I don't know Python or pandas or matplotlib.

Good news: you don't need to.

[SCREEN: Natural language prompt transforming into visualization]

There's a concept called "Vibe Coding." You describe what you want in plain English—focus on the outcome, the "vibe"—and Claude handles all the technical implementation.

[DEMO: Live demonstration]

Let me show you. I'll upload this CSV of quarterly metrics and say:

"Create a bar chart comparing productive hours by department. Make it look professional and clean—use ActivTrak blue, sort from highest to lowest, add data labels on each bar. Make it presentation-ready."

[SCREEN: Claude generating the chart]

Watch what happens. Claude interprets "professional and clean" and translates that into specific styling parameters. It figures out the sorting, the colors, the labels—all from my description.

[SCREEN: Final visualization]

The result? A presentation-quality chart. No Python knowledge required.

And here's the magic—I can refine it conversationally:
- "Make the bars horizontal instead"
- "Change the colors to show positive green and negative red"
- "Add the percentage change as a secondary label"

Each refinement, Claude adjusts the code and regenerates. I'm directing; the AI is implementing.

[SCREEN: Quote card]

**Vibe Coding:** Describe outcomes in natural language. Let AI handle implementation. Iterate through conversation.

---

## SECTION 4: PRACTICAL WORKFLOWS [6:30-8:30]

[SCREEN: CSV file upload demonstration]

**NARRATOR:**
Let's walk through a real workflow. Say you're preparing for a client QBR.

[DEMO: Step-by-step process]

**Step 1: Upload the data.**
Drag your CSV into Claude. You'll see it acknowledge the file and understand its structure.

**Step 2: Verify the load.**
Ask Claude to show you the first five rows. This confirms it parsed correctly and lets you spot any data issues immediately.

[SCREEN: Data preview in Claude]

**Step 3: Request analysis with explicit code.**

Here's my prompt:

"Using Python, calculate the exact percentage change in Productive Hours from Q2 to Q3 for each department. Show me the code you're using and format the results as a table."

[SCREEN: Claude showing code and results]

Notice what I get back: the actual code, plus the results. I can verify the methodology. If something looks wrong, I know exactly where to look.

**Step 4: Generate visuals.**

"Now create a chart comparing these changes. Use bar format, sort by change amount, and color-code improvements in green and declines in red."

[SCREEN: Generated visualization]

**Step 5: Iterate and refine.**

Maybe I want to add context: "Add a horizontal line showing the company average for comparison."

Or adjust presentation: "Make the font larger for projection."

Each request, Claude modifies the code and regenerates.

[SCREEN: Final output package]

By the end, I have:
- Verified calculations with visible methodology
- Professional visualizations
- A repeatable process I can use next quarter

---

## SECTION 5: THE VERIFICATION PROTOCOL [8:30-10:00]

[SCREEN: "Trust but Verify" header]

**NARRATOR:**
Here's the Squadron Leader protocol for data analysis:

[SCREEN: Three rules]

**Rule 1: No numbers without code.**

If Claude gives you a calculation, look for the code block. If there's no code, the number is a guess. Ask "show me the code you used" or "use Python to verify this calculation."

**Rule 2: Spot-check critical figures.**

Pick one or two important numbers and verify them manually. Pull out a calculator, cross-reference with Excel. This isn't about distrusting the AI—it's about catching any potential issues before they reach a client.

**Rule 3: Document methodology.**

When you share AI-generated analysis, note how it was produced. "Calculated using Python pandas library" gives your findings credibility and allows others to verify if needed.

[SCREEN: Common pitfalls]

Watch out for these pitfalls:
- **Confident wrong numbers:** AI doesn't express uncertainty about math
- **Aggregation errors:** Sums and averages can hide issues in underlying data
- **Missing data handling:** Ask explicitly how nulls or empty values were treated
- **Rounding confusion:** Presentation rounding versus calculation precision

[SCREEN: ActivTrak context]

For ActivTrak work specifically—remember "Insights, Not Oversight" applies to data too. When you're analyzing client metrics, frame your prompts supportively. Ask about "trends and patterns" not "underperformers." The AI follows your framing.

---

## CLOSING: THE SQUADRON CONNECTION [10:00-10:45]

[SCREEN: Squadron framework diagram]

**NARRATOR:**
In the Squadron framework, data analysis is Mission Control's specialty. Claude processes with code execution for precision, then synthesizes insights with its reasoning capabilities.

But Claude can't access real-time information. It can't verify current facts or check today's competitor pricing.

[SCREEN: Module 5 preview]

In Module 5, you'll learn how Gemini—your Recon and Radar—provides grounded, verified information. You'll discover how to combine Gemini's real-time research with Claude's analytical power for workflows that are both accurate and current.

[SCREEN: Lab preview]

For now, head to the lab exercise. You'll:
- Run the Hallucination Test yourself
- Upload a sample CSV and perform verified analysis
- Create a professional visualization using Vibe Coding
- Practice the verification protocol

Remember the rule: **AI predicts text. Code calculates math.** When you need numbers you can trust, make sure there's code behind them.

[TITLE CARD: Module 4 Complete - Proceed to Lab]

---

## END OF SCRIPT

**Total Runtime:** ~10:45

**Key Visual Assets Needed:**
- Split screen with Claude and calculator
- Probabilistic vs. deterministic animation
- Code execution demonstration screen captures
- Vibe Coding transformation visual
- Sample CSV analysis walkthrough
- Verification protocol summary card
- Squadron framework diagram with data analysis highlighted
