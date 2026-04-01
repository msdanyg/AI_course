# Module 4: Personal Projects & Folders
## Quiz (5-7 questions)

---

**Instructions:** Answer all questions below. Each question includes feedback explaining the correct answer.

**Passing Score:** 70% (5 out of 7 questions correct)

---

### Question 1 (Multiple Choice)

**What is the "Context Rebuild Tax" and how does it affect your productivity?**

A) The cost of upgrading from Claude Free to Claude Pro
B) The time wasted re-explaining your role, company, and preferences at the start of every new chat
C) The computational resources Claude uses to rebuild its neural network
D) The memory overhead from storing too many files in a Project

<details>
<summary><b>Answer & Feedback</b></summary>

**Correct Answer: B**

**Explanation:** The Context Rebuild Tax refers to the 5-10 minutes you spend at the beginning of every standard chat re-establishing basic context the AI has already heard dozens of times. This includes your role, company, preferences, terminology rules, and output formatting. Over time, this adds up to hours per month of wasted effort. Claude Projects and ChatGPT Projects eliminate this tax by maintaining persistent context across all chats within a Project.

**Why other answers are wrong:**
- **A:** Projects are available on all Claude tiers, including Free. There's no upgrade required.
- **C:** This is not a technical term related to AI architecture.
- **D:** While file storage does consume resources, the Context Rebuild Tax specifically refers to human time wasted, not computational resources.

</details>

---

### Question 2 (Multiple Choice)

**Your team needs to analyze quarterly customer contracts containing PII (personally identifiable information) every month. Which platform and approach should you use?**

A) Standard ChatGPT chats with files uploaded inline each time
B) Claude Projects with hard-wall isolation
C) ChatGPT Projects with cross-conversation memory enabled
D) Standard Claude chats, deleting the conversation after each analysis

<details>
<summary><b>Answer & Feedback</b></summary>

**Correct Answer: B**

**Explanation:** Claude Projects with hard-wall isolation are ideal for recurring work involving sensitive PII. The 100% isolation between Projects ensures that customer data in one Project never leaks into another Project or standard chats. The 200-file capacity handles document-heavy analysis well, and custom instructions ensure consistent output formatting every month. This is a recurring monthly task with sensitive data—both criteria point to Claude Projects.

**Why other answers are wrong:**
- **A:** Standard chats require re-uploading files and re-explaining context every time, creating the Context Rebuild Tax. No isolation guarantees for PII.
- **C:** ChatGPT's cross-conversation memory means insights could bleed across chats, which is risky for PII. Soft boundaries are not ideal for sensitive data.
- **D:** Deleting conversations doesn't eliminate the Context Rebuild Tax, and standard chats lack persistent custom instructions.

</details>

---

### Question 3 (True/False with Explanation)

**True or False: You should create a Claude Project or ChatGPT Project for every task you perform, even one-time questions, to maximize AI effectiveness.**

<details>
<summary><b>Answer & Feedback</b></summary>

**Correct Answer: False**

**Explanation:** Projects have setup overhead—uploading files, writing custom instructions, and testing. They're designed for **recurring work** (weekly/monthly tasks), document-heavy analysis, or scenarios where you'd spend 5+ minutes re-briefing the AI. For one-time questions, quick research, or low-stakes tasks, standard chat is faster and more appropriate. The 80/20 rule applies: only create Projects for the 20% of work that will benefit from 80% of the value. If you won't revisit the task in 30 days, skip the Project.

**The test:** "Would I spend 5+ minutes re-briefing the AI on this context?" If no, use standard chat.

</details>

---

### Question 4 (Multiple Choice)

**What is the primary difference between Claude Projects (hard walls) and ChatGPT Projects (soft boundaries)?**

A) Claude Projects support more file types than ChatGPT Projects
B) ChatGPT Projects cost more than Claude Projects
C) Claude Projects have complete isolation between Projects; ChatGPT Projects have cross-conversation memory that can bleed between chats
D) Claude Projects only work on desktop; ChatGPT Projects work on mobile

<details>
<summary><b>Answer & Feedback</b></summary>

**Correct Answer: C**

**Explanation:** The fundamental architectural difference is memory isolation. **Claude Projects have "hard walls"**—what happens in Project A stays in Project A with zero awareness of other Projects. **ChatGPT Projects have "soft boundaries"**—cross-conversation memory is enabled by default, meaning insights from one chat can inform another, even outside Projects. This makes Claude ideal for sensitive data and compartmentalized work, while ChatGPT excels at iterative creative work where you want the AI to learn your style over time.

**Squadron Metaphor:** Claude = classified military bases with restricted access. ChatGPT = open-plan offices with flexible dividers.

**Why other answers are wrong:**
- **A:** Both platforms support similar file types (PDFs, Word docs, spreadsheets, text).
- **B:** Pricing varies by tier, but cost isn't the primary architectural difference.
- **D:** Both platforms support mobile access for Projects (though functionality may vary).

</details>

---

### Question 5 (Scenario-Based)

**You're creating a Claude Project for ActivTrak competitive intelligence. You write 2,000 words of custom instructions covering every possible edge case, format preference, and stylistic choice. After testing, Claude's outputs are inconsistent and often ignore your instructions. What went wrong?**

A) Claude Projects have a strict 500-word limit for custom instructions
B) You over-instructed—Claude ignores instructions that drown in noise
C) You need to upgrade to Claude Pro for custom instructions to work
D) Claude can't process competitive intelligence due to ethical restrictions

<details>
<summary><b>Answer & Feedback</b></summary>

**Correct Answer: B**

**Explanation:** This is the classic **over-instruction mistake**. When custom instructions exceed 500-1,000 words and try to cover every edge case, the AI treats everything as low-priority noise and ignores most of it. The best practice is to **start with 200 words** focused on the most critical rules: role, context, output format, and never-do rules. Only add instructions when Claude **consistently** makes the same mistake. Prune ruthlessly—if Claude follows something naturally without being told, remove that instruction.

**Pro tip:** Think of custom instructions as "Standing Orders" for Mission Control, not a 50-page operations manual.

**Why other answers are wrong:**
- **A:** Claude Projects support approximately 2,000 characters (~400 words), but the issue isn't hitting a hard limit—it's cognitive overload.
- **C:** Custom instructions work on all Claude tiers, including Free.
- **D:** Claude has no restrictions on competitive intelligence analysis (as long as you're not violating copyright or IP laws).

</details>

---

### Question 6 (Multiple Choice)

**You've created a Claude Project with 5 uploaded files and custom instructions. You run your first test prompt, and Claude's response doesn't follow any of your instructions. What should you do FIRST?**

A) Delete the Project and start over from scratch
B) Upgrade to Claude Pro—custom instructions only work on paid tiers
C) Run 2-3 more test prompts to verify whether this is a one-time issue or a pattern
D) Add more detailed instructions to fix the problem

<details>
<summary><b>Answer & Feedback</b></summary>

**Correct Answer: C**

**Explanation:** Custom instructions are notoriously hard to get right on the first try. Before making changes, **run 2-3 more test prompts** to determine whether Claude consistently ignores certain instructions or if this was a one-time anomaly (perhaps your prompt conflicted with the instructions). After testing, refine only the rules that were consistently violated—don't add more instructions speculatively. This is part of the iterative refinement process described in the Lab Exercise.

**Testing protocol:**
1. Test Prompt 1: Role memory (does Claude remember your company/role?)
2. Test Prompt 2: Knowledge base usage (does Claude reference uploaded files?)
3. Test Prompt 3: Terminology compliance (does Claude follow formatting and language rules?)

**Why other answers are wrong:**
- **A:** Deleting and starting over wastes the setup time you've already invested. Refinement is faster than rebuilding.
- **B:** Custom instructions work on all Claude tiers, including Free.
- **D:** Adding more instructions before diagnosing the issue often makes the problem worse (over-instruction).

</details>

---

### Question 7 (True/False with Explanation)

**True or False: Once you set up a Claude Project with custom instructions, you should never modify those instructions—they're permanent and changing them will confuse the AI.**

<details>
<summary><b>Answer & Feedback</b></summary>

**Correct Answer: False**

**Explanation:** Claude Projects are **living systems** that require ongoing maintenance and iteration. You should expect to refine your custom instructions over the first 2-3 weeks of use based on what Claude consistently forgets or misinterprets. The lesson teaches this explicitly: "Start with 200 words. If Claude consistently forgets something, add it. If it follows something without being told, remove it. Prune ruthlessly." Additionally, you should conduct monthly audits to remove outdated files and update instructions as your work evolves.

**Best practices for iteration:**
- Add instructions only when Claude makes the same mistake 2-3 times
- Remove instructions for behaviors Claude does naturally
- Make vague rules more specific (e.g., "be professional" → "use warm but professional tone, avoid jargon")
- Archive files older than 90 days unless evergreen

**Squadron Metaphor:** Your Mission Headquarters evolves as you learn what works. Standing Orders are updated based on field experience.

</details>

---

### Question 8 (Multiple Choice)

**You've uploaded 80 files (~1.5 million tokens) to a Claude Project. Claude's responses reference your documents accurately. What technology is Claude using behind the scenes?**

A) Full Context Mode—Claude is reading all 80 files into its context window simultaneously
B) RAG (Retrieval-Augmented Generation)—Claude is searching and retrieving relevant chunks from indexed documents
C) Compressed Context Mode—Claude is summarizing files to fit them into the context window
D) Cached Memory—Claude is storing your files in long-term memory across sessions

<details>
<summary><b>Answer & Feedback</b></summary>

**Correct Answer: B**

**Explanation:** At 1.5 million tokens, Claude has automatically switched from Full Context Mode to **RAG (Retrieval-Augmented Generation) Mode**. This transition happens automatically when your knowledge base exceeds ~200K tokens. RAG works by:
1. Converting your documents into searchable "numerical fingerprints" (embeddings)
2. When you ask a question, searching semantically for the most relevant chunks
3. Retrieving those chunks and grounding responses in evidence from your files

This is why Claude Projects can handle 200 files instead of just 20—RAG enables 10x capacity expansion by searching documents intelligently rather than trying to keep everything in working memory.

**Squadron Metaphor:** Instead of memorizing every page in the Intelligence Archive, Mission Control can rapidly retrieve relevant intelligence reports on demand.

**Why other answers are wrong:**
- **A:** Full Context Mode only works for knowledge bases under 200K tokens. At 1.5 million tokens, this is impossible.
- **C:** Claude doesn't compress files into summaries—it indexes them for semantic search with RAG.
- **D:** Claude doesn't store files in long-term memory across sessions. Files exist only within the Project and are re-indexed each time.

</details>

---

### Question 9 (Scenario-Based)

**You're creating two ChatGPT Projects: (1) "Creative Writing Coach" for personal fiction projects, (2) "Client Legal Briefs" for sensitive attorney-client work. How should you configure memory settings for each?**

A) Both should use Cross-Conversation Memory to maximize ChatGPT's learning
B) Both should use Project-Only Memory to prevent data leakage
C) Creative Writing = Cross-Conversation Memory; Legal Briefs = Project-Only Memory
D) Creative Writing = Project-Only Memory; Legal Briefs = Cross-Conversation Memory

<details>
<summary><b>Answer & Feedback</b></summary>

**Correct Answer: C**

**Explanation:** This scenario requires **strategic memory configuration** based on sensitivity and learning goals:

**Creative Writing Coach (Cross-Conversation Memory ON):**
- You WANT ChatGPT to remember your writing style, recurring characters, and creative preferences across all your chats
- No sensitive data—it's your personal fiction work
- Benefits from ChatGPT learning your voice over time

**Client Legal Briefs (Project-Only Memory):**
- Attorney-client privilege requires strict compartmentalization
- Information from one client's case MUST NOT bleed into another client's case
- Shared Projects automatically enforce project-only memory to prevent team data leakage

**The decision rule:** Sensitive client/PII work = Project-only memory. Personal creative work where you want style learning = Cross-conversation memory.

**Why other answers are wrong:**
- **A:** Cross-conversation memory for legal work creates risk of confidential information leaking across cases. This violates attorney-client privilege.
- **B:** Project-only memory for creative writing prevents ChatGPT from learning your style over time, eliminating one of the platform's key advantages.
- **D:** This reverses the logic—you'd be isolating creative work while allowing legal briefs to cross-contaminate.

</details>

---

## Scoring Guide

- **9/9 correct (100%):** Squadron Leader Mastery—you understand Projects inside and out
- **8/9 correct (89%):** Strong understanding—minor refinements needed
- **7/9 correct (78%):** Passing—review missed questions and revisit lesson sections
- **6/9 or below (67% or less):** Review the lesson and retake the quiz

**Passing Score:** 70% (7 out of 9 questions correct)

---

## What to Do After the Quiz

- **If you passed (7+ correct):** Proceed to the Study Guide for a quick reference, then start building Projects for your real work
- **If you didn't pass:** Review the lesson sections corresponding to your missed questions, then retake the quiz
- **For deeper understanding:** Complete the stretch goals in the Lab Exercise

---

**Next Module Preview:** Module 5 introduces **Gemini (Recon & Radar)** and **Granola (Flight Recorder)**—giving your Squadron eyes, ears, and meeting intelligence.
