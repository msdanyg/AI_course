# Module 5: The Sensory System
## Video Script: Connecting Your Squadron to the Real World

**Duration:** 14-16 minutes

---

## OPENING HOOK [0:00-0:45]

[SCREEN: Claude chat interface]

**NARRATOR:**
Let me show you Claude's biggest weakness.

[DEMO: Type into Claude: "What is Teramind's current Enterprise pricing?"]

Watch Claude's response. It might give you a number, sound confident, maybe even add some context about features. But here's the thing—that information could be months or years out of date. Or it could be completely invented.

[SCREEN: Side-by-side with actual Teramind website]

Claude is extraordinary at reasoning. But it can't see outside its training data. It's like having a brilliant strategist who's locked in a room with no windows.

This is the Blind Strategist Problem. And today, you're going to learn how to give your Squadron the recon tools it needs.

Welcome to Module 5: The Sensory System.

[TITLE CARD: Module 5 - Gemini & Granola]

---

## SECTION 1: THE COMPLETE SQUADRON [0:45-2:15]

[SCREEN: Squadron diagram with five components]

**NARRATOR:**
Let's build your Squadron's complete sensor array.

[SCREEN: Claude icon with "Mission Control" label]

You already know Claude, your Mission Control. It handles reasoning, strategy, synthesis and writing. Brilliant at thinking, but blind to the outside world without help.

[SCREEN: Add "Supply Lines" icon with connector logos]

First, we have Supply Lines. These are data connectors: Google Drive, Slack, Gmail, Monday, Atlassian. They pipe your existing workspace data directly into Mission Control so Claude and ChatGPT can access your files, emails and project boards without copy-pasting.

[SCREEN: Add Gemini icon with "Recon & Radar" label]

Next, Gemini, your Recon and Radar. Google's AI has something Claude lacks: Grounding with Google Search. It can browse the web, retrieve current information and provide citations. It even extends into your browser with extensions and a Deep Research mode for comprehensive analysis.

[SCREEN: Add meeting tools icon with "Flight Recorder" label]

Then your Flight Recorders. Granola, Zoom AI Companion, Chorus AI. These capture meeting audio and transform it into structured, AI-ready notes.

[SCREEN: Add Slack AI icon with "Comms Network" label]

And finally Slack AI, your Comms Network. It reads your team's conversations and gives you synthesized answers, channel summaries and decision histories.

[SCREEN: Show arrows connecting all five to Mission Control]

Together, these form a complete sensory system:
- Connectors feed your workspace data directly
- Gemini gathers external intelligence
- Meeting tools capture conversations
- Slack AI monitors team communications
- Claude processes everything and produces deliverables

Let's see how each one works, starting with the most impactful: data connectors.

---

## SECTION 2: DATA CONNECTORS — THE SUPPLY LINES [2:15-4:00]

[SCREEN: Claude Settings > Connected Apps]

**NARRATOR:**
Data connectors might be the single most underused feature in your AI toolkit. Let me show you why they matter.

[DEMO: Navigate to Claude settings, show Connected Apps]

Without connectors, every conversation with Claude starts from scratch. You copy-paste documents, re-explain context, manually upload files. With connectors, Claude can reach directly into your Google Drive, Slack, Gmail and project boards.

[SCREEN: Show toggling on Google Drive connector]

Setting them up is simple. In Claude, go to Settings, then Connected Apps. Toggle on the services you need. Google Drive is the easiest win: once connected, Claude can reference any document in your workspace.

[SCREEN: Show connector list with toggles]

Your go-to connectors: Google Drive for documents and spreadsheets. Slack for team discussions and decisions. Gmail for email context. And Atlassian or Monday for project status and tickets.

[SCREEN: Highlight "turn off unused connectors" with visual]

Here's the critical tip: turn OFF connectors you aren't actively using. Each active connector consumes context window space. If you're working on a document analysis task, you don't need Slack and Monday consuming room that Claude could use for reasoning.

ChatGPT has similar connectors in its settings. Same principle: connect what you need, disconnect what you don't.

[SCREEN: Show example prompt using connectors]

Once connected, your prompts can reference workspace data directly: "Check my Google Drive for the latest project status deck" or "What was discussed about our Q2 priorities in the Slack channel this week?"

No copy-pasting. No context lost. Direct supply lines into Mission Control.

---

## SECTION 3: GEMINI AS RECON & RADAR [4:00-6:30]

[SCREEN: Gemini interface]

**NARRATOR:**
Now let's talk about gathering intelligence from the outside world. Gemini's superpower is grounded research.

[DEMO: Research query in Gemini]

I'll ask: "What are the current best practices for hybrid work productivity measurement and which tools are leading the market?"

[SCREEN: Gemini generating response with sources]

Watch what happens. Gemini doesn't just predict an answer. It generates multiple search queries, retrieves results, synthesizes the information and provides source citations.

[SCREEN: Highlight the "Double Check" button]

See this "Double Check" button? This is critical. When I click it, Gemini highlights which claims are grounded in sources.

[SCREEN: Show highlighted claims with source links]

Green highlights mean this statement is backed by a specific source you can verify. If something isn't highlighted, treat it with more skepticism.

[SCREEN: Show Gemini browser extension icon]

Now here's something many people miss: Gemini also works as a browser extension. Install it from the Chrome Web Store and you get AI assistance on any webpage you visit. Summarize a vendor's documentation page. Get key points from an industry report. Draft a reply in Gmail. It's like having Recon and Radar deployed across your entire browsing experience, not just the Gemini chat window.

[SCREEN: Show Deep Research mode selection]

And for comprehensive analysis, both Gemini and ChatGPT offer a Deep Research mode. Instead of a quick search, Deep Research conducts multi-step autonomous research across dozens of sources, follows threads of information and produces a detailed report with citations. It takes five to ten minutes, but it produces intelligence that would take you hours manually.

[SCREEN: Comparison table]

Here's when to use each:

| Quick fact check? | Standard Gemini query |
| Comprehensive market analysis? | Deep Research |
| Summarize a webpage? | Browser extension |
| Analyze data you already have? | Claude with connectors |
| Strategic reasoning? | Claude |

The rule is simple: **Gemini gathers; Claude processes.**

---

## SECTION 4: THE FACT BRIEF [6:30-8:30]

[SCREEN: "Fact Brief" title card]

**NARRATOR:**
The most important workflow in your Squadron is the Fact Brief—the structured handoff from research to reasoning.

Here's why this matters: When Claude writes without verified facts, it can hallucinate convincing information. The Fact Brief prevents this by constraining what Claude can work with.

[DEMO: Creating a Fact Brief]

**Step 1:** Research in Gemini.

[SCREEN: Show Gemini research query]

"Research the current landscape of employee engagement platforms: pricing trends, recent feature announcements and key differentiators. Format as a bulleted fact brief with sources."

**Step 2:** Verify with Double Check.

[SCREEN: Click Double Check, show verification]

I'm confirming which claims have source support. Anything that's not grounded, I'll either research further or note as unverified.

**Step 3:** Transfer to Claude.

[SCREEN: Claude interface with structured prompt]

Now I paste this into Claude with explicit constraints:

"Based ONLY on the facts in this brief, create a comparison summary with recommendations. If you need additional facts, tell me what to research—do not invent information."

[SCREEN: Show Claude's constrained output]

See how Claude works within the boundaries? It's not inventing details because I've given it verified facts to work with. This is the power of the handoff.

[SCREEN: Fact Brief template]

Here's the template structure:

```
# Fact Brief: [Topic]
Research Date: [Date]

## Verified Facts
- [Fact] — Source: [URL]

## Needs Verification
- [Ungrounded claims]

## Research Gaps
- [What we couldn't find]
```

---

## SECTION 5: MEETING INTELLIGENCE — THE FLIGHT RECORDER [8:30-10:30]

[SCREEN: Granola interface on Mac]

**NARRATOR:**
Now let's talk about the knowledge that evaporates every day.

Think about your last important meeting. A stakeholder explained the real priorities behind a request. A teammate shared an insight about what's actually working. Someone raised a concern that could change the direction of a project.

Where did that information go?

[SCREEN: Show information "evaporating"]

If you didn't capture it in the moment, it's gone. You might remember pieces, but the nuance, the exact wording, the context is lost.

[SCREEN: Granola capturing a meeting]

This is where Flight Recorders come in. Our primary tool is Granola. It records your meeting audio locally on your Mac. No bot joining the call, no awkward "this meeting is being recorded" from a third party.

[SCREEN: Show annotation during meeting]

What makes Granola powerful: You take notes during the meeting in the Granola window. Type key points as they happen.

[SCREEN: Highlight user annotations]

"Decision: Team wants to prioritize the dashboard redesign before the Q2 launch."
"Action: Share the updated project timeline by Friday."
"Note: Engineering lead seemed concerned about the migration timeline."

[SCREEN: Show AI-enhanced summary]

When the meeting ends, Granola combines your manual notes with the transcript. Your annotations are weighted higher because they reflect your judgment about what mattered. The result is a structured, searchable, AI-ready capture of the meeting.

[SCREEN: Export to Markdown]

Export as Markdown, and you have context ready to feed to Claude.

[SCREEN: Show Chorus AI and Zoom AI Companion logos]

Now, Granola isn't the only Flight Recorder available. You should know about two alternatives.

Chorus AI, owned by ZoomInfo, is designed for teams with high call volumes. It automatically records and transcribes calls, identifies key moments like decisions, objections and action items, and integrates with CRM and project management systems. If your team has many recurring meetings, Chorus can analyze patterns across all of those conversations.

Then there's Zoom AI Companion. If your meetings already live in Zoom, AI Companion provides automatic meeting summaries, action item extraction and smart chapter markers, with zero additional setup.

[SCREEN: Comparison table of three tools]

Here's the key insight: the tool matters less than the habit. Whatever Flight Recorder you use, the workflow is the same. Capture the meeting. Export structured notes. Feed to Claude for synthesis.

---

## SECTION 6: SLACK AI — THE COMMS NETWORK [10:30-11:45]

[SCREEN: Slack AI interface with sparkle icon]

**NARRATOR:**
There's one more sensor in your array: Slack AI. Your team communicates constantly in Slack. Decisions get made. Context accumulates in channels and threads. Dependencies surface and get buried.

[SCREEN: Show Slack AI summarizing a channel]

Slack AI reads all of that and synthesizes answers on demand. Ask it "What happened in my team channel this week?" and it gives you a summary, not a scroll through hundreds of messages.

[SCREEN: Show practical examples]

Use it as your morning briefing. Before diving into work, ask Slack AI to summarize the channels most relevant to your projects. "What decisions were made about the Q2 roadmap?" "What blockers were raised in the engineering channel this sprint?"

It takes thirty seconds and can save you twenty minutes of scrolling. Think of it as your Comms Network intelligence officer, always listening and ready to brief you.

---

## SECTION 7: THE COMPLETE WORKFLOW [11:45-14:00]

[SCREEN: Workflow diagram showing all five sensor types]

**NARRATOR:**
Let's see the complete Squadron in action. Imagine you're preparing for an important cross-functional meeting where you need to present a recommendation backed by solid research.

[SCREEN: Phase 0 - Morning Briefing]

**Phase 0: Morning Briefing**

Before any research, I check what the team already knows. I ask Slack AI to summarize any relevant discussions in the project channel. Then I ask Claude, with Google Drive connected, to find any existing documents on this topic. Thirty seconds, and I know whether this work has already been done.

[SCREEN: Phase 1 - Gemini]

**Phase 1: Research Gathering**

In Gemini, I research the topic: current trends, best practices, benchmarks and expert recommendations. For a quick check, standard Gemini. For a comprehensive analysis, Deep Research mode. I verify with Double Check and create a Fact Brief.

[SCREEN: Phase 2 - Meeting Notes]

**Phase 2: Historical Context**

I pull my Flight Recorder notes from previous meetings on this initiative. The kickoff where stakeholders explained their priorities. The last check-in where certain approaches got positive reactions. The concerns that were raised about timeline or resources.

[SCREEN: Phase 3 - Claude]

**Phase 3: Synthesis**

Now I bring it all together in Claude with connectors active:

[SCREEN: Show combined prompt]

"Here's my research from Gemini. Here's what I know about stakeholder priorities from our meeting history. Also check my Google Drive for our existing project brief. Create a recommendation document that's grounded in data, addresses stakeholder concerns and proposes clear next steps."

[SCREEN: Show Claude's strategic output]

Claude produces a recommendation tailored to this exact situation. It's not a generic report. It's a deliverable informed by verified research, real stakeholder context and existing team knowledge.

[SCREEN: Summary diagram]

That's the Squadron at full power:
- Slack AI surfaced what the team already knew
- Connectors pulled in existing documents
- Gemini gathered fresh research and data
- Meeting notes preserved the stakeholder context
- Claude synthesized everything into an actionable deliverable

No hallucination. No guessing. No duplicated effort. Grounded, contextual, strategic.

---

## CLOSING: PRIVACY AND NEXT STEPS [14:00-15:00]

[SCREEN: Privacy considerations]

**NARRATOR:**
A quick word on privacy. Every sensor in your array has different data handling.

Meeting recordings create consent obligations. In two-party consent states, everyone on the call must agree to recording, whether you use Granola, Zoom AI or Chorus. Disclose when legally required.

Data connectors give AI access to everything your account can see in the connected service. Be intentional about what you connect and when. Turn off connectors when you don't need them.

[SCREEN: Module 6 preview]

Your Squadron now has complete senses: connectors for direct data feeds, Gemini for web intelligence, meeting tools for conversation capture and Slack AI for team context. But there's one more danger we haven't addressed: **sycophancy**.

AI models want to please you. They tend to agree with your ideas, avoid challenging your assumptions and tell you what you want to hear rather than what you need to know.

[SCREEN: "Module 6: Decision Hygiene" preview]

In Module 6, you'll learn to beat sycophancy with Red Teaming, Pre-Mortem analysis and neutral framing, techniques that ensure your AI tells you the truth.

[SCREEN: Lab preview]

For now, head to the lab. You'll practice:
- Setting up and managing data connectors
- Conducting Gemini research with verification and Deep Research
- Creating and transferring Fact Briefs
- Processing meeting context with Claude
- Using Slack AI for team intelligence
- Executing a complete Squadron workflow with all sensors active

Remember: Connectors feed your data. Gemini sees the world. Meeting tools capture conversations. Slack AI monitors your team. And Claude thinks it all through. Together, they're unstoppable.

[TITLE CARD: Module 5 Complete - Proceed to Lab]

---

## END OF SCRIPT

**Total Runtime:** ~15:00

**Key Visual Assets Needed:**
- Squadron diagram with five components (expanded from three)
- Claude Settings > Connected Apps walkthrough
- Gemini interface with Double Check demonstration
- Gemini browser extension in action
- Deep Research mode selection and results
- Fact Brief template visual
- Granola Mac interface with annotation
- Chorus AI and Zoom AI Companion comparison
- Slack AI interface with channel summary
- Five-phase workflow animation
- Privacy considerations summary (expanded)
