# Module 9 Study Guide
## Code Execution & File Creation

**One-Page Quick Reference**

---

## Core Concept

**Mission Output Commander**: Your Squadron now produces tangible deliverables—presentations, spreadsheets, data exports—using Claude's code execution capabilities.

**The Architecture**: Claude doesn't "generate" files directly. It writes Python code using specialized libraries, executes that code in a sandbox, and captures the output file for download.

---

## Squadron Mapping for Module 9

| Concept | Squadron Term | Tool/Platform |
|---------|--------------|---------------|
| File generation | Mission Artifacts | Claude Code Execution |
| Presentation creation | Mission Briefings | Claude (python-pptx) / Gemini Canvas |
| Data exports | Intelligence Reports | Claude (pandas/CSV) |
| Structural drafts | Scaffolding | Claude output before polish |
| Visual polish | Final Paint | PowerPoint/Google Slides |

---

## The Library Stack

| Library | Purpose | Output |
|---------|---------|--------|
| `python-pptx` | PowerPoint generation | .pptx |
| `openpyxl` | Excel with formatting | .xlsx |
| `pandas` | Data manipulation | .csv, .xlsx |
| `csv` | Simple CSV operations | .csv |

---

## Tool Decision Matrix

| Need | Use Claude | Use Gemini |
|------|------------|------------|
| Downloadable .pptx file | ✓ | |
| Precise structural control | ✓ | |
| Detailed speaker notes | ✓ | |
| Native Google Slides format | | ✓ |
| AI-selected imagery/themes | | ✓ |
| One-click Slides export | | ✓ |

**Decision Rule**: Claude creates .pptx via code; Gemini creates native Slides format.

---

## PowerPoint Prompt Template

```
Create a [X]-slide PowerPoint presentation about [TOPIC].

Slide 1: Title - "[TITLE]"
Slide 2: [CONTENT]
Slide 3: [CONTENT]
...
Final Slide: [SUMMARY/NEXT STEPS]

Use title-and-content layouts.
Include speaker notes for each slide.
[VIBE: Make it feel professional and data-driven.]
```

---

## The Structural Draft Workflow

| Step | Action | Tool |
|------|--------|------|
| 1 | Generate content structure | Claude |
| 2 | Download .pptx file | Claude |
| 3 | Apply corporate template | PowerPoint/Slides |
| 4 | Add visuals, polish design | PowerPoint/Slides |

*Claude handles content organization; design tools handle visual polish.*

---

## CSV vs. Excel Decision

| Use CSV When... | Use Excel When... |
|-----------------|-------------------|
| Data transfer between systems | Multiple sheets needed |
| Database import | Formatting required |
| Universal compatibility | Formulas included |
| Simple tabular data | Conditional formatting |

---

## Vibe Coding

**What it is**: Describing outcomes aesthetically rather than technically.

**Instead of:**
```
Use hex color #0056D2, font-size 24pt, border-collapse: collapse
```

**Try:**
```
Make it feel like a Fortune 500 investor presentation—clean,
professional, data-driven. The vibe should say "we know what
we're doing."
```

**Non-developer power**: Generate HTML tables, styled reports, formatted outputs without knowing code. Describe the aesthetic; Claude handles the technical translation. Screenshot or export for professional deliverables.

**Best Practice**: Combine vibe descriptions (style) with structural precision (content).

---

## Mission Output Framework

| Phase | Activity | Output |
|-------|----------|--------|
| Intel Gathering | Research, upload | Facts, raw data |
| Analysis | Claude reasoning | Insights, findings |
| Synthesis | Structuring | Organized narrative |
| **Delivery** | **File creation** | **Slides, spreadsheets** |

---

## Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| Vague prompts | Generic outputs | Specify slide-by-slide content |
| Design expectations | Basic styling | Use structural draft workflow |
| Unverified data | Errors in exports | Always spot-check outputs |
| Wrong tool | Unnecessary friction | Match tool to workflow |

---

## Quick Reference: File Requests

**PowerPoint:**
```
Create a downloadable PowerPoint with [X] slides...
Include speaker notes...
```

**CSV Export:**
```
Export this data as a CSV file with columns: [LIST]
Sort by [COLUMN] descending...
```

**Excel with Formatting:**
```
Create an Excel file with:
- Sheet 1: [CONTENT]
- Sheet 2: [CONTENT]
Format headers: bold, gray background...
```

---

## Bridge to Module 10

You now produce mission-ready deliverables. But you're still orchestrating manually.

**Module 10: Future Frontiers** introduces AI Agents and MCP (Model Context Protocol)—systems that execute multi-step workflows autonomously, access external tools, and operate with minimal intervention.

From file factory to autonomous operations.

---

## The Output Creed

> **"Intelligence without deliverables is just conversation. Your Squadron produces artifacts that move business forward."**

---

## Self-Assessment

Can you:
- [ ] Explain how Claude creates downloadable files (code execution)?
- [ ] Apply the structural draft workflow for presentations?
- [ ] Choose between Claude and Gemini for presentation creation?
- [ ] Use vibe coding combined with structural precision?
- [ ] Decide when to use CSV vs. Excel formats?

If yes to all: **Module 9 mastered. Proceed to Module 10.**
If no to any: **Review corresponding lesson section, re-attempt lab.**

---

**End of Module 9 Study Guide**
