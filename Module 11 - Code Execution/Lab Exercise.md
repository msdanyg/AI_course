# Module 9 Lab Exercise
## Building Mission-Ready Deliverables

**Objective:** Practice creating downloadable files using Claude's code execution and Gemini's native Google integration.

**Time:** 25-30 minutes (Core Lab) | +15 minutes (Advanced Credit)

**Prerequisites:**
- Claude account with code execution enabled
- Gemini account with Google Workspace access
- Sample data or willingness to use provided examples

---

## Part 1: PowerPoint Generation with Claude (10 minutes)

### Scenario

You're preparing for a customer check-in meeting tomorrow. You need a professional slide deck to guide the conversation.

### Task 1A: Create Your Presentation Prompt

Choose one of the following scenarios (or use your own real situation):

**Option A: Customer QBR**
```
Create a 6-slide PowerPoint presentation for a Quarterly Business Review.

Slide 1: Title
- Title: "Q3 Business Review"
- Subtitle: "[Customer Name] Partnership Update"

Slide 2: Agenda
- Adoption Metrics
- Key Wins This Quarter
- Challenges Addressed
- Q4 Roadmap Preview

Slide 3: Adoption Metrics
- Active users: [X] (up X% from Q2)
- Daily engagement rate: [X]%
- Features adopted: [X] of [Y] available

Slide 4: Key Wins
- [Win 1]
- [Win 2]
- [Win 3]

Slide 5: Challenges & Solutions
- Challenge: [Describe]
- Solution: [How we addressed it]

Slide 6: Next Steps
- Q4 focus areas
- Upcoming milestones
- Action items

Use title-and-content layouts. Include speaker notes for each slide summarizing key talking points.
```

**Option B: Internal Team Update**
```
Create a 5-slide PowerPoint for a weekly team meeting.

Slide 1: Title
- "Week of [Date] - Team Update"

Slide 2: Last Week's Accomplishments
- [3-4 bullet points]

Slide 3: This Week's Priorities
- [3-4 bullet points with owners]

Slide 4: Blockers & Needs
- [Any issues requiring attention]

Slide 5: Reminders
- [Upcoming deadlines, meetings, etc.]

Keep it scannable. Include speaker notes with context.
```

### Task 1B: Generate the File

1. Open Claude Desktop or claude.ai
2. Paste your customized prompt (fill in the bracketed values with real or sample data)
3. Wait for Claude to generate the file
4. Click the download button when it appears

### Task 1C: Review and Evaluate

Open the downloaded .pptx file in PowerPoint or Google Slides.

**Evaluation Checklist:**
- [ ] Correct number of slides?
- [ ] Content matches your specifications?
- [ ] Speaker notes included?
- [ ] Logical flow and structure?

**Note what's missing:** Visual polish—this is expected. Claude produces structural drafts.

**Deliverable:** Screenshot of your generated presentation (at least the title slide and one content slide)

---

## Part 2: Google Slides via Gemini (8 minutes)

### Scenario

You need a quick presentation for an internal sync. You want it directly in Google Drive without file downloads.

### Task 2A: Create with Gemini Canvas

1. Go to [gemini.google.com](https://gemini.google.com)
2. Ensure you're logged into your work Google account
3. Enter this prompt (customize as needed):

```
Create a 4-slide presentation for an internal team sync.

Topic: Project Status Update

Slide 1: Title - "Project [Name] Status Update"
Slide 2: Progress Summary - What we've completed
Slide 3: Current Focus - What we're working on now
Slide 4: Next Steps - Upcoming milestones and deadlines

Keep slides clean and visual. Use a professional blue theme.
```

### Task 2B: Export to Google Slides

1. Review the generated slides in Gemini's interface
2. Click "Export to Google Slides"
3. Open the presentation in your Google Drive

### Task 2C: Compare the Experience

Answer these questions:

| Aspect | Claude | Gemini |
|--------|--------|--------|
| Time to deliverable | | |
| Control over structure | | |
| Visual quality | | |
| Ease of iteration | | |
| Best for... | | |

**Deliverable:** Link to your Google Slides presentation (share with view access)

---

## Part 3: CSV Data Export (7 minutes)

### Scenario

You need to create a clean data export for stakeholders or system integration.

### Task 3A: Choose Your Data Scenario

**Option A: Create Sample Data**
```
Create a CSV file with sample customer engagement data:

Columns:
- Customer_ID
- Company_Name
- Industry
- Active_Users
- Engagement_Score (0-100)
- Last_Login_Date
- Subscription_Tier (Basic, Professional, Enterprise)

Include 15 rows of realistic sample data.
Sort by Engagement_Score descending.
```

**Option B: Transform Existing Data**

If you have a messy spreadsheet or data file:
```
[Upload your file]

Clean this data:
1. Standardize date formats to YYYY-MM-DD
2. Remove any duplicate rows
3. Fill empty [Column] values with "Not Specified"
4. Sort by [Column] ascending
5. Export as a clean CSV
```

### Task 3B: Generate and Download

1. Enter your prompt in Claude
2. If using Option B, upload your file first
3. Download the generated CSV

### Task 3C: Verify the Output

Open the CSV in Excel or Google Sheets.

**Verification Checklist:**
- [ ] Correct columns present?
- [ ] Data formatted as specified?
- [ ] Sorting applied correctly?
- [ ] No obvious errors or inconsistencies?

**Deliverable:** Screenshot showing your CSV open in a spreadsheet application

---

## Part 4: Vibe Coding Practice (5 minutes)

### Task 4A: Compare Prompt Styles

Create the same output with two different prompting approaches.

**Technical Prompt:**
```
Create a 3-slide presentation.
Slide 1: Title with 32pt bold font
Slide 2: 4 bullet points, 18pt font
Slide 3: Summary with centered text
Use color #0056D2 for headers.
```

**Vibe Prompt:**
```
Create a 3-slide presentation about team goals.
Make it feel modern and confident—like something
a tech startup would present to investors.
Clean design, minimal text, emphasis on clarity.
The vibe should say "we know what we're doing."
```

### Task 4B: Generate Both

Run both prompts and download the results.

### Task 4C: Evaluate

Which output better matches what you'd actually use? Why?

**Reflection Questions:**
1. What did vibe coding capture that technical specs missed?
2. What did technical specs control that vibe coding left ambiguous?
3. How would you combine both approaches?

**Deliverable:** One sentence describing your preferred prompting strategy

---

## Lab Completion Checklist

Core deliverables:

- [ ] PowerPoint generated via Claude (Part 1)
- [ ] Google Slides created via Gemini with share link (Part 2)
- [ ] CSV export generated and verified (Part 3)
- [ ] Vibe coding reflection completed (Part 4)

---

## Advanced Credit: Integrated Workflow (+15 minutes)

### Scenario

Create an end-to-end workflow that goes from raw data to polished deliverable.

### The Challenge

You have customer usage data and need to:
1. Analyze it for insights
2. Create a summary CSV for the data team
3. Generate a presentation for the executive review

### Step 1: Upload and Analyze

Use this sample prompt (or your own data):

```
[Upload customer usage CSV or describe the data]

Analyze this customer usage data:
1. Calculate average engagement score by industry
2. Identify the top 5 customers by active users
3. Find any customers with engagement below 50%
4. Calculate month-over-month growth trends
```

### Step 2: Generate Summary CSV

```
Based on this analysis, create a summary CSV with:
- One row per industry
- Columns: Industry, Avg_Engagement, Customer_Count, Total_Active_Users
- Sort by Avg_Engagement descending
- Include a "Total" row at the bottom
```

### Step 3: Generate Executive Presentation

```
Now create a 5-slide executive presentation summarizing these findings:

Slide 1: Title - "Customer Engagement Analysis"
Slide 2: Key Metrics Overview
Slide 3: Industry Breakdown (reference the data)
Slide 4: At-Risk Customers Requiring Attention
Slide 5: Recommended Actions

Make it executive-ready: clean, data-driven, actionable.
Include speaker notes with the supporting details.
```

### Step 4: Document Your Workflow

```
INTEGRATED WORKFLOW: [Name]

DATA SOURCE: [What you uploaded/used]

ANALYSIS PERFORMED:
- [List key analyses]

OUTPUTS GENERATED:
1. Summary CSV: [Description]
2. Executive Presentation: [Slide count, key content]

TIME INVESTED: [Total minutes]

COMPARED TO MANUAL APPROACH: [Estimated time savings]
```

### Advanced Deliverables

- [ ] Summary CSV downloaded and verified
- [ ] Executive presentation downloaded
- [ ] Workflow documentation completed
- [ ] Reflection on time saved vs. manual approach

---

## Troubleshooting

**Problem:** Claude doesn't generate a downloadable file
- **Solution:** Ensure code execution is enabled. Rephrase to explicitly request "Create a downloadable [file type] file"

**Problem:** PowerPoint has no content on slides
- **Solution:** Be more specific about what goes on each slide. Claude needs content, not just structure.

**Problem:** CSV has wrong formatting
- **Solution:** Specify exact column names, data types, and sort order. Review and iterate.

**Problem:** Gemini won't export to Slides
- **Solution:** Ensure you're logged into a Google Workspace account. Try refreshing and re-generating.

**Problem:** Generated file won't open
- **Solution:** Check file extension. Try opening in a different application (Google Slides for .pptx, Google Sheets for .csv).

---

## Reflection Questions

After completing the lab:

1. Which file type was most valuable for your actual work?
2. Where did Claude's output exceed expectations? Where did it fall short?
3. How will you incorporate the "structural draft" workflow into your routine?
4. What's one deliverable you create regularly that this could automate?

**Save your reflections—they'll inform how you apply these skills in your role.**

---

**Lab Complete. Proceed to Quiz when ready.**
