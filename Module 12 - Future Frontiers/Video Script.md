# Module 10 Video Script
## Future Frontiers: Agents & MCP

**Duration:** ~12 minutes
**Format:** Instructor-led with screen demonstrations and conceptual diagrams

---

## OPENING (45 seconds)

**[SCREEN: Module title card - "Future Frontiers: Agents & MCP"]**

**INSTRUCTOR (V.O.):**
"You've spent nine modules becoming a Squadron Leader. You've built Projects that hold context, Skills that encode methodology, and learned to produce deliverables through code execution.

**[SCREEN: Quick montage of previous module concepts]**

A quick note before we dive in: This module covers advanced concepts. If you're still building fluency with the fundamentals, feel free to skim this and return when you're ready. The core course skills don't require mastering this material immediately.

But here's the thing: you're still pushing every button. Every analysis, every research task, every workflow—you're manually orchestrating each step.

**[SCREEN: Animation showing human at center of all AI interactions]**

Module 10 introduces the next evolution: AI Agents and the Model Context Protocol. This is where AI shifts from answering questions to completing missions."

---

## SECTION 1: THE EVOLUTION (1.5 minutes)

**[SCREEN: Three-phase diagram appearing step by step]**

**INSTRUCTOR (V.O.):**
"Let's trace the evolution of AI capability.

**[SCREEN: Phase 1 - "Chat" highlighted]**

Phase 1: Chat. You type a question, AI responds with text. Useful, but limited. The AI can only talk—it can't *do* anything.

**[SCREEN: Phase 2 - "Tools" highlighted]**

Phase 2: Tools. This is where you are now. AI can execute code, create files, access the web, maintain context in Projects. Powerful, but you're still triggering each action manually.

**[SCREEN: Phase 3 - "Agents" highlighted]**

Phase 3: Agents. AI receives a *goal*, determines what tools it needs, executes multiple steps autonomously, and adapts based on results.

**[SCREEN: Side-by-side comparison animation]**

The difference: You define the mission objective. The agent executes the flight plan."

---

## SECTION 2: WHAT ARE AGENTS? (2 minutes)

**[SCREEN: Agent loop diagram]**

**INSTRUCTOR (V.O.):**
"An AI Agent is an LLM that can plan, act, observe, and iterate.

**[SCREEN: Traditional flow - "Input → Model → Output → Done"]**

Traditional AI is a straight line. Input goes in, output comes out, you're done.

**[SCREEN: Agent flow - circular "Goal → Plan → Act → Observe → Repeat"]**

Agents operate in a loop. They receive a goal, make a plan, take action, observe the results, and repeat until the goal is achieved.

**[SCREEN: Research example appearing]**

Let me show you the difference. Say you need competitive pricing research.

**[SCREEN: Traditional approach - 6 manual steps listed]**

Traditional approach: You search in Gemini, copy results, paste into Claude, request analysis, ask for a table, download the output. Six manual steps, all triggered by you.

**[SCREEN: Agent approach - single goal with autonomous execution]**

Agent approach: You give one goal—'Research competitor pricing, compare to ours, output a memo.' The agent autonomously researches, structures, analyzes, and generates. You review the final output.

**[SCREEN: "Mission objective → Agent executes → Human reviews"]**

That's the shift. From orchestrating every step to defining the mission and reviewing results."

---

## SECTION 3: MODEL CONTEXT PROTOCOL (1.5 minutes)

**[SCREEN: MCP logo and concept diagram]**

**INSTRUCTOR (V.O.):**
"MCP—Model Context Protocol—is the infrastructure that makes agents possible.

**[SCREEN: "USB standard for AI" analogy]**

Think of it like the USB standard for connecting AI to external tools. Before USB, every device needed a custom cable. Before MCP, every AI integration required custom code.

**[SCREEN: MCP capabilities list]**

MCP provides a standardized way for AI to connect to data sources, use tools, maintain context, and execute actions.

**[SCREEN: Without MCP vs. With MCP comparison]**

Without MCP, Claude can only work with what you paste into the conversation. With MCP, Claude can query databases, read and write files, interact with APIs, and execute workflows across systems.

**[SCREEN: Claude Desktop with MCP servers]**

When you use Claude Desktop with MCP servers enabled, you're using this protocol. The model gains capabilities beyond its base functions—not through magic, but through standardized connections to external tools."

---

## SECTION 3B: CONNECTORS TODAY (1 minute)

**[SCREEN: "Connectors: MCP in Action Today"]**

**INSTRUCTOR (V.O.):**
"Here's the good news: you can start using these capabilities today through connectors—pre-built integrations in Claude.

**[SCREEN: Web connector icons - Slack, Google Drive, Gmail, etc.]**

In Claude.ai, you can connect to tools you already use: Slack for posting updates, Google Drive for accessing documents, Gmail for email, Jira and Monday.com for project management, Google Calendar for scheduling, even GitHub for code.

**[SCREEN: Demo of enabling a connector]**

Just enable the connector, authorize access, and Claude can interact with these systems directly.

**[SCREEN: Desktop connectors - Apple Notes, Granola MCP]**

The Claude Desktop app goes further with MCP servers: Apple Notes, Granola for meeting transcripts, file system access.

**[SCREEN: "Web connectors = Getting started | Desktop MCPs = Advanced"]**

Think of web connectors as getting started, and desktop MCPs as advanced configuration. Start with what's easy—enable Slack or Monday.com—and explore deeper integrations when you're ready."

---

## SECTION 4: THE AGENTIC MINDSET (2 minutes)

**[SCREEN: "Goals vs. Tasks" header]**

**INSTRUCTOR (V.O.):**
"Working with agents requires a mindset shift.

**[SCREEN: Task examples appearing]**

Task thinking is what you're used to: 'Summarize this document.' 'Create a chart.' 'Write an email.' Single actions.

**[SCREEN: Goal examples appearing]**

Goal thinking is different: 'Prepare me for my client meeting tomorrow.' 'Identify cost-saving opportunities in our software stack.' 'Monitor competitor announcements and alert me to changes.'

**[SCREEN: "Tasks = Single Actions | Goals = Outcomes"]**

Goals are outcomes that may require multiple actions. The agent figures out the path.

**[SCREEN: If/Then logic example]**

This means prompts start looking like programs. Here's an example:

**[SCREEN: Code-like prompt with IF/THEN structure]**

'Analyze sales data. IF revenue is below target, identify shortfall accounts and draft follow-up emails. IF revenue meets target, generate team celebration summary.'

**[SCREEN: "Prompt as decision tree" concept]**

The prompt becomes a decision tree the agent navigates. This is why your structured prompting skills from Module 3 matter even more in an agentic world—structure is the programming language of autonomous workflows."

---

## SECTION 5: PREPARING NOW (1.5 minutes)

**[SCREEN: "Prepare Today for Tomorrow"]**

**INSTRUCTOR (V.O.):**
"You don't need to wait for mature agent systems. The skills you've built directly translate.

**[SCREEN: Four preparation strategies]**

First: Master structured communication. Agents parse XML and JSON more reliably than natural language. Your structured prompting skills are agent-readiness skills.

Second: Define clear success criteria. Agents need to know when they're done. Vague goals create problems. 'Improve the report' is vague. 'Revise to include executive summary, data tables, and three recommendations—mark complete when all pass review checklist'—that's clear.

Third: Build modular workflows. The Skills framework from Module 8 is exactly this—discrete, well-defined components that can be chained together.

**[SCREEN: Skill chain example]**

An agent might chain your RESEARCH skill, then your ANALYSIS skill, then your FORMAT skill. Modular design enables autonomous orchestration.

Fourth: Plan for human checkpoints. Even with agents, human oversight remains essential. Design workflows with clear review points—autonomous data gathering, human review, autonomous analysis, human validation, human-approved delivery."

---

## SECTION 6: GOVERNANCE (1 minute)

**[SCREEN: Traffic Light Protocol with agent additions]**

**INSTRUCTOR (V.O.):**
"Autonomous systems require enhanced governance.

**[SCREEN: Permission boundaries]**

Permission boundaries: What can the agent access? Which systems? What actions require human approval?

**[SCREEN: Audit trails]**

Audit trails: What did the agent do? Log all tool uses, record decision points, maintain rollback capability.

**[SCREEN: Human accountability principle]**

And the principle from Module 0 becomes even more critical:

**[SCREEN: Quote highlighted]**

'You clear missions for takeoff and own what leaves the runway.'

**[SCREEN: "Agents execute. Humans remain accountable."]**

Agents execute. Humans remain accountable. Every agent output that affects customers, partners, or external stakeholders requires human review before release."

---

## CLOSING (45 seconds)

**[SCREEN: Squadron evolution diagram]**

**INSTRUCTOR (V.O.):**
"Module 8 made you a Squadron Architect—building persistent infrastructure. Module 10 introduces the Squadron Commander—deploying autonomous units under your strategic direction.

**[SCREEN: Key takeaways]**

Remember: Agents extend your skills, they don't replace them. Everything you've learned prepares you for this future. Goals, not tasks. Structure matters more than ever. And human oversight remains essential.

**[SCREEN: Module 11 preview]**

Next, Module 11 brings everything together in the Capstone Mission—your final demonstration of mastery.

**[SCREEN: "From Solo Pilot to Squadron Commander"]**

From Solo Pilot to Squadron Commander. The transformation is complete."

---

## PRODUCTION NOTES

**Visual Assets Needed:**
- Three-phase evolution diagram (Chat → Tools → Agents)
- Agent loop animation
- MCP infrastructure diagram
- Side-by-side comparison animations
- If/Then prompt example
- Squadron evolution concept

**Screen Recordings Needed:**
- Claude Desktop with MCP servers (showing tool access)
- Example of structured agent-style prompt

**Timing:**
- Opening: 0:00-0:45
- The Evolution: 0:45-2:15
- What Are Agents: 2:15-4:15
- Model Context Protocol: 4:15-5:45
- Connectors Today: 5:45-6:45
- The Agentic Mindset: 6:45-8:45
- Preparing Now: 8:45-10:15
- Governance: 10:15-11:15
- Closing: 11:15-12:00

**Total Runtime:** ~12 minutes

---

**End of Video Script**
