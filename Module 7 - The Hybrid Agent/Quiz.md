# Module 7 Quiz
## The Hybrid Agent (Mac, Mobile & Docs)

**Instructions:** 7 questions. Mix of multiple choice, true/false with explanation, and scenario-based. Feedback provided for all answers.

---

### Question 1 (Multiple Choice)

**What are the four phases of the Ramble-to-Gold workflow in the correct order?**

A) Process → Capture → Sync → Refine
B) Capture → Process → Sync → Refine
C) Capture → Sync → Process → Refine
D) Sync → Capture → Process → Refine

**Correct Answer:** C

**Feedback for C (Correct):**
Exactly right. The workflow is:
1. **Capture** (record voice on mobile)
2. **Sync** (automatic iCloud/account sync)
3. **Process** (feed to Claude Desktop with structured prompt)
4. **Refine** (iterate on the draft)

This sequence lets you capture thinking when clarity strikes, then refine it when you have processing power.

**Feedback for other answers:**
The workflow must start with Capture (getting the raw thinking down) and end with Refine (polishing the output). Process can only happen after Sync delivers the content to your desktop environment.

---

### Question 2 (True/False with Explanation)

**TRUE or FALSE: When pasting a table from Claude into Google Docs, you should copy the Markdown code block and paste it directly.**

**Correct Answer:** FALSE

**Feedback if FALSE (Correct):**
Correct. Google Docs doesn't understand Markdown formatting. Instead, you should:
1. Ask Claude to generate an HTML table with inline CSS
2. Have Claude render it (not show code)
3. Copy the **rendered visual table**
4. Paste into Google Docs

The HTML/CSS structure is what Docs translates into formatted tables. Markdown will paste as plain text with pipes and hyphens.

**Feedback if TRUE (Incorrect):**
Google Docs doesn't natively support Markdown. Pasting Markdown code results in unformatted text. The correct approach is the "HTML Bridge": ask for HTML with inline CSS, copy the rendered output, and paste that into Docs. The browser's clipboard contains the HTML structure that Docs can interpret.

---

### Question 3 (Multiple Choice)

**Which CSS property is MOST critical to include when asking Claude to generate HTML tables for Google Docs?**

A) `font-family`
B) `border-collapse: collapse`
C) `margin: auto`
D) `width: 100%`

**Correct Answer:** B

**Feedback for B (Correct):**
Correct. `border-collapse: collapse` is critical because it prevents double borders when pasting into Docs. Without it, each cell might have individual borders that don't connect properly, creating a messy visual appearance. This single property ensures clean, professional table formatting.

**Feedback for other answers:**
While font-family, margin, and width can improve appearance, `border-collapse: collapse` is the make-or-break property for tables in Google Docs. Without it, your table borders will be doubled or misaligned, requiring manual fixing. Always include it in your HTML table requests.

---

### Question 4 (Scenario-Based)

**Scenario:** You're on a train headed to a client meeting in 20 minutes. You need to quickly review the key concerns from the last three QBRs with this client and prepare talking points.

**Which approach is MOST effective?**

A) Wait until you reach your desk, then review files and prepare
B) Open Claude mobile, voice query your Squadron Project for QBR synthesis
C) Scroll through old emails on your phone trying to find notes
D) Text a colleague to ask what they remember

**Correct Answer:** B

**Feedback for B (Correct):**
Exactly right. This is the perfect use case for Claude mobile with Projects:
- Your Project already contains QBR history
- Voice query is fast (no typing on mobile)
- Claude synthesizes across multiple meetings instantly
- You can screenshot the summary for reference during the meeting

This workflow turns transit time into productive prep time with zero friction.

**Feedback for other answers:**
Option A wastes the 20 minutes you have. Option C is inefficient (searching email threads is slow and incomplete). Option D puts burden on others and relies on fallible human memory. Claude mobile with Projects gives you instant, comprehensive synthesis of documented history—exactly what you need for preparation.

---

### Question 5 (Multiple Choice - Multiple Correct Indicators)

**Select ALL advantages of Claude Desktop on Mac compared to the web version:**

A) Universal drag-and-drop for PDFs, screenshots, and folders
B) Access to real-time web search
C) Native Mac notifications when analysis completes
D) Faster response times due to local processing
E) Keyboard shortcuts for common actions

**Correct Answers:** A, C, E

**Feedback if A, C, E selected (Correct):**
Correct. Claude Desktop on Mac provides:
- **Universal drag-and-drop** (A): Drag files directly from Finder, screenshots immediately after capture
- **Native notifications** (C): Get alerts when long tasks complete, even if you've switched apps
- **Keyboard shortcuts** (E): Cmd+N for new chat, Cmd+Shift+P for new Project, etc.

Options B and D are incorrect: Claude Desktop doesn't have real-time web search (that's Gemini's strength), and processing still happens on Anthropic's servers, not locally.

**Feedback for other combinations:**
Claude Desktop doesn't provide real-time web search (B)—that's Gemini's capability. Processing doesn't happen locally (D)—Claude still uses Anthropic's cloud servers. The real advantages are Mac ecosystem integration: drag-and-drop (A), notifications (C), and keyboard shortcuts (E).

---

### Question 6 (True/False with Explanation)

**TRUE or FALSE: You should use Gemini instead of Claude when you need deep reasoning and complex strategic analysis.**

**Correct Answer:** FALSE

**Feedback if FALSE (Correct):**
Correct. The decision matrix is:
- **Claude**: Deep reasoning, complex analysis, coding, large context synthesis
- **Gemini**: Real-time research, Google Workspace integration, quick collaborative edits

Gemini's strength is grounding (current information) and native Google app integration. Claude excels at sophisticated reasoning, strategy, and processing large contexts. For strategic analysis, Claude is the primary tool; Gemini provides the verified facts that feed Claude's reasoning.

**Feedback if TRUE (Incorrect):**
This is backwards. Claude is purpose-built for deep reasoning with features like Extended Thinking, large context windows (200k tokens), and Projects for persistent knowledge. Gemini's strengths are real-time research (grounding) and native Google Workspace integration. For complex strategic analysis, use Claude. Use Gemini to gather current facts, then transfer those to Claude for synthesis and reasoning.

---

### Question 7 (Scenario-Based)

**Scenario:** You're building a quarterly report that requires:
- Current industry statistics (real-time data)
- Analysis of internal usage data (CSV file)
- Strategic recommendations based on trends
- A formatted deliverable for team review in Google Docs

**What is the optimal Squadron workflow?**

A) Do everything in Claude from start to finish
B) Do everything in Gemini from start to finish
C) Gemini (research) → Claude (analysis + strategy) → HTML Bridge (to Docs)
D) Claude (analysis) → Gemini (research) → Directly edit in Docs

**Correct Answer:** C

**Feedback for C (Correct):**
Perfect. This leverages each tool's strengths:

1. **Gemini** (research): Gather current industry stats with grounding, create Fact Brief
2. **Claude** (analysis + strategy): Upload internal CSV, analyze with Python, synthesize with Fact Brief, generate strategic recommendations, output as HTML
3. **HTML Bridge** (to Docs): Paste formatted content into Docs for team collaboration

This workflow ensures verified data, powerful analysis, and collaborative delivery. Each tool does what it does best.

**Feedback for other answers:**
- **Option A**: Claude can't gather current real-time stats (no web access)
- **Option B**: Gemini isn't as strong at deep strategic analysis or complex data processing
- **Option D**: The sequence is wrong—you need verified facts before you can analyze

The correct sequence always starts with research (Gemini for current data), moves to synthesis (Claude for reasoning), and ends with collaboration (Docs with proper formatting).

---

## Quiz Complete

**Score Interpretation:**

- **6-7 correct**: Squadron Leader mastery. You understand how to orchestrate tools across platforms for maximum efficiency.
- **4-5 correct**: Squadron competency. Review the sections on HTML Bridge and platform selection to strengthen your workflows.
- **0-3 correct**: Revisit the lesson, focusing on the decision matrix (when to use which tool) and the Ramble-to-Gold workflow.

**Key Concepts to Master:**
1. Ramble-to-Gold captures thinking when it happens, refines later
2. HTML Bridge solves Google Docs formatting with inline CSS
3. Claude Desktop provides Mac ecosystem advantages (drag-and-drop)
4. Platform selection is strategic: use each tool for its strength
5. Cross-device context persistence eliminates repetition

---

**Proceed to Study Guide to consolidate your learning.**
