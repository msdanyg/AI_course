# Module 8 Lab Exercise
## Build Your First Mission Card: The Gmail Action Item Extractor

**Objective:** Build a working Claude Skill that scans your Gmail, isolates messages from internal teammates and ActivTrak senders, extracts action items, and returns a prioritized to-do list. By the end of this lab, you will have one Mission Card in your Squadron Playbook and the diagnostic framework to debug any future skill.

**Time:** 25–30 minutes

**Prerequisites:**
- Claude with the Gmail connector installed and authorized
- The `skill-creator` skill installed (covered in Part 1)
- At least one week of recent emails in your inbox to test against
- A note-taking app or paper for the design phase

---

## Part 1: Feel the Loop (4 minutes)

Before you build, you need to experience how someone else's skill behaves end-to-end. This grounds everything that follows.

### Task 1A: Browse the catalog

Open the Skill catalog inside Claude. Scan ten skills. Read their descriptions, not their names. Notice the patterns:

- Good descriptions list ACTUAL phrases users say
- Good descriptions are written in third person ("Use when the user asks to...")
- Bad descriptions read like marketing copy ("This powerful skill helps with...")

### Task 1B: Install your first skill

Pick one skill that maps to your real work. Suggested options if you are unsure:

- `skill-creator` — the official Skill Builder (you will need this in Part 3, so this is a safe bet)
- A research skill if you do competitive intelligence
- A writing skill if you draft a lot of customer-facing content

Install it.

### Task 1C: Trigger it twice

Trigger the skill in two different ways:

**Auto-invocation test:** type a natural sentence that matches the description. Do NOT mention the skill by name. Watch what happens.

**Manual invocation test:** explicitly tell Claude to use the skill by name. Compare the output.

### Reflection (write down)

- Did the skill auto-fire on your first natural sentence? If not, what did the description NOT match?
- Did the manual output differ from the auto-fired output? Why might that be?

**Deliverable:** One sentence describing the install/trigger experience, plus one observation about how the description controlled (or failed to control) firing behavior.

---

## Part 2: Design on Paper (5 minutes)

Stop. Before you open Skill Builder, design your Gmail skill the old-fashioned way. Skills built without a paper design produce vague descriptions and bloated steps.

Fill in the worksheet below.

### Worksheet

**Skill name** (gerund-form, lowercase, hyphenated):
```
extracting-gmail-action-items
```
*(Or your preferred variation. Keep the gerund pattern.)*

**Description draft** (third person, list 3–5 actual user phrases):
```
Use when the user asks to:
- "summarize my inbox"
- "find action items from this week's emails"
- "what do I owe people"
- "pull my to-do list from email"
- "what's outstanding in Gmail"

The skill searches Gmail via the connector, filters for messages from internal teammates and ActivTrak senders, extracts action items with deadlines and priorities, and returns a structured to-do list.
```

**Inputs to the skill** (what configurable parameters does it accept?):
```
- Time range (default: last 7 days; user can override with "this month," "today," etc.)
- Sender filter (default: internal + ActivTrak; user can narrow to one)
- Label filter (optional: only emails with specific labels)
```

**Output template** (literal, not described):
```
## Action Items from Gmail (Last 7 Days)

| Sender | Subject | Action | Due | Priority |
|--------|---------|--------|-----|----------|
| Chris Michael | Q3 launch deck | Review draft section 3 | Friday | High |
| Rebekah Weber | Academy module review | Send feedback on quiz | Today | Medium |

**Total open items:** 6
**Overdue:** 1
**Due this week:** 4
```

**Gotcha section** (failure patterns you can predict):
```
- Marketing emails contain action verbs ("Click to learn more") that are NOT real action items. Ignore senders matching marketing domains.
- Calendar invites are NOT action items unless the body explicitly asks the user to do something (e.g., "please prepare slides before").
- Automated notifications from Jira, Monday, GitHub, etc., usually surface noise, not work the user owes another human. Exclude unless explicitly requested.
- "FYI" and "no action needed" messages should be skipped even if they contain verbs.
- Internal forwards (someone forwarding a customer email) should be evaluated based on the original sender's intent, not the forwarder's.
```

**Constraints** (rules specific to this skill):
```
- Never include emails older than 30 days
- Never surface a personal/private email even if it contains action items
- If fewer than 3 items are found, ask the user if they want to expand the time range
```

**Deliverable:** Completed paper worksheet (text or handwritten — both work).

---

## Part 3: Build with Skill Builder (10 minutes)

Now you bring the paper design into Claude.

### Task 3A: Invoke Skill Builder

In a fresh Claude conversation, type:

```
I want to build a skill that extracts action items from my Gmail.
It should filter for messages from internal teammates and ActivTrak senders,
extract real action items (not marketing or notifications),
and return a structured to-do list with sender, subject, action, due date, and priority.
```

Skill Builder should auto-fire. If it does not, type `/skill-creator` to invoke it manually. Note this — manual invocation when auto should have fired is itself a Killer 1 symptom on the Skill Builder description, not on you.

### Task 3B: Walk the conversation

Skill Builder will ask you clarifying questions. Use your paper worksheet to answer fast and consistently. Specifically:

- When asked for the description, paste in your phrase list from the worksheet
- When asked for steps, give it the input/filter/extract/output flow
- When asked for the output format, paste the literal table template
- When asked for gotchas, paste your failure patterns

Do not let Skill Builder write the gotcha section for you. Skill Builder has not lived your work. The gotcha section is where YOUR judgment lands.

### Task 3C: Review the generated SKILL.md

Skill Builder will produce a draft `SKILL.md` file. Read it carefully. Run this checklist:

- [ ] Is the description in third person?
- [ ] Does the description list the actual phrases your users say?
- [ ] Are the steps numbered (not prose)?
- [ ] Is the output format a literal template (not a description of one)?
- [ ] Is the gotcha section present and specific?
- [ ] Is the file under 500 lines?

Edit anything that fails the checklist. Save the skill.

**Deliverable:** Final `SKILL.md` content (paste into your lab notes).

---

## Part 4: Test Against Real Gmail (5 minutes)

Now you fly the skill.

### Task 4A: Run three test queries

In a fresh Claude conversation (no project, no special setup), run all three of these as natural sentences:

**Test 1 (auto-trigger test):**
```
What do I owe people from this week?
```

**Test 2 (specific time range):**
```
Pull my action items from the last 3 days.
```

**Test 3 (edge case):**
```
What's outstanding in my inbox right now?
```

For each test, record:

| Test | Did it auto-fire? | Was the output structured correctly? | Did it filter out marketing/automated? | Misses or false positives? |
|------|-------------------|--------------------------------------|----------------------------------------|----------------------------|
| 1 | Yes / No | Yes / Partial / No | Yes / No | |
| 2 | Yes / No | Yes / Partial / No | Yes / No | |
| 3 | Yes / No | Yes / Partial / No | Yes / No | |

### Task 4B: Note the failures

Look at every "No" or "Partial." Write a one-line description of each failure.

**Deliverable:** Test results table plus failure notes.

---

## Part 5: Apply the Five Killers Framework (5 minutes)

Failures are not failures. They are diagnostic signals. For each failure you noted in Part 4, identify which Killer applies and apply the fix.

### The diagnostic table

| Symptom | Killer | Fix |
|---------|--------|-----|
| Skill did not auto-fire on the natural sentence | Killer 1: Vague description | Add the exact phrase you said to the description's trigger list |
| Skill fired but output was robotic / off-format on edge cases | Killer 2: Over-defined process | Loosen the relevant step. Match degrees of freedom to the actual task variance |
| Skill output included things Claude already does (e.g., generic email summary) | Killer 3: Stating the obvious | Cut the step. Claude does that natively |
| Skill returned marketing emails or calendar invites as action items | Killer 4: Missing gotcha | Add the specific failure pattern to the gotcha section |
| Skill file feels bloated, Claude is skipping sections | Killer 5: Monolithic | Split content into companion files; reference them from SKILL.md |

### Task 5A: Diagnose

For each failure from Part 4, identify the Killer and the fix in your lab notes.

### Task 5B: Apply ONE fix

Pick the most impactful failure. Apply the fix to your `SKILL.md`. Re-run the failed test. Did the fix work?

### Task 5C: The Litmus Test

Ask yourself: did you, at any point in testing, find yourself manually cleaning up Claude's output AFTER the skill ran? If yes, the skill is not done. The cleanup belongs INSIDE the skill. Make a note of what to add next.

**Deliverable:** Diagnostic table + one applied fix + litmus-test answer.

---

## Lab Completion Checklist

Submit or save these deliverables:

- [ ] Part 1: Install/trigger experience notes
- [ ] Part 2: Completed paper worksheet
- [ ] Part 3: Final `SKILL.md` content (with Skill Builder review checklist passed)
- [ ] Part 4: Test results table with failure notes
- [ ] Part 5: Diagnostic table + applied fix + litmus-test answer

---

## Stretch Goals (Optional, +15 minutes)

### Stretch 1: Build a second skill

Now that you have the loop, build a second skill targeting a different recurring task. Some good candidates from ActivTrak workflows:

- A skill that drafts QBR prep briefs from CRM context
- A skill that converts a customer support ticket into an internal escalation note
- A skill that audits a piece of writing against the ActivTrak terminology rules ("users" not "customers," no Oxford comma, etc.)

### Stretch 2: Refactor for the 500-line rule

If your Gmail skill is approaching 500 lines, split it. Move the gotcha section into a companion file `gotchas.md`. Reference it from SKILL.md. Confirm Claude still respects the gotchas after the split.

### Stretch 3: Share with a teammate

If your team uses Claude, share your skill via the appropriate sharing mechanism (plugin, copy/paste, internal repo). Watch one teammate use it. What did THEY find that you missed?

---

## Reflection Questions (Post-Lab)

Spend three minutes on these. They are the most valuable part of the lab.

1. **Capability vs. Preference:** Was your Gmail skill mostly capability uplift or encoded preference? Why? If it was capability uplift, what part could become obsolete in six months as Claude's email handling improves?

2. **Description failure:** Which Killer surprised you the most? If the answer is Killer 1 (vague description), you are not alone — almost everyone underweights the description on their first skill.

3. **The next Mission Card:** Walk through your work week mentally. Which task do you do at least three times a week, where you find yourself rebuilding the same context every time? That task is your next skill. Write the name and description down now, before the energy fades.

4. **The Litmus Test, applied broadly:** Look back at your last five Claude conversations OUTSIDE this lab. In how many of them did you clean up the output afterward? Each one is a candidate for skill encoding.

**Save your reflections — they inform what you build next, and they are the seed of your full Squadron Playbook.**

---

## Troubleshooting

**Problem:** Gmail connector not authorizing
- **Solution:** Disconnect and reconnect from Settings → Connectors. If using SSO, ensure your Google account has the relevant scopes enabled. ActivTrak admin may need to whitelist the connector.

**Problem:** Skill Builder asks too many clarifying questions and never produces the SKILL.md
- **Solution:** Skill Builder is calibrated for first-time users who give vague answers. Paste your full paper worksheet at the start of the conversation. Tell it explicitly: "I have a complete design. Generate the SKILL.md and I will refine."

**Problem:** Skill fires on EVERYTHING (over-triggering)
- **Solution:** This is the inverse of Killer 1. The description is too broad. Tighten it. Remove generic phrases like "any email task." Keep ONLY phrases that should fire the skill.

**Problem:** Output table renders as raw markdown in the chat
- **Solution:** Add a constraint to the skill: "Always render the output table using Claude's native table rendering, not raw markdown."

**Problem:** Skill works in a fresh chat but not inside a project
- **Solution:** Confirm the skill is installed at the user level, not the project level. Skills should live above projects in the hierarchy. If it is project-scoped, reinstall at user scope.

---

**Lab Complete. Proceed to the Quiz when ready.**
