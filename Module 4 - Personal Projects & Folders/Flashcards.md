# Module 4: Personal Projects & Folders
## Flashcards

---

### Card 1: Context Rebuild Tax

**FRONT:**
What is the "Context Rebuild Tax" and how much time does it cost?

**BACK:**
The time wasted re-explaining your role, company, preferences, and context to the AI at the start of every new chat. Typically costs 5-10 minutes per session, adding up to hours per month. Projects eliminate this by maintaining persistent context.

---

### Card 2: Claude Projects (Hard Walls)

**FRONT:**
What does "hard walls" mean for Claude Projects?

**BACK:**
Complete isolation between Projects. What happens in Project A stays in Project A—Claude has zero awareness of your other Projects. This prevents context pollution and is ideal for sensitive data, document-heavy analysis, or work that must stay compartmentalized.

**Squadron Metaphor:** Classified military bases with restricted access.

---

### Card 3: ChatGPT Projects (Soft Boundaries)

**FRONT:**
How do ChatGPT Projects differ from Claude Projects in terms of memory?

**BACK:**
ChatGPT Projects have "soft boundaries" with cross-conversation memory enabled by default. Insights from one chat can inform another, even outside Projects. Best for iterative creative work and scenarios where you want the AI to learn your style over time.

**Squadron Metaphor:** Open-plan offices with flexible dividers.

---

### Card 4: When to Use Which Platform

**FRONT:**
You need to analyze customer contracts containing PII monthly. Which platform should you use?

**BACK:**
**Claude Projects.** The hard walls guarantee complete isolation, making it ideal for sensitive PII work. The 200-file capacity handles document-heavy analysis well, and persistent custom instructions ensure consistent output every month.

---

### Card 5: Custom Instructions

**FRONT:**
What are Custom Instructions and how should you approach writing them?

**BACK:**
Custom Instructions are your "Standing Orders"—rules that apply to every chat in a Project. Start with 200 words focused on role, context, output format, and never-do rules. Add instructions only when the AI consistently makes the same mistake. Prune ruthlessly—over-instruction causes the AI to ignore everything.

**Squadron Metaphor:** Mission briefing that applies to every sortie from this base.

---

### Card 6: The 80/20 Rule for Projects

**FRONT:**
When should you create a Project vs. using standard chat?

**BACK:**
Create a Project for recurring work (weekly/monthly tasks), document-heavy analysis, or when you'd spend 5+ minutes re-briefing the AI. Use standard chat for one-time research, quick questions, or low-stakes tasks. Projects have setup overhead—only use them for work you'll revisit in 30 days.

---

### Card 7: The Junk Drawer Mistake

**FRONT:**
What's the "Junk Drawer" mistake and how do you avoid it?

**BACK:**
Creating one giant Project with 200 random files dumped in. The AI can't distinguish signal from noise, wasting context on irrelevant documents. **Fix:** Create focused Projects with 5-15 files max. Separate "Competitive Intel" from "Customer Success" from "Product Docs." Each Project should serve one clear purpose.

---

### Card 8: Testing Your Project

**FRONT:**
Why must you test a new Project immediately after setup?

**BACK:**
Custom instructions are notoriously hard to get right on the first try. Run 3 test prompts to verify the AI remembers your role, follows output formatting, applies terminology rules, and avoids forbidden patterns. If any requirement fails, refine instructions and test again before using the Project for real work.

---

### Card 9: RAG (Retrieval-Augmented Generation)

**FRONT:**
What is RAG and how does it relate to Claude Projects?

**BACK:**
RAG gives Claude Projects a "research assistant" that searches your files semantically instead of keeping everything in working memory. When your knowledge base exceeds 200K tokens, Claude automatically switches from Full Context Mode (reading all files) to RAG Mode (searching and retrieving relevant chunks). This enables 10x capacity expansion—up to 200 files instead of 20.

**Squadron Metaphor:** Intelligence Archive with rapid retrieval system.

---

### Card 10: Full Context vs RAG Mode

**FRONT:**
When does Claude Projects switch between Full Context Mode and RAG Mode?

**BACK:**
Claude automatically switches at 200K tokens (~150 pages). Below that threshold, it reads all files into memory. Above it, RAG activates—Claude indexes documents and retrieves relevant chunks on demand. The transition is invisible and enables 10x capacity expansion.

---

### Card 11: ChatGPT Memory Settings

**FRONT:**
What's the difference between Cross-Conversation Memory and Project-Only Memory in ChatGPT?

**BACK:**
**Cross-Conversation:** ChatGPT remembers across all chats. Use for personal creative work.

**Project-Only:** Information stays siloed within that Project. Use for sensitive client work.

Shared Projects automatically enforce project-only memory to prevent team data leakage.

---

**Total Cards:** 11
**Focus Areas:** Context Rebuild Tax (1), Platform differences (2-3), Decision-making (4, 6), Best practices (5, 7-8), Advanced concepts (9-11)
