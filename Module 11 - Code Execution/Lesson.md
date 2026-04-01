# Module 9: Code Execution & File Creation
## From Analysis to Deliverables

---

## Introduction: The Output Problem

You've built your Squadron infrastructure. Your Projects hold context. Your Skills standardize methodology. Your Gems gather current intelligence. But here's the gap: **all that intelligence lives inside the AI interface.**

Your stakeholders don't want a chat transcript. They want a slide deck. Your finance team doesn't want you to describe the analysis—they want the spreadsheet. Your clients don't read AI conversations—they read polished reports.

Module 9 solves the output problem. You're about to learn how Claude transforms from a reasoning engine into a **file factory**—generating PowerPoint presentations, CSV exports, formatted spreadsheets, and more. The key? Understanding that Claude doesn't just describe files; it **writes code that builds them.**

This is where your Squadron starts producing mission-ready deliverables.

---

## The Architecture: How File Creation Actually Works

Before we create files, you need to understand what's happening behind the scenes. This understanding prevents frustration and unlocks advanced capabilities.

### The Code Execution Environment

When you ask Claude to "create an Excel file," Claude doesn't magically conjure a binary file. Instead, it:

1. **Writes a Python script** using specialized libraries
2. **Executes that script** in a secure, sandboxed environment
3. **Captures the output file** and presents it for download

This is the same "Code Execution" capability you learned about in Module 4 for data analysis. Now we're using it to produce deliverables rather than just analyze data.

### The Library Stack

Claude has access to several Python libraries for file creation:

| Library | Purpose | File Type |
|---------|---------|-----------|
| `python-pptx` | PowerPoint generation | .pptx |
| `openpyxl` | Excel with formatting | .xlsx |
| `pandas` | Data manipulation, CSV export | .csv, .xlsx |
| `csv` | Simple CSV operations | .csv |

When you request a file, Claude selects the appropriate library and writes code to construct your deliverable. This is why **specificity matters**—vague requests produce generic outputs; precise requests produce exactly what you need.

---

## PowerPoint Generation: Slide Decks on Demand

PowerPoint presentations are among the most time-consuming deliverables to create manually. Claude can generate complete .pptx files in seconds—but understanding the constraints helps you get better results.

### How Claude Builds Slides

Claude uses `python-pptx` to programmatically construct presentations. This means:

- **Structure is precise**: Titles, bullet points, and placeholders are positioned exactly as specified
- **Visual design is basic**: Claude builds content structure, not graphic design
- **Iteration is easy**: Request changes and Claude regenerates the file

Think of it as "content scaffolding." Claude handles the tedious work of organizing information across slides; you apply visual polish afterward.

### The Basic Prompt Pattern

```
Create a PowerPoint presentation with [X] slides about [TOPIC].

Structure:
- Slide 1: Title slide with [TITLE] and [SUBTITLE]
- Slide 2: Agenda/Overview
- Slides 3-X: [CONTENT DESCRIPTION]
- Final slide: Summary/Next Steps

Use a title-and-content layout for body slides.
Include speaker notes for each slide.
```

### Example: Customer QBR Presentation

Let's say you need to prepare a Quarterly Business Review for a customer.

**Prompt:**
```
Create a 6-slide PowerPoint presentation for a customer QBR.

Slide 1: Title
- Title: "Q3 Business Review"
- Subtitle: "Acme Healthcare Partnership"

Slide 2: Agenda
- Adoption Metrics
- Key Wins This Quarter
- Challenges & Solutions
- Roadmap Preview
- Q&A

Slide 3: Adoption Metrics
- Active users: 847 (up 12% from Q2)
- Daily engagement: 78%
- Feature utilization: 6 of 8 core features

Slide 4: Key Wins
- Reduced time-to-insight by 40%
- Identified 3 at-risk teams before turnover
- Executive dashboard adoption reached 100%

Slide 5: Challenges & Solutions
- Challenge: Mobile adoption lagging (32%)
- Solution: Scheduled mobile training sessions for Q4

Slide 6: Next Steps
- Q4 Goals
- Renewal discussion timeline
- Support contact information

Use standard title-and-bullet layouts. Include speaker notes summarizing talking points for each slide.
```

Claude generates a downloadable .pptx file with all content organized across slides, speaker notes included.

### The "Structural Draft" Workflow

The most efficient approach treats Claude's output as a **structural draft**:

1. **Generate with Claude**: Create the content structure and organization
2. **Download the file**: Get the .pptx to your local machine
3. **Apply your template**: Open in PowerPoint/Google Slides, apply corporate theme
4. **Polish visuals**: Adjust colors, add images, refine layout

This workflow leverages Claude for what it does best (content organization) while using design tools for what they do best (visual polish).

---

## Google Slides: The Native Alternative

While Claude generates PowerPoint files via code, Gemini offers a different approach: **native Google Slides integration**.

### Claude vs. Gemini for Presentations

| Approach | Tool | Strengths | Limitations |
|----------|------|-----------|-------------|
| Code-generated .pptx | Claude | Precise structure, detailed speaker notes, downloadable file | Basic styling, requires post-processing |
| Native Slides format | Gemini | Built directly in Slides format, AI-selected imagery and themes | Less structural control, requires Google account |

**Note**: Both tools can integrate with Google Drive. The key distinction is output format: Claude creates .pptx files via python-pptx code execution; Gemini creates presentations directly in Google Slides format.

### When to Use Each

**Use Claude when:**
- You need a downloadable .pptx file
- You want precise control over slide structure
- You need detailed, specific speaker notes
- You prefer the structural draft workflow

**Use Gemini when:**
- You want native Google Slides format
- You want AI to select imagery and themes
- You prefer one-click export to Slides
- Speed matters more than structural precision

### The Gemini Canvas Workflow

In Gemini, you can create presentations using Canvas:

1. **Prompt**: "Create a 5-slide presentation about [TOPIC]"
2. **Review**: Gemini builds slides in the Canvas interface
3. **Export**: Click "Export to Google Slides"
4. **Result**: Editable presentation in your Drive

This bypasses file downloads entirely—the presentation goes directly to your Google account.

---

## CSV Generation: Data Exports Made Easy

CSV (Comma-Separated Values) files are the universal exchange format for data. Claude can generate CSVs from analysis, transform data formats, or create structured datasets from scratch.

### Basic CSV Creation

**Prompt:**
```
Create a CSV file with sample sales data:
- Columns: Date, Region, Product, Units_Sold, Revenue
- Include 20 rows of realistic data
- Date range: October 2024
- Regions: North, South, East, West
- Products: Basic, Professional, Enterprise
```

Claude writes a Python script that generates the data and outputs a downloadable .csv file.

### Data Transformation Exports

More commonly, you'll transform existing data:

**Prompt:**
```
I've uploaded a messy spreadsheet with inconsistent date formats.

Clean this data:
1. Normalize all dates to YYYY-MM-DD format
2. Remove duplicate rows
3. Fill missing "Region" values with "Unknown"
4. Export as a clean CSV file
```

Claude reads your upload, writes transformation code, executes it, and provides the cleaned CSV.

### Aggregated Exports

You can also create summary exports:

**Prompt:**
```
From the uploaded sales data, create a summary CSV with:
- One row per Region
- Columns: Region, Total_Revenue, Avg_Order_Value, Transaction_Count
- Sort by Total_Revenue descending
```

This combines analysis and export—Claude calculates the aggregations and outputs them as a downloadable file.

---

## Excel Generation: Formatted Spreadsheets

While CSVs handle raw data, Excel files (.xlsx) support formatting, multiple sheets, and formulas. Claude uses `openpyxl` to create these.

### When to Use Excel vs. CSV

| Need | Use CSV | Use Excel |
|------|---------|-----------|
| Raw data transfer | ✓ | |
| Multiple sheets | | ✓ |
| Formatted headers | | ✓ |
| Conditional formatting | | ✓ |
| Formulas | | ✓ |
| Universal compatibility | ✓ | |

### Basic Excel with Formatting

**Prompt:**
```
Create an Excel file with sales data:
- Sheet 1: "Raw Data" with the transaction details
- Sheet 2: "Summary" with aggregated metrics

Formatting requirements:
- Header row: Bold, gray background (#f0f0f0)
- Currency columns: Format as $X,XXX.XX
- Date columns: Format as MM/DD/YYYY
- Freeze the header row
```

Claude generates a properly formatted .xlsx file with both sheets configured as specified.

### Multi-Sheet Workbooks

**Prompt:**
```
Create an Excel workbook for monthly reporting:

Sheet 1 - "October Data": Raw transaction data
Sheet 2 - "By Region": Pivot summary by region
Sheet 3 - "By Product": Pivot summary by product
Sheet 4 - "Trends": Month-over-month comparison

Apply consistent formatting:
- All sheets: Header row with bold text, light blue background
- Summary sheets: Include totals row at bottom
- Currency values: Two decimal places with dollar sign
```

This creates a complete reporting workbook ready for stakeholder review.

---

## Vibe Coding: Describing Outcomes, Not Syntax

One of the most powerful aspects of AI file creation is **vibe coding**—describing what you want in natural, aesthetic terms rather than technical specifications.

### What is Vibe Coding?

Traditional programming requires knowing exact syntax:
```python
plt.style.use('dark_background')
ax.set_facecolor('#1a1a2e')
colors = ['#e94560', '#0f3460', '#16213e']
```

Vibe coding describes the outcome:
```
Create a chart with a dark, modern aesthetic. Use deep blues
and accent with a vibrant coral color. Make it look like
something you'd see in a tech company's annual report.
```

Claude translates your aesthetic description into the technical parameters.

### Why This Matters for Non-Developers

Here's the key insight: **you don't need to know how to code to get code-quality outputs.**

Even if you've never written HTML, CSS, or Python, you can use vibe coding to generate:
- **Formatted HTML tables** that look polished when pasted into emails or documents
- **Styled reports** with professional layouts you can export or screenshot
- **Interactive elements** that would normally require developer skills
- **Structured outputs** formatted exactly how you need them for copy/paste workflows

For example:
```
Create an HTML table showing our top 5 accounts by revenue.
Make it look like something from a modern SaaS dashboard—clean
lines, alternating row colors, bold headers. I want to screenshot
this for my executive summary.
```

Claude generates the HTML, renders it visually, and you capture exactly what you need. No coding knowledge required—just clear aesthetic direction.

### Vibe Coding for Presentations

**Instead of:**
```
Create slides with font-size 24pt for titles, 18pt for body,
using hex colors #0056D2 for headers...
```

**Try:**
```
Create a professional slide deck that feels modern and clean.
Use a corporate blue color scheme. The design should feel
authoritative but approachable—like a Fortune 500 company's
investor presentation.
```

### Vibe Coding for Data Visualizations

**Instead of:**
```
Use matplotlib with figsize=(10,6), dpi=100,
grid alpha=0.3...
```

**Try:**
```
Create a chart that's presentation-ready. Clean, minimal
gridlines, easy-to-read labels, professional color palette.
The kind of chart you'd show to executives.
```

### When Vibe Coding Works Best

Vibe coding excels for:
- Visual styling and aesthetics
- Tone and presentation feel
- General structure and organization

But be specific for:
- Exact data values and calculations
- Structural requirements (number of slides, columns)
- File format specifications

**Best practice**: Combine vibe descriptions with structural precision.

```
Create a 6-slide presentation about Q3 results.
[STRUCTURAL: specific slide content here]

Make it feel confident and data-driven. Clean design,
minimal text per slide, emphasis on the metrics.
Use our brand blue (#0056D2) as the accent color.
```

---

## Practical Workflows: End-to-End Examples

Let's walk through complete workflows that combine analysis with deliverable creation.

### Workflow 1: Meeting Prep Deck

**Scenario**: You have meeting notes and need a presentation for tomorrow's client call.

**Step 1: Provide Context**
```
I have notes from my last call with Acme Corp. I need to
create a follow-up presentation for tomorrow's meeting.

[Paste meeting notes or upload document]
```

**Step 2: Request Structure**
```
Based on these notes, create a 5-slide PowerPoint:

1. Title: "Acme Corp Follow-Up"
2. Recap: Key points from last meeting
3. Updates: Progress on their requests
4. Recommendations: Our suggested next steps
5. Discussion: Open questions for tomorrow

Include speaker notes with talking points.
```

**Step 3: Download and Polish**
- Download the .pptx
- Apply your company template
- Add any visuals or screenshots
- Review speaker notes

### Workflow 2: Data Export for Stakeholders

**Scenario**: You've analyzed productivity data and need to share findings.

**Step 1: Upload and Analyze**
```
[Upload CSV]

Analyze this productivity data:
- Calculate average productivity score by team
- Identify teams below 70% threshold
- Find week-over-week trends
```

**Step 2: Create Export**
```
Now create an Excel file for the leadership team:

Sheet 1 - "Team Scores": All teams with current scores
Sheet 2 - "At Risk": Only teams below 70%
Sheet 3 - "Trends": Week-over-week changes

Format for executive review:
- Clear headers
- Conditional formatting: Red for scores below 70%
- Sort by score ascending (worst first on At Risk sheet)
```

**Step 3: Distribute**
- Download the .xlsx
- Add any manual annotations
- Share via email or Slack

### Workflow 3: Customer-Ready Slides via Gemini

**Scenario**: You need a quick presentation for an internal meeting, native to Google.

**Step 1: Open Gemini**
- Navigate to gemini.google.com
- Ensure you're logged into your work account

**Step 2: Request Presentation**
```
Create a 5-slide presentation for our team meeting:

Topic: Q4 Planning Priorities
Slides:
1. Title slide
2. Q3 Recap (key wins)
3. Q4 Focus Areas
4. Resource Needs
5. Timeline

Keep it simple and visual. Use a professional blue theme.
```

**Step 3: Export and Customize**
- Click "Export to Google Slides"
- Open in Google Slides
- Adjust as needed
- Share with team

---

## Common Pitfalls and Solutions

### Pitfall 1: Vague File Requests

**Problem**: "Make me a PowerPoint about our product"
**Result**: Generic, unfocused slides

**Solution**: Specify structure, content, and purpose
```
Create a 7-slide product overview for enterprise prospects:
[Detailed slide-by-slide content]
```

### Pitfall 2: Expecting Design Excellence

**Problem**: Assuming Claude will produce visually stunning slides
**Result**: Disappointment with basic formatting

**Solution**: Treat Claude's output as structural draft
- Generate content and organization with Claude
- Apply visual design in PowerPoint/Slides

### Pitfall 3: Forgetting to Verify Data

**Problem**: Trusting CSV/Excel outputs without review
**Result**: Potential calculation errors in deliverables

**Solution**: Always verify critical numbers
- Check totals and aggregations
- Spot-check formulas
- Review before distributing

### Pitfall 4: Wrong Tool for the Job

**Problem**: Using Claude for quick Google Slides when Gemini is faster
**Result**: Unnecessary file downloads and uploads

**Solution**: Match tool to workflow
- Claude: Downloadable files, precise structure, offline work
- Gemini: Native Google integration, quick drafts

---

## The Mission Output Framework

Think of file creation as the final phase of a Squadron mission:

| Phase | Activity | Output |
|-------|----------|--------|
| **Intel Gathering** | Gemini research, data upload | Facts, raw data |
| **Analysis** | Claude reasoning, code execution | Insights, findings |
| **Synthesis** | Claude structuring | Organized narrative |
| **Delivery** | File creation | Slides, spreadsheets, reports |

Your Squadron infrastructure (Projects, Skills, Gems) handles phases 1-3. Code execution handles phase 4—turning intelligence into tangible deliverables.

---

## ActivTrak Applications

### Sales: Prospect Presentations
- Generate custom slide decks for each prospect
- Include relevant case studies and metrics
- Create comparison tables as formatted exports

### Customer Success: QBR Materials
- Build quarterly review presentations from account data
- Export usage summaries to Excel for customer sharing
- Create trend visualizations for business reviews

### Product Marketing: Competitive Battle Cards
- Generate formatted comparison tables
- Create presentation slides for sales enablement
- Export competitive data for CRM integration

### Operations: Reporting Automation
- Transform raw data into formatted Excel reports
- Create standardized presentation templates
- Generate CSV exports for system integrations

---

## Connection to Module 10

You now command a Squadron that produces mission-ready deliverables. But currently, you're orchestrating everything manually—uploading files, switching between tools, copying outputs.

**Module 10: Future Frontiers** introduces the next evolution: **AI Agents and MCP (Model Context Protocol)**. You'll learn how AI can autonomously execute multi-step workflows, access external systems, and operate with minimal human intervention.

From file factory to autonomous operations center.

---

## Key Takeaways

1. **Claude writes code to create files**—understand the architecture to use it effectively
2. **PowerPoint generation** produces structural drafts; apply visual polish afterward
3. **Choose the right tool**: Claude for downloadable files, Gemini for native Google integration
4. **Vibe coding** lets you describe aesthetics naturally; combine with structural precision
5. **Verify outputs**—always check critical data before distributing

---

## The Architect's Output Creed

> "Intelligence without deliverables is just conversation. Your Squadron produces artifacts that move business forward."

---

**End of Module 9 Lesson**
