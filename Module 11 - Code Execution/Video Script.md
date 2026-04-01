# Module 9 Video Script
## Code Execution & File Creation: From Analysis to Deliverables

**Duration:** 8-10 minutes
**Format:** Screen share with instructor voice-over
**Tone:** Practical, focused on outcomes

---

## OPENING (45 seconds)

**[SCREEN: Title card - "Module 9: Code Execution & File Creation"]**

**INSTRUCTOR (V.O.):**
"You've built your Squadron infrastructure. Projects hold your context. Skills standardize your workflows. But here's the question:

**[SCREEN: Chat interface with analysis text]**

Where do these insights go?

Your stakeholders don't read AI chat transcripts. They want slide decks. Spreadsheets. Reports they can share.

**[SCREEN: Transformation animation - Chat → PowerPoint/Excel/CSV icons]**

Module 9 solves the output problem. You're about to turn Claude from a reasoning engine into a file factory.

Let's build some deliverables."

---

## SECTION 1: HOW IT WORKS (1.5 minutes)

**[SCREEN: Architecture diagram showing prompt → code → file]**

**INSTRUCTOR (V.O.):**
"First, understand what's actually happening. When you ask Claude to create a PowerPoint file, it doesn't magically conjure one.

**[SCREEN: Code execution flow diagram]**

Claude writes a Python script using specialized libraries. Python-pptx for PowerPoint. Openpyxl for Excel. Pandas for CSVs.

Then it executes that script in a secure sandbox and captures the output file for you to download.

**[SCREEN: Highlighting the libraries]**

This is the same code execution you learned in Module 4 for analysis. Now we're using it to produce deliverables.

**[SCREEN: Before/After comparison]**

This means Claude can be incredibly precise—exact slide structures, specific formatting, calculated values. But it also means you need to be specific about what you want.

Vague prompts produce generic outputs. Precise prompts produce exactly what you need."

---

## SECTION 2: POWERPOINT GENERATION (2 minutes)

**[SCREEN: Claude interface with PowerPoint prompt]**

**INSTRUCTOR (V.O.):**
"Let's create a presentation. I need a customer QBR deck.

**[SCREEN: Typing prompt]**

Watch my prompt structure. I'm specifying:
- Number of slides
- Content for each slide
- Layout preferences
- Request for speaker notes

**[SCREEN: Show full prompt]**

```
Create a 6-slide PowerPoint presentation for a customer QBR.

Slide 1: Title - 'Q3 Business Review'
Slide 2: Agenda
Slide 3: Adoption Metrics with specific numbers
Slide 4: Key Wins
Slide 5: Challenges and Solutions
Slide 6: Next Steps

Use title-and-content layouts. Include speaker notes.
```

**[SCREEN: Claude generating, then download button appears]**

Claude writes the python-pptx code, executes it, and gives me a downloadable file.

**[SCREEN: Opening the PowerPoint file]**

Here's the output. Six slides, exactly as specified. Speaker notes included.

**[SCREEN: Highlighting the basic styling]**

Now notice—the visual design is basic. That's intentional. Claude excels at content structure, not graphic design.

**[SCREEN: Applying a template in PowerPoint]**

My workflow: Generate structure with Claude, then apply my corporate template for visual polish. This takes a task that used to take an hour down to five minutes."

---

## SECTION 3: CLAUDE VS. GEMINI (1.5 minutes)

**[SCREEN: Side-by-side Claude and Gemini interfaces]**

**INSTRUCTOR (V.O.):**
"Now, there's another option. Gemini can create presentations too—but it works differently.

**[SCREEN: Gemini Canvas interface]**

With Gemini Canvas, I prompt for a presentation, and instead of generating a downloadable file, it builds slides right here in the interface.

**[SCREEN: 'Export to Google Slides' button highlighted]**

Then I click 'Export to Google Slides' and it goes directly to my Drive as a native Google Slides file—not a converted PowerPoint, but actual Slides format with AI-selected imagery and themes.

**[SCREEN: Decision matrix appearing]**

So when do you use which? Now, both tools can integrate with Google Drive—Claude can save files there too if you enable it. The key distinction is output format.

**[SCREEN: Highlighting each row as mentioned]**

Use Claude when you need a downloadable .pptx file, when you want precise structural control, or when you need detailed speaker notes.

Use Gemini when you want native Google Slides format, when you want AI-selected imagery and themes, or when speed matters more than structural precision.

Claude creates PowerPoint files via code. Gemini creates native Slides format. Choose based on your output needs."

---

## SECTION 4: CSV AND DATA EXPORTS (1.5 minutes)

**[SCREEN: Data export scenario]**

**INSTRUCTOR (V.O.):**
"Beyond presentations, you'll frequently need data exports. CSVs are the universal exchange format.

**[SCREEN: Claude interface with data]**

I've uploaded a messy spreadsheet. Watch what I ask Claude to do.

**[SCREEN: Typing transformation prompt]**

```
Clean this data:
1. Normalize all dates to YYYY-MM-DD
2. Remove duplicate rows
3. Fill missing Region values with 'Unknown'
4. Export as a clean CSV
```

**[SCREEN: Claude processing, download appears]**

Claude reads the file, writes transformation code, executes it, and gives me the cleaned CSV.

**[SCREEN: Opening CSV in Excel]**

No manual data cleaning. No formula writing. Upload, describe the transformation, download the result.

**[SCREEN: Aggregation example]**

I can also create summary exports. 'From this data, create a CSV with one row per region showing total revenue and transaction count.'

**[SCREEN: Download and open summary]**

Analysis and export combined. This is how your Squadron produces data deliverables."

---

## SECTION 5: VIBE CODING (1.5 minutes)

**[SCREEN: Traditional code vs. natural description]**

**INSTRUCTOR (V.O.):**
"Here's a technique that makes this even more powerful: vibe coding.

**[SCREEN: Technical prompt example]**

Traditional approach: You specify exact parameters. Font sizes, hex colors, pixel dimensions.

**[SCREEN: Vibe coding prompt example]**

Vibe coding: You describe the outcome aesthetically.

**[SCREEN: Side-by-side comparison]**

Instead of 'use hex color #0056D2 for headers,' try 'use a professional corporate blue.'

Instead of 'set font-size 24pt,' try 'make it feel like a Fortune 500 investor presentation.'

**[SCREEN: Generated output]**

Claude translates your aesthetic description into technical parameters.

**[SCREEN: HTML table example rendering]**

Here's the key insight for non-developers: you don't need to know how to code to get code-quality outputs.

Watch this. I'll ask Claude to 'create an HTML table of our top accounts—make it look like a modern SaaS dashboard, clean lines, alternating row colors.'

**[SCREEN: Rendered HTML table]**

Claude generates the HTML, renders it visually, and I can screenshot this for my executive summary. Professional output, zero coding knowledge required.

This works for formatted tables, styled reports, even interactive elements. Just describe the aesthetic, and Claude handles the technical translation.

**[SCREEN: Best practice callout]**

Best practice: Combine vibe descriptions with structural precision. Be specific about what content you need. Be aesthetic about how it should look and feel."

---

## SECTION 6: COMPLETE WORKFLOW (1.5 minutes)

**[SCREEN: Workflow diagram]**

**INSTRUCTOR (V.O.):**
"Let me show you a complete workflow. I need to prepare for a customer meeting tomorrow.

**[SCREEN: Step 1 - Meeting notes]**

Step one: I paste my notes from the last call.

**[SCREEN: Step 2 - Request structure]**

Step two: I request a presentation structure.

```
Based on these notes, create a 5-slide follow-up presentation:
1. Title
2. Recap of last meeting
3. Progress updates
4. Recommendations
5. Discussion questions

Include speaker notes with talking points.
```

**[SCREEN: Claude generating]**

Step three: Claude generates the structural draft.

**[SCREEN: Downloading file]**

Step four: I download the file.

**[SCREEN: Applying template in PowerPoint]**

Step five: I apply my template and add any visuals.

**[SCREEN: Final presentation]**

What used to take an hour of copy-pasting and formatting now takes ten minutes. My Squadron produces the content. I provide the polish.

This is how file creation should work."

---

## CLOSING (45 seconds)

**[SCREEN: Mission Output Framework diagram]**

**INSTRUCTOR (V.O.):**
"Think of file creation as the final phase of any Squadron mission.

Intel gathering. Analysis. Synthesis. And now—delivery.

**[SCREEN: Files appearing - PPT, CSV, XLSX]**

Your infrastructure handles the first three phases. Code execution handles the fourth—turning intelligence into tangible deliverables that move business forward.

**[SCREEN: Preview of Module 10]**

Next module: Future Frontiers. You'll learn about AI Agents and MCP—Model Context Protocol. Systems that can execute multi-step workflows autonomously, access external tools, and operate with minimal intervention.

From file factory to autonomous operations.

**[SCREEN: Lab preview]**

Head to the lab. You're going to build a customer presentation from scratch—or for advanced credit, create an integrated workflow that goes from data analysis to formatted deliverables.

Your Squadron now produces artifacts. Let's put it to work."

---

## PRODUCTION NOTES

**Visual Requirements:**
- Claude interface screen recordings (PowerPoint generation)
- Gemini Canvas demonstration
- PowerPoint/Google Slides opening generated files
- Architecture diagrams (code execution flow)
- Split-screen comparisons (Claude vs. Gemini)

**Demo Files Needed:**
- Sample messy CSV for transformation demo
- Generated PowerPoint file
- Generated CSV exports
- Before/after template application

**Timing Breakdown:**
- Opening: 0:00-0:45
- How It Works: 0:45-2:15
- PowerPoint Generation: 2:15-4:15
- Claude vs. Gemini: 4:15-5:45
- CSV and Data Exports: 5:45-7:15
- Vibe Coding: 7:15-8:15
- Complete Workflow: 8:15-9:45
- Closing: 9:45-10:30

**Total Runtime:** ~10 minutes

---

**End of Video Script**
