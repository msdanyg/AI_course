# Concept Map: Solo Pilot to Squadron Leader

This document maps all concepts, skills and topics across the 12-module curriculum for search optimization and cross-referencing.

---

## Core Transformation Journey

```
SOLO PILOT                          SQUADRON LEADER
─────────────────────────────────────────────────────────────
One person, one AI, one-off prompts → Commander of specialized agents
Reactive, improvisational           → Proactive, systematic
Generic outputs, wasted effort      → High-quality, consistent outputs
Limited by individual expertise     → Amplified by orchestrated intelligence
```

---

## Module-Concept Matrix

| Concept | M0 | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 |
|---------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:---:|:---:|
| Squadron Metaphor | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| Data Safety (Tower Lights) | ● | | | | | | | | | | | ● |
| Probabilistic Reasoning | | ● | ● | | | | | | | | | |
| Water Glass Effect | | ● | | | | | | | | | | |
| Context Window | | ● | | ● | | | | | ● | | | |
| Model Selection | | | ● | | | | | | | | | |
| Extended Thinking | | | ● | | | | | | | | | |
| XML Tagging | | | | ● | | | | | | | | |
| Chain of Thought | | | | ● | | | | | | | | |
| COSTAR/PREP/CARE | | | | ● | | | | | | | | |
| Code Execution | | | | | ● | | | | | ● | | |
| Calculator Problem | | | | | ● | | | | | | | |
| Gemini Grounding | | | | | | ● | | | | | | |
| Granola Templates | | | | | | ● | | | | | | |
| Sycophancy | | | | | | | ● | | | | | |
| Red Teaming | | | | | | | ● | | | | | |
| Cross-Platform | | | | | | | | ● | | | | |
| Projects/Artifacts | | | | | | | | | ● | | | |
| File Creation | | | | | | | | | | ● | | |
| MCP/Agents | | | | | | | | | | | ● | |
| Human-in-the-Loop | | | | | | | | | | | | ● |

---

## Concept Definitions & Locations

### Foundation Concepts (Modules 0-1)

#### Squadron Metaphor
> The learner as "Squadron Leader" commanding specialized AI agents rather than flying solo.

**Squadron Mapping:**
| Concept | Squadron Term | Function |
|---------|--------------|----------|
| Learner | Squadron Leader | Architects and commands |
| Claude | Mission Control | Reasoning and synthesis |
| Gemini | Recon & Radar | Research and grounding |
| Granola | Flight Recorder | Context capture |
| Templates | Mission Cards | Reusable procedures |
| Projects | Missions | Multi-step operations |
| Data Safety | Tower Lights | Green/Yellow/Red clearance |

**Found in:** [[Module 1 - The Cognitive Shift/Lesson|Module 1 Lesson]], [[Course Development Guide]]

#### Probabilistic Reasoning Engine
> LLMs predict the next likely token based on training data patterns—they don't retrieve or calculate, they generate.

**Key insight:** Not a search engine (retrieves) or calculator (computes), but a pattern completion system.

**Found in:** [[From Solo Pilot to Squadron Leader_ Practical AI For Knowledge Work (1)|(1)]], [[From Solo Pilot to Squadron Leader_ Practical AI For Knowledge Work (6)|(6)]]

#### Water Glass Effect
> Too much irrelevant context degrades AI reasoning capability.

**The riddle:** Three glasses with objects (paperclip, scissors, watch) appear to have equal water. Which has the most? Answer: Glass A (smallest object = least displacement = most actual water).

**Corporate application:** Cluttered prompts scatter attention across irrelevant details instead of core reasoning tasks.

**Found in:** [[From Solo Pilot to Squadron Leader_ Practical AI For Knowledge Work (2)|(2)]], [[Module 1 - The Cognitive Shift/Lesson|Module 1 Lesson]]

#### Context Window
> The total information AI can hold in working memory at once (~200k tokens for Claude).

**Context Topology:**
- Beginning: High attention
- Middle: Attention drops ("Lost in the Middle")
- End: High attention (especially for instructions)

**Found in:** [[From Solo Pilot to Squadron Leader_ Practical AI For Knowledge Work (3)|(3)]], [[From Solo Pilot to Squadron Leader_ Practical AI For Knowledge Work (6)|(6)]]

---

### Model & Tool Selection (Module 2)

#### Model Taxonomy
| Model | Role | Best For |
|-------|------|----------|
| Haiku | Speed/Volume | Simple summaries, chat, translations |
| Sonnet 4.5 | Daily Driver | Coding, standard reasoning, vibe coding |
| Opus 4.5 | Strategist | Deep nuance, complex creative, highest logic |

**Found in:** [[From Solo Pilot to Squadron Leader_ Practical AI For Knowledge Work (1)|(1)]], [[From Solo Pilot to Squadron Leader_ Practical AI For Knowledge Work (4)|(4)]]

#### Extended Thinking (System 2)
> Buying intelligence with latency—allowing the model to generate reasoning tokens before committing to output.

**Standard Mode (System 1):** Fast, intuitive, prone to math errors
**Extended Thinking (System 2):** Slow, analytical, self-correcting

**Found in:** [[From Solo Pilot to Squadron Leader_ Practical AI For Knowledge Work (1)|(1)]], [[From Solo Pilot to Squadron Leader_ Practical AI For Knowledge Work (4)|(4)]]

---

### Prompt Architecture (Module 3)

#### XML Tagging
> Using XML tags as "attention anchors" to structure prompts and prevent context bleeding.

**Standard tags:**
- `<system_role>` - Who the AI is
- `<task_context>` - What we're doing
- `<user_data>` - The data payload
- `<constraints>` - What NOT to do
- `<thinking>` - Triggers Chain of Thought
- `<answer>` - Contains final output

**Found in:** [[From Solo Pilot to Squadron Leader_ Practical AI For Knowledge Work (2)|(2)]], [[From Solo Pilot to Squadron Leader_ Practical AI For Knowledge Work (6)|(6)]]

#### COSTAR Framework
| Component | Definition |
|-----------|------------|
| **C**ontext | Background information |
| **O**bjective | Specific goal |
| **S**tyle | Writing style to emulate |
| **T**one | Emotional inflection |
| **A**udience | Who consumes the output |
| **R**esponse | Required format |

**Found in:** [[From Solo Pilot to Squadron Leader_ Practical AI For Knowledge Work (3)|(3)]]

#### PREP Framework (Lighter weight)
- **P**rompt: Direct request
- **R**ole: Assign persona
- **E**xplicit Instructions: Constraints
- **P**arameters: Format definition

**Found in:** [[From Solo Pilot to Squadron Leader_ Practical AI For Knowledge Work (3)|(3)]]

#### CARE Framework (Persuasive/QBR)
- **C**ontext: Situation/problem
- **A**ction: What was done
- **R**esult: Outcome
- **E**xample: Specific proof point

**Found in:** [[From Solo Pilot to Squadron Leader_ Practical AI For Knowledge Work (3)|(3)]]

---

### Data Analysis (Module 4)

#### Calculator Problem
> LLMs don't calculate—they predict the most likely sequence of numbers. Complex math requires code execution.

**Solution:** Use Code Execution/Python Sandbox for all quantitative analysis.

**Found in:** [[From Solo Pilot to Squadron Leader_ Practical AI For Knowledge Work (4)|(4)]]

#### Vibe Coding
> Using natural language to instruct AI to write code, focusing on desired outcome ("vibe") rather than technical syntax.

**Example:** "Create a scatter plot. Make it look professional and clean. Use dark background, soft pastel colors."

**Found in:** [[From Solo Pilot to Squadron Leader_ Practical AI For Knowledge Work (4)|(4)]]

---

### Research & Grounding (Module 5)

#### Gemini Grounding
> Anchoring model outputs to verifiable, real-world data sources via dynamic Google Search.

**Workflow:**
1. Prompt analysis → determines external knowledge needed
2. Dynamic query generation → optimized search queries
3. Retrieval and synthesis → filters noise, prioritizes authority
4. Citation and attribution → groundingSupports with source URLs

**Found in:** [[From Solo Pilot to Squadron Leader_ Practical AI For Knowledge Work (2)|(2)]], [[From Solo Pilot to Squadron Leader_ Practical AI For Knowledge Work (3)|(3)]]

#### Fact Brief
> Bulleted, citation-heavy document from Researcher (Gemini) fed to Writer (Claude) to prevent hallucination.

**Found in:** [[From Solo Pilot to Squadron Leader_ Practical AI For Knowledge Work (2)|(2)]]

---

### Decision Hygiene (Module 6)

#### Sycophancy
> AI's bias to agree with the user rather than tell the truth.

**Mitigation techniques:**
- Neutral framing ("Evaluate risks and benefits" not "Why is this a good idea?")
- Persona rotation ("Critique as the skeptical CFO")
- Red teaming (explicitly find flaws)
- Pre-mortem ("Imagine this failed. Why?")

**Found in:** [[From Solo Pilot to Squadron Leader_ Practical AI For Knowledge Work (1)|(1)]]

---

### Advanced Workflows (Modules 7-10)

#### Ramble-to-Gold Workflow
> Voice Memos → Apple Notes → Claude transcription and synthesis

**Found in:** [[From Solo Pilot to Squadron Leader_ Practical AI For Knowledge Work (1)|(1)]]

#### HTML Bridge
> Generating HTML tables for copy-paste into Google Docs with formatting preserved.

**Critical CSS:** `border-collapse: collapse` for clean single borders

**Found in:** [[From Solo Pilot to Squadron Leader_ Practical AI For Knowledge Work (5)|(5)]]

#### Skills Framework
> Reusable, version-controlled instruction sets saved as Markdown files (SKILL.md).

**Structure:**
1. YAML Frontmatter (metadata)
2. System Prompt (persona)
3. Input Schema (what user provides)
4. Instruction Chain (algorithm)
5. Output Template (format)

**Found in:** [[From Solo Pilot to Squadron Leader_ Practical AI For Knowledge Work (2)|(2)]], [[From Solo Pilot to Squadron Leader_ Practical AI For Knowledge Work (6)|(6)]]

#### Artifacts
> Standalone, interactive content blocks (code, React apps, documents) separate from chat conversation.

**Types:**
- Interactive Previews (React, HTML/CSS/JS)
- Documents (Markdown rendering)

**Found in:** [[From Solo Pilot to Squadron Leader_ Practical AI For Knowledge Work (5)|(5)]]

---

## Skills & Capabilities by Role

### All Employees
- [ ] Configure toolchain (Claude, Gemini, Granola)
- [ ] Apply Data Safety Traffic Light protocol
- [ ] Structure prompts using XML tags
- [ ] Recognize and mitigate sycophancy
- [ ] Use Projects for persistent context

### Managers
- [ ] Create meeting templates in Granola
- [ ] Execute Meeting-to-Action pipeline
- [ ] Run Strategic Red Team reviews
- [ ] Build department-specific Projects

### Analysts
- [ ] Use Code Execution for data analysis
- [ ] Create interactive dashboards via Artifacts
- [ ] Apply Claude for Excel dependency tracing
- [ ] Generate visualizations with vibe coding

### Content Creators
- [ ] Execute Content Supply Chain workflow
- [ ] Use HTML Bridge for Google Docs
- [ ] Apply COSTAR for high-stakes content
- [ ] Build reusable Skills for content types

---

## Related Documents

- [[00 - Source Material Index]] - Source file reference
- [[Tags/Tag Index]] - Tag taxonomy
- [[Course Development Guide]] - Content standards

---

*Last updated: November 2025*
