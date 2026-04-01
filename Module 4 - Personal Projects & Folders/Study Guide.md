# Module 4: Personal Projects & Folders
## Study Guide (One-Page Quick Reference)

---

## The Problem: Context Rebuild Tax

**What it is:** The 5-10 minutes wasted at the start of every chat re-explaining your role, company, preferences, and context
**Cost:** Hours per month of repeated explanations
**Solution:** Claude Projects and ChatGPT Projects/Folders maintain persistent context

---

## Platform Comparison

| Feature | Claude Projects | ChatGPT Projects | When to Use |
|---------|----------------|------------------|-------------|
| **Memory Model** | Hard Walls (100% isolated) | Soft Boundaries (cross-conversation memory) | Claude: Sensitive data<br>ChatGPT: Learning your style |
| **File Capacity** | 200 files (~10MB each) | 25-40 files (tier-dependent) | Claude: Doc-heavy work |
| **Custom Instructions** | Up to ~2,000 chars | Up to ~1,500 chars | Both support robust instructions |
| **Best For** | PII work, competitive intel, compartmentalized tasks | Creative work, team Projects, iterative drafts |

**Squadron Metaphor:**
- **Claude Projects** = Classified military bases with restricted access
- **ChatGPT Projects** = Open-plan offices with flexible dividers

---

## Decision Tree: When to Create a Project

1. **Do you need persistent files or custom instructions?**
   → No: Use standard chat
   → Yes: Continue

2. **Is this work recurring (weekly/monthly)?**
   → One-time: Standard chat is fine
   → Recurring: Create a Project

3. **Does it involve sensitive PII or must stay isolated?**
   → Yes: Use **Claude Projects**
   → No: Continue

4. **Do you want AI to learn your style across all chats?**
   → Yes: Use **ChatGPT Projects** with memory enabled
   → No: Use **Claude Projects** for focused work

**The 5-Minute Test:** "Would I spend 5+ minutes re-briefing the AI on this context?" If no, skip the Project.

---

## Building a Claude Project (Quick Steps)

1. **Create:** Click "Projects" → "New Project" → Name it (e.g., "Competitive Intel HQ")
2. **Upload:** Add 3-5 core documents (feature matrices, positioning guides, past briefs)
3. **Instruct:** Write 200-word custom instructions covering:
   - **Role:** Your job title at ActivTrak
   - **Context:** Company, competitors, privacy philosophy
   - **Output Rules:** Format, tone, length preferences
   - **Never Do:** Forbidden language, surveillance positioning
4. **Test:** Run 3 test prompts (role memory, file usage, terminology compliance)
5. **Refine:** Adjust instructions based on what Claude forgets or misinterprets

---

## Custom Instructions Template (200 words)

```
ROLE: You are [Your Job Title] at ActivTrak, a workforce analytics company.

CONTEXT: ActivTrak competes with [Competitors] in [Market Segment]. Our philosophy: "Insights, Not Oversight."

YOUR MISSION:
- [Primary task, e.g., Analyze competitor moves]
- [Secondary task, e.g., Identify gaps to exploit]
- [Positioning focus, e.g., Highlight our privacy-first approach]

OUTPUT RULES:
- Start with [Format, e.g., 3-bullet exec summary]
- Use [Structure, e.g., tables for comparisons]
- Tone: [Professional/warm/analytical]
- Length: [500-750 words unless specified]
- Terminology: [Use "users" not "customers"]

NEVER:
- [Forbidden language, e.g., surveillance terminology]
- [Forbidden actions, e.g., recommend features we lack]
```

**Pro Tip:** Start with 200 words. Add only when Claude consistently forgets. Prune ruthlessly.

---

## Common Mistakes to Avoid

| Mistake | Fix |
|---------|-----|
| **The Junk Drawer** (200 files in one Project) | Create focused Projects with 5-15 files max |
| **Over-Instructing** (2,000-word instructions) | Start with 200 words; add sparingly |
| **Never Pruning** (outdated files accumulate) | Monthly audit; archive files >90 days old |
| **Forgetting to Test** (assume instructions work) | Run 3 test prompts immediately after setup |
| **One-Time Projects** (vacation planning) | Projects are for recurring work only |

---

## Organizing ChatGPT with Folders

**Recommended Structure:**
```
📁 Work - ActivTrak
   📁 Competitive Intel
   📁 Customer Success
   📁 Content Drafting
📁 Personal
   📁 Learning & Research
📁 Archive (completed projects)
```

**How to:** Click "+" → "New Folder" → Drag chats into folders
**Pro Tip:** Keep structure shallow (2 levels max) for easy navigation

---

## Understanding RAG in Claude Projects

**What It Is:** Retrieval-Augmented Generation—Claude's "research assistant" that searches your files semantically

**When It Activates:**
| Mode | Threshold | How It Works |
|------|----------|--------------|
| **Full Context** | <200K tokens (~150 pages) | Claude reads ALL files into memory |
| **RAG Mode** | >200K tokens | Claude searches indexed documents for relevant chunks |

**Why It Matters:** Enables 10x capacity expansion (200 files instead of 20)

**Squadron Metaphor:** Intelligence Archive with rapid retrieval—Mission Control doesn't memorize every report, just knows how to find relevant intel on demand

**Optimization Tips:**
1. Use Markdown format when possible
2. Structure documents with clear headers (RAG retrieves by section)
3. Remove redundant/outdated content
4. Keep file names descriptive
5. Don't over-upload—quality > quantity

---

## ChatGPT Memory Settings

**Two Memory Modes:**

| Setting | Behavior | Best For |
|---------|----------|----------|
| **Cross-Conversation Memory** | ChatGPT remembers facts/preferences across ALL chats | Personal creative work, learning your style |
| **Project-Only Memory** | Information stays siloed within that Project | Sensitive client work, PII handling |

**Important:** Shared Projects (Business/Enterprise) automatically use project-only memory to prevent team data leakage

**Decision Rule:**
- Sensitive data/clients → Project-only memory
- Personal creative work → Cross-conversation memory

---

## Key Terminology

- **Context Rebuild Tax:** Time wasted re-explaining context every chat (5-10 min per session)
- **Hard Walls (Claude):** 100% isolation between Projects—what happens in Project A stays in Project A
- **Soft Boundaries (ChatGPT):** Cross-conversation memory bleeds between chats (unless project-only mode)
- **Custom Instructions:** Persistent "Standing Orders" for every chat in a Project (start with 200 words)
- **RAG (Retrieval-Augmented Generation):** Technology that lets Claude search large file sets semantically; auto-activates at 200K tokens
- **Full Context Mode:** Claude reads all files into memory (<200K tokens)
- **Vectorization/Embeddings:** Converting documents into "numerical fingerprints" for semantic search
- **Cross-Conversation Memory:** ChatGPT remembers facts across all chats (global)
- **Project-Only Memory:** Information stays siloed within one Project (for sensitive data)
- **Squadron Metaphor:** Projects = Mission Headquarters with pre-briefed AI; RAG = Intelligence Archive

---

## Quick Troubleshooting

**Claude forgets your instructions?**
→ Make rules more explicit and specific in Custom Instructions

**Claude ignores uploaded files?**
→ Explicitly say "Based on the documents in this Project..." in your prompt

**Output format is wrong?**
→ Be more specific in OUTPUT RULES (e.g., "Use markdown tables with columns: Feature | ActivTrak | Competitor")

**Instructions too long?**
→ Remove anything Claude does naturally without being told

---

## Next Steps

1. Build your first Claude Project for a recurring ActivTrak task
2. Organize your ChatGPT sidebar with 3-5 folders
3. Use Projects in real work this week—iterate on instructions as you learn
4. Conduct monthly audits: prune files, refine instructions, archive old chats

**Remember:** Projects are living systems. Expect to refine over 2-3 weeks. That's normal.

---

## Module 5 Preview

**The Sensory System: Gemini & Granola**
Your Squadron needs eyes, ears, and a flight recorder. Next module integrates:
- **Gemini** for real-time web research (Recon & Radar)
- **Granola** for meeting intelligence (Flight Recorder)

Your AI will no longer start from zero. It starts from a fully briefed **Mission Headquarters**.

---

*Print this page and keep it at your desk for quick reference.*
