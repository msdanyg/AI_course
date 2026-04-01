# Module 7 Flashcards
## The Hybrid Agent (Mac, Mobile & Docs)

---

### Card 1: The Ramble-to-Gold Workflow

**FRONT:**

What are the four phases of the Ramble-to-Gold workflow?

**BACK:**

1. **Capture**: Record voice notes on mobile (Claude app or Voice Memos)
2. **Sync**: Automatic iCloud sync to Mac (Apple Notes/Claude account)
3. **Process**: Feed raw transcript to Claude Desktop with structured prompt
4. **Refine**: Iterate on Claude's draft to polish final deliverable

This workflow eliminates the "blank page problem" by letting you capture thinking when clarity strikes, then refining it later with AI assistance.

---

### Card 2: Mac Drag-and-Drop Advantage

**FRONT:**

What files can you drag-and-drop directly into Claude Desktop, and why does this matter?

**BACK:**

You can drag:
- PDFs from Finder
- Screenshots immediately after capture
- CSV files for analysis
- Entire folders (uploads multiple files)
- Images from Photos app

**Why it matters**: Eliminates upload friction. No browse dialog, no "select file" button. The instant you capture something (like a screenshot), you can drag it directly into analysis. Saves 10-20 seconds per file, which compounds to hours over time.

---

### Card 3: The HTML Bridge

**FRONT:**

How do you paste a formatted table from Claude into Google Docs without it breaking?

**BACK:**

1. Ask Claude to create an **HTML table** (not Markdown)
2. Include specific CSS requirements:
   - `border-collapse: collapse`
   - `border: 1px solid #333`
   - Header row: `background #f0f0f0`
3. Instruct Claude to "render directly" (not in code block)
4. Copy the **rendered visual table** (not the HTML code)
5. Paste into Google Docs

**Why**: Google Docs doesn't understand Markdown, but it does understand HTML. Copying the rendered output preserves the HTML/CSS structure, which Docs translates into formatted tables.

---

### Card 4: Mobile vs. Desktop Claude

**FRONT:**

When should you use Claude mobile vs. Claude Desktop?

**BACK:**

**Use Claude Mobile when:**
- Voice capture/brainstorming
- Quick questions or research
- On-the-go document review
- Meeting prep during commute
- Immediate email responses

**Use Claude Desktop when:**
- Deep analysis requiring reasoning
- Uploading multiple files
- Accessing Projects (knowledge bases)
- Code execution/data analysis
- Building structured deliverables

**Key insight**: Mobile is for capture and quick queries. Desktop is for synthesis and power work. Context syncs between them via your account.

---

### Card 5: Apple Notes as Staging Area

**FRONT:**

How should you structure Apple Notes to support your Squadron workflows?

**BACK:**

Create a dedicated "AI Squadron" notebook with folders:

```
📁 AI Squadron
  └─ Active Missions (pinned)
  └─ Voice Captures
  └─ Research Briefs (from Gemini)
  └─ Meeting Intelligence (from Granola)
  └─ Templates
```

**Why Apple Notes?**
- Zero friction (native, always available)
- Instant iCloud sync across devices
- Rich text support (tables, images, formatting)
- Quick Note feature for instant capture
- Integrates with voice memos for transcription

---

### Card 6: Gemini's Native Workspace Advantage

**FRONT:**

What can Gemini do in Google Workspace that Claude cannot?

**BACK:**

In Google Docs:
- Read document automatically (no pasting)
- Insert content at cursor position
- Native side panel integration

In Google Slides:
- Generate presentation from text prompt
- Export directly to Slides with one click
- No download/upload/format cycle

In Google Sheets:
- Enrich data rows with research (e.g., add industry for company names)
- Native formula assistance

**Strategic use**: Use Gemini for native Google app workflows and quick collaborative edits. Use Claude for deep reasoning and analysis, then transfer to Google apps.

---

### Card 7: Cross-Platform Context Persistence

**FRONT:**

What is "cross-platform context persistence" and why does it matter?

**BACK:**

Cross-platform context persistence means your AI conversations sync across devices automatically.

**Example workflow**:
- **Morning (iPhone)**: Start conversation: "I need to prepare a QBR deck for Acme Corp."
- **Midday (Mac)**: Continue same conversation: "Here's their usage data [upload CSV]. Analyze and create talking points."
- **Afternoon (iPhone)**: Finalize in same conversation: "Convert to a one-page brief."

**Why it matters**: You don't restart the conversation on each device. The AI maintains full context across mobile capture, desktop processing, and mobile reference. Eliminates repetition and context loss.

---

### Card 8: The Platform Decision Matrix

**FRONT:**

Give the optimal tool for each task:
1. Voice capture
2. Deep analysis
3. Current research
4. Presentation creation
5. Document collaboration

**BACK:**

1. **Voice capture**: Claude mobile or Apple Voice Memos (transcription + sync)
2. **Deep analysis**: Claude Desktop (reasoning, Projects, large context)
3. **Current research**: Gemini (grounding, real-time data)
4. **Presentation creation**: Gemini → Export to Slides (native integration)
5. **Document collaboration**: Google Docs + Gemini (team workflow, version control)

**Principle**: Choose the tool that eliminates friction for that specific cognitive task.

---
