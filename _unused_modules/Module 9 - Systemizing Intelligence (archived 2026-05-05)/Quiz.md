# Module 8 Quiz
## Systemizing Intelligence: Projects, Skills, Gems & Custom GPTs

**Instructions:** 7 questions. Mix of multiple choice, true/false with explanation, and scenario-based. Feedback provided for all answers.

---

### Question 1 (Multiple Choice)

**What are the three components that make up a Claude Project?**

A) Custom GPTs, Skills, and Conversations
B) Custom Instructions, Knowledge Files, and Conversation History
C) Templates, Documents, and Chat Logs
D) Prompts, Files, and Memory

**Correct Answer:** B

**Feedback for B (Correct):**
Exactly right. A Claude Project consists of:
1. **Custom Instructions** - Persistent prompts that shape Claude's behavior
2. **Knowledge Files** - Documents Claude can reference (PDFs, CSVs, etc.)
3. **Conversation History** - Past chats that provide ongoing context

This trio creates a persistent workspace that eliminates the "contextual amnesia" of starting fresh every conversation.

**Feedback for other answers:**
The correct components are Custom Instructions (how Claude behaves), Knowledge Files (reference documents), and Conversation History (ongoing context). Custom GPTs are a separate ChatGPT feature. "Skills" are reusable prompt templates, not a Project component. "Memory" and "Templates" aren't official Claude terminology.

---

### Question 2 (True/False with Explanation)

**TRUE or FALSE: You should create a Claude Project for every task you do with AI.**

**Correct Answer:** FALSE

**Feedback if FALSE (Correct):**
Correct. Projects are powerful but should be used strategically. Create a Project when:
- You'll have 5+ conversations on the same topic
- You need consistent context across sessions
- You have reference documents to upload
- The work requires specialized behavior

For one-off questions, quick research, or exploratory conversations, a regular chat is more appropriate. Over-creating Projects leads to maintenance burden and scattered context.

**Feedback if TRUE (Incorrect):**
Projects require setup time and maintenance. Creating them for every task would be inefficient. Reserve Projects for ongoing work requiring persistent context. Use regular conversations for one-off questions, quick research, or experimental prompting. The rule of thumb: create a Project when you'll have 5+ conversations on the same topic.

---

### Question 3 (Multiple Choice)

**What is the key difference between Claude Skills and Claude Projects?**

A) Skills are free, Projects require a paid subscription
B) Projects provide persistent context, Skills provide portable methodology
C) Skills can access the internet, Projects cannot
D) Projects are for teams, Skills are for individuals

**Correct Answer:** B

**Feedback for B (Correct):**
Perfect distinction.
- **Projects** = Persistent context for ongoing work in one domain (the "where" of your work)
- **Skills** = Portable methodology for repeatable tasks across contexts (the "how" of your work)

Best practice is to combine them: use Skills inside Projects for maximum efficiency. Projects remember everything about a domain; Skills standardize how you work regardless of domain.

**Feedback for other answers:**
Both Skills and Projects are available at the same subscription tier. Neither has internet access (that's Gemini's strength). Both are primarily individual tools, though methodologies can be shared. The key difference is context persistence (Projects) vs. methodology portability (Skills).

---

### Question 4 (Scenario-Based)

**Scenario:** You're a Customer Success Manager who needs to prepare QBR presentations for your top 10 accounts. Each account has unique history, contracts, and stakeholder preferences. You also need to create consistent executive summaries using the same format every time.

**What combination of tools would be most effective?**

A) One large Project containing all 10 accounts
B) 10 separate Projects (one per account) plus one Skill for executive summary formatting
C) One Gemini Gem for research and one Custom GPT for summaries
D) 10 separate Skills, one for each account

**Correct Answer:** B

**Feedback for B (Correct):**
Excellent reasoning. This approach leverages each tool's strengths:

**10 Projects (Client Hubs):** Each account gets dedicated context—their specific history, contracts, stakeholder preferences, and conversation history. This is the "Client Hub" architecture pattern.

**1 Skill (Executive Summary):** The same formatting methodology applies across all accounts. Instead of recreating the format each time, invoke your Skill within whichever Project you're working in.

This combination gives you account-specific depth with methodology consistency.

**Feedback for other answers:**
- **Option A**: One mega-Project would create context confusion—Claude might mix up account details. Separate Projects maintain clean boundaries.
- **Option C**: Gems excel at research but aren't ideal for account-specific context. Custom GPTs could work but don't offer the same document integration as Projects.
- **Option D**: Skills don't store account context. They're for methodology, not persistent knowledge about specific accounts.

---

### Question 5 (Multiple Choice)

**When should you use a Gemini Gem instead of a Claude Project?**

A) When you need deep reasoning with complex analysis
B) When you need real-time web research and Google Workspace integration
C) When you want to share an assistant with teammates
D) When you have large documents to analyze

**Correct Answer:** B

**Feedback for B (Correct):**
Exactly. Gemini Gems excel at:
- **Real-time web research** with current data (grounding)
- **Native Google Workspace integration** (Docs, Sheets, Slides)
- **Collaborative scenarios** with shared access
- **Current information tasks** where training data might be outdated

Claude Projects are better for deep reasoning and document analysis. Gems are your reconnaissance specialists—use them when you need current, grounded research with Google integration.

**Feedback for other answers:**
- **Option A**: Deep reasoning is Claude's strength, not Gemini's primary advantage.
- **Option C**: That's Custom GPTs' key differentiator (shareability).
- **Option D**: Claude handles large document analysis well with its 200k token context.

---

### Question 6 (True/False with Explanation)

**TRUE or FALSE: The "repetition tax" refers to the cost of having multiple AI subscriptions.**

**Correct Answer:** FALSE

**Feedback if FALSE (Correct):**
Correct. The "repetition tax" refers to the **time and effort** spent at the start of every AI conversation re-establishing context—explaining who you are, what you do, your preferences, and background information.

Persistence tools (Projects, Skills, Gems) eliminate this tax by maintaining context across sessions. You start at "expert level" instead of zero, saving the 2-3 exchanges typically needed for setup.

**Feedback if TRUE (Incorrect):**
The repetition tax isn't about subscription costs. It's about the time wasted rebuilding context every conversation—re-explaining your role, preferences, terminology, and background. This is what persistence tools solve: Custom Instructions remember who you are, Knowledge Files contain your references, and Conversation History maintains ongoing context.

---

### Question 7 (Scenario-Based)

**Scenario:** You've built a Project, two Skills, and a Gem for your competitive intelligence workflow. It's been three months since you set them up.

**What maintenance activities should you have completed by now (select the most comprehensive answer)?**

A) Nothing—once built, AI infrastructure is self-maintaining
B) Weekly: reviewed conversations for patterns; Monthly: refreshed knowledge files and audited instructions; Quarterly: evaluated expansion and shared patterns with team
C) Deleted everything and started fresh—AI improves so fast that old infrastructure is obsolete
D) Only update when something breaks

**Correct Answer:** B

**Feedback for B (Correct):**
Perfect. AI infrastructure requires regular maintenance:

**Weekly (15 min):**
- Review Project conversations for patterns
- Update Skills that aren't producing desired outputs
- Check Gem accuracy

**Monthly (30 min):**
- Refresh knowledge files with current documents
- Audit Custom Instructions for relevance
- Archive inactive Projects

**Quarterly (1 hour):**
- Evaluate which Projects deserve expansion
- Consider new Skills for emerging workflows
- Share successful patterns with teammates

This keeps your infrastructure current and effective.

**Feedback for other answers:**
- **Option A**: "Set and forget" leads to stale outputs. Knowledge files become outdated, instructions drift from your evolving needs.
- **Option C**: Well-designed infrastructure improves with refinement, not replacement. Starting fresh loses institutional context.
- **Option D**: Reactive maintenance means degraded performance until problems become obvious. Proactive maintenance keeps quality high.

---

## Quiz Complete

**Score Interpretation:**

- **6-7 correct**: Squadron Architect level achieved. You understand how to build and maintain persistent AI infrastructure.
- **4-5 correct**: Solid foundation. Review the sections on tool selection (Projects vs. Skills vs. Gems) and maintenance practices.
- **0-3 correct**: Revisit the lesson focusing on the four persistence tools and when to use each. The decision matrix is key.

**Key Concepts to Master:**
1. Projects provide persistent context (documents + instructions + history)
2. Skills provide portable methodology (reusable prompt templates)
3. Gems excel at grounded research with Google integration
4. Custom GPTs enable distribution to teams
5. Maintenance is ongoing, not one-time

---

**Proceed to Study Guide to consolidate your learning.**
