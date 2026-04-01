# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Obsidian vault for ActivTrak's GenAI training course ("Solo Pilot to Squadron Leader"). Transforms employees into "AI Architects" who orchestrate Claude, Gemini and Granola. The course has 14 modules (0-13) delivered via SCORM 1.2 packages to Articulate Reach 360.

## Common Commands

```bash
# Build individual SCORM packages for all modules
./SCORM_Packages/create_packages.sh

# Build combined multi-SCO course package
./SCORM_Packages/create_combined_package.sh

# Apply ActivTrak branding to all index.html files (source + SCORM copies)
python update_branding.py

# Convert video from .mov to .mp4 (required for SCORM - browsers don't support .mov)
/opt/homebrew/bin/ffmpeg -i "Module X - Title/video.mov" -c:v libx264 -c:a aac "Module X - Title/video.mp4"

# Verify SCORM integration across all modules
for i in {0..13}; do
    grep -q "setSCORMScore" "SCORM_Packages/full_course/module_$i/index.html" && echo "Module $i: OK" || echo "Module $i: MISSING"
done

# Validate SCORM manifest XML (catches unescaped & characters)
xmllint --noout SCORM_Packages/temp_module_X/imsmanifest.xml
```

## Content Pipeline

Source content flows through this pipeline:

```
Module X - Title/           ← Source folder (7+ markdown deliverables + index.html)
    ↓ update_branding.py    ← Applies ActivTrak CSS variables and color replacements
    ↓ create_packages.sh    ← Copies index.html, injects SCORM script, adds manifest + video
SCORM_Packages/output/      ← Final .zip files for Reach 360 upload
```

**Source of truth** is always the `Module X - Title/index.html` file. SCORM copies are derived artifacts. After editing a module's HTML, re-run the packaging pipeline.

## Building Modules

**Command:** `/design-module [module number or topic]` (custom skill - invoke via Skill tool)

**Each module folder contains 7+ deliverables:**
- Lesson.md (2,500-4,000 words)
- Video Script.md (1,500-2,000 words, ~10 min)
- Video Script - ElevenLabs.md (TTS-optimized narration)
- Flashcards.md (5-8 cards)
- Lab Exercise.md (20-30 min)
- Quiz.md (5-7 questions with feedback)
- Study Guide.md (one-page summary)
- index.html (self-contained interactive UI with 7 sections)

**Before building a module:**
1. Read `Data Repo/00 - Source Material Index.md` to find relevant source files
2. Read `Course Development Guide.md` for content standards
3. Check adjacent modules for prerequisites and what to set up

## Module index.html Architecture

Each `index.html` is a self-contained single-page app with SCORM integration.

**7-Section Navigation:** Welcome | Video | Lessons | Flashcards | Lab | Quiz | Study Guide

**Quiz-to-SCORM Integration Pattern:**
```javascript
function showResults() {
    const scorePercent = Math.round((correct / total) * 100);
    if (typeof setSCORMScore === 'function') {
        setSCORMScore(scorePercent);
        setSCORMStatus(scorePercent >= 70 ? 'passed' : 'failed');
    }
}
```

- Pass threshold: 70% (hardcoded in status logic)
- SCORM functions are defined in `scorm_api.js` (included via `<script src="scorm_api.js">`)
- Functions gracefully no-op when not in LMS context (local testing works fine)

## SCORM Packaging

**Build command:** `/build-scorm` (custom skill - invoke via Skill tool)

**Package types:**
- `SCORM_Packages/output/` - Final zip files (individual per module + master bundle)
- `SCORM_Packages/full_course/` - Multi-SCO combined course (module_0/ through module_13/)
- `SCORM_Packages/individual_modules/` - Single-SCO packages per module

**Each SCORM package contains:** `index.html` + `scorm_api.js` + `imsmanifest.xml` + optional `.mp4` video

**`create_packages.sh` automatically:**
- Finds each module folder and its index.html
- Injects `<script src="scorm_api.js">` after `<head>`
- Detects and copies .mp4 video files
- Generates imsmanifest.xml with correct module title
- Creates zip in output directory

### CRITICAL: XML Escaping in Manifests

**Ampersands MUST be escaped:** `&` to `&amp;` - common in titles like "Projects & Folders"

Unescaped `&` causes: `parser error: xmlParseEntityRef: no name`

**Always validate:** `xmllint --noout imsmanifest.xml` before packaging

### Manual Single-Module Build

```bash
SCORM_DIR="SCORM_Packages/temp_module_X"
rm -rf "$SCORM_DIR" && mkdir -p "$SCORM_DIR"
cp "SCORM_Packages/scorm_api.js" "$SCORM_DIR/"
cp "Module X - Title/index.html" "$SCORM_DIR/"
# Create imsmanifest.xml (see template in build-scorm skill)
cd "$SCORM_DIR" && zip -r "../output/Module_X_Title.zip" .
rm -rf "$SCORM_DIR"
```

### Verification Checklist

```bash
# 1. XML valid
xmllint --noout SCORM_Packages/temp_module_X/imsmanifest.xml

# 2. SCORM script referenced
grep -n "scorm_api.js" "Module X - Title/index.html"

# 3. Quiz reports score (should return 4: two functions called twice each)
grep -c "setSCORMScore\|setSCORMStatus" "Module X - Title/index.html"

# 4. Package contents correct
unzip -l "SCORM_Packages/output/Module_X_Title.zip"
```

| Issue | Fix |
| ----- | --- |
| `xmlParseEntityRef: no name` | Replace `&` with `&amp;` in manifest XML |
| Quiz doesn't report completion | Add `setSCORMScore()` and `setSCORMStatus()` to quiz `showResults()` |
| Video doesn't play | Convert to .mp4: `ffmpeg -i in.mov -c:v libx264 -c:a aac out.mp4` |

## ElevenLabs Audio Optimization

When creating `Video Script - ElevenLabs.md`:
- Remove all visual cues: `[SCREEN:]`, `[DEMO:]`, `[PAUSE]`, `**NARRATOR:**`
- Use `<break time="Xs" />` sparingly (max 2s)
- Use CAPS for emphasis instead of markdown bold/italic
- Expand abbreviations: "Q3" to "third quarter", "100x" to "one hundred times"
- Convert tables to spoken prose
- Add closing segment leading into lesson/lab/quiz

## ActivTrak Brand Colors

```css
--dark-navy: #14203F    /* Body text, closing backgrounds */
--medium-navy: #19316A  /* Header bars, accents */
--blue: #1657A0         /* Section dividers */
--teal: #2ED4B5         /* CTAs, highlights */
--yellow: #FFC83B       /* Secondary accents - sparingly */
--white: #FFFFFF        /* Backgrounds */
```

**Typography:** Century Gothic, slide dimensions 10" x 7.5" (4:3)

`update_branding.py` replaces old color variables and hardcoded hex values across both source module HTML and SCORM copies.

## Module Curriculum

| Module | Title | Focus |
|--------|-------|-------|
| 0 | Pre-Flight Check | Setup, Policy & Boundaries |
| 1 | The Cognitive Shift | Understanding the Reasoning Engine |
| 2 | Model Selection | The "Thinking" Protocol |
| 3 | Prompt Architecture | Advanced Prompt Architecture (XML) |
| 4 | Personal Projects & Folders | Claude Projects and ChatGPT Folders |
| Bonus | SARA | Mission-Specific Command Center (Claude Project) |
| 5 | The Sensory System | Gemini & Granola |
| 6 | Decision Hygiene | Beating Sycophancy |
| 7 | The Hybrid Agent | Mac, Mobile & Docs |
| 8 | Introduction to Skills | Building Reusable Prompt Templates |
| 9 | Systemizing Intelligence | Team Collaboration and Shared Projects |
| 10 | Agentic Data Analysis | The "No Math" Rule |
| 11 | Code Execution | File Creation (Excel, PPT, PDF) |
| 12 | Future Frontiers | Agents & MCP |
| 13 | Capstone & Governance | Accountability & Certification |

## Squadron Metaphor (Mandatory)

**Never introduce other metaphor families (nautical, medical, sports, etc.):**

| Concept | Squadron Term |
|---------|--------------|
| Learner | Squadron Leader |
| Claude | Mission Control / Command Center |
| Gemini | Recon & Radar |
| Granola | Flight Recorder |
| Templates/Skills | Mission Cards / Playbook |
| Projects | Missions |
| Data Safety | Tower Lights (Green/Yellow/Red) |

**Core principle:** "AI drafts. Humans send." / "You clear missions for takeoff and own what leaves the runway"

## Content Standards

**Learning Objectives:** `By the end of this module, learners will be able to [ACTION VERB] + [SPECIFIC CONTENT] + [CONTEXT]`

**Marzano Levels:** Retrieval, Comprehension, Analysis, Utilization

**Module Arc:** Hook, Foundation, Demonstration, Practice, Application, Reflection

## Key Files

| File | Purpose |
|------|---------|
| `Course Development Guide.md` | Authoritative content standards and deliverable formats |
| `Data Repo/00 - Source Material Index.md` | Find source content by topic with concept cross-references |
| `Data Repo/From Solo Pilot..._(1).md` | Full curriculum outline |
| `Data Repo/From Solo Pilot..._(2).md` | Multi-agent architecture, XML prompting, Skills framework |
| `Data Repo/From Solo Pilot..._(3).md` | COSTAR, PREP, CARE prompt frameworks |
| `Data Repo/From Solo Pilot..._(4).md` | Calculator problem, code execution, Python sandbox |
| `Data Repo/From Solo Pilot..._(5).md` | Artifacts, file creation, cross-platform workflows |
| `Data Repo/From Solo Pilot..._(6).md` | Personas, skills, context management, token economics |
| `Data Repo/From Solo Pilot..._(7-10).md` | Additional research and supporting content |
| `SCORM_Packages/scorm_api.js` | SCORM 1.2 API wrapper (shared across all packages) |
| `SCORM_Packages/create_packages.sh` | Automated individual module packaging |
| `update_branding.py` | Apply ActivTrak colors to all module HTML |
| `.claude/commands/` | Custom skills: `/design-module`, `/build-scorm` |

## Specialized Agents

- **module-curriculum-architect**: Module design, Marzano alignment, metaphor consistency, gap analysis
- **articulate-learning-designer**: Articulate (Storyline/Rise) visual design, ActivTrak branding

## Terminology Rules

- "Users" or "accounts" (never "customers" for end users)
- "Flexible hours schedules" and "schedule adherence" (not "flex work")
- "Insights, Not Oversight" (privacy philosophy)
- "Productivity Optimization" (not "Performance Optimization")
- No Oxford comma
- No em-dashes unless necessary

## Tool Selection

- Use standard file system tools: Read, Write, Edit, Glob, Grep
- **Do NOT use Obsidian MCP tools** (`mcp__obsidian-semantic__*`) in this project - use file system tools instead
- Obsidian conventions: Wikilinks `[[Note]]`, callouts `> [!tip]`, YAML frontmatter
- Use ffmpeg for video conversion (available at /opt/homebrew/bin/ffmpeg)
- Custom skills (`/design-module`, `/build-scorm`) are invoked via the Skill tool
