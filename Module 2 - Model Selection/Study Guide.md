# Module 2: Model Selection & The "Thinking" Protocol
## Quick Reference Study Guide

---

## Core Concept

**Claude is a fleet, not a single aircraft.** Match the model tier and thinking mode to your mission requirements—don't default to the fastest or most expensive option.

---

## The Claude Fleet

| Model | Role | Best For | Cost |
|-------|------|----------|------|
| **Haiku** | The Scout | Simple lookups, translations, bulk processing | Lowest (~1/60 of Opus) |
| **Sonnet** | The Daily Driver | Coding, standard reasoning, dashboards, iteration | Moderate |
| **Opus** | The Strategist | Complex logic, strategy, nuanced analysis | Highest |

---

## System 1 vs System 2

| Standard Mode (System 1) | Extended Thinking (System 2) |
|--------------------------|------------------------------|
| Fast pattern-matching | Deliberate reasoning |
| Intuitive | Analytical |
| Prone to confident errors | Self-correcting |
| Best for defined tasks | Best for complex logic |
| No visible reasoning | Thinking block visible |

**Rule:** Always use Extended Thinking for mathematical reasoning or low-error-tolerance tasks.

---

## The Decision Matrix

| Task Complexity | Error Tolerance | Recommendation |
|-----------------|-----------------|----------------|
| Simple | High | **Haiku** |
| Simple | Low | **Sonnet** |
| Standard | High | **Sonnet** |
| Standard | Low | **Sonnet + Extended Thinking** |
| Complex | High | **Opus** |
| Complex | Low | **Opus + Extended Thinking** |

---

## Reading the Thinking Block

### Good Signs ✓
- Breaking problems into steps
- Considering multiple approaches
- Checking intermediate results
- Self-correction ("Wait, that's not right...")
- Noting assumptions

### Warning Signs ✗
- Rushing to conclusion
- Ignoring parts of prompt
- Confident assertions without verification
- Circular reasoning

---

## Common Mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| Opus for everything | 60x cost, slower iteration | Default to Sonnet, escalate when needed |
| Haiku for complex reasoning | Wrong answers, wasted time | If 3+ attempts fail, upgrade model |
| Skipping Extended Thinking for math | Pattern-matching, not calculating | Always use for numerical tasks |
| Not reading Thinking block | Missing catchable errors | Scan before accepting high-stakes output |

---

## Quick Selection Guide

**Use Haiku when:**
- Speed matters most
- High volume / bulk processing
- Simple lookups or translations
- Cost is a constraint

**Use Sonnet when:**
- Standard business tasks
- Code generation / debugging
- Building artifacts / dashboards
- Iteration speed matters

**Use Opus when:**
- Strategic or ambiguous tasks
- Path to solution is unclear
- Nuance and judgment required
- Multi-step complex reasoning

**Add Extended Thinking when:**
- Math or logic involved
- Output goes directly to stakeholders
- Errors would be costly
- You need to verify reasoning

---

## ActivTrak Task Examples

| Task | Model Choice |
|------|--------------|
| Categorizing support tickets | Haiku |
| Drafting customer emails | Sonnet |
| Building internal dashboards | Sonnet |
| Quick data lookups | Haiku |
| Competitive analysis deep dive | Opus + Extended Thinking |
| QBR strategy for complex account | Opus |
| Verifying calculations | Any + Extended Thinking |

---

## Key Principle

> **"Buying Intelligence with Latency"**
>
> You can trade time for better reasoning. Make this trade consciously based on mission requirements—not by habit.

---

## Next Module Preview

**Module 3: The Reasoning Engine (Advanced Prompt Architecture)**

Learn to "program in English" using XML tags that control Claude's attention, prevent context bleeding, and ensure consistent outputs.

---

*Keep this guide handy when selecting models for new tasks.*
