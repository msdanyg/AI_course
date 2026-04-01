# Module 9 Flashcards
## Code Execution & File Creation

---

### Card 1

**Front:**
How does Claude actually create downloadable files like PowerPoint or Excel?

**Back:**
Claude **writes Python code** using specialized libraries (python-pptx, openpyxl, pandas), **executes that code** in a secure sandbox, and **captures the output file** for download.

It doesn't "generate" files directly—it programs them.

---

### Card 2

**Front:**
What Python libraries does Claude use for file creation?

**Back:**
| Library | File Type |
|---------|-----------|
| `python-pptx` | PowerPoint (.pptx) |
| `openpyxl` | Excel with formatting (.xlsx) |
| `pandas` | CSV, Excel, data manipulation |
| `csv` | Simple CSV operations |

---

### Card 3

**Front:**
What is "vibe coding" and when should you use it?

**Back:**
**Vibe coding**: Describing desired outcomes aesthetically rather than technically.

**Instead of:** "Use hex color #0056D2, font-size 24pt"
**Try:** "Make it feel like a Fortune 500 investor presentation"

**Key insight for non-developers:** You can generate HTML tables, styled reports, and formatted outputs without knowing code—just describe the aesthetic.

**Use for:** Visual styling, tone, general feel
**Be specific for:** Data values, structure, exact requirements

*Best practice: Combine vibe descriptions with structural precision.*

---

### Card 4

**Front:**
When should you use Claude vs. Gemini for creating presentations?

**Back:**
**Use Claude when:**
- You need a downloadable .pptx file
- You want precise structural control
- You need detailed speaker notes
- You prefer the structural draft workflow

**Use Gemini when:**
- You want native Google Slides format
- You want AI-selected imagery and themes
- You prefer one-click Slides export
- Speed matters more than precision

*Key distinction: Claude creates .pptx via code; Gemini creates native Slides format.*

---

### Card 5

**Front:**
What is the "structural draft" workflow for presentations?

**Back:**
1. **Generate with Claude**: Create content structure and organization
2. **Download the file**: Get the .pptx
3. **Apply template**: Open in PowerPoint/Slides, apply corporate theme
4. **Polish visuals**: Adjust colors, add images, refine layout

*Claude handles content organization; design tools handle visual polish.*

---

### Card 6

**Front:**
When should you export data as CSV vs. Excel (.xlsx)?

**Back:**
**Use CSV when:**
- Raw data transfer between systems
- Universal compatibility needed
- Simple tabular data
- Importing to databases

**Use Excel when:**
- Multiple sheets required
- Formatting needed (headers, colors)
- Formulas must be included
- Conditional formatting desired

---

### Card 7

**Front:**
What prompt elements produce the best PowerPoint outputs from Claude?

**Back:**
1. **Number of slides** specified
2. **Content for each slide** described
3. **Layout preferences** stated (title-and-content, etc.)
4. **Speaker notes** requested if needed
5. **Aesthetic direction** via vibe coding

*Vague prompts → generic outputs. Specific prompts → precise deliverables.*

---

### Card 8

**Front:**
What is the "Mission Output Framework" for file creation?

**Back:**
| Phase | Activity | Output |
|-------|----------|--------|
| Intel Gathering | Research, data upload | Facts, raw data |
| Analysis | Claude reasoning | Insights, findings |
| Synthesis | Structuring | Organized narrative |
| **Delivery** | **File creation** | **Slides, spreadsheets, reports** |

*File creation is the final phase—turning intelligence into tangible deliverables.*

---

**End of Flashcards**
