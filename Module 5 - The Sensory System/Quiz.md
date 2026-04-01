# Module 5: The Sensory System
## Knowledge Check Quiz

**Instructions:** Answer all questions. Review feedback after each answer to reinforce learning.

---

### Question 1 (Multiple Choice)

What is "The Blind Strategist Problem"?

A) Claude cannot process images or visual content
B) Claude lacks real-time access to web information and current events
C) Claude cannot understand complex strategic questions
D) Claude's knowledge is encrypted and inaccessible

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** Claude's knowledge has a training cutoff date. It cannot browse the web, check current prices, verify recent news or access real-time information. Like a brilliant strategist working in a sealed room, Claude can reason powerfully but only with the information you provide.
- **Why A is wrong:** Claude can process images—the issue is about current information access, not visual processing.
- **Why C is wrong:** Claude excels at strategic reasoning; the limitation is input, not processing.
- **Why D is wrong:** Claude's knowledge is accessible; it's just frozen at the training cutoff.

---

### Question 2 (Multiple Choice)

What is "Grounding with Google Search" in Gemini?

A) A feature that connects Gemini to Google Drive
B) Gemini's ability to retrieve current web information and provide source citations
C) A search engine built into the Gemini interface
D) A way to verify Gemini's training data accuracy

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** Grounding with Google Search allows Gemini to access current web information and cite sources. Unlike Claude's frozen knowledge, Gemini can retrieve today's pricing, recent announcements, current reviews and breaking news—then provide links to verify each claim.
- **Why A is wrong:** While Google Drive integration exists, grounding specifically refers to web search capability.
- **Why C is wrong:** It's more than a search engine—Gemini synthesizes and cites information.
- **Why D is wrong:** Grounding retrieves new information; it doesn't verify training data.

---

### Question 3 (Multiple Choice)

What is the purpose of Gemini's "Double Check" feature?

A) To run calculations twice for accuracy
B) To highlight which claims are supported by current sources vs. which may need verification
C) To compare Gemini's response to Claude's response
D) To check grammar and spelling in responses

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** Double Check analyzes Gemini's response and highlights statements according to their source support. Green highlighting indicates claims backed by found sources; orange indicates statements that couldn't be verified. This helps you distinguish between grounded facts and potential AI additions.
- **Why A is wrong:** Double Check is about source verification, not mathematical accuracy.
- **Why C is wrong:** Double Check works within Gemini; it doesn't compare to other AI tools.
- **Why D is wrong:** Double Check is about factual verification, not writing quality.

---

### Question 4 (Multiple Choice)

What is a "Fact Brief"?

A) A short summary of a conversation
B) A structured document containing verified research with sources for handoff to Claude
C) A template for writing meeting notes
D) A checklist for verifying AI outputs

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** A Fact Brief is a structured document that captures verified research from Gemini, organized with sources, and formatted for clean handoff to Claude. It includes: Verified Facts (with URLs), items Needing Verification, and Research Gaps. This ensures Claude works with grounded information rather than generating assumptions.
- **Why A is wrong:** A Fact Brief is specifically for verified research, not general summaries.
- **Why C is wrong:** Meeting notes are captured by Granola; Fact Briefs are for research.
- **Why D is wrong:** While it helps verification, a Fact Brief is a research document, not a checklist.

---

### Question 5 (True/False with Explanation)

**Statement:** Granola records meetings locally on your device and never sends audio to external servers.

A) True
B) False

**Correct Answer:** A (True)

**Feedback:**
Granola uses a local-first architecture. Audio is processed on your Mac using on-device transcription, and recordings stay on your local machine. This addresses privacy concerns about cloud-based recording services. However, you should still follow proper disclosure practices and be aware of two-party consent requirements in states like California.

---

### Question 6 (Multiple Choice)

Why does Granola weight your typed notes more heavily than raw transcription in its summaries?

A) Typed notes are shorter and easier to process
B) Typed notes capture what you found important in the moment
C) Transcription is less accurate than typed notes
D) Granola cannot process long transcriptions

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** When you type a note during a conversation, you're signaling that moment's importance. Granola's algorithm gives higher weight to sections where you annotated, surfacing what mattered most to you rather than just what was said longest.
- **Why A is wrong:** Length doesn't determine importance in Granola's algorithm.
- **Why C is wrong:** Transcription accuracy isn't the differentiator—relevance is.
- **Why D is wrong:** Granola handles long transcriptions; weighting is about relevance.

---

### Question 7 (Scenario-Based)

A team member is evaluating new software tools for their department. They want current pricing, recent feature updates and customer review themes. Which approach follows the Squadron workflow?

A) Ask Claude to provide a comparison of the tools
B) Use Gemini to research and create a Fact Brief, then give the Fact Brief to Claude for analysis and recommendation
C) Search Google manually and paste results directly into Claude
D) Ask Gemini for a recommendation document

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** This follows the complete Squadron workflow: Gemini (Recon) gathers current, grounded intelligence with sources → Fact Brief structures the verified information → Claude (Mission Control) synthesizes analysis and recommendations based on verified facts. Each tool does what it's best at.
- **Why A is wrong:** Claude would draw on potentially outdated training data, not current information.
- **Why C is wrong:** Manual searching works but misses Gemini's synthesis and citation capabilities.
- **Why D is wrong:** Gemini should gather facts; Claude should synthesize recommendations. Using Gemini for analysis skips the grounding advantage.

---

### Question 8 (Multiple Choice)

What information should you NOT include when pasting Granola transcripts into Claude?

A) Attendee names and roles
B) Key discussion points
C) Confidential data not approved for AI processing
D) Action items discussed

**Correct Answer:** C

**Feedback:**
- **Why C is correct:** Before sharing meeting content with any AI, verify the information classification. Confidential data, sensitive personnel discussions or information covered by NDAs may not be appropriate for AI processing. When in doubt, consult your data classification policies or ask your manager.
- **Why A, B, D are wrong:** Attendee context, discussion points and action items are typically appropriate and valuable for AI processing, assuming the meeting content itself is cleared for AI use.

---

### Question 9 (Multiple Choice)

In the Squadron Framework, what are the five sensor types and their roles?

A) Claude = Research, Gemini = Analysis, Granola = Storage, Slack = Chat, Connectors = Backup
B) Mission Control (Claude: reasoning), Supply Lines (Connectors: data feeds), Recon & Radar (Gemini: research), Flight Recorder (meeting AI: capture), Comms Network (Slack AI: team intel)
C) All five tools perform the same functions interchangeably
D) Claude = Writing, Gemini = Search, Granola = Calendar, Slack = Messaging, Connectors = File sharing

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** The Squadron Framework assigns specialized roles:
  - **Mission Control (Claude/ChatGPT):** Deep reasoning, strategic synthesis, content generation
  - **Supply Lines (Connectors):** Direct data feeds from Google Drive, Slack, Gmail, Monday/Atlassian
  - **Recon & Radar (Gemini + extensions + Deep Research):** Real-time web research with source citations
  - **Flight Recorder (Granola, Chorus AI, Zoom AI):** Meeting capture and institutional memory
  - **Comms Network (Slack AI):** Team communication intelligence and async knowledge
  Together they create a complete sensory system.
- **Why A is wrong:** Claude does analysis/synthesis, not primary research; connectors provide live data, not backup.
- **Why C is wrong:** Each tool has distinct strengths; interchangeable use wastes their specialization.
- **Why D is wrong:** This oversimplifies each tool's sophisticated capabilities.

---

### Question 10 (Scenario-Based)

Order these steps according to the correct Squadron workflow for preparing a client meeting brief:

1. Paste Fact Brief and meeting context into Claude for synthesis
2. Use Gemini to research competitive intelligence
3. Export relevant Granola notes from previous client meetings
4. Ask Claude to create a meeting preparation document

A) 4 → 1 → 2 → 3
B) 2 → 3 → 1 → 4
C) 3 → 2 → 4 → 1
D) 1 → 4 → 2 → 3

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** The proper Squadron workflow is:
  1. **Gemini research (2):** Gather current intelligence, create Fact Brief
  2. **Granola export (3):** Pull historical meeting context
  3. **Claude synthesis (1):** Combine Fact Brief + meeting context
  4. **Final deliverable (4):** Generate the meeting preparation document
- This ensures Claude works with verified, current facts and relevant historical context.

---

### Question 11 (Multiple Choice)

What are data connectors (Supply Lines) in the Squadron framework?

A) External APIs that connect different AI tools to each other
B) Integrations that give Claude and ChatGPT direct access to workspace data like Google Drive, Slack and Gmail
C) Physical cables connecting your computer to cloud services
D) Browser extensions that sync data between tabs

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** Data connectors are integrations in Claude and ChatGPT that create direct pipelines to your existing work systems. Once enabled, Claude can reference Google Drive documents, Slack channel discussions, Gmail threads and project boards without you manually copy-pasting content. They are the "Supply Lines" that feed intelligence directly into Mission Control.
- **Why A is wrong:** Connectors link AI tools to data sources, not to each other.
- **Why C is wrong:** Connectors are software integrations, not physical connections.
- **Why D is wrong:** Browser extensions are a separate capability (Gemini extensions), not data connectors.

---

### Question 12 (Multiple Choice)

Why is it important to turn off unused data connectors?

A) Unused connectors slow down your internet connection
B) Each active connector consumes context window space, leaving less room for Claude's reasoning
C) Connectors expire if left on too long
D) Active connectors continuously send notifications

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** Every active connector takes up space in Claude's context window. If you have Google Drive, Slack, Gmail and Monday all connected but you're only doing a document analysis task, the other connectors are consuming valuable context capacity that Claude could use for deeper reasoning. Best practice is to enable only what you need for the current task.
- **Why A is wrong:** Connectors don't affect internet speed.
- **Why C is wrong:** Connectors remain active until you disable them.
- **Why D is wrong:** Connectors provide data access, not notifications.

---

### Question 13 (Multiple Choice)

When should you use Deep Research mode instead of a standard Gemini query?

A) For any question that requires a web search
B) When you need a comprehensive, multi-source analysis such as a market landscape or competitive deep-dive
C) Only when Gemini's standard response is incorrect
D) Whenever you're in a hurry and need quick results

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** Deep Research is designed for comprehensive analysis that draws from dozens of sources. It autonomously conducts multi-step research, follows threads of information and produces detailed reports with citations. Best use cases include market landscapes, multi-competitor reviews, industry trend reports and executive presentation prep.
- **Why A is wrong:** Standard queries handle simple fact checks efficiently; Deep Research is overkill for quick lookups.
- **Why C is wrong:** Deep Research isn't a correction tool; it's for depth, not accuracy fixes.
- **Why D is wrong:** Deep Research takes 5-10 minutes, making it slower than standard queries. Use it when depth matters more than speed.

---

### Question 14 (Scenario-Based)

A team member returns from a week of PTO and needs to quickly catch up on what happened with their projects. Which approach best uses the Squadron's sensory system?

A) Read through every Slack channel manually to find relevant updates
B) Ask Claude to summarize what happened while they were away
C) Use Slack AI to summarize key channels, then check meeting notes from their Flight Recorder for any meetings they missed
D) Email colleagues asking for updates

**Correct Answer:** C

**Feedback:**
- **Why C is correct:** This combines two Squadron sensors efficiently. Slack AI (Comms Network) can instantly summarize channel activity from the past week, surfacing decisions, key discussions and action items. The Flight Recorder (Granola, Zoom AI or Chorus) captures any meetings that happened during PTO. Together, they provide comprehensive catch-up in minutes instead of hours.
- **Why A is wrong:** Manual scrolling through channels is exactly the time-consuming approach Slack AI replaces.
- **Why B is wrong:** Claude doesn't have access to what happened in your Slack channels or meetings unless that information is provided to it (via connectors or manual input).
- **Why D is wrong:** While colleagues can help, this puts the burden on others and produces incomplete, delayed results.

---

## Scoring Guide

- **14/14 correct:** Excellent! You've mastered the complete Squadron Sensory System. Ready for Module 6.
- **12-13 correct:** Strong understanding. Review the concepts you missed before proceeding.
- **10-11 correct:** Good foundation. Rewatch the video sections on connectors and the expanded toolkit.
- **7-9 correct:** Review the lesson content and repeat the lab exercise.
- **0-6 correct:** Schedule time to thoroughly review Module 5 before proceeding.

---

*Quiz complete. Review the Study Guide for a quick reference summary.*
