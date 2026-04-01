# Module 9 Quiz
## Code Execution & File Creation

**Instructions:** 7 questions. Mix of multiple choice, true/false with explanation, and scenario-based. Feedback provided for all answers.

---

### Question 1 (Multiple Choice)

**How does Claude create downloadable files like PowerPoint presentations?**

A) It generates binary file data directly from its training
B) It writes Python code using specialized libraries, executes it in a sandbox, and captures the output
C) It connects to Microsoft Office servers to create files remotely
D) It converts Markdown to the requested file format

**Correct Answer:** B

**Feedback for B (Correct):**
Exactly right. Claude uses a code execution approach:
1. Writes Python code using libraries like `python-pptx` (PowerPoint), `openpyxl` (Excel), or `pandas` (CSV)
2. Executes that code in a secure, sandboxed environment
3. Captures the resulting file and presents it for download

This is why specificity matters—Claude is essentially programming your deliverable, not generating it from memory.

**Feedback for other answers:**
Claude doesn't "generate" binary files from training data or connect to external servers. The mechanism is code execution: Claude writes a Python script that constructs the file, runs it in a sandbox, and outputs the result. This is the same code execution capability used for data analysis in Module 4.

---

### Question 2 (True/False with Explanation)

**TRUE or FALSE: Claude produces visually stunning presentations that are ready to share with clients without any modifications.**

**Correct Answer:** FALSE

**Feedback if FALSE (Correct):**
Correct. Claude produces **structural drafts**—content that is well-organized and properly distributed across slides, but with basic visual design.

The recommended workflow is:
1. Generate content structure with Claude
2. Download the .pptx file
3. Apply your corporate template for visual polish
4. Add images, adjust colors, refine layout

Claude excels at content organization; design tools (PowerPoint, Google Slides) excel at visual polish. Use each for their strengths.

**Feedback if TRUE (Incorrect):**
Claude generates structurally sound presentations with content properly organized across slides, but the visual design is basic (typically white backgrounds, black text, minimal styling). The "structural draft" workflow treats Claude's output as a starting point: generate structure with AI, apply visual polish with design tools. This approach leverages each tool's strengths.

---

### Question 3 (Multiple Choice)

**When should you use Gemini instead of Claude for creating a presentation?**

A) When you need precise control over slide structure and speaker notes
B) When you want a native Google Slides file built directly in the Slides format
C) When you need to work offline
D) When you need to include complex data tables

**Correct Answer:** B

**Feedback for B (Correct):**
Correct. Gemini creates **native Google Slides** directly in the Slides format, with AI-selected imagery and themes.

While Claude can also integrate with Google Drive (when enabled), it generates .pptx files via python-pptx that you then upload or convert. Gemini builds presentations natively in Google Slides format with one-click export.

Use Claude when you need precise structural control, detailed speaker notes, or prefer the python-pptx approach. Use Gemini when you want native Slides format with AI-assisted visual design.

**Feedback for other answers:**
- **Option A**: Claude offers more structural control, making this a reason to use Claude, not Gemini
- **Option C**: Both require internet; this isn't the key differentiator
- **Option D**: Both can handle tables; this isn't a differentiator

The key distinction is output format: Gemini creates native Google Slides; Claude creates .pptx files via code execution.

---

### Question 4 (Multiple Choice)

**What is "vibe coding"?**

A) Writing code that has good "vibes" and follows best practices
B) Describing desired outcomes aesthetically rather than technically
C) Using emojis and casual language in prompts
D) Generating code that looks visually pleasing in the editor

**Correct Answer:** B

**Feedback for B (Correct):**
Exactly. Vibe coding means describing what you want in natural, aesthetic terms:

**Instead of:** "Use hex color #0056D2, font-size 24pt, border-collapse: collapse"

**Try:** "Make it feel like a Fortune 500 investor presentation—clean, professional, data-driven"

Claude translates your aesthetic description into the technical parameters.

**Key insight for non-developers:** You don't need to know HTML, CSS, or Python to get code-quality outputs. Describe "an HTML table that looks like a modern SaaS dashboard" and Claude generates it—ready to screenshot or export.

**Best practice:** Combine vibe descriptions (for style and feel) with structural precision (for content and organization). Be specific about *what* content you need; be aesthetic about *how* it should look.

**Feedback for other answers:**
Vibe coding isn't about best practices, casual language, or code aesthetics. It's about prompting technique—describing outcomes in terms of how they should *feel* rather than specifying exact technical parameters. This makes AI file creation accessible to non-technical users while still producing professional results.

---

### Question 5 (Scenario-Based)

**Scenario:** You need to clean a messy customer data spreadsheet and share the results with your analytics team. The data has inconsistent date formats, duplicate rows, and missing values.

**What's the most efficient approach?**

A) Manually clean the data in Excel, then email the file
B) Upload to Claude, describe the transformations needed, download the cleaned CSV
C) Copy-paste the data into Google Sheets and use formulas to clean it
D) Ask Claude to describe how to clean the data, then do it manually

**Correct Answer:** B

**Feedback for B (Correct):**
Perfect. This leverages Claude's code execution for data transformation:

1. **Upload** the messy file to Claude
2. **Describe** the transformations: "Normalize dates to YYYY-MM-DD, remove duplicates, fill missing Region values with 'Unknown'"
3. **Download** the cleaned CSV

Claude writes a Python script (using pandas) that performs all transformations and outputs a clean file. What might take 30 minutes manually takes 2 minutes with AI.

This is the "analysis to deliverable" workflow in action—upload raw data, describe desired outcome, download clean export.

**Feedback for other answers:**
- **Option A**: Manual cleaning is time-consuming and error-prone
- **Option C**: Formulas work but require manual formula writing and don't scale
- **Option D**: Having Claude describe the process but doing it manually defeats the purpose of code execution

The efficiency gain comes from letting Claude execute the transformation code, not just explain it.

---

### Question 6 (True/False with Explanation)

**TRUE or FALSE: You should always use Excel (.xlsx) format instead of CSV because it's more capable.**

**Correct Answer:** FALSE

**Feedback if FALSE (Correct):**
Correct. Each format has appropriate use cases:

**Use CSV when:**
- Transferring raw data between systems
- Importing to databases or other tools
- Maximum compatibility needed
- Simple tabular data without formatting

**Use Excel when:**
- Multiple sheets required
- Formatting needed (headers, colors, borders)
- Formulas must be included
- Conditional formatting desired

CSV is often preferred for data interchange precisely because it's simple and universal. Excel is better when presentation and structure matter.

**Feedback if TRUE (Incorrect):**
While Excel is more capable (formatting, multiple sheets, formulas), that capability isn't always needed. CSV files are the universal exchange format—they work with virtually any system, database, or tool. For data transfers, system integrations, or simple exports, CSV is often the better choice. Use Excel when you need its specific features; use CSV when simplicity and compatibility matter.

---

### Question 7 (Scenario-Based)

**Scenario:** You're preparing for a customer meeting tomorrow. You have notes from your last call and need both a presentation deck and a data summary to share.

**What is the optimal workflow using the tools from this module?**

A) Use Gemini for everything since it integrates with Google
B) Use Claude to generate both the presentation and data summary as downloadable files
C) Create the presentation manually in Google Slides and use Claude only for the data export
D) Use Claude for the data analysis and CSV export, then use either Claude or Gemini for the presentation based on your preference

**Correct Answer:** D

**Feedback for D (Correct):**
Excellent reasoning. This applies the decision framework correctly:

1. **Data work (Claude)**: Upload your data, analyze it, export as CSV. Claude's code execution handles transformation and export precisely.

2. **Presentation (Claude OR Gemini)**:
   - Choose Claude if you want a downloadable .pptx with precise structure
   - Choose Gemini if you want direct Google Drive export and are already in that ecosystem

This approach uses each tool for its strengths and respects your workflow preferences. There's no single "right" tool for presentations—the choice depends on whether you prioritize downloadable files (Claude) or native Google integration (Gemini).

**Feedback for other answers:**
- **Option A**: Gemini is great for Google-native presentations but Claude is stronger for data analysis and transformation
- **Option B**: Works, but doesn't leverage Gemini's Google integration if that's your ecosystem
- **Option C**: Manual presentation creation defeats the purpose of this module's capabilities

The key insight is matching tool to task: Claude for data work, then choose your presentation tool based on workflow preference.

---

## Quiz Complete

**Score Interpretation:**

- **6-7 correct**: Mission Output Commander achieved. You understand how to produce deliverables from your Squadron.
- **4-5 correct**: Solid foundation. Review the Claude vs. Gemini decision framework and vibe coding concepts.
- **0-3 correct**: Revisit the lesson focusing on how code execution creates files and when to use each tool.

**Key Concepts to Master:**
1. Claude writes Python code to create files (code execution architecture)
2. PowerPoint outputs are structural drafts—apply visual polish afterward
3. Choose Claude for downloadable files, Gemini for native Google integration
4. Vibe coding describes aesthetics; combine with structural precision
5. CSV for data interchange, Excel when formatting/sheets matter

---

**Proceed to Study Guide to consolidate your learning.**
