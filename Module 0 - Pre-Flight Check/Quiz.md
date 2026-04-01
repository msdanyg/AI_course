# Module 0 Quiz
## Pre-Flight Check: Setup, Policy & Boundaries

**Instructions:** 6 questions. Mix of multiple choice, true/false with explanation, and scenario-based. Feedback provided for all answers.

---

### Question 1 (Multiple Choice)

**What is the "Mission Control" role in the Squadron framework?**

A) Real-time web search and fact verification
B) Meeting transcription and note capture
C) Reasoning, strategy, writing, and synthesis
D) Google Workspace integration and document search

**Correct Answer:** C

**Feedback for C (Correct):**
Exactly right. Mission Control is your reasoning engine—tools like Claude, ChatGPT, or Claude Code that excel at strategic thinking, writing, coding, and synthesizing information. Different employees may have different Mission Control tools, but they all serve this same role.

**Feedback for other answers:**
- **Option A**: Real-time web search is the Recon & Radar role (Gemini, Bing AI)
- **Option B**: Meeting transcription is the Flight Recorder role (Granola, Chorus, Zoom AI)
- **Option D**: Workspace integration is also part of the Recon & Radar role

---

### Question 2 (Scenario-Based)

**Scenario:** You need to draft a QBR email for a customer. You have meeting notes from your last call, you want to check their current industry news, and you need to write the email.

**What is the optimal Squadron role workflow?**

A) Use Recon & Radar for everything
B) Use Mission Control for everything
C) Flight Recorder for notes → Recon & Radar for research → Mission Control for writing
D) Mission Control for notes → Flight Recorder for research → Recon & Radar for writing

**Correct Answer:** C

**Feedback for C (Correct):**
This is the Squadron Leader approach. Each role handles what it does best:
- **Flight Recorder** (Granola, Chorus, Zoom AI) captured the meeting notes
- **Recon & Radar** (Gemini, Bing AI) fetches current industry news in real-time
- **Mission Control** (Claude, ChatGPT) synthesizes everything into a well-crafted email

This workflow leverages each role's strengths rather than forcing one tool to do everything.

**Feedback for other answers:**
- **Option A**: Recon tools can't access your meeting notes and aren't optimized for long-form writing
- **Option B**: Mission Control tools can't search the web for current industry news
- **Option D**: The roles are assigned to wrong tasks

---

### Question 3 (True/False with Explanation)

**TRUE or FALSE: Customer names and email addresses from Salesforce should never be shared with AI tools because they contain PII.**

**Correct Answer:** FALSE

**Feedback if FALSE (Correct):**
Correct. Customer names and emails are **Green zone** data—you can use them freely for analysis and drafting. The Traffic Light Protocol is about risk management, not blanket prohibition.

The key principles:
- The risk is in **unreviewed output**, not in analysis
- Green zone data can be used for internal work
- Just review AI outputs before sharing externally

This is why "AI drafts, humans send" is the core principle—the human review step is where governance happens.

**Feedback if TRUE (Incorrect):**
Customer names and emails are actually **Green zone** data. The Traffic Light Protocol doesn't prohibit using PII for analysis—it requires you to review outputs before external distribution. The risk isn't in analyzing data; it's in sharing unreviewed AI output. Use customer data freely for your work, and apply the "AI drafts, humans send" principle.

---

### Question 4 (Multiple Choice)

**Which data type falls into the RED zone and should NEVER be shared with AI tools?**

A) A customer's account usage data from ActivTrak analytics
B) Internal meeting notes discussing competitive strategy
C) An API key for a Salesforce integration
D) A draft case study that includes a customer quote

**Correct Answer:** C

**Feedback for C (Correct):**
Exactly. API keys, passwords, and credentials are **Red zone**—never share them with any AI tool. These create genuine security risks regardless of how the output is used.

The other options:
- Account usage data is Green (internal analytics)
- Meeting notes are Green (internal documentation)
- Case study with quotes is Yellow (may need PR review before external distribution, but safe to analyze)

Red zone is specifically for security credentials and secrets that could compromise systems if exposed.

**Feedback for other answers:**
- **Option A**: Account usage data is Green zone—internal analytics used freely for analysis
- **Option B**: Internal meeting notes are Green zone—safe for AI analysis
- **Option D**: Case study with quotes is Yellow zone—safe to analyze, but may need review before external distribution

---

### Question 5 (Scenario-Based)

**Scenario:** You've asked Claude to draft a competitive positioning email based on data you provided. Claude produces a response that looks good. What should you do next?

A) Copy and send immediately—Claude's outputs are reliable
B) Review the output for accuracy and appropriateness before sending
C) Ask Claude to verify its own output before sending
D) Run the same prompt in Gemini to cross-check

**Correct Answer:** B

**Feedback for B (Correct):**
This is the "AI drafts, humans send" principle in action. You review AI outputs before they go external because:

1. You own what leaves the runway—AI-generated content is your responsibility
2. AI can make subtle errors or assumptions you'd catch on review
3. Tone, accuracy, and appropriateness require human judgment
4. External communications affect relationships and reputation

This doesn't mean you distrust the AI—it means you apply professional standards to anything going out under your name.

**Feedback for other answers:**
- **Option A**: Never auto-send AI outputs externally. Review is always required.
- **Option C**: AI can't reliably verify its own output—human review is the governance mechanism
- **Option D**: Cross-checking might help, but the core requirement is human review before sending

---

### Question 6 (True/False with Explanation)

**TRUE or FALSE: The difference between a Solo Pilot and a Squadron Leader is primarily about which AI tools they use.**

**Correct Answer:** FALSE

**Feedback if FALSE (Correct):**
Correct. The difference is about **mindset and approach**, not tool selection.

**Solo Pilot thinking:**
- Minimal context ("Write me an email")
- Freeform, one-off questions
- Starts fresh every conversation
- Copy-pastes outputs directly

**Squadron Leader thinking:**
- Rich context (background, goals, constraints)
- Structured requests with clear outputs
- Maintains persistent knowledge (Projects)
- Verifies and refines before use

Both might use the same tools. The Squadron Leader gets dramatically better results by orchestrating those tools with context, structure, and review.

**Feedback if TRUE (Incorrect):**
The difference is actually about mindset, not tools. A Solo Pilot with access to Claude, Gemini, and Granola still gets mediocre results if they use minimal context and freeform questions. A Squadron Leader gets excellent results by providing rich context, structuring requests, maintaining persistent knowledge, and reviewing outputs—regardless of which specific tools they use.

---

## Quiz Complete

**Score Interpretation:**

- **5-6 correct**: Ready to fly. You understand your tools and the governance framework.
- **3-4 correct**: Review the Traffic Light Protocol and tool roles before proceeding.
- **0-2 correct**: Re-read the lesson. Understanding these fundamentals is essential for the rest of the course.

**Key Concepts to Master:**
1. Three tools: Claude (reasoning), Gemini (research), Granola (capture)
2. Traffic Light: Green (go), Yellow (review), Red (never)
3. Core principle: "AI drafts, humans send"
4. Squadron Leader = mindset shift, not just tool access

---

**Proceed to Study Guide to consolidate your learning.**
