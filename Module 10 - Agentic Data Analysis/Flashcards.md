# Module 4: Agentic Data Analysis
## Flashcards

---

### Card 1

**Front:**
What is "The Calculator Problem" and why does it matter?

**Back:**
**The Calculator Problem:** LLMs predict text (including numbers) rather than calculating them. When you ask Claude "What is 847 × 293?" it generates digits that look probable based on patterns—it doesn't actually compute.

**Why it matters:** AI can be confidently wrong about math. A plausible-sounding incorrect number in a QBR or financial analysis erodes trust and leads to bad decisions.

**Solution:** Use Code Execution—have Claude write and run Python code, which actually calculates rather than predicts.

---

### Card 2

**Front:**
What is the difference between probabilistic and deterministic output?

**Back:**
| Type | How It Works | Reliability |
|------|--------------|-------------|
| **Probabilistic** | AI predicts the most likely next tokens | Variable—great for language, unreliable for math |
| **Deterministic** | Code executes actual calculations | Precise—the computer computes the exact answer |

**Key insight:** When Claude writes Python code, the math is calculated by the Python interpreter, not predicted by the AI. Same AI, completely different reliability.

---

### Card 3

**Front:**
How do you ensure Claude uses Code Execution for data analysis?

**Back:**
**Explicit requests:**
- "Write and run Python code to calculate..."
- "Use the Analysis Tool to process this data..."
- "Show me the code you're using"

**Upload data files:**
- Drag CSV or Excel files into Claude
- System automatically enables code processing

**Specify numerical precision:**
- "Calculate the exact percentage change..."
- "Perform statistical analysis on..."

**The key phrase:** "Show me the code"—if Claude shows code, the numbers are calculated, not guessed.

---

### Card 4

**Front:**
What is "Vibe Coding" and how do non-technical users use it?

**Back:**
**Vibe Coding:** Describing desired outcomes in natural language while AI handles technical implementation.

**Example:**
- Instead of learning matplotlib syntax
- Say: "Create a professional bar chart with dark background, soft pastel colors, and a trend line"
- Claude interprets your description and writes the code

**The workflow:**
1. Describe the general outcome ("vibe")
2. Review the output
3. Refine with specific requests ("make bars horizontal")
4. Verify data accuracy

**Key insight:** You direct; AI implements. No coding knowledge required.

---

### Card 5

**Front:**
What are the three rules of the Verification Protocol for AI-generated data?

**Back:**
**Rule 1: No numbers without code**
- If Claude gives a calculation, look for the code block
- No code = number is a guess
- Ask: "Show me the code you used"

**Rule 2: Spot-check critical figures**
- Pick 1-2 important numbers to verify manually
- Cross-reference with calculator or Excel
- Catch issues before they reach clients

**Rule 3: Document methodology**
- Note how analysis was produced
- "Calculated using Python pandas library"
- Enables verification and builds credibility

---

### Card 6

**Front:**
What common pitfalls should you watch for with AI-generated data analysis?

**Back:**
| Pitfall | Why It Happens | Prevention |
|---------|----------------|------------|
| **Confident wrong numbers** | AI doesn't express uncertainty about math | Always verify code was used |
| **Aggregation errors** | Sums/averages can hide underlying issues | Check intermediate calculations |
| **Missing data handling** | AI might ignore null values | Ask explicitly about data quality |
| **Rounding confusion** | Presentation vs. calculation precision | Specify precision requirements |

**Remember:** Trust but verify. The AI is a tool, not an oracle.

---

### Card 7

**Front:**
How does data analysis fit into the Squadron framework?

**Back:**
| Stage | Tool | Role |
|-------|------|------|
| **Research** | Gemini (Recon & Radar) | Gather market data, verify facts |
| **Analysis** | Claude (Mission Control) | Process with code execution |
| **Synthesis** | Claude (Mission Control) | Generate insights from calculations |
| **Presentation** | Claude (Mission Control) | Create charts, format findings |

**The handoff:** Gemini provides verified input data → Claude analyzes with code → Output is both accurate (code-calculated) and insightful (AI-reasoned)

---

### Card 8

**Front:**
Write a sample prompt for analyzing account data using the Squadron Leader approach.

**Back:**
```
ROLE: Customer Success Analyst at ActivTrak

DATA: [Upload account usage CSV]

TASK: Using Python analysis:
1. Load data and show first 5 rows to verify
2. Calculate exact percentage change Q2 to Q3
3. Break down changes by department
4. Identify top 3 at-risk accounts

CONSTRAINTS:
- All calculations must use code execution
- Flag any data quality issues
- Frame insights supportively ("may need support" not "underperforming")

FORMAT:
- Executive summary
- Data table with calculations
- Risk visualization
- Show all code used
```

---

## Study Tips

1. **Run the Hallucination Test yourself:** Ask Claude a multiplication question with and without code execution to see the difference firsthand.

2. **Practice Vibe Coding:** Upload a simple CSV and describe what visualization you want conversationally. Iterate until you get it right.

3. **Build the verification habit:** Every time you see numbers in an AI response, ask yourself "Where's the code?"

4. **Remember the mantra:** AI predicts text. Code calculates math.
