# Module 4: Agentic Data Analysis
## Lab Exercise: The Precision Analysis Challenge

**Duration:** 25-30 minutes
**Tools Required:** Claude (claude.ai)

---

## Objective

Experience the Calculator Problem firsthand, then master code-verified data analysis using Claude's Analysis Tool. You'll compare probabilistic versus deterministic outputs and practice Vibe Coding to create professional visualizations.

---

## Scenario

You're a Customer Success Manager preparing quarterly metrics for a client review. You have data on department productivity and need to create accurate analysis with professional visualizations.

---

## Part 1: The Hallucination Test (5 minutes)

### Step 1: Test Probabilistic Output

Open a **new Claude conversation** and paste this prompt:

```
Quick question: What is 98,765 multiplied by 12,345?
```

**Record Claude's answer:** ____________

### Step 2: Verify with Code Execution

In the **same conversation**, paste this prompt:

```
Now use Python to calculate 98,765 × 12,345. Show me the code you're running.
```

**Record the code-verified answer:** ____________

### Step 3: Compare Results

Open your computer's calculator app and compute: 98,765 × 12,345

**Calculator answer:** 1,219,253,925

**Reflection Questions:**
- Did Claude's first answer match the calculator?
- Did the code-executed answer match exactly?
- What does this tell you about trusting AI-generated numbers?

```
Your observations:


```

---

## Part 2: CSV Analysis with Code Verification (10 minutes)

### Step 4: Create Sample Data

Since you may not have a data file handy, we'll have Claude create sample data. Open a **new conversation** and paste:

```
Create a sample CSV dataset representing quarterly productivity metrics for a healthcare company. Include:

- 5 departments: Nursing, Administrative, IT, Pharmacy, Facilities
- Q2 and Q3 Productive Hours for each
- Q2 and Q3 Focus Time averages
- Make the data realistic but include a noticeable decline in Nursing (they implemented a new EHR system)

Format as a proper CSV that I could copy into a file. Then load it as a dataframe for analysis.
```

### Step 5: Request Verified Analysis

After Claude creates and loads the data, paste this prompt:

```
Now analyze this data using Python. I need:

1. Calculate the exact percentage change in Productive Hours from Q2 to Q3 for EACH department
2. Calculate the company-wide average change
3. Identify which departments improved vs. declined

Requirements:
- Use Python/pandas for all calculations
- Show me the code you're using
- Format results as a clean table

This is for a client QBR, so accuracy is critical.
```

### Step 6: Apply the Verification Protocol

Review Claude's response and check:

- [ ] Did Claude show the actual Python code?
- [ ] Can you see the calculation methodology?
- [ ] Pick one percentage calculation—does the math check out manually?

**Verification check:** Take one department's numbers and verify the percentage calculation yourself:

```
Department: ____________
Q2 value: ____________
Q3 value: ____________
My calculation: (Q3 - Q2) / Q2 × 100 = ____________%
Claude's result: ____________%
Match? Yes / No
```

---

## Part 3: Vibe Coding for Visualizations (10 minutes)

### Step 7: Create a Basic Chart

Using the same conversation with your data loaded, paste:

```
Create a bar chart showing the percentage change by department. Make it look professional and clean—something I could put in a presentation.
```

**Observe:** Did Claude interpret "professional and clean" into specific styling choices?

### Step 8: Refine with Natural Language

Now iterate on the visualization. Try these refinement prompts one at a time:

**Refinement 1:**
```
Good start. Now sort the bars from largest decline to largest improvement (left to right).
```

**Refinement 2:**
```
Color-code the bars: red shades for declines, green shades for improvements. Keep it professional, not too bright.
```

**Refinement 3:**
```
Add the exact percentage value as a label on each bar. And add a title: "Q3 Productivity Change by Department"
```

### Step 9: Brand Customization

Now apply ActivTrak branding:

```
One more version: Use ActivTrak brand colors:
- Primary blue (#0042F3) for the title
- Use the teal (#2FD3B4) for positive changes
- Use a muted coral for negative changes
- Add a subtle horizontal line at 0% for reference

Make sure the font is readable at presentation size.
```

**Reflection:** How many iterations did it take to get a chart you'd actually use? Did you need to know any Python to create it?

```
Your observations:


```

---

## Part 4: The Complete Analysis Workflow (5 minutes)

### Step 10: Build a QBR-Ready Output

Now combine everything into a workflow that produces client-ready materials. Paste:

```
I need to prepare materials for a client QBR based on this data. Generate:

1. EXECUTIVE SUMMARY
   - One paragraph summarizing the key findings
   - Frame supportively (Insights, Not Oversight)
   - Focus on systemic factors, not individual blame

2. KEY METRICS TABLE
   - All departments with Q2, Q3, and % change
   - Highlight the largest changes
   - Include company average

3. VISUALIZATION
   - The professional bar chart we created
   - Make sure it's presentation-ready

4. TALKING POINTS
   - 3 discussion items for the client meeting
   - Frame the Nursing decline as "EHR transition investment"
   - Suggest questions to explore with the client

CONSTRAINTS:
- All numbers must be calculated using Python
- Use supportive language throughout
- This is for ActivTrak—use "insights" and "analytics," never "tracking" or "monitoring"

Show the code for all calculations.
```

### Step 11: Review Your Output Package

Check the final deliverable:

- [ ] Executive summary frames insights supportively
- [ ] Numbers are backed by visible code
- [ ] Visualization is professional quality
- [ ] Talking points avoid surveillance-oriented language
- [ ] Would you feel confident presenting this to a client?

---

## Reflection Questions

1. **The Calculator Problem:** Before this lab, did you trust AI-generated numbers? How has your approach changed?

```


```

2. **Vibe Coding:** What was easier—describing what you wanted in natural language, or would you have preferred to write Python yourself?

```


```

3. **The Verification Protocol:** How will you apply "no numbers without code" in your daily work?

```


```

4. **ActivTrak Application:** Think of a real analysis you need to do. How would you structure the prompt to ensure code-verified accuracy?

```


```

---

## Success Criteria

You've completed this lab successfully if you can:

- [ ] Explain why AI-generated math can be unreliable without code execution
- [ ] Request and verify code-backed calculations from Claude
- [ ] Use Vibe Coding to create professional visualizations without writing Python
- [ ] Apply the verification protocol (check for code, spot-check results)
- [ ] Structure analysis prompts that produce QBR-ready outputs

---

## Bonus Challenge

Create a reusable prompt template for your recurring analysis needs. Include:

- Clear role definition
- Data input section (placeholder for uploaded file)
- Specific calculations required
- Verification requirements ("show code")
- Output format specifications
- ActivTrak-appropriate framing

Test it with sample data and refine until it produces consistent, high-quality results.

---

## Key Takeaways

1. **Trust code, not predictions.** AI math without code execution is guessing.

2. **Vibe Coding works.** You can direct professional visualizations with natural language.

3. **Verification is quick.** Spot-checking one calculation takes 30 seconds and catches errors.

4. **Iteration is expected.** Refining visualizations through conversation is normal and efficient.

5. **Framework matters.** How you ask (supportive vs. surveillance) shapes the output.

---

*Lab complete. Proceed to the Module 4 Quiz when ready.*
