# Module 5: The Sensory System
## Connecting Your Squadron to the Real World

---

## Introduction: The Blind Strategist Problem

Here's a critical limitation: **Claude can't see the world.** 

Ask Claude "What's the current price of Teramind's Enterprise plan?" and it will either:
1. Admit it doesn't know (best case)
2. Confidently give you outdated information from its training data (worse case)
3. Hallucinate a plausible-sounding but completely wrong answer (worst case)

Claude is an extraordinary reasoning engine, but it operates in a sealed room. It can think brilliantly about whatever you bring it, but it can't look outside to verify facts, check current events, or confirm that the information it's using is still accurate.

This creates the **Blind Strategist Problem**: Your Mission Control (Claude) can create sophisticated strategies, but those strategies are built on potentially stale or invented foundations.

Welcome to Module 5, where you'll learn to give your Squadron eyes, ears and a direct data feed. From data connectors and browser extensions to meeting intelligence and deep research, you'll build a complete sensor array that keeps Mission Control grounded in reality.

---

## The Squadron's Sensory Architecture

In aviation, a pilot doesn't fly blind. They have instruments, radar, and communication systems that connect them to the world outside the cockpit. Your AI Squadron needs the same.

### The Complete Squadron

| Role | Tools | Function |
|------|-------|----------|
| **Mission Control** | Claude, ChatGPT | Reasoning, strategy, synthesis, writing |
| **Supply Lines** | Data Connectors (Google Drive, Slack, Gmail, Monday/Atlassian) | Direct data feeds into Mission Control |
| **Recon & Radar** | Gemini, Gemini Browser Extensions, Deep Research | Real-time research, fact verification, grounding |
| **Flight Recorder** | Granola, Chorus AI, Zoom AI Companion | Meeting capture, structured context, institutional memory |
| **Comms Network** | Slack AI Bot | Team communication intelligence, async knowledge retrieval |

Think of it this way:
- **Claude and ChatGPT** are brilliant at thinking but can't leave the command center
- **Data Connectors** pipe your existing files, emails and project data directly into the command center
- **Gemini** can go out into the world and bring back verified intelligence
- **Meeting AI tools** capture what happens in meetings so nothing is lost
- **Slack AI** monitors your team's communications for quick answers and context

Together, they form a complete sensory system.

---

## Part 1: Data Connectors — The Supply Lines

### Why Connectors Change Everything

Without connectors, every AI interaction starts from zero. You copy-paste documents, re-explain context and manually feed information into each conversation. It's like a command center that requires hand-delivered messages for every piece of intelligence.

**Data connectors** solve this by creating persistent pipelines between your AI tools and your existing work systems. Once connected, Claude or ChatGPT can directly access your Google Drive files, Slack messages, Gmail threads and project boards without you copy-pasting anything.

This is the difference between a sealed room and a command center with live data feeds.

### Connectors in Claude

Claude Enterprise (which we use at ActivTrak) supports connectors that give Claude direct access to your organizational data:

**How to manage connectors:**
1. Open Claude → click your profile icon → **Settings**
2. Navigate to **Connected Apps** (or **Connectors** depending on version)
3. Toggle on the integrations you need
4. Authorize access when prompted

**Go-to connectors for Claude:**

| Connector | What It Provides | Best For |
|-----------|-----------------|----------|
| **Google Drive** | Access to Docs, Sheets, Slides in your workspace | Referencing existing documents, analyzing spreadsheets, building on prior work |
| **Slack** | Channel history and message context | Understanding team discussions, finding decisions, gathering context |
| **Gmail** | Email threads and attachments | Processing email chains, drafting replies with full context |
| **Atlassian/Monday** | Project boards, tickets, sprint data | Understanding project status, writing updates, analyzing workload |

> [!tip] Squadron Protocol
> **Turn OFF connectors you aren't actively using.** Each active connector consumes context window space. If you have Google Drive, Slack, Gmail and Monday all connected but you're only working on a document analysis task, disable the others temporarily so Claude has maximum room for reasoning.

### Connectors in ChatGPT

ChatGPT offers a similar connector ecosystem through its settings:

1. Open ChatGPT → **Settings** → **Connected Apps**
2. Available connectors include Google Drive, OneDrive, Slack and others
3. Toggle on what you need for the current workflow

The same principle applies: **connect what you need, disconnect what you don't.**

### The Connector Workflow

Connectors are most powerful when you combine them with the structured prompting from earlier modules:

```
ROLE: Team lead at ActivTrak preparing for a cross-functional planning meeting

CONTEXT: Our department's quarterly planning session is tomorrow. I need to
pull together updates from multiple sources.

TASK: Using my connected Google Drive and Slack:
1. Find the latest project status deck in my team's shared drive
2. Check the #team-updates Slack channel for recent progress and blockers
3. Draft a pre-meeting summary combining both sources

CONSTRAINTS:
- Flag any data points older than 30 days
- Highlight open items that need decisions
```

Because connectors give Claude direct access, you skip the manual copy-paste step entirely. Claude pulls what it needs and synthesizes across sources.

### When Connectors vs. Manual Upload

| Situation | Use Connectors | Use Manual Upload |
|-----------|---------------|-------------------|
| Referencing existing workspace docs | ✓ | |
| Quick context from Slack/email | ✓ | |
| Sensitive or confidential data | | ✓ (with redaction) |
| One-off external documents | | ✓ |
| Large datasets or spreadsheets | | ✓ (upload directly) |
| Regular recurring workflows | ✓ | |

**The Rule:** Connectors for your everyday ecosystem. Manual upload for anything sensitive or one-time.

---

## Part 2: Gemini as Recon & Radar

### Why Gemini for Research?

Google's Gemini has a capability Claude lacks: **Grounding with Google Search**. When you ask Gemini a factual question, it doesn't just predict an answer—it actually searches the web, retrieves current information, and synthesizes a response with citations.

This isn't like asking ChatGPT to "search the web." Gemini's grounding is architecturally integrated:

1. **Dynamic Query Generation**: Gemini doesn't just Google your question verbatim. It generates multiple optimized search queries to cover different aspects
2. **Source Synthesis**: It processes and combines information from multiple sources
3. **Citation Attribution**: It provides links between specific claims and their sources
4. **Confidence Scoring**: It can indicate when information might need additional verification

### The "Double Check" Feature

Gemini Advanced includes a "Double Check" button that highlights claims in the response and shows which sources support them. This visual verification allows you to:

- Instantly see which statements are grounded in sources
- Click through to original sources for verification
- Identify any claims that lack strong source support

> [!tip] Squadron Protocol
> Use Gemini's Double Check feature before including any researched facts in deliverables — whether for leadership, clients or cross-functional partners. If a claim isn't grounded, verify it independently or exclude it.

### Gemini Browser Extensions: Radar Everywhere

Gemini's capabilities extend beyond gemini.google.com through **browser extensions** that bring AI assistance directly into your browsing workflow.

**What Gemini browser extensions do:**
- Summarize web pages, articles and PDFs you're viewing
- Answer questions about the page content in a sidebar
- Help compose emails and messages directly in Gmail
- Provide context and suggestions while you browse

**How to enable:**
1. Install the Gemini extension from the Chrome Web Store
2. Click the Gemini icon in your browser toolbar while on any page
3. Ask questions about what you're reading or request summaries

**Best use cases at ActivTrak:**
- Summarize a vendor's documentation or product changelog
- Get key points from an industry report without reading 40 pages
- Draft email replies with Gemini's help while staying in Gmail
- Pull highlights from a partner's website before a collaboration meeting

> [!tip] Squadron Protocol
> Browser extensions are your "passive radar." They work in the background while you browse, ready to provide intelligence on demand. Think of them as Recon & Radar deployed across your entire browsing experience, not just the Gemini chat window.

### Deep Research: Long-Range Reconnaissance

Sometimes you need more than a quick search. Both Gemini and ChatGPT offer **Deep Research** capabilities that go far beyond a standard query.

**What Deep Research does:**
- Conducts multi-step, autonomous research across dozens of sources
- Follows threads of information, refining queries as it learns
- Synthesizes findings into a comprehensive, structured report
- Includes citations and source links throughout

**Gemini Deep Research:**
1. Open Gemini Advanced
2. Select the "Deep Research" option (available in Gemini Advanced plans)
3. Enter your research question
4. Gemini creates a research plan, then executes it autonomously
5. Returns a detailed report (often several pages) with citations

**ChatGPT Deep Research:**
1. Open ChatGPT (Plus or Enterprise)
2. Select the "Deep Research" model/mode
3. Enter your question
4. ChatGPT browses the web extensively, synthesizing as it goes
5. Returns a thorough analysis with sources

**When to use Deep Research vs. standard queries:**

| Scenario | Standard Query | Deep Research |
|----------|---------------|---------------|
| Quick fact check | ✓ | |
| Current pricing lookup | ✓ | |
| Comprehensive market analysis | | ✓ |
| Multi-competitor landscape review | | ✓ |
| Industry trend report | | ✓ |
| Background prep for executive presentation | | ✓ |

**Example Deep Research prompt:**
```
Conduct a comprehensive analysis of the workforce analytics market:

1. Key players and their market positioning
2. Pricing trends across the industry (2024-2025)
3. Emerging features and capabilities
4. Customer sentiment themes from review sites
5. Regulatory considerations affecting the market

Focus on mid-market and enterprise segments. Include sources for all claims.
```

Deep Research takes longer (sometimes 5-10 minutes) but produces intelligence that would take you hours of manual research. Think of it as sending a reconnaissance team on an extended mission rather than a quick flyover.

### When to Use Gemini vs. Claude

| Task | Use Gemini | Use Claude |
|------|-----------|------------|
| Current competitor pricing | ✓ | |
| Latest industry news | ✓ | |
| Verifying a statistic | ✓ | |
| Comprehensive market research | ✓ (Deep Research) | |
| Browsing page summaries | ✓ (Extension) | |
| Strategic analysis of data you provide | | ✓ |
| Writing polished content | | ✓ |
| Complex reasoning tasks | | ✓ |
| Processing meeting transcripts | | ✓ |
| Analyzing connected workspace data | | ✓ (Connectors) |

**The Rule**: Gemini gathers; Claude processes. Gemini finds the facts; Claude makes sense of them.

---

## The Fact Brief: The Critical Handoff

The most important workflow in your Squadron is the **Fact Brief**—the structured handoff from Gemini (research) to Claude (synthesis).

### Why the Fact Brief Matters

When Claude writes without verified facts, it can hallucinate convincing-sounding information. The Fact Brief prevents this by:

1. **Constraining Claude's inputs**: Claude can only work with facts you've verified
2. **Creating an audit trail**: Every claim traces back to a source
3. **Separating concerns**: Research and writing are handled by specialized tools

### Creating a Fact Brief

**Step 1: Research in Gemini**

```
I'm evaluating project management tools for our team. Please research and provide:

1. Current pricing tiers for Asana, Monday.com and ClickUp
2. Their most recent feature updates (last 6 months)
3. Key strengths according to customer reviews
4. Common complaints or limitations users report

For each fact, include the source URL. Format as a bulleted fact brief.
```

**Step 2: Verify with Double Check**

Click the Double Check button to ensure claims are grounded. Note any statements without strong source support.

**Step 3: Transfer to Claude**

```
ROLE: You are helping me evaluate project management tools for our team.

CONTEXT: We're choosing between three tools and need an objective comparison
based on current facts, not assumptions.

FACT BRIEF (verified via Gemini research):
"""
[Paste the verified Fact Brief here]
"""

TASK: Based ONLY on the facts in this brief, create:
1. A comparison table across pricing, key features and user sentiment
2. A recommendation summary highlighting which tool fits which team type
3. Key questions we should answer before deciding

CONSTRAINTS:
- Use ONLY information from the Fact Brief
- If you need additional facts, tell me what to research
- Flag any areas where our Fact Brief has gaps
```

### The Fact Brief Template

```markdown
# Fact Brief: [Topic]
**Research Date:** [Date]
**Source Tool:** Gemini Advanced

## Verified Facts

### [Category 1]
- [Fact] — Source: [URL]
- [Fact] — Source: [URL]

### [Category 2]
- [Fact] — Source: [URL]
- [Fact] — Source: [URL]

## Unverified/Needs Confirmation
- [Statement that lacked strong source support]

## Research Gaps
- [Information you couldn't find but might need]
```

---

## Part 3: Meeting Intelligence — The Flight Recorder

### The Ephemeral Knowledge Problem

Every day at ActivTrak, valuable information evaporates:
- A stakeholder explains the real priority behind a request
- A teammate shares an approach that solved a tricky problem
- A cross-functional partner mentions a dependency you didn't know about
- A decision is made but the reasoning isn't documented

Without capture, this institutional knowledge is lost. You might remember pieces, but the nuance, the exact phrasing, the context—gone.

**Granola** solves this by capturing meeting audio and transforming it into structured, searchable, AI-ready context.

### How Granola Works

Unlike meeting bots that join calls as visible participants (which can change meeting dynamics), Granola:

1. **Captures locally**: Records system audio directly on your Mac
2. **Runs invisibly**: No bot joins the call; participants don't know unless you tell them
3. **Enables annotation**: You take notes during the meeting; Granola enhances them
4. **Exports to Markdown**: Output is structured text ready for AI processing

### The Annotation Workflow

Granola isn't just passive recording—it's **active noting enhanced by AI**.

**During the meeting:**
- Open Granola before the call
- Type key points as they happen: "Decision: Prioritize mobile dashboard"
- Mark important moments: "Action: Send pricing by Friday"
- Capture your interpretation, not just transcription

**After the meeting:**
- Granola combines your notes with the transcript
- AI generates a structured summary
- Your manual notes are weighted higher (reflecting your judgment)
- Export as Markdown for use with Claude

### Custom Templates in Granola

Granola allows custom templates for different meeting types. Create templates for:

**Cross-Functional Meeting Template:**
```markdown
## Meeting: [Topic / Project Name]

### Attendees
[Auto-populated]

### Key Discussion Points
- Decisions made:
- Open questions:
- Dependencies raised:

### Action Items
- [Item] — Owner: [Name] — Due: [Date]

### Risks or Blockers
[Anything that could delay progress]

### My Observations
[Your interpretation of the dynamics, priorities or subtext]
```

**Recurring Project Sync Template:**
```markdown
## Project Sync: [Project Name] - [Date]

### Progress Since Last Meeting
[Key updates and milestones]

### Blockers and Needs
[What's slowing things down]

### Decisions Needed
[Items requiring sign-off or alignment]

### Stakeholder Sentiment
[Overall mood, concerns, energy level]

### Next Steps
[With owners and deadlines]
```

### Other Flight Recorders: Chorus AI and Zoom AI Companion

Granola is our primary Flight Recorder, but you should know about alternatives that serve similar purposes with different strengths.

**Chorus AI (ZoomInfo)**

Chorus is a conversation intelligence platform designed for teams with high call volumes:
- Automatically records and transcribes calls
- Uses AI to identify key moments: decisions, objections, action items, next steps
- Analyzes patterns across conversations to surface trends
- Integrates with CRM and project management systems to log outcomes

**Best for:** Teams that need automated call analysis at scale with system integration. Chorus is particularly strong at tracking themes and coaching opportunities across an entire team's conversations.

**Zoom AI Companion**

If your meetings live in Zoom, the built-in AI Companion provides:
- Automatic meeting summaries generated immediately after calls
- Action item extraction and assignment
- Smart chapter markers for recording navigation
- In-meeting questions ("What was discussed about the timeline?")
- Integration with Zoom's existing ecosystem (chat, whiteboard, docs)

**Best for:** Teams already invested in the Zoom ecosystem who want meeting intelligence without additional tools. The advantage is zero setup: if you use Zoom, AI Companion is already available.

**Choosing Your Flight Recorder**

| Feature | Granola | Chorus AI | Zoom AI Companion |
|---------|---------|-----------|-------------------|
| **Visibility** | Invisible (local recording) | Bot joins call | Built into Zoom |
| **Best for** | Individual capture + annotation | Sales team analytics | Zoom-native workflows |
| **AI summary** | Enhanced by your notes | Automated with deal focus | Automated general summary |
| **CRM integration** | Manual export | Automatic | Through Zoom ecosystem |
| **Privacy** | Local-first | Cloud-based | Zoom cloud |
| **Setup** | Install Mac app | Enterprise deployment | Already in Zoom |

The key insight: **the tool matters less than the habit.** Whatever Flight Recorder you use, the workflow is the same: capture the meeting → export structured notes → feed to Claude for synthesis.

---

## Part 4: Slack AI Bot — The Comms Network

### Intelligence from Your Team's Conversations

Slack isn't just a messaging app. With **Slack AI**, it becomes an intelligence layer across your team's communication.

### What Slack AI Does

Slack AI analyzes your workspace's messages to provide:
- **Channel summaries**: "What happened in #product-updates this week?"
- **Thread summaries**: Condense long threads into key points
- **Search answers**: Ask questions and get answers synthesized from your workspace history
- **Catch-up digests**: Summarize what you missed while you were away

### How to Use Slack AI

1. Look for the **AI sparkle icon** in Slack's interface
2. Click it to ask questions about channel content
3. Or type in the search bar with natural language: "What decisions were made about the Q1 roadmap?"

### Slack AI at ActivTrak: Practical Applications

**Catching up after PTO:**
> "Summarize the key discussions in #general and #my-team-channel from the past week"

**Pre-meeting prep:**
> "What has been discussed about the Q2 roadmap in #product-development this month?"

**Cross-team awareness:**
> "What are the main topics in #engineering-updates this sprint?"

**Finding decisions:**
> "When did we decide on the new onboarding workflow? Check #operations"

### Slack AI vs. Searching Manually

The difference is synthesis vs. scrolling. Manual search returns individual messages you have to read and piece together. Slack AI reads everything and gives you the answer, often pulling context from multiple messages and threads.

> [!tip] Squadron Protocol
> Use Slack AI as your "morning briefing." Before diving into work, ask it to summarize the channels most relevant to your projects. It takes 30 seconds and can save you 20 minutes of scrolling.

---

## The Complete Handoff: Meeting Notes → Claude

The magic happens when you connect Granola's captured context to Claude's reasoning power.

### Workflow: Meeting to Follow-Up

**Step 1: Capture the meeting in Granola**

Take notes during the call, marking key decisions and action items.

**Step 2: Export the structured notes**

Copy the Markdown output from Granola.

**Step 3: Process with Claude**

```
ROLE: You are helping me prepare post-meeting follow-up materials.

MEETING NOTES:
"""
[Paste Granola export here]
"""

TASK: Based on these meeting notes, draft:
1. A follow-up email to attendees summarizing decisions and next steps (under 150 words)
2. Internal Slack summary for my team (3-4 bullets)
3. A structured list of action items with owners

CONSTRAINTS:
- Reference specific points from the meeting
- Clearly distinguish decisions from open questions
- Include concrete next steps with dates mentioned
```

### Workflow: Meeting Series to Strategy

Over time, your Flight Recorder creates an archive of meeting intelligence. Use this for pattern analysis across recurring meetings:

```
ROLE: Project lead analyzing trends across recurring team syncs

CONTEXT: Here are notes from our last three monthly project reviews:

October Review:
"""
[Paste Granola notes]
"""

November Review:
"""
[Paste Granola notes]
"""

December Review:
"""
[Paste Granola notes]
"""

TASK: Analyze the trajectory of this project:
1. How has team morale and momentum evolved?
2. What recurring blockers appear across meetings?
3. What decisions were made vs. deferred?
4. What risks should we flag for leadership?

Base your analysis ONLY on evidence from these meeting notes.
```

---

## The Complete Squadron Workflow

Now let's see all the components working together, including the new sensor array.

### Scenario: Preparing for an Important Cross-Functional Meeting

You're leading a project that requires buy-in from multiple departments. Let's walk through how every sensor in your array contributes.

**Phase 0: Morning Briefing (Slack AI + Connectors)**

Before you start any research, check what your team already knows:

1. Open Slack AI: "Summarize the key discussions in #project-alpha and #operations from the past two weeks"
2. In Claude with connectors: "Check my Google Drive for any existing research or planning docs related to this initiative"

This takes 30 seconds and may save you from duplicating work someone already did.

**Phase 1: Research Gathering (Gemini)**

```
Research the following for a presentation on workforce analytics best practices:

1. Current industry benchmarks for employee productivity measurement
2. Recent trends in hybrid work analytics (last 6 months)
3. Common implementation challenges organizations report
4. Expert recommendations from industry analysts

Provide as a Fact Brief with sources.
```

For a deeper analysis, use **Deep Research** mode and ask for a comprehensive landscape.

**Phase 2: Historical Context (Meeting Notes → Claude)**

Pull notes from your Flight Recorder (Granola, Zoom AI Companion or Chorus):

```
ROLE: Project lead preparing for a stakeholder alignment meeting

PREVIOUS MEETING HISTORY:
"""
[Paste meeting notes from kickoff meeting]
"""
"""
[Paste meeting notes from last check-in]
"""

Based on these conversations:
1. What are the key stakeholders' actual priorities?
2. What concerns or objections have been raised?
3. What ideas got the most positive response?
```

**Phase 3: Strategy Synthesis (Claude with Connectors)**

Combine research and context:

```
ROLE: Project lead at ActivTrak preparing a stakeholder presentation

RESEARCH (from Gemini):
"""
[Paste Fact Brief]
"""

MEETING CONTEXT (from previous discussions):
"""
[Paste Claude's analysis from Phase 2]
"""

ADDITIONAL CONTEXT: Check my connected Google Drive for our team's
latest project brief and timeline document.

TASK: Create a meeting preparation brief that:
1. Summarizes the current state of the project with supporting data
2. Addresses concerns raised in previous meetings
3. Proposes next steps grounded in industry best practices
4. Anticipates likely questions and prepares responses

Format as a one-page executive summary with talking points.
```

---

## Privacy and Consent: Flying Right

### Meeting Recording Consent

Any Flight Recorder that captures audio creates privacy obligations:

**Two-Party Consent States**: In some jurisdictions (California, Illinois, etc.), all parties must consent to recording. Whether you use Granola, Zoom AI Companion or Chorus, you must disclose recording when legally required.

**Best Practices:**
- Disclose recording at the start of calls when legally required
- Understand what each tool does with audio (local vs. cloud processing)
- Delete recordings after processing if not needed long-term
- Never record without consent in contexts where it's expected (e.g., sensitive HR discussions)

### Connector Privacy Considerations

When you connect Claude or ChatGPT to your workspace data, understand the access scope:
- **Connectors give AI access to everything in the connected service** that your account can see
- Be intentional about what you connect and when
- Disconnect services when not needed for the current task
- Never connect personal accounts to shared AI workspaces

### Data Flow Considerations

Understand where your data goes across the full sensor array:

| Tool | Data Location | Training Use |
|------|---------------|--------------|
| **Claude Enterprise** | Anthropic servers (Enterprise: no training) | Not used for training |
| **ChatGPT Enterprise** | OpenAI servers (Enterprise: no training) | Not used for training |
| **Gemini Advanced** | Google servers | Check workspace settings |
| **Granola** | Local first, then processing API | Review privacy policy |
| **Zoom AI Companion** | Zoom cloud | Check admin settings |
| **Chorus AI** | ZoomInfo cloud | Enterprise agreement |
| **Slack AI** | Slack workspace (existing data) | Check workspace settings |
| **Connectors** | Varies by service | Governed by AI tool's policy |

For sensitive client information, always verify your organization's approved tools and data handling requirements.

---

## Common Patterns and Anti-Patterns

### Do: The Connected Workspace Pattern
1. Enable relevant connectors before starting a task
2. Let Claude pull context from Google Drive, Slack or Gmail directly
3. Disable connectors you don't need to preserve context window
4. Combine connector data with manual uploads for complete picture

### Don't: The Always-On Pattern
❌ Leaving every connector enabled at all times (wastes context window)
❌ Assuming connectors see everything (check permissions)
❌ Sending sensitive data through connectors without checking classification
❌ Forgetting to disconnect after finishing a workflow

### Do: The Verified Research Pattern
1. Research in Gemini with specific questions (or Deep Research for comprehensive analysis)
2. Verify with Double Check
3. Use browser extensions to quickly summarize pages during research
4. Create structured Fact Brief
5. Feed to Claude with explicit constraints

### Don't: The Blind Research Pattern
❌ Asking Claude to "research" competitors (it can't without connectors to current sources)
❌ Assuming Claude's information is current
❌ Skipping verification of Gemini's claims
❌ Mixing unverified assumptions with verified facts

### Do: The Captured Context Pattern
1. Record meetings with your Flight Recorder (Granola, Zoom AI or Chorus)
2. Annotate during the meeting
3. Export structured notes
4. Feed to Claude for synthesis
5. Check Slack AI for related async discussions
6. Maintain history for longitudinal analysis

### Don't: The Lost Context Pattern
❌ Relying on memory for meeting details
❌ Manually transcribing for AI processing
❌ Losing nuance by summarizing too early
❌ Failing to capture decisions and reasoning
❌ Ignoring Slack discussions that add context to meetings

---

## Key Takeaways

1. **Data connectors are your Supply Lines.** Connect Google Drive, Slack, Gmail and project tools to give Claude and ChatGPT direct access to your workspace. Turn off what you don't need to preserve context window.

2. **Gemini is your Recon & Radar.** Use it for real-time research with grounded, verifiable results. Extend its reach with browser extensions and Deep Research for comprehensive analysis.

3. **The Fact Brief is critical.** Always transfer verified research to Claude in structured form. This prevents hallucination.

4. **Choose your Flight Recorder.** Granola, Zoom AI Companion or Chorus AI all capture meeting intelligence. The tool matters less than the habit of capturing every meeting.

5. **Slack AI is your Comms Network.** Use it for morning briefings, pre-meeting prep and finding decisions buried in channel history.

6. **The handoff matters.** Connectors + Gemini research + meeting context → Claude synthesis. Each sensor feeds Mission Control with different intelligence.

7. **Privacy requires attention.** Each tool in your sensor array has different data handling. Know where your data goes and manage connector access intentionally.

---

## Bridge to Module 6

You now have a complete sensory system: connectors for direct data feeds, Gemini for external intelligence, meeting AI for conversation capture, and Slack AI for team communications. Your Squadron can gather facts, access workspace data and capture conversations.

But there's a subtle danger in AI assistance: **sycophancy**. AI models tend to agree with you, tell you what you want to hear, and avoid challenging your assumptions.

In **Module 6: Decision Hygiene**, you'll learn to beat sycophancy using Red Teaming, Pre-Mortem analysis and neutral framing to ensure your AI tells you the truth, not just what sounds good.

---

## Lab Preview

In the hands-on lab, you'll:

1. Explore data connectors in Claude and understand when to enable/disable them
2. Conduct a Gemini research mission and create a Fact Brief
3. Practice the verified handoff to Claude
4. Process sample meeting notes (simulating Flight Recorder output)
5. Use Slack AI to gather team context (or simulate the workflow)
6. Execute a complete Squadron workflow combining all sensor inputs

**Time:** 30-35 minutes
**Tools Required:** Claude (claude.ai), Gemini (gemini.google.com), Slack

---

*Module 5 Complete. Proceed to the Lab Exercise when ready.*
