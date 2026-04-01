# Module 5: The Sensory System
## Flashcards

---

### Card 1

**Front:**
What is the "Blind Strategist Problem" and how does it affect Claude?

**Back:**
**The Blind Strategist Problem:** Claude is an extraordinary reasoning engine, but it operates in a sealed room—it can't access current information from the outside world.

**Effects:**
- Can't verify current pricing, news, or facts
- May provide outdated information from training data
- May hallucinate plausible-sounding but incorrect information

**Solution:** Use Gemini (Recon & Radar) to gather verified, current intelligence and feed it to Claude.

---

### Card 2

**Front:**
What are the five sensor types in a complete Squadron, and what does each do?

**Back:**
| Component | Tools | Function |
|-----------|-------|----------|
| **Mission Control** | Claude, ChatGPT | Reasoning, strategy, synthesis, writing |
| **Supply Lines** | Data Connectors (GDrive, Slack, Gmail, Monday) | Direct data feeds into Mission Control |
| **Recon & Radar** | Gemini, browser extensions, Deep Research | Real-time research, fact verification, grounding |
| **Flight Recorder** | Granola, Chorus AI, Zoom AI Companion | Meeting capture, structured context, institutional memory |
| **Comms Network** | Slack AI Bot | Team communication intelligence, async knowledge |

**The Rule:** Connectors feed; Gemini gathers; meeting tools capture; Slack AI listens; Claude processes.

---

### Card 3

**Front:**
What is "Grounding with Google Search" and why does it matter?

**Back:**
**Grounding:** Gemini's capability to anchor outputs to verifiable, real-world data sources by actually searching the web.

**How it works:**
1. Analyzes your question
2. Generates multiple optimized search queries
3. Retrieves and synthesizes information from sources
4. Provides citations linking claims to sources

**Why it matters:** Unlike Claude (which predicts based on training data), Gemini retrieves current, verifiable information—preventing hallucination of facts.

---

### Card 4

**Front:**
What is the "Double Check" feature in Gemini and how should you use it?

**Back:**
**Double Check:** A Gemini Advanced feature that highlights which claims in a response are grounded in sources.

**How to use it:**
1. After receiving a research response, click "Double Check"
2. Green highlights = claim backed by verifiable source
3. Click highlighted claims to see source links
4. Ungrounded claims need additional verification

**Squadron Protocol:** Always Double Check before including researched facts in client-facing materials.

---

### Card 5

**Front:**
What is a "Fact Brief" and why is it critical to the Squadron workflow?

**Back:**
**Fact Brief:** A structured document transferring verified research from Gemini to Claude.

**Why it's critical:**
- Constrains Claude to work only with verified facts
- Creates an audit trail (every claim traces to a source)
- Separates research (Gemini) from writing (Claude)
- Prevents Claude from hallucinating information

**Template sections:**
- Verified Facts (with sources)
- Needs Verification (ungrounded claims)
- Research Gaps (what couldn't be found)

---

### Card 6

**Front:**
What are the three Flight Recorder options and how do they compare?

**Back:**
| Feature | Granola | Chorus AI | Zoom AI Companion |
|---------|---------|-----------|-------------------|
| Visibility | Invisible (local) | Bot joins call | Built into Zoom |
| Best for | Individual capture + annotation | Sales team analytics | Zoom-native workflows |
| AI summary | Enhanced by your notes | Automated with deal focus | Automated general |
| CRM integration | Manual export | Automatic | Zoom ecosystem |
| Privacy | Local-first on Mac | Cloud-based | Zoom cloud |

**Key insight:** The tool matters less than the habit. Whatever Flight Recorder you use, the workflow is the same: capture → export → feed to Claude.

---

### Card 7

**Front:**
Describe the three-phase workflow for preparing an important meeting using all Squadron components.

**Back:**
**Phase 1: Research Gathering (Gemini)**
- Research the topic: trends, benchmarks, best practices
- Verify with Double Check
- Create structured Fact Brief

**Phase 2: Historical Context (Flight Recorder → Claude)**
- Pull meeting notes from previous discussions on this topic
- Identify stakeholders' real priorities, concerns, positive reactions

**Phase 3: Synthesis (Claude)**
- Combine Fact Brief + meeting context
- Generate tailored deliverable (brief, recommendation, presentation)
- Output based on verified research, not guessing

**Result:** Grounded, contextual, strategic output.

---

### Card 8

**Front:**
What privacy considerations apply when using Granola for meeting recording?

**Back:**
**Legal Requirements:**
- Two-party consent states require all participants to agree to recording
- Granola's invisible operation doesn't exempt you from consent requirements
- Disclose recording at start of calls when legally required

**Best Practices:**
- Never record sensitive conversations without appropriate consent
- Use Granola's local processing to minimize data exposure
- Delete recordings after processing if not needed long-term
- Know your organization's approved tools and data handling requirements

---

### Card 9

**Front:**
What are data connectors (Supply Lines) and why are they important?

**Back:**
**Data connectors** are integrations that give Claude and ChatGPT direct access to your workspace data: Google Drive, Slack, Gmail, Monday/Atlassian.

**Why they matter:**
- Eliminate copy-pasting documents into every conversation
- Let Claude pull context from existing files, emails and project boards
- Enable prompts like "Check my Google Drive for the latest project status deck"

**Critical rule:** Turn OFF connectors you aren't actively using. Each active connector consumes context window space, leaving less room for Claude's reasoning.

**Go-to connectors:** Google Drive, Slack, Gmail, Atlassian/Monday

---

### Card 10

**Front:**
What is Deep Research and when should you use it instead of a standard query?

**Back:**
**Deep Research** is an autonomous, multi-step research mode available in Gemini Advanced and ChatGPT Plus/Enterprise.

**How it differs from standard queries:**
- Conducts research across dozens of sources (not just one search)
- Follows threads of information, refining queries as it goes
- Produces comprehensive reports (often several pages) with citations
- Takes 5-10 minutes instead of seconds

**Use Deep Research for:**
- Comprehensive market analysis
- Multi-competitor landscape reviews
- Industry trend reports
- Executive presentation prep

**Use standard queries for:**
- Quick fact checks, current pricing lookups, single-topic questions

---

### Card 11

**Front:**
What is Slack AI and how does it function as the Squadron's Comms Network?

**Back:**
**Slack AI** analyzes your workspace's messages to provide synthesized intelligence from team communications.

**Key capabilities:**
- **Channel summaries:** "What happened in #product-updates this week?"
- **Thread summaries:** Condense long discussions into key points
- **Search answers:** Natural language questions answered from workspace history
- **Catch-up digests:** Summarize what you missed

**Squadron Protocol:** Use Slack AI as your "morning briefing" before diving into work. Ask it to summarize the channels most relevant to your projects. Takes 30 seconds, saves 20 minutes of scrolling.

**The difference:** Manual search returns individual messages you piece together. Slack AI reads everything and gives you the synthesized answer.

---

### Card 12

**Front:**
What are Gemini browser extensions and what are they best used for?

**Back:**
**Gemini browser extensions** bring AI assistance to any webpage you visit, extending Recon & Radar beyond the Gemini chat window.

**What they do:**
- Summarize web pages, articles and PDFs you're viewing
- Answer questions about page content in a sidebar
- Help compose emails directly in Gmail
- Provide context while you browse

**Best ActivTrak use cases:**
- Summarize a vendor's documentation page or product changelog
- Get key points from a long industry report
- Draft email replies with Gemini's help in Gmail
- Pull highlights from a partner's website before a collaboration meeting

**Squadron metaphor:** "Passive radar" deployed across your entire browsing experience.

---

## Study Tips

1. **Set up your connectors:** Go to Claude Settings > Connected Apps and enable Google Drive as a starting point. Try asking Claude to reference an existing document.

2. **Practice the Fact Brief workflow:** Research something in Gemini, verify with Double Check, and transfer to Claude. Notice how constraining Claude improves output.

3. **Try Deep Research:** Pick a topic you'd normally spend an hour researching manually. Use Deep Research mode and compare the result.

4. **Map your Squadron:** For each type of task you do regularly, identify which sensor should handle which part.

5. **Start your morning with Slack AI:** Ask it to summarize yesterday's activity in your most important channels.

6. **Think about capture:** What valuable information evaporates after your meetings? Which Flight Recorder fits your workflow?

7. **Remember the rule:** Connect first, ground second, synthesize third. Never skip the verification step.
