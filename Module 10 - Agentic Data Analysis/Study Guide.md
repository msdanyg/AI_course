# Module 4: Agentic Data Analysis
## Quick Reference Study Guide

---

## Core Concept

**AI predicts text; code calculates math.** When you need numbers you can trust, ensure Claude uses Code Execution. No numbers without code—ever.

---

## Key Terms

| Term | Definition |
|------|------------|
| **The Calculator Problem** | AI predicts numbers rather than calculating them, leading to confident but potentially wrong answers |
| **Probabilistic Output** | AI-generated text/numbers based on pattern prediction—unreliable for math |
| **Deterministic Output** | Code-calculated results—mathematically precise |
| **Code Execution** | Claude's Analysis Tool that writes and runs Python for precise calculations |
| **Vibe Coding** | Describing desired outcomes in natural language while AI handles technical implementation |
| **Verification Protocol** | Three-rule system for ensuring AI-generated data accuracy |

---

## The Problem and Solution

| Without Code Execution | With Code Execution |
|------------------------|---------------------|
| AI predicts likely digits | Python calculates exact result |
| Can be confidently wrong | Mathematically precise |
| No way to verify methodology | Code visible for review |
| Unreliable for critical work | Trustworthy for client deliverables |

---

## How to Trigger Code Execution

**Explicit Requests:**
- "Write and run Python code to calculate..."
- "Use the Analysis Tool to process this data..."
- "Show me the code you're using"

**Upload Data:**
- Drag CSV or Excel files into Claude
- System enables code processing automatically

**Specify Precision:**
- "Calculate the exact percentage change..."
- "Perform statistical analysis on..."

---

## The Verification Protocol

### Rule 1: No Numbers Without Code
- If Claude gives a calculation, look for the code block
- No code visible = number is a guess
- Ask: "Show me the code you used"

### Rule 2: Spot-Check Critical Figures
- Pick 1-2 important numbers to verify manually
- Cross-reference with calculator or Excel
- Takes 30 seconds, catches major errors

### Rule 3: Document Methodology
- Note how analysis was produced
- "Calculated using Python pandas library"
- Builds credibility and enables verification

---

## Vibe Coding Workflow

```
┌─────────────────────────────────────┐
│     1. DESCRIBE the outcome         │ ← Natural language
├─────────────────────────────────────┤
│     2. REVIEW the output            │ ← Check if it matches vision
├─────────────────────────────────────┤
│     3. REFINE with specifics        │ ← Add constraints
├─────────────────────────────────────┤
│     4. VERIFY data accuracy         │ ← Spot-check numbers
└─────────────────────────────────────┘
```

**Example Refinement Prompts:**
- "Sort the bars from highest to lowest"
- "Change colors to red for negative, green for positive"
- "Add data labels on each bar"
- "Use ActivTrak brand colors (#0042F3)"

---

## Common Pitfalls

| Pitfall | Prevention |
|---------|------------|
| Confident wrong numbers | Always verify code was used |
| Aggregation errors hiding issues | Check intermediate calculations |
| Unknown missing data handling | Ask explicitly about nulls |
| Rounding confusion | Specify precision requirements |
| Accepting first response | Always request "show code" |

---

## Analysis Prompt Template

```
ROLE: [Your role - e.g., Customer Success Analyst]

DATA: [Upload file or describe data]

TASK: Using Python analysis:
1. [First calculation/analysis]
2. [Second calculation/analysis]
3. [Third calculation/analysis]

CONSTRAINTS:
- All calculations must use code execution
- Flag any data quality issues
- [ActivTrak framing requirements]

FORMAT:
- [Desired output structure]
- Show all code used
```

---

## Squadron Framework: Data Analysis

| Stage | Tool | Data Analysis Role |
|-------|------|-------------------|
| Research | Gemini (Recon) | Gather market data, verify facts |
| Analysis | Claude (Mission Control) | Process with code execution |
| Synthesis | Claude (Mission Control) | Generate insights from calculations |
| Presentation | Claude (Mission Control) | Create charts, format findings |

---

## Quick Diagnostic

| If Output Is... | The Problem | The Fix |
|-----------------|-------------|---------|
| Numbers without code visible | Probabilistic prediction | Ask "show me the code" |
| Numbers that don't match manual check | Code logic error or prediction | Request recalculation with code |
| Vague visualizations | Under-specified prompt | Add specific requirements |
| Wrong framing in analysis | Missing constraints | Add ActivTrak language requirements |
| Inconsistent results | Varying methodology | Request explicit code verification |

---

## ActivTrak Language for Data Analysis

**Use:**
- Analytics, insights, visibility
- Patterns, trends, opportunities
- "May need support," "systemic factors"

**Avoid:**
- Tracking, monitoring, surveillance
- "Underperformers," "slackers"
- Individual blame framing

---

## Module 3 → Module 4 → Module 5 Bridge

| Module | You Learned | Applied To |
|--------|-------------|------------|
| Module 3 | Structure prevents context bleeding | Write clear prompts |
| Module 4 | AI predicts; code calculates | Data analysis with verification |
| Module 5 | Real-time grounding with Gemini | Current facts + Claude analysis |

---

## The Mantra

> **Never trust AI to do math—but always trust it to write code that does math.**

---

*Keep this guide handy when analyzing data. Remember: no numbers without code.*
