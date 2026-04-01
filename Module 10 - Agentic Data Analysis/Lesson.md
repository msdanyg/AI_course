# Module 4: Agentic Data Analysis
## The "No Math" Rule

---

## Introduction: When Your Calculator Lies

Picture this: You're preparing a QBR deck for a major account. You need to show their productivity trends, calculate the percentage change across departments, and generate a chart comparing this quarter to last. You paste the numbers into Claude and ask for the analysis.

Claude confidently reports: "Productive hours decreased by 23.7% quarter-over-quarter."

You plug the same numbers into Excel. The actual answer? 18.2%.

The AI didn't hesitate. It didn't flag uncertainty. It just... guessed. And it guessed wrong.

Welcome to Module 4, where we learn the most counterintuitive rule for working with AI: **Never trust an AI to do math—but always trust it to write code that does math.**

---

## The Calculator Problem

### Why AI Fails at Basic Arithmetic

Here's a truth that surprises most people: Claude, the same system that can write sophisticated legal arguments and debug complex code, struggles with multiplication.

Ask Claude directly: "What is 847 × 293?"

In standard mode, it might respond with something close but wrong. Why? Because Claude isn't calculating—it's **predicting**. It's generating the most probable sequence of digits that would follow "847 × 293 =" based on patterns in its training data.

For simple math (2 + 2), the training data contains so many examples that the prediction is reliable. For complex or unusual calculations, the model is essentially guessing which digits "look right."

> [!warning] The Calculator Illusion
> LLMs are **probabilistic reasoning engines**, not calculators. Text is generated; math must be **calculated**. When an AI gives you a number without showing its work, you're seeing a prediction, not a computation.

### The Stakes at ActivTrak

This matters enormously for workforce analytics. When you're telling a client their "Productive Hours dropped 15%," that number needs to be exact. A confident-sounding wrong number is worse than no number at all—it erodes trust and can lead to bad decisions.

Consider the scenarios where math accuracy is critical:
- **QBR presentations**: Percentage changes, trend calculations, comparisons
- **Renewal conversations**: ROI calculations, productivity gains
- **Executive summaries**: Aggregate statistics, department breakdowns
- **Competitive analysis**: Feature comparisons, pricing calculations

In each case, a plausible-sounding wrong number could damage credibility or lead to poor decisions.

---

## The Solution: Code Execution

### Probabilistic vs. Deterministic

The breakthrough insight is understanding the difference between two types of AI output:

| Output Type | How It Works | Reliability |
|-------------|--------------|-------------|
| **Probabilistic** | AI predicts likely text | Variable—great for language, unreliable for math |
| **Deterministic** | Code executes calculations | Precise—the computer actually computes the answer |

When Claude writes Python code to calculate 847 × 293, it's not predicting the answer. It's writing instructions that a real computer executes. The Python interpreter actually multiplies those numbers and returns the exact result.

### The Analysis Tool (Code Execution)

Claude's **Analysis Tool** (also called Code Execution) transforms how you work with data. When enabled, Claude can:

1. **Write Python code** to process your data
2. **Execute that code** in a secure sandbox
3. **Return calculated results** that are mathematically precise
4. **Generate visualizations** based on actual data

> [!tip] The Squadron Leader Protocol
> Operational protocol: **No quantitative analysis is accepted unless it's backed by code.** If you see numbers in an AI response, verify the Analysis Tool was used. Look for the code block or "Show work" indicator.

### How to Trigger Code Execution

Claude's Analysis Tool activates automatically for many data tasks, but you can ensure it's used by:

**Explicit requests:**
- "Write and run Python code to calculate..."
- "Use the Analysis Tool to process this data..."
- "Generate a chart using code..."

**Data upload:**
- Drag a CSV or Excel file into Claude
- The system recognizes data and enables code processing

**Clear numerical tasks:**
- "Calculate the exact percentage change..."
- "Perform statistical analysis on..."
- "Create a visualization showing..."

---

## Practical Data Analysis Workflows

### Workflow 1: The Hallucination Test

Before trusting AI with real data, run this diagnostic:

**Step 1:** Ask Claude (without code execution): "What is 98,765 × 12,345?"

**Step 2:** Note whether it shows code or just gives an answer.

**Step 3:** Ask again: "Use Python to calculate 98,765 × 12,345 and show me the code."

**Step 4:** Compare results.

The difference demonstrates why code execution matters. The first response is a guess; the second is a computation.

### Workflow 2: CSV Analysis

Here's how Squadron Leaders analyze data files:

**The Setup:**
```
I'm uploading our Q3 account metrics. I need you to:

1. Load the CSV and show me the first 5 rows so I can verify it loaded correctly
2. Calculate the exact percentage change in Productive Hours from Q2 to Q3
3. Break down the change by department
4. Identify which departments improved vs. declined

Use Python for all calculations. Show me the code you're using.
```

**Why This Works:**
- Explicit request for code verification
- Step-by-step breakdown prevents errors cascading
- "Show me the code" enables you to verify methodology

### Workflow 3: Visual Asset Generation

Creating charts and graphs for presentations:

**The Prompt:**
```
Using the uploaded data, create a professional bar chart comparing productive hours by department. Requirements:

- Use ActivTrak brand colors (Primary Blue: #0042F3)
- Sort departments from highest to lowest
- Add data labels on each bar
- Include a clear title and axis labels
- Make it presentation-ready (clean, minimal)

Generate this using Python/matplotlib and show me the code.
```

**What You Get:**
- A downloadable chart image
- The exact code that created it
- Ability to request modifications ("Make the bars horizontal instead")

---

## "Vibe Coding" for Non-Technical Users

### What Is Vibe Coding?

"Vibe Coding" is the practice of describing what you want in natural language and letting AI write the technical implementation. You focus on outcomes; Claude handles syntax.

**Traditional approach:** Learn Python, matplotlib parameters, pandas functions
**Vibe Coding approach:** "Make it look professional with soft colors"

### Example: From Vibe to Visualization

**Your Request:**
> "Create a scatter plot of this data. I want it to look clean and professional—dark background, soft pastel data points, readable fonts. Add a trend line."

**What Claude Does:**
- Interprets "clean and professional" → specific styling choices
- Translates "soft pastel" → appropriate color hex codes and alpha values
- Implements "trend line" → linear regression overlay
- Applies "dark background" → plt.style.use('dark_background')

**The Result:** A publication-quality visualization without knowing a single Python function.

### The Refinement Loop

Vibe Coding works through iteration:

1. **Initial request:** Describe the general outcome
2. **Review output:** Check if it matches your vision
3. **Refine specifics:** Add constraints as needed
4. **Verify accuracy:** Ensure data is represented correctly

**Example Refinement:**
- "That looks good, but change the X-axis to logarithmic scale"
- "Can you make the data points larger?"
- "Add department names as labels instead of IDs"

---

## Advanced Capabilities

### Data Cleaning and Transformation

Claude can clean messy data before analysis:

```
Here's a CSV export from Salesforce. Before we analyze it:

1. Identify any missing values in the Revenue column
2. Find and flag duplicate Account IDs
3. Standardize the date format to YYYY-MM-DD
4. Remove rows where Status is "Cancelled"

Show me a summary of what you cleaned, then output the cleaned data as a new CSV.
```

### Statistical Analysis

For deeper insights:

```
Using the cleaned data:

1. Calculate Pearson correlation between Time Spent on Site and Subscription Tier
2. Run a basic regression analysis
3. Tell me if the correlation is statistically significant (p < 0.05)
4. Explain what this means for our customer health scoring

Use Python for all statistical calculations.
```

### File Format Conversions

Claude can transform data between formats:

- CSV → Formatted Excel with headers
- JSON → Structured table
- Multiple files → Merged dataset
- Raw data → Pivot table

---

## The Excel Connection

### When You're Already in Excel

Many ActivTrak workflows involve Excel files. Claude can help in two ways:

**1. Upload to Claude:**
- Drag the Excel file into Claude
- Claude reads all sheets and can analyze relationships
- Ask questions like "Why does cell B15 show an error?"

**2. Claude for Excel Add-in:**
- Works directly inside Excel
- Traces formula dependencies
- Explains complex calculations
- Suggests fixes for errors

### Dependency Tracing Example

```
This Excel model calculates Net Revenue, but something's wrong with row 23.

Can you:
1. Trace the precedent cells for the Net Revenue calculation
2. Identify which inputs are causing the discrepancy
3. Explain the formula chain in plain English
```

Claude analyzes the spreadsheet structure and explains what each cell depends on—often catching circular references or mislinked cells that are hard to spot manually.

---

## Governance: Protecting Data Accuracy

### The Verification Protocol

**Rule 1:** No numbers without code
- If Claude gives you a calculation, ask to see the code
- If there's no code, the number is a guess

**Rule 2:** Spot-check results
- Pick one or two calculations to verify manually
- Compare Claude's output to Excel/calculator results

**Rule 3:** Document methodology
- When sharing AI-generated analysis, include the approach used
- "Calculated using Python pandas library with the following methodology..."

### Common Pitfalls to Avoid

| Pitfall | Why It Happens | Prevention |
|---------|----------------|------------|
| **Accepting confident wrong numbers** | AI doesn't express uncertainty about math | Always verify code was used |
| **Trusting aggregations** | Sums and averages can hide errors | Check intermediate calculations |
| **Missing data handling** | AI might ignore null values | Explicitly ask about data quality |
| **Rounding errors** | Presentation rounding vs. calculation rounding | Specify precision requirements |

---

## Connecting to the Squadron

### Where Data Analysis Fits

In the Squadron framework:

| Stage | Tool | Data Analysis Role |
|-------|------|-------------------|
| **Research** | Gemini (Recon) | Gather market data, competitive pricing |
| **Analysis** | Claude (Mission Control) | Process with code execution |
| **Synthesis** | Claude (Mission Control) | Generate insights from calculations |
| **Presentation** | Claude (Mission Control) | Create charts, format findings |

### The Handoff Pattern

**From Gemini to Claude:**
1. Use Gemini to gather verified facts and figures
2. Export or copy the data
3. Upload to Claude for mathematical analysis
4. Claude processes with code execution
5. Output is both accurate (code) and insightful (reasoning)

**From Granola to Claude:**
1. Meeting captured key metrics mentioned by client
2. Export structured notes from Granola
3. Upload to Claude with analysis prompt
4. Claude extracts numbers and analyzes trends
5. QBR prep is both complete and accurate

---

## ActivTrak Applications

### Account Health Analysis

```
ROLE: You are a Customer Success Analyst at ActivTrak.

DATA: [Upload account usage CSV]

TASK: Using Python analysis:
1. Calculate health score based on: login frequency, feature adoption, support tickets
2. Identify accounts in the bottom quartile
3. Generate a risk matrix showing health vs. contract value
4. Create a prioritized list for CSM outreach

CONSTRAINTS:
- All calculations must use code execution
- Flag any data quality issues you find
- Use "accounts" not "customers" in output

FORMAT: Executive summary + detailed data table + visualization
```

### QBR Preparation

```
ROLE: CSM preparing a Quarterly Business Review

DATA: [Upload client's quarterly metrics]

TASK: Generate QBR materials using Python analysis:
1. Calculate exact percentage changes for all key metrics
2. Create comparison charts (this quarter vs. last)
3. Identify top 3 improvement areas with supporting data
4. Draft talking points that frame insights supportively

CONSTRAINTS:
- Frame as "Insights, Not Oversight"
- Focus on systemic patterns, not individual blame
- All numbers must be code-verified

FORMAT:
- Executive summary (1 paragraph)
- Key metrics table
- 2-3 visualizations
- Recommended discussion topics
```

---

## Key Takeaways

1. **The Calculator Problem is real.** AI predicts text, including numbers. Predictions can be confidently wrong.

2. **Code execution is the solution.** When Claude writes and runs Python, the math is calculated, not guessed.

3. **Always verify.** Look for code blocks, ask "show your work," spot-check results.

4. **Vibe Coding democratizes analysis.** Describe what you want; let AI handle the technical implementation.

5. **Data governance matters.** No numbers without code. Document methodology. Verify critical calculations.

---

## Bridge to Module 5

You've learned to use Claude's Analysis Tool for precise data work. But Claude can't access real-time information or verify facts against current sources.

In **Module 5: The Sensory System**, you'll learn how Gemini (Recon & Radar) provides grounded, verified information—and how to combine it with Claude's analytical power for workflows that are both accurate and current.

---

## Lab Preview

In the hands-on lab, you'll:
1. Run the Hallucination Test to see probabilistic vs. deterministic output
2. Upload a sample CSV and perform code-verified analysis
3. Generate a professional visualization using Vibe Coding
4. Practice the verification protocol on AI-generated numbers

**Time:** 25-30 minutes
**Tools Required:** Claude (claude.ai)

---

*Module 4 Complete. Proceed to the Lab Exercise when ready.*
