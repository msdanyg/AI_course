# Module 2: Model Selection & The "Thinking" Protocol
## Flashcards

---

### Card 1

**Front:**
What are the three Claude model tiers and their primary roles?

**Back:**
- **Haiku (The Scout):** Speed and cost efficiency—simple lookups, translations, bulk processing
- **Sonnet (The Daily Driver):** Balance of speed and intelligence—coding, standard reasoning, everyday work
- **Opus (The Strategist):** Deep reasoning and nuance—complex logic, strategy, multi-step analysis

---

### Card 2

**Front:**
What is the difference between System 1 and System 2 thinking in AI?

**Back:**
**System 1 (Standard Mode):** Fast, intuitive, pattern-matching. Generates tokens by predicting the most likely next word. Quick but prone to confident errors on complex tasks.

**System 2 (Extended Thinking):** Slow, deliberate, analytical. Claude gets a "scratchpad" to reason through problems before answering. Catches errors that standard mode misses.

---

### Card 3

**Front:**
When should you use Extended Thinking instead of standard mode?

**Back:**
Use Extended Thinking when:
- Task involves mathematical or logical reasoning
- Errors would be costly (low tolerance)
- Problem requires multi-step analysis
- You need to verify the AI's reasoning process
- The task requires self-correction or considering multiple approaches

Standard mode is fine when speed matters more than depth and you'll review the output anyway.

---

### Card 4

**Front:**
What are the two axes of the model selection decision matrix?

**Back:**
1. **Task Complexity:** Simple → Standard → Complex
   - How many steps? How clear is the path to solution?

2. **Error Tolerance:** High → Low
   - Will you review the output, or does it go directly to stakeholders?

Cross-reference these to select: Haiku for simple/high-tolerance, Sonnet for standard work, Opus for complex/low-tolerance. Add Extended Thinking when error tolerance is low.

---

### Card 5

**Front:**
What should you look for when reading Claude's Thinking Block?

**Back:**
**Good signs:**
- Breaking problems into steps
- Considering multiple approaches
- Checking intermediate results
- Self-correction ("Wait, that's not right...")

**Warning signs:**
- Rushing to conclusion without analysis
- Ignoring parts of your prompt
- Confident assertions without verification
- Circular reasoning or missing obvious considerations

---

### Card 6

**Front:**
Why is using Opus for everything a mistake?

**Back:**
- **Cost:** Opus costs ~60x more per token than Haiku
- **Speed:** Slower responses break iteration flow
- **Overkill:** Simple tasks don't benefit from deep reasoning
- **Habit:** You don't build skills matching resources to requirements

Default to Sonnet. Escalate to Opus only when Sonnet demonstrably struggles with the complexity.

---

### Card 7

**Front:**
What does "buying intelligence with latency" mean?

**Back:**
You can trade time for better reasoning. This trade-off appears in multiple forms:

- **Haiku vs Opus:** Speed vs depth
- **Standard vs Extended Thinking:** Fast pattern-matching vs deliberate analysis
- **Quick iteration vs careful single-shot:** Multiple fast attempts vs one thorough attempt

Squadron Leaders make this trade consciously based on mission requirements, not by defaulting to the fastest or most expensive option.

---

### Card 8

**Front:**
When should you use Haiku vs Sonnet vs Opus for ActivTrak tasks?

**Back:**
| Task | Model |
|------|-------|
| Categorizing support tickets | Haiku |
| Drafting customer emails | Sonnet |
| Building internal dashboards | Sonnet |
| Quick data lookups | Haiku |
| Competitive analysis deep dive | Opus + Extended Thinking |
| QBR strategy for complex account | Opus |

Match the aircraft to the mission.

---
