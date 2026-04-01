# Module 7 Lab Exercise
## The Hybrid Agent: Building Cross-Platform Workflows

**Objective:** Practice capturing, syncing, processing, and delivering intelligence across mobile, Mac, and Google Workspace environments.

**Time:** 25-30 minutes

**Prerequisites:**
- Claude account (desktop and mobile)
- Google Workspace access (Docs, Slides)
- Apple device with Notes app (iPhone/iPad) OR ability to simulate voice capture

---

## Part 1: The Ramble-to-Gold Workflow (8-10 minutes)

### Setup

You're preparing for a client meeting with "Acme Healthcare." They're concerned about nurse burnout and high turnover. You need to draft talking points.

### Task 1A: Capture (Voice or Text Simulation)

**If you have iPhone/mobile device:**
1. Open Claude mobile app
2. Use voice input to record this thought (speak it naturally):

"Okay so for Acme Healthcare tomorrow, I think the angle is nurse burnout causing turnover which costs them millions. We should lead with their pain point not our features. Open with the stat about healthcare turnover costing 5 million per 100 nurses. Then show how our workload balance reports can identify teams at risk before people quit. The demo should focus on their specific metrics—show them what their current data would look like in our dashboard, don't just show generic screenshots."

**If you don't have mobile/prefer text:**
1. Open Claude Desktop
2. Simulate a "voice ramble" by typing this conversationally (with the imperfect grammar):

"okay so acme healthcare meeting tomorrow, thinking we lead with burnout → turnover problem not feature list. that stat about 5M per 100 nurses. workload balance reports spot at-risk teams early. demo should use THEIR metrics not generic screenshots so it feels real for them."

### Task 1B: Process the Ramble

Create a new Claude conversation (Desktop) and use this prompt:

```xml
<role>You are my Chief of Staff, helping transform rough thoughts into polished meeting prep.</role>

<raw_capture>
[Paste your voice ramble or rough text here]
</raw_capture>

<context>This is for a client meeting with Acme Healthcare, a 500-bed hospital system concerned about nursing turnover.</context>

<task>
1. Extract the core strategic insights
2. Structure these into 5-7 clear talking points
3. Identify any gaps (data needs, questions to ask them)
4. Format as a one-page meeting brief
</task>

<constraints>
- Use "insights" and "workforce analytics" language
- Avoid "monitoring" or "tracking" terminology
- Keep it consultative, not sales-y
- Include a "Questions to Ask Them" section
</constraints>
```

**Expected Output:** A structured meeting brief with:
- Opening angle
- Key talking points
- Demo approach
- Questions to ask
- Data gaps to address

**Deliverable for Part 1:** Copy your meeting brief and paste into a new note (Apple Notes or text file) titled "Lab - Meeting Brief."

---

## Part 2: The HTML Bridge (5-7 minutes)

### Task 2A: Create a Comparison Table

Continue in Claude Desktop. Prompt:

```
Create a comparison table for the Acme Healthcare meeting:

COMPARISON: ActivTrak vs. "Manual Time Tracking" (their current approach)

DIMENSIONS:
- Real-time visibility
- Burnout risk detection
- Privacy & compliance
- Time to insight

Format as an HTML table. Requirements:
- Use inline CSS
- border-collapse: collapse
- border: 1px solid #333
- Header row: background-color: #f0f0f0; font-weight: bold
- Render the table directly (do not show me code in a block)

In the comparison, emphasize ActivTrak's advantages while being fair about their manual approach limitations.
```

### Task 2B: Test the HTML Bridge

1. Claude will generate a visual HTML table
2. Click inside the rendered table
3. Select all cells (Cmd+A or drag to select)
4. Copy (Cmd+C)
5. Open a new Google Doc: [Create here](https://docs.google.com/document/create)
6. Paste (Cmd+V)

**Success Check:**
- Does the table have visible borders?
- Is the header row shaded gray?
- Are the cells properly formatted?

If yes: You've mastered the HTML Bridge.
If no: Check that you copied the *rendered* table, not the code.

**Deliverable for Part 2:** Screenshot or share link to your Google Doc showing the properly formatted table.

---

## Part 3: Mobile-to-Desktop Workflow (5-7 minutes)

### Scenario

You're reviewing a competitor's website on your phone during lunch. You need to capture intelligence for later analysis.

### Task 3A: Simulate Mobile Capture

**If you have Claude mobile:**
1. Go to a competitor website (use Hubstaff.com as example)
2. Take a screenshot
3. Open Claude mobile
4. Upload screenshot
5. Voice prompt or type: "Analyze the positioning and value prop in this screenshot. What are they emphasizing? How does it compare to ActivTrak's 'Insights, Not Oversight' approach?"

**If desktop only:**
1. Go to Hubstaff.com on your Mac
2. Take screenshot (Cmd+Shift+4)
3. Drag directly into Claude Desktop
4. Same prompt as above

### Task 3B: Create Competitive Brief

Claude will provide analysis. Continue the conversation:

```
Based on this analysis, create a "Competitive Quick Ref" that includes:
1. Their core value prop (1 sentence)
2. Where they're vulnerable (2-3 points)
3. How we position against them (talking points)

Format as a brief I can reference during a competitive deal.
```

**Expected Output:** A concise competitive reference.

**Deliverable for Part 3:** Copy the competitive brief into your notes collection.

---

## Part 4: Google Workspace Integration (5-7 minutes)

### Task 4A: Research Brief with Gemini

1. Open Gemini: [gemini.google.com](https://gemini.google.com)
2. Prompt:

```
I need to research nurse burnout statistics for a healthcare client meeting. Please find:

1. Current average turnover rate for nurses in the US
2. Estimated cost per nurse turnover
3. Top 3 cited reasons for nurse burnout
4. Any recent studies (2023-2024) on workload and burnout correlation

Provide as a Fact Brief with source links.
```

3. Use Gemini's "Double Check" feature (if available)
4. Copy the Fact Brief

### Task 4B: Create a Micro-Presentation

While still in Gemini:

```
Create a 5-slide presentation based on this research about nurse burnout:

[Paste the Fact Brief]

Slides should cover:
1. Title: "The Nurse Burnout Crisis"
2. The Problem (statistics)
3. Root Causes
4. Business Impact
5. Path Forward (general, not product-specific)

Use a professional, healthcare-appropriate tone.
```

If Gemini offers "Export to Google Slides," click it.

If not, copy the structured content and create a simple slide deck manually.

**Deliverable for Part 4:** Share link to the Google Slides deck (even if rough).

---

## Part 5: The Complete Workflow Integration (5 minutes)

### Task 5: Synthesize Everything

Now combine all your work into a final brief for the Acme Healthcare meeting.

In Claude Desktop:

```xml
<role>Executive briefing specialist</role>

<context>I'm meeting with Acme Healthcare tomorrow about workforce analytics for nursing teams.</context>

<materials>
<meeting_brief>
[Paste your meeting brief from Part 1]
</meeting_brief>

<competitive_intel>
[Paste your Hubstaff analysis from Part 3]
</competitive_intel>

<research_data>
[Paste Gemini's Fact Brief from Part 4]
</research_data>
</materials>

<task>Create a comprehensive one-page executive brief that integrates all three sources. Structure:
- Meeting Objective
- Key Statistics (from research)
- Our Strategic Approach
- Competitive Context
- Questions to Ask
- Success Metrics for This Meeting
</task>

<format>Output as clean HTML that I can paste into Google Docs.</format>
```

### Final Step

1. Copy the HTML output Claude generates
2. Paste into a new Google Doc
3. Title it: "Acme Healthcare Meeting Brief - [Today's Date]"
4. Share with view access

**Deliverable for Part 5:** Share link to your final comprehensive brief in Google Docs.

---

## Stretch Goals (Optional, +10 minutes)

### Stretch 1: Build a Custom Shortcut

If on Mac/iOS, create an Apple Shortcut that:
1. Takes selected text
2. Appends to a note called "Daily Squadron Intel"
3. Adds timestamp

Test it by highlighting text and running the shortcut.

### Stretch 2: Voice-to-Brief Speed Run

Time yourself:
1. Record a 60-second voice memo about any work topic
2. Process it with Claude to create a structured brief
3. Export to Google Docs with formatting

**Goal: Under 5 minutes from voice to formatted doc.**

### Stretch 3: Multi-Device Context Test

Start a conversation on mobile, continue on desktop, reference back on mobile—all in the same chat thread. Verify context persists across all three interactions.

---

## Lab Completion Checklist

Submit or save these deliverables:

- [ ] Meeting brief from Ramble-to-Gold (Part 1)
- [ ] Google Doc with properly formatted HTML table (Part 2)
- [ ] Competitive analysis brief (Part 3)
- [ ] Gemini research brief or slides link (Part 4)
- [ ] Final integrated executive brief in Google Docs (Part 5)

**Bonus:**
- [ ] Completed at least one stretch goal

---

## Troubleshooting

**Problem:** HTML table doesn't paste correctly into Google Docs
- **Solution:** Ensure you copied the *rendered* table (the visual output), not the code block. Try again, selecting only the visual table cells.

**Problem:** Voice input not working on Claude mobile
- **Solution:** Check microphone permissions in iOS Settings > Claude. Alternatively, use text input to simulate voice capture.

**Problem:** Gemini can't export to Slides
- **Solution:** Copy the structured outline and manually create 5 slides in Google Slides. The learning is in the workflow, not the automation.

**Problem:** Don't have mobile device
- **Solution:** All tasks can be completed on desktop by simulating mobile workflows (screenshots, text instead of voice).

---

## Reflection Questions (Post-Lab)

1. Which workflow felt most useful for your actual job?
2. Where did you encounter the most friction?
3. How would you modify these workflows for your specific role at ActivTrak?
4. Which tool (Claude mobile/desktop, Gemini, Docs) felt most natural for which task?

**Save your reflections—you'll use them in Module 8 to design your personal Squadron system.**

---

**Lab Complete. Proceed to Quiz when ready.**
