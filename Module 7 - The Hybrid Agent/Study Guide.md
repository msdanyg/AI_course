# Module 7 Study Guide
## The Hybrid Agent (Mac, Mobile & Docs)

**One-Page Quick Reference**

---

## Core Concept

**The Hybrid Agent Model**: Your Squadron operates seamlessly across mobile, Mac, and Google Workspace—capturing intelligence anywhere, processing with power tools, delivering in collaborative formats.

**The Problem It Solves**: Fragmented tools cause friction. Great ideas happen away from your desk but are lost by the time you sit down. The Hybrid Agent eliminates this friction.

---

## Squadron Mapping for Module 7

| Concept | Squadron Term | Tool/Platform |
|---------|--------------|---------------|
| Mobile capture | Forward Observer | Claude mobile, Voice Memos, Apple Notes |
| Desktop processing | Command Center | Claude Desktop (Mac app) |
| Research with current data | Recon & Radar | Gemini |
| Collaborative delivery | Mission Reports | Google Docs/Slides via HTML Bridge |
| Context persistence | Flight Log | Synced conversations across devices |

---

## The Four Core Workflows

### 1. Ramble-to-Gold

**Purpose:** Capture raw thinking when clarity strikes, refine later.

**Steps:**
1. **Capture** (mobile voice): Record thoughts conversationally
2. **Sync** (automatic): iCloud or account sync to desktop
3. **Process** (Claude Desktop): Use structured prompt to transform ramble
4. **Refine** (iterative): Polish Claude's draft

**When to use:** Commute, walking, any time you have mental clarity but can't type formally.

---

### 2. The HTML Bridge

**Purpose:** Paste formatted tables/content into Google Docs without breaking.

**Steps:**
1. Ask Claude for **HTML output** (not Markdown)
2. Include CSS requirements:
   - `border-collapse: collapse`
   - `border: 1px solid #333`
   - Header: `background #f0f0f0`
3. Render directly (not in code block)
4. Copy **rendered visual**, paste into Docs

**When to use:** Anytime you need tables or formatted content in Google Docs.

---

### 3. Mac Power User

**Advantages of Claude Desktop:**
- **Drag-and-drop**: PDFs, screenshots, folders directly from Finder
- **Keyboard shortcuts**: Cmd+N (new chat), Cmd+Shift+P (new Project)
- **Native notifications**: Alerts when analysis completes

**Apple Notes as Staging:**
- Create "AI Squadron" notebook
- Folders: Voice Captures, Research Briefs, Meeting Intel
- Syncs via iCloud (zero friction)

**When to use:** Mac is your primary work environment; leverage native integration.

---

### 4. Mobile Command Center

**Claude Mobile Capabilities:**
- Voice conversation mode
- Image analysis (photos of whiteboards, screenshots)
- Quick research on-the-go
- Project access (full knowledge base)

**Synced context:** Start on mobile, continue on desktop, reference back on mobile—all same conversation.

**When to use:** Transit, between meetings, quick queries, anywhere away from desk.

---

## Platform Decision Matrix

| Task | Primary Tool | Why |
|------|-------------|-----|
| Voice capture | Claude mobile / Voice Memos | Transcription, sync |
| Deep analysis | Claude Desktop | Reasoning, Projects, code execution |
| Current research | Gemini | Grounding, real-time data |
| Formatted deliverables | HTML Bridge → Docs | Preserves formatting |
| Presentations | Gemini → Slides export | Native integration |
| Collaboration | Google Docs + Gemini | Team workflow |

**Decision Principle:** Choose the tool that eliminates friction for that specific task.

---

## Do's and Don'ts

### ✅ DO:

- **Capture immediately**: Voice note when thinking is clear, refine later
- **Use drag-and-drop**: Leverage Mac's zero-friction file handling
- **Ask for HTML**: When you need formatted content in Docs
- **Leverage sync**: Start on mobile, finish on desktop seamlessly
- **Pick the right tool**: Claude for reasoning, Gemini for research/Workspace

### ❌ DON'T:

- **Wait for your desk**: Capture ideas when they happen, not when convenient
- **Copy Markdown to Docs**: It will break—use HTML Bridge instead
- **Use mobile for deep work**: Mobile is for capture, desktop for synthesis
- **Ignore native integration**: Gemini in Docs/Slides is faster than external tools
- **Forget context persists**: Your mobile and desktop conversations sync

---

## Quick Reference: Critical Prompts

### Ramble-to-Gold Processing:
```xml
<role>Chief of Staff transforming voice notes to polished work.</role>
<raw_capture>[paste ramble]</raw_capture>
<task>Extract insights, structure logically, draft polished version.</task>
```

### HTML Table for Docs:
```
Create [topic] table as HTML with inline CSS:
- border-collapse: collapse
- border: 1px solid #333
- Header: background #f0f0f0
Render directly (not in code block).
```

### Mobile Meeting Prep:
```
I'm meeting with [Client] in [time]. Pull from [Project].
What are key points from recent interactions?
What should I prioritize?
```

---

## Common Pitfalls

1. **Trying to type formally on mobile** → Use voice, refine later
2. **Pasting Markdown tables to Docs** → Use HTML Bridge
3. **Starting over on each device** → Use synced conversations
4. **Using Claude for current data** → Use Gemini, then transfer to Claude
5. **Manual file transfers** → Use native sync (iCloud, account sync)

---

## ActivTrak Applications

**Customer Success:**
- Voice capture client concerns during site visit
- Process on Mac: meeting brief + follow-up email
- Deliver via Docs for team visibility

**Sales:**
- Mobile competitor research during commute
- Desktop analysis: competitive brief
- HTML Bridge: formatted battle card to Docs

**Product Marketing:**
- Voice brainstorm feature positioning
- Gemini research: market trends
- Claude synthesis: strategic narrative
- Docs collaboration: team refinement

---

## Bridge to Module 8

You now command a hybrid, anywhere-capable Squadron:
- **Capture** intelligence in any form (voice, screenshot, document)
- **Process** with full desktop power (Claude Projects, code execution)
- **Deliver** in collaborative formats (Google Workspace)

**Next level:** In Module 8, you'll systematize these workflows—creating reusable Projects that encapsulate knowledge, Skills that standardize processes, and Gems that act as specialized team members. You'll move from Squadron Leader to Squadron Architect.

---

## The Mantra

> **"Great thinking doesn't wait for your desk—capture it where it happens, refine it where you have power."**

---

## Self-Assessment

Can you:
- [ ] Explain the four phases of Ramble-to-Gold?
- [ ] Describe how the HTML Bridge works and why?
- [ ] List three Mac-specific advantages of Claude Desktop?
- [ ] Decide when to use Claude vs. Gemini vs. Google Docs?
- [ ] Explain why context persistence matters?

If yes to all: **Module 7 mastered. Proceed to Module 8.**
If no to any: **Review corresponding lesson section, re-attempt lab.**

---

**End of Module 7 Study Guide**
