# Module 10 Flashcards
## Future Frontiers: Agents & MCP

---

### Card 1

**Front:**
What are the three phases of AI capability evolution?

**Back:**
1. **Chat**: Human asks, AI responds with text (can only talk)
2. **Tools**: AI can execute code, create files, access web (can do things, but human triggers each action)
3. **Agents**: AI receives goals, autonomously plans and executes multiple steps (mission-based operation)

*Key shift: From human orchestrating every step to human defining mission and reviewing results.*

---

### Card 2

**Front:**
What is an AI Agent and how does it differ from traditional AI?

**Back:**
An AI Agent can **Plan**, **Act**, **Observe**, and **Iterate**.

**Traditional AI:**
Input → Model → Output → Done (single pass)

**Agent AI:**
Goal → Plan → Act → Observe → (Repeat if needed) → Final Output (loop until goal achieved)

*Agents determine what tools they need and adapt based on results.*

---

### Card 3

**Front:**
What is MCP (Model Context Protocol)?

**Back:**
MCP is the **standardized protocol** that connects AI models to external tools and data sources.

Think of it as "USB for AI"—before USB, every device needed custom cables; before MCP, every AI integration needed custom code.

**MCP enables:**
- Database connections
- File system access
- API interactions
- Cross-system workflows

---

### Card 4

**Front:**
What connectors are available in Claude today?

**Back:**
**Web-Based (Claude.ai)** - Easy to enable:
- Slack, Google Drive, Gmail, Google Calendar
- Jira, Monday.com, GitHub

**Desktop (Claude App)** - Advanced setup:
- Apple Notes, Granola MCP, File System

*Start with web connectors (like Monday.com for tasks from meeting notes) and explore desktop MCPs when ready.*

---

### Card 5

**Front:**
What is "goal thinking" vs. "task thinking" in agentic AI?

**Back:**
**Task thinking** (traditional):
- Single actions: "Summarize this document"
- Human orchestrates each step

**Goal thinking** (agentic):
- Outcomes: "Prepare me for my client meeting tomorrow"
- Agent determines and executes the steps

*Goals may require multiple actions. The agent figures out the path.*

---

### Card 6

**Front:**
Why does structured output (XML/JSON) matter more with agents?

**Back:**
Agents need structure because they:
- **Pass information between steps** reliably
- **Interface with external systems** expecting specific formats
- **Make programmatic decisions** based on logic

Prompts become like programs with If/Then logic:
```
IF revenue < target:
  - Identify shortfall accounts
  - Draft follow-ups
ELSE:
  - Generate celebration summary
```

*Structure is the programming language of autonomous workflows.*

---

### Card 7

**Front:**
What four skills prepare you for an agentic future?

**Back:**
1. **Master structured communication** — XML/JSON skills translate to agent-readiness
2. **Define clear success criteria** — Agents need to know when they're done
3. **Build modular workflows** — Skills framework enables chainable operations
4. **Plan for human checkpoints** — Design review points into autonomous workflows

*Everything you've learned in this course prepares you for agents.*

---

### Card 8

**Front:**
What governance considerations apply to AI agents?

**Back:**
**Permission boundaries:**
- What can the agent access?
- Which actions require human approval?

**Audit trails:**
- Log all tool invocations
- Record decision points
- Maintain rollback capability

**Human accountability:**
"You clear missions for takeoff and own what leaves the runway."

*Agents execute. Humans remain accountable.*

---

### Card 9

**Front:**
What is Claude's "Computer Use" capability?

**Back:**
Claude's Computer Use (beta) allows the model to:
- **See** a screen via screenshots
- **Control** mouse and keyboard
- **Navigate** applications like a human user
- **Complete tasks** across multiple applications

**Limitations:**
- Currently requires controlled environments
- Slower than direct human action for simple tasks
- Needs careful permission management

*Demonstrates the trajectory toward AI that can operate any software a human can.*

---

**End of Flashcards**
