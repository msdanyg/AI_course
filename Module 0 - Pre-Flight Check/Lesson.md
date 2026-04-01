# Module 0: Pre-Flight Check
## Setup, Policy & Boundaries

---

## Video Lesson

Watch the video lesson for Module 0 (~11 minutes):

<video controls width="100%">
  <source src="Modele 0 video.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

## Introduction: Before You Fly

Every pilot completes a pre-flight check before takeoff. They verify systems, confirm clearances, and ensure they understand the rules of the airspace. The check isn't bureaucracy—it's what separates safe flights from disasters.

Your journey from Solo Pilot to Squadron Leader begins the same way.

This module establishes your operational foundation: the tools you'll command, the data boundaries you'll respect, and the mindset that transforms casual AI usage into professional orchestration. Skip this, and you'll spend the rest of the course fighting friction. Complete it properly, and every subsequent module flows smoothly.

**By the end of this module, you will:**
- Configure your complete AI toolchain (Claude, Gemini, Granola)
- Understand the ActivTrak data safety protocol (what you can and cannot share with AI)
- Know the role each tool plays in your Squadron
- Feel confident that you're using AI responsibly and effectively

Let's get your cockpit ready.

---

## The Squadron Framework

Before we discuss policy, let's understand what you're working with. At ActivTrak, different employees have access to different AI tools depending on their role and team. Rather than prescribing specific tools, this course teaches you to think in terms of **Squadron roles**—functional capabilities that various tools can fill.

### The Four Squadron Roles

Every effective AI workflow involves some combination of these roles:

#### Mission Control (Reasoning & Synthesis)

This is your reasoning engine—the brain of your operations. Tools in this role excel at:

- **Strategic thinking**: Analyzing complex situations, weighing options, making recommendations
- **Writing and editing**: Drafting content, refining messaging, adapting tone
- **Coding and automation**: Writing scripts, analyzing data, creating files
- **Synthesis**: Taking disparate information and creating coherent outputs

**Tools that fill this role:**
- **Claude/Anthropic** (Product, others): Deep reasoning, writing, coding
- **Claude Code** (Engineering): IDE-integrated coding assistance
- **ChatGPT** (various teams): Research, content editing
- **Cursor/GitHub Copilot** (Engineering): Code-focused reasoning

#### Recon & Radar (Research & Grounding)

These are your eyes and ears on the outside world. Tools in this role excel at:

- **Real-time research**: Current information, recent events, live web data
- **Grounding**: Verifying facts, finding sources, checking claims
- **Workspace integration**: Searching your documents and data

**Tools that fill this role:**
- **Gemini** (company-wide): Real-time web search, Workspace integration
- **Bing AI**: Cost estimation, planning, forecasting
- **Genspark** (Marketing): Content research
- **Google NotebookLM**: Summarization and research synthesis

#### Flight Recorder (Capture & Memory)

These tools capture what happens in meetings and conversations. They:

- **Transcribe**: Create accurate records of conversations
- **Summarize**: Distill key points and action items
- **Preserve**: Maintain institutional memory

**Tools that fill this role:**
- **Granola** (many teams): Meeting notes and transcription
- **Chorus.ai** (Sales, Support, Solutions): Meeting documentation
- **Zoom AI** (company-wide): Call summaries
- **Slack AI**: Conversation summaries

#### Specialized Units (Domain-Specific Tools)

Many teams have AI tools tailored to specific workflows:

- **Figma AI** (Product): Design prototyping
- **Zendesk AI** (Support): Ticket summaries, autoreplies
- **Salesforce Einstein** (Ops): Sales enablement
- **ChurnZero** (CS): Customer summaries
- **Grammarly** (company-wide): Writing assistance

### Your Personal Squadron

You don't need access to every tool. You need to understand what roles are covered by the tools you *do* have.

**Identify your toolkit:**
1. What do you have for **Mission Control** (reasoning/writing)?
2. What do you have for **Recon & Radar** (research/grounding)?
3. What do you have for **Flight Recorder** (meeting capture)?
4. What **Specialized Units** serve your specific workflows?

---

## Why Multiple Tools?

You might wonder: Why not just use one AI for everything?

Each tool has different strengths, access, and limitations. Using them together creates a more reliable system than any single tool alone:

| Scenario | Squadron Role | Example Tools |
|----------|---------------|---------------|
| Draft a competitive positioning email | Mission Control | Claude, ChatGPT |
| Check competitor's current pricing | Recon & Radar | Gemini, Bing AI |
| Summarize yesterday's client call | Flight Recorder + Mission Control | Granola → Claude, Chorus → ChatGPT |
| Analyze a spreadsheet of account data | Mission Control | Claude, ChatGPT with Code Interpreter |
| Find a document in Google Drive | Recon & Radar | Gemini |
| Generate design variations | Specialized Unit | Figma AI |

The Squadron Leader orchestrates their available tools by role. The Solo Pilot uses whatever's in front of them without thinking about fit.

---

## The Traffic Light Protocol: Your Data Safety System

Here's the most important concept in this module: **what you can share with AI tools.**

ActivTrak has established a clear protocol using a traffic light system. This isn't about restricting your work—it's about giving you confidence to move fast while staying safe.

### The Key Insight: Input vs. Output

The risk is rarely in *analyzing* data. The risk is in *sharing* unreviewed AI output.

Think about it: If you upload customer data to Claude and ask for analysis, that data stays in your conversation. But if you then copy the AI's response—without review—into an email to that customer, you've potentially shared something problematic.

This leads to our core principle:

> **"AI drafts. Humans send."**

You clear missions for takeoff. You own what leaves the runway.

### The Three Zones

#### Green Zone: Go Freely

These data types can be used freely with AI tools for analysis, drafting, and preparation:

- **Customer/Account Information**: Names, emails, company details, deal information
- **Internal Documents**: Meeting notes, project plans, strategy documents
- **Usage Data**: Analytics, metrics, behavioral data (anonymized or named)
- **Business Communications**: Past emails, Slack threads, internal discussions

**Why it's green:** This information helps you do your job. The AI processes it in a sandboxed environment. As long as you review outputs before sharing externally, using this data is not only safe but expected.

**Example uses:**
- "Analyze this account's usage trends and suggest expansion opportunities"
- "Draft a QBR email based on these meeting notes"
- "Compare these three accounts and identify common patterns"

#### Yellow Zone: Review Required

These data types require additional consideration before use:

- **Marketing/Public Collateral with PII**: Customer quotes in case studies, named testimonials
- **Competitive Information**: Intelligence gathered from conversations that includes source details
- **Third-Party Data**: Information shared under NDA or partnership agreements

**Why it's yellow:** The data itself may be fine to analyze, but outputs might need PR, Legal, or partner review before external distribution.

**Example caution:**
- You can analyze competitive intel in Claude
- But before sharing that analysis in a public-facing document, get appropriate review

#### Red Zone: Never Share

These data types should never be entered into any AI tool:

- **Secrets and Credentials**: API keys, passwords, admin credentials
- **Security Configurations**: Infrastructure details, access tokens
- **Highly Sensitive Personal Data**: SSN, financial account numbers (these shouldn't be in our systems anyway)

**Why it's red:** These create genuine security risks regardless of how the output is used. If in doubt, don't include it.

### Practical Decision Framework

When you're about to paste something into an AI tool, ask:

1. **What is this data?** (Customer info? Internal doc? Credential?)
2. **What zone is it in?** (Green/Yellow/Red)
3. **What will I do with the output?** (Internal analysis? External communication?)
4. **Have I reviewed before sending?** (Never auto-send AI outputs externally)

If it's Green and you're reviewing outputs: proceed confidently.
If it's Yellow: proceed with awareness that outputs may need review.
If it's Red: stop and find another approach.

---

## Setting Up Your Cockpit

Now let's identify and configure the tools you have access to. Your cockpit will look different from your colleagues'—that's expected.

### Step 1: Inventory Your Tools

First, identify what you have access to in each Squadron role:

**Mission Control (Reasoning/Writing):**
- [ ] Claude.ai or Claude Desktop
- [ ] Claude Code (in VS Code or other IDE)
- [ ] ChatGPT
- [ ] Cursor or GitHub Copilot
- [ ] Other: _____________

**Recon & Radar (Research/Grounding):**
- [ ] Gemini (web or Workspace)
- [ ] Bing AI
- [ ] Google NotebookLM
- [ ] Other: _____________

**Flight Recorder (Meeting Capture):**
- [ ] Granola
- [ ] Chorus.ai
- [ ] Zoom AI summaries
- [ ] Other: _____________

**Specialized Units (your team's tools):**
- [ ] _____________
- [ ] _____________

### Step 2: Configure Your Primary Tools

For each tool you have access to, verify it's working:

**For Mission Control tools (Claude, ChatGPT, etc.):**
1. Log in and verify your account is active
2. Test with a simple prompt: "Summarize what you can help me with"
3. Check if you can upload files
4. Note any special features (Projects, Custom GPTs, extended thinking)

**For Recon & Radar tools (Gemini, Bing AI, etc.):**
1. Log in with your ActivTrak credentials
2. Test real-time search: "What is ActivTrak's current pricing?"
3. Verify Workspace/document integration if available

**For Flight Recorder tools (Granola, Chorus, Zoom AI):**
1. Verify the tool is connected to your calendar/meetings
2. Check a recent meeting for transcript/summary quality
3. Know how to export or copy notes

### Step 3: Understand Your Gaps

Not everyone has tools in every role. If you're missing coverage:

| If you lack... | Consider... |
|----------------|-------------|
| Mission Control | Request access to Claude or ChatGPT from IT |
| Recon & Radar | Gemini is available company-wide |
| Flight Recorder | Zoom AI summaries are available to all |

### Step 4: Verification Checklist

Before moving on, confirm:

- [ ] I know which tools I have for Mission Control
- [ ] I know which tools I have for Recon & Radar
- [ ] I know which tools I have for Flight Recorder
- [ ] My primary tools are configured and working
- [ ] I understand the three traffic light zones
- [ ] I know the "AI drafts, humans send" principle

If any item is incomplete, address it before proceeding. Module 1 assumes your cockpit is ready.

### A Note on Restricted Tools

Some AI tools are not approved for ActivTrak use due to security concerns:

- **DeepSeek AI**: Banned from Texas state government use; security concerns regarding proprietary data
- **RedNote AI apps**: Similar security and data handling concerns

When in doubt about a tool's status, check with IT before using it for work purposes. Stick to the approved tools in your toolkit.

---

## The Squadron Mindset

With your tools configured and data boundaries understood, let's establish the mindset that distinguishes Solo Pilots from Squadron Leaders.

### Solo Pilot Thinking

The Solo Pilot approaches AI as a question-answer machine:
- "Write me an email"
- "Summarize this document"
- "What should I say?"

They get generic outputs, restart conversations constantly, and never build reusable workflows. Every task starts from zero.

### Squadron Leader Thinking

The Squadron Leader orchestrates AI as a reasoning system:
- "Given this account's history, usage patterns, and our expansion goals, draft a QBR email that..."
- "Analyze this transcript, identify the three main concerns, and suggest talking points that address each..."
- "Here's our competitive positioning—red team this and identify weaknesses..."

They provide context, structure requests, maintain persistent knowledge, and review everything before it goes external.

### The Key Differences

| Aspect | Solo Pilot | Squadron Leader |
|--------|------------|-----------------|
| **Context** | Minimal ("Help me with this") | Rich (background, goals, constraints) |
| **Structure** | Freeform questions | Organized requests with clear outputs |
| **Continuity** | New chat for everything | Projects and ongoing conversations |
| **Review** | Copy-paste outputs directly | Verify, refine, then use |
| **Tools** | One tool, one way | Right tool for each task |

The rest of this course teaches you to operate as a Squadron Leader. But the mindset starts now: every interaction with AI is an opportunity for orchestration, not just conversation.

---

## ActivTrak Context: Insights, Not Oversight

One final piece of orientation: how our AI usage aligns with ActivTrak's philosophy.

ActivTrak exists to help organizations understand work patterns and improve productivity. Our guiding principle is "Insights, Not Oversight"—we help companies see what's working without creating surveillance culture.

Your AI usage should reflect this same philosophy:
- **Use AI to generate insights**, not to create busywork
- **Focus on understanding patterns**, not just producing output
- **Prioritize quality over quantity**, leveraging AI to do better work, not just more work

When you use AI to analyze customer data, draft communications, or prepare for meetings, you're using it to create genuine value—not to generate content for content's sake.

This alignment matters. Squadron Leaders use AI purposefully. They know why they're asking for something and how it serves their work. They don't generate outputs they don't need.

---

## Preview: What's Ahead

With your cockpit configured and mindset established, here's what the rest of the course covers:

**Module 1: The Cognitive Shift** — Understanding how LLMs actually work (reasoning engines, not search engines)

**Module 2: Model Selection** — Choosing the right model for each task

**Module 3: Advanced Prompt Architecture** — Structuring requests using XML and professional patterns

**Module 4: Agentic Data Analysis** — Using code execution for error-free analysis

**Module 5: The Sensory System** — Orchestrating Gemini and Granola with Claude

**Module 6: Decision Hygiene** — Beating sycophancy and getting honest AI feedback

**Module 7: The Hybrid Agent** — Cross-device and cross-platform workflows

**Module 8: Systemizing Intelligence** — Projects, Skills, and reusable knowledge

**Module 9: Code Execution** — Creating files (Excel, PowerPoint, PDF) with AI

**Module 10: Future Frontiers** — Agents, MCP, and what's coming next

**Module 11: Capstone & Governance** — Your final mission and certification

---

## Key Takeaways

1. **Three tools, three purposes**: Claude (reasoning), Gemini (research), Granola (capture)
2. **Traffic Light Protocol**: Green (use freely), Yellow (review required), Red (never share)
3. **AI drafts, humans send**: You own every output that leaves your desk
4. **Squadron Leader mindset**: Orchestrate with context, structure, and review
5. **Insights, not busywork**: Use AI purposefully to create genuine value

---

## Self-Assessment

Before proceeding to Module 1, verify:

- [ ] Can you name the three AI tools and their primary purposes?
- [ ] Can you categorize any data type into Green/Yellow/Red zones?
- [ ] Is your toolchain fully configured and tested?
- [ ] Do you understand the "AI drafts, humans send" principle?
- [ ] Can you articulate the difference between Solo Pilot and Squadron Leader thinking?

If yes to all: proceed to Module 1.
If no to any: review the relevant section before continuing.

---

**End of Module 0 Lesson**
