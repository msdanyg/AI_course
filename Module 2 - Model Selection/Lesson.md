# Module 2: Model Selection & The "Thinking" Protocol

## Choosing the Right Brain for the Mission

---

## Learning Objectives

By the end of this module, you will be able to:

1. **Identify** the three Claude model tiers (Haiku, Sonnet, Opus) and their optimal use cases (Retrieval)
2. **Explain** the difference between System 1 (fast/intuitive) and System 2 (slow/analytical) thinking modes (Comprehension)
3. **Evaluate** task requirements to select the appropriate model and thinking mode (Analysis)
4. **Apply** Extended Thinking to solve complex logic and strategy problems that standard mode fails (Utilization)

---

## The Hook: Why Your Simple Question Cost $47

Picture this: A sales rep needs to check if a prospect's company is in our ICP. They open Claude, select Opus 4.5 with Extended Thinking, and ask: "Is Acme Corp a good fit for ActivTrak?"

Thirty seconds later, they have their answer. But they also just spent roughly 100x more than necessary on a question that Haiku could have answered in 2 seconds.

Meanwhile, their colleague is trying to debug a complex pricing model using Haiku because "it's faster." Three hours later, they're still getting wrong answers and have burned more time than the task is worth.

Model selection isn't just about capability—it's about matching the right tool to the task. Squadron Leaders don't send a reconnaissance drone to carpet bomb, and they don't deploy a strategic bomber to take photos.

This module teaches you to read the mission requirements and select the right aircraft.

---

## Part 1: The Claude Fleet

Claude isn't one model—it's a family of models optimized for different mission profiles. Understanding this taxonomy is fundamental to Squadron Leader operations.

### The Three Tiers

| Model | Codename | Strengths | Best For |
|-------|----------|-----------|----------|
| **Haiku** | The Scout | Speed, volume, cost efficiency | Simple lookups, translations, chat, bulk processing |
| **Sonnet 4.5** | The Daily Driver | Balance of speed and intelligence, coding | Standard reasoning, "vibe coding," everyday tasks |
| **Opus 4.5** | The Strategist | Deep reasoning, nuance, complex logic | Strategy, complex creative writing, multi-step analysis |

### Haiku: The Scout

Haiku is your fast-response reconnaissance unit. It's optimized for tasks where speed and cost matter more than deep reasoning.

**Optimal missions:**
- Quick factual lookups ("What's the timezone in Singapore?")
- Simple text transformations (formatting, basic summarization)
- High-volume processing (categorizing hundreds of support tickets)
- Chat and conversational responses
- Translations

**Limitations:**
- Struggles with multi-step reasoning
- May miss nuance in complex instructions
- Not suitable for tasks requiring deep analysis

**Cost consideration:** Haiku costs roughly 1/60th of Opus per token. For bulk operations, this difference is massive.

### Sonnet 4.5: The Daily Driver

Sonnet is where most Squadron Leaders spend most of their time. It offers the best balance of capability and responsiveness for typical knowledge work.

**Optimal missions:**
- Code generation and debugging
- Standard business writing (emails, reports, proposals)
- Data analysis with code execution
- Building Artifacts (dashboards, visualizations)
- Explaining concepts and documentation
- "Vibe coding" (describing desired outcomes in natural language)

**Why Sonnet dominates daily work:**
Sonnet solves 64% of complex coding challenges in benchmarks—sufficient for most tasks—while offering inference speeds that enable tight iteration loops. When you're building a dashboard and need to say "make the bars blue" twelve times, Sonnet's speed keeps you in flow.

**Limitations:**
- May struggle with highly ambiguous strategic questions
- Can miss subtle logical errors in complex reasoning chains
- Not ideal for tasks requiring extended deliberation

### Opus 4.5: The Strategist

Opus is your strategic command capability. Deploy it when the mission requires deep sustained reasoning, handling ambiguity, or navigating complex multi-step problems.

**Optimal missions:**
- Strategic planning and analysis
- Complex debugging (tracing dependencies across systems)
- Nuanced creative writing (maintaining voice across long documents)
- Red-teaming and adversarial analysis
- Multi-document synthesis with conflicting information
- Tasks where the path to solution is unclear

**The Opus advantage:**
Opus 4.5 demonstrates "agentic" capability—it can autonomously formulate hypotheses, explore multiple approaches, and self-correct without constant user intervention. When presented with a spreadsheet containing financial discrepancies, Opus can plan its own investigation across tabs and formulas.

**The Opus cost:**
Opus is significantly more expensive and slower than Sonnet. Use it deliberately, not by default.

---

## Part 2: System 1 vs System 2 Thinking

Beyond model selection, Claude offers different *thinking modes* that dramatically affect output quality for certain tasks.

### The Dual-Process Framework

Psychologist Daniel Kahneman's research describes two modes of human cognition:

| System 1 | System 2 |
|----------|----------|
| Fast and automatic | Slow and deliberate |
| Intuitive | Analytical |
| Pattern-matching | Step-by-step reasoning |
| Prone to bias and shortcuts | Careful and methodical |
| "What's 2+2?" | "What's 347 × 829?" |

AI models exhibit similar behavior. Standard inference is "System 1"—fast pattern completion. Extended Thinking enables "System 2"—deliberate reasoning with a scratchpad.

### Standard Mode (System 1)

When you send a prompt to Claude in standard mode, it generates tokens in a continuous stream, predicting the most likely next word based on your input. This is fast and usually sufficient.

**Where System 1 excels:**
- Well-defined tasks with clear patterns
- Tasks the model has seen many times in training
- Speed-critical applications
- Simple factual responses

**Where System 1 fails:**
- Novel logic puzzles
- Multi-step mathematical reasoning
- Tasks requiring self-correction
- Problems where the obvious answer is wrong

### Extended Thinking (System 2)

Extended Thinking gives Claude a "scratchpad"—space to reason through problems before committing to an answer. The model generates internal reasoning tokens (visible in a collapsible block) that let it plan, check its work, and self-correct.

**How it works:**
1. Claude receives your prompt
2. Before responding, it generates "thinking tokens"—internal deliberation
3. You can expand the "Thinking" block to see this reasoning
4. The final response reflects this deeper analysis

**Where System 2 excels:**
- Complex logic and mathematical problems
- Multi-step strategic analysis
- Tasks requiring the model to catch its own errors
- Novel problems without clear patterns
- Synthesis across conflicting information

**The cost:**
Extended Thinking uses additional tokens (the thinking itself costs money) and takes longer. A 30-second Extended Thinking response might have taken 3 seconds in standard mode.

---

## Part 3: The Decision Matrix

Squadron Leaders need a systematic way to select the right model and mode for each mission. Use this decision matrix:

### Step 1: Assess Task Complexity

**Simple (Haiku territory):**
- Single-step task
- Clear right answer
- Speed matters more than depth
- Bulk/volume processing

**Standard (Sonnet territory):**
- Multi-step but well-defined
- Requires good reasoning but not exceptional
- Iteration speed matters
- Code generation or artifact building

**Complex (Opus territory):**
- Ambiguous or strategic
- Requires handling conflicting information
- Path to solution is unclear
- Nuanced judgment needed

### Step 2: Assess Error Tolerance

**High tolerance (Standard mode):**
- You'll review and edit the output
- Mistakes are easily caught
- Speed of iteration matters more than first-shot accuracy

**Low tolerance (Extended Thinking):**
- Output goes directly to stakeholders
- Mathematical or logical errors would be costly
- Complex reasoning where mistakes compound

### Step 3: The Matrix

| Task Complexity | Error Tolerance | Recommendation |
|-----------------|-----------------|----------------|
| Simple | High | Haiku (standard) |
| Simple | Low | Sonnet (standard) |
| Standard | High | Sonnet (standard) |
| Standard | Low | Sonnet (Extended Thinking) or Opus |
| Complex | High | Opus (standard) |
| Complex | Low | Opus (Extended Thinking) |

### Real-World Examples

**"Translate this email to Spanish"**
→ Simple task, high tolerance → **Haiku**

**"Build a dashboard showing our Q3 metrics"**
→ Standard task, high tolerance (you'll iterate) → **Sonnet**

**"Analyze why our churn increased and recommend three interventions"**
→ Complex task, low tolerance (exec presentation) → **Opus with Extended Thinking**

**"Check if 23 × 47 = 1081"**
→ Simple task, but low tolerance (math) → **Sonnet with Extended Thinking** (to force verification)

**"Debug this Excel model—something's wrong with the Q4 projections"**
→ Complex task, path unclear → **Opus** (can autonomously investigate)

---

## Part 4: Reading the Thinking Block

When you enable Extended Thinking, Claude's reasoning becomes visible. Learning to read this block is a Squadron Leader skill—it lets you verify the AI's logic and catch errors before they propagate.

### What to Look For

**Good signs:**
- Breaking the problem into steps
- Considering multiple approaches
- Checking intermediate results
- Noting assumptions and constraints
- Self-correction ("Wait, that's not right...")

**Warning signs:**
- Rushing to conclusion without analysis
- Ignoring parts of your prompt
- Circular reasoning
- Confident assertions without verification
- Missing obvious considerations

### Example: The Verification Pattern

**Prompt:** "Our total revenue is the sum of Product ($2.3M), Services ($1.1M), and Support ($0.4M). What's our total revenue?"

**Bad Thinking Block:**
> "The total revenue is $3.8M."

(No verification—the model just pattern-matched)

**Good Thinking Block:**
> "Let me add these up: Product + Services + Support = $2.3M + $1.1M + $0.4M. Adding 2.3 + 1.1 = 3.4. Then 3.4 + 0.4 = 3.8. So total revenue is $3.8M."

The good thinking block shows work. You can verify each step.

### When the Thinking Block Reveals Problems

Sometimes the thinking block reveals that Claude misunderstood your question. This is valuable—you can correct course before accepting a flawed output.

**Example:**
You ask about "churn rate" and the thinking block shows Claude calculating customer acquisition instead. The final answer might sound plausible, but the thinking block reveals the error.

---

## Part 5: The ActivTrak Connection

Model selection directly impacts how we work at ActivTrak—and the recommendations we give customers.

### Internal Operations

| Task | Model Choice | Rationale |
|------|--------------|-----------|
| Categorizing support tickets | Haiku | High volume, simple classification |
| Drafting customer emails | Sonnet | Standard writing, iteration needed |
| Competitive analysis deep dive | Opus + Extended Thinking | Strategic, requires synthesis |
| Building internal dashboards | Sonnet | Artifact generation, fast iteration |
| QBR presentation strategy | Opus | Nuanced customer situation analysis |
| Quick data lookups | Haiku | Speed matters, simple retrieval |

### Customer Conversations

When discussing AI with customers, model selection framing helps explain ActivTrak's approach:

**"Insights, Not Oversight" through smart automation:**
- We use efficient models (Haiku-equivalent) for bulk data processing
- We use sophisticated models (Opus-equivalent) for nuanced analysis
- We don't over-engineer simple tasks or under-engineer complex ones

This mirrors the productivity optimization philosophy—right-sizing resources to tasks.

### The "Buying Intelligence with Latency" Trade-off

Extended Thinking embodies a core Squadron Leader principle: you can *buy* better reasoning by *spending* time. This trade-off appears everywhere:

- Quick Haiku response vs. thorough Opus analysis
- Standard mode speed vs. Extended Thinking accuracy
- First-draft iteration vs. careful single-shot

Squadron Leaders consciously make this trade-off based on mission requirements, not habit.

---

## Part 6: Common Mistakes

### Mistake 1: Opus for Everything

"I want the best, so I'll always use Opus."

**The problem:** You're paying 60x more for simple tasks, waiting longer for responses, and not building iteration skills.

**The fix:** Default to Sonnet. Escalate to Opus only when Sonnet demonstrably struggles.

### Mistake 2: Haiku for Complex Reasoning

"It's faster, so I'll use Haiku for everything."

**The problem:** You spend hours re-prompting and getting wrong answers. The time cost exceeds any model savings.

**The fix:** If you've prompted the same thing three times without success, escalate the model tier.

### Mistake 3: Ignoring Extended Thinking for Math

"It's just a quick calculation."

**The problem:** Standard mode pattern-matches numbers rather than calculating. You get confident wrong answers.

**The fix:** Any task involving specific numerical reasoning benefits from Extended Thinking.

### Mistake 4: Not Reading the Thinking Block

"I just want the answer."

**The problem:** You miss errors that the thinking block would reveal.

**The fix:** For high-stakes tasks, always expand and scan the thinking block before accepting the output.

---

## Key Takeaways

1. **Claude is a fleet, not a single aircraft.** Haiku (speed), Sonnet (balance), Opus (depth) serve different missions.

2. **System 1 vs System 2 applies to AI.** Standard mode is fast and intuitive. Extended Thinking is slow and analytical.

3. **Use the decision matrix.** Assess task complexity and error tolerance to select the right combination.

4. **Read the thinking block.** It reveals the AI's reasoning process and helps you catch errors.

5. **Buy intelligence with latency deliberately.** Don't default to the most expensive option or the fastest one—match resources to requirements.

---

## What's Next

In the lab exercise, you'll compare model performance on identical tasks—seeing firsthand where Haiku fails, where Sonnet succeeds, and where only Opus with Extended Thinking gets the right answer.

Module 3 will introduce advanced prompt architecture using XML structure. You'll learn to "program in English" with tags that control Claude's attention and prevent context bleeding.

---

*Mission Control is ready. Time to test your fleet.*
