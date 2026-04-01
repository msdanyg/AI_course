# Module 5: The Sensory System
## Quick Reference Study Guide

---

## Core Concept

**Connectors feed; Gemini grounds; Meeting tools remember; Slack AI listens; Claude reasons.** The complete Squadron uses each sensor for what it does best, creating an intelligence pipeline that's current, contextual and strategically powerful.

---

## Key Terms

| Term | Definition |
|------|------------|
| **The Blind Strategist Problem** | Claude's lack of real-time web access means it works with frozen training data, not current information |
| **Data Connectors (Supply Lines)** | Integrations that pipe Google Drive, Slack, Gmail and project tools directly into Claude or ChatGPT |
| **Grounding with Google Search** | Gemini's ability to retrieve current web information and provide source citations |
| **Double Check** | Gemini feature that highlights which claims are source-backed vs. which may need verification |
| **Browser Extensions** | Gemini tools that provide AI assistance on any webpage (summarize, answer questions, compose) |
| **Deep Research** | Multi-step autonomous research mode (Gemini and ChatGPT) that produces comprehensive reports with citations |
| **Fact Brief** | Structured document containing verified research with sources, formatted for handoff to Claude |
| **Flight Recorder** | Squadron metaphor for meeting AI tools (Granola, Chorus AI, Zoom AI Companion) |
| **Comms Network** | Squadron metaphor for Slack AI Bot, which synthesizes team communication intelligence |
| **The Intelligence Pipeline** | Full workflow: Connectors + Gemini research + meeting context + Slack AI → Claude synthesis |

---

## The Squadron Sensor Array

| Tool | Squadron Role | Best For |
|------|---------------|----------|
| **Claude / ChatGPT** | Mission Control | Deep reasoning, strategy synthesis, content generation |
| **Data Connectors** | Supply Lines | Direct access to Google Drive, Slack, Gmail, Monday/Atlassian |
| **Gemini** | Recon & Radar | Current web research, fact verification, source citations |
| **Gemini Extensions** | Extended Radar | Page summaries, in-browser AI assistance |
| **Deep Research** | Long-Range Recon | Comprehensive multi-source analysis and reports |
| **Granola** | Flight Recorder | Local meeting capture with annotation weighting |
| **Chorus AI** | Flight Recorder | Sales call analytics with CRM integration |
| **Zoom AI Companion** | Flight Recorder | Built-in Zoom meeting summaries and action items |
| **Slack AI** | Comms Network | Channel summaries, decision history, team intelligence |

---

## When to Use Each Sensor

### Use Data Connectors (Supply Lines) When You Need:
- Direct access to existing workspace docs without copy-pasting
- Context from Slack channels, email threads or project boards
- Recurring workflows that pull from the same data sources
- **Critical tip:** Turn OFF unused connectors to preserve context window

### Use Gemini (Recon) When You Need:
- Current pricing or product information
- Recent news or announcements
- User reviews from review sites
- Verified research with source citations
- Quick page summaries (browser extension)
- Comprehensive topic analysis (Deep Research mode)

### Use Meeting AI (Flight Recorder) When You Need:
- Meeting transcripts and summaries (Granola, Zoom AI or Chorus)
- Historical context from past conversations
- Stakeholder preferences and concerns
- Decision history and rationale
- Continuity across multiple meetings

### Use Slack AI (Comms Network) When You Need:
- Morning briefings on what you missed
- Pre-meeting context from team discussions
- Decision history buried in channel threads
- Cross-team awareness of project status

### Use Claude (Mission Control) When You Need:
- Strategic synthesis from multiple inputs
- Complex reasoning and analysis
- Content generation and writing
- Pattern recognition across data
- Personalized recommendations

---

## The Fact Brief Template

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

## Needs Verification
- [Statement that lacked strong source support]

## Research Gaps
- [Information you couldn't find but might need]
```

---

## The Squadron Workflow

```
┌─────────────────────────────────────┐
│  1. GEMINI RESEARCH                 │ ← Current intelligence
│     - Gather facts with sources     │
│     - Use Double Check              │
│     - Create Fact Brief             │
├─────────────────────────────────────┤
│  2. GRANOLA CONTEXT                 │ ← Historical memory
│     - Export relevant meetings      │
│     - Note key stakeholders         │
│     - Identify past concerns        │
├─────────────────────────────────────┤
│  3. CLAUDE SYNTHESIS                │ ← Strategic reasoning
│     - Combine Fact Brief + Context  │
│     - Generate deliverables         │
│     - Apply ActivTrak framing       │
└─────────────────────────────────────┘
```

---

## Gemini Research Best Practices

**Effective Research Prompts:**
- Be specific about what you need
- Request source citations explicitly
- Ask for structured output
- Specify recency requirements

**Example Prompt:**
```
Research [topic or tool] and provide:
1. Current pricing tiers with what's included
2. Product updates from the last 6 months
3. Key strengths from user reviews
4. Common complaints from user feedback

For each fact, include the source URL.
Format as a structured brief with clear sections.
```

**After Research:**
- Click Double Check to verify grounding
- Note green-highlighted (verified) vs. orange (unverified) claims
- Move unverified claims to "Needs Verification" section

**Browser Extension Tips:**
- Install from Chrome Web Store for on-demand page summaries
- Use while browsing vendor sites, industry reports or news articles
- Great for quick intelligence without leaving your current page

**Deep Research Tips:**
- Use for comprehensive multi-source analysis (takes 5-10 minutes)
- Available in both Gemini Advanced and ChatGPT Plus/Enterprise
- Best for market landscapes, comprehensive research and executive prep
- Always review citations in the output report

---

## Meeting AI Comparison

| Feature | Granola | Chorus AI | Zoom AI Companion |
|---------|---------|-----------|-------------------|
| **Visibility** | Invisible (local) | Bot joins call | Built into Zoom |
| **Best for** | Individual + annotation | High-volume team call analytics | Zoom-native teams |
| **AI summary** | Enhanced by your notes | Automated with pattern focus | Automated general |
| **CRM integration** | Manual export | Automatic | Zoom ecosystem |
| **Privacy** | Local-first | Cloud-based | Zoom cloud |

**Using Meeting AI Output:**
1. Export meeting notes in markdown format
2. Include attendee names and roles
3. Paste into Claude with clear context
4. Request analysis based on meeting history
5. Check Slack AI for related async discussions

## Data Connector Quick Reference

| Connector | Claude | ChatGPT | What It Provides |
|-----------|--------|---------|-----------------|
| **Google Drive** | ✓ | ✓ | Docs, Sheets, Slides |
| **Slack** | ✓ | ✓ | Channel history and messages |
| **Gmail** | ✓ | ✓ | Email threads and attachments |
| **Monday/Atlassian** | ✓ | Varies | Project boards and tickets |

**Critical rule:** Turn OFF unused connectors to preserve context window space.

---

## Privacy Considerations

### Meeting Recording
- Always inform participants that meeting is being recorded
- Check two-party consent requirements (CA, IL, etc.)
- Applies to all Flight Recorders: Granola, Zoom AI, Chorus

### Connector Privacy
- Connectors give AI access to everything your account can see
- Turn off connectors when not needed for the current task
- Never connect personal accounts to shared AI workspaces

### AI Processing
- Verify information classification before sharing
- Redact confidential data if needed
- Follow ActivTrak data handling policies
- When in doubt, ask your manager

---

## Common Pitfalls

| Pitfall | Prevention |
|---------|------------|
| Asking Claude for current information | Use Gemini for anything time-sensitive |
| Leaving all connectors on at once | Turn off unused connectors to preserve context window |
| Skipping source verification | Always use Double Check in Gemini |
| Using standard query for deep analysis | Use Deep Research mode for comprehensive topics |
| Unstructured research handoff | Use Fact Brief template |
| Missing meeting context | Export from your Flight Recorder (Granola, Zoom AI or Chorus) |
| Ignoring team discussions | Check Slack AI for related async context |
| Sharing sensitive data | Verify classification before AI processing |

---

## Quick Diagnostic

| If You Need... | Use This Tool |
|----------------|---------------|
| Today's pricing | Gemini (standard query) |
| Comprehensive market landscape | Gemini or ChatGPT (Deep Research) |
| Quick summary of a webpage | Gemini browser extension |
| What was said in last week's meeting | Your Flight Recorder (Granola, Zoom AI, Chorus) |
| What the team discussed in Slack | Slack AI |
| Reference an existing document | Claude with Google Drive connector |
| Context from email threads | Claude with Gmail connector |
| Strategic recommendation | Claude (with Fact Brief + connectors) |
| Source-cited research | Gemini |
| Deep analysis of meeting patterns | Claude + meeting notes context |
| Polished deliverable | Claude (after all sensor inputs) |

---

## Squadron Framework: Complete Pipeline

| Phase | Tool | Action |
|-------|------|--------|
| Briefing | Slack AI (Comms Network) | Check what the team already knows |
| Existing intel | Connectors (Supply Lines) | Pull relevant docs, emails, project data |
| Fresh intelligence | Gemini (Recon & Radar) | Research with sources, create Fact Brief |
| Meeting context | Flight Recorder (Granola/Zoom/Chorus) | Export relevant meeting history |
| Synthesis | Claude (Mission Control) | Combine all inputs, generate deliverable |
| Verification | You (Squadron Leader) | Spot-check facts, review framing |

---

## Module 4 → Module 5 → Module 6 Bridge

| Module | You Learned | Applied To |
|--------|-------------|------------|
| Module 4 | Claude Projects and ChatGPT Folders for persistent context | Organizing AI workspace for recurring workflows |
| Module 5 | Connectors feed; Gemini grounds; meeting tools remember; Slack AI listens | Complete sensor array for real-world intelligence |
| Module 6 | Beating sycophancy with Red Teaming and neutral framing | Ensuring AI tells you the truth |

---

## The Mantra

> **Connect your data. Ground your research. Capture your meetings. Monitor your team channels. Then let Claude think it all through.**

---

*Keep this guide handy when orchestrating your AI Squadron. Remember: connect first, ground second, synthesize third.*
