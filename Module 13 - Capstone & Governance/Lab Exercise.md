# Module 11 Lab Exercise
## The Squadron Mission: Capstone Project

**Objective:** Execute a comprehensive multi-step workflow demonstrating mastery of all Squadron capabilities.

**Time:** 45-60 minutes (this is an extended capstone lab)

**Prerequisites:**
- Completion of Modules 0-10
- Access to Mission Control tool (Claude, ChatGPT, etc.)
- Access to Recon & Radar tool (Gemini, Bing AI, etc.)
- A real business challenge to address

---

## Mission Brief

You will create a **one-page strategic recommendation** for your team. This brief must:

- Address a real business challenge you face
- Be grounded in verified facts
- Include analysis (data-based or logical)
- Follow your organization's format
- Be ready for distribution

The mission has five required phases. Complete all five to demonstrate certification-level proficiency.

---

## Pre-Mission Planning (5 minutes)

### Select Your Challenge

Choose a real business challenge for your capstone. It should be:
- Something you actually need to address at work
- Complex enough to require research and analysis
- Appropriate for a one-page recommendation

**Good challenge examples:**
- Recommendation for a process improvement
- Strategic response to a market change
- Proposal for a new initiative
- Analysis of a competitive situation
- Recommendation for resource allocation

**Less suitable:**
- Simple administrative tasks
- Purely creative work without analysis
- Topics requiring extensive confidential data

**My challenge:** ________________________________________________

**Key question to answer:** ________________________________________________

---

## Phase 1: Capture (8-10 minutes)

### Task 1A: Create Source Material

Choose one capture method:

**Option A: Voice Memo**
1. Record a 2-3 minute voice memo describing:
   - The problem or opportunity
   - Key stakeholders and their concerns
   - Constraints or requirements
   - What success looks like
2. Transcribe the memo (use your phone's transcription or type key points)

**Option B: Meeting Notes**
1. Pull notes from a recent relevant meeting
2. Or write structured notes capturing the same information

### Task 1B: Structure for Mission Control

Transfer your capture to Mission Control using XML structure:

```xml
<context>
<source>[Voice memo / Meeting notes from DATE]</source>
<problem>
[Describe the challenge in 2-3 sentences]
</problem>
<stakeholders>
[Who cares about this? What are their concerns?]
</stakeholders>
<constraints>
[Budget, timeline, resource, or other limitations]
</constraints>
<success_criteria>
[How will we know if the recommendation succeeds?]
</success_criteria>
</context>

Now help me understand this challenge. What clarifying questions would you ask before developing a recommendation?
```

**Checkpoint:**
- [ ] I have source material from capture (voice/notes)
- [ ] I've structured it in XML for Mission Control
- [ ] Mission Control understands my challenge

---

## Phase 2: Research (10-12 minutes)

### Task 2A: Identify Research Needs

Based on your challenge, what facts do you need to verify or discover?

Examples:
- Current market data or competitor information
- Industry benchmarks or best practices
- Recent news or developments
- Regulatory or compliance considerations

**My research needs:**
1. ________________________________________________
2. ________________________________________________
3. ________________________________________________

### Task 2B: Execute Recon & Radar

Using Gemini or your Recon tool, research each item:

```
Research [your topic]. I need:
- Current data from 2024-2025
- Authoritative sources with citations
- Specific numbers or benchmarks where available

Focus on: [your specific research questions]
```

### Task 2C: Create Fact Brief

Compile your research into a Fact Brief:

```markdown
## Fact Brief: [Your Topic]
Generated: [Today's Date]
Sources: [Recon tool used]

### Key Facts
1. [Fact] - Source: [URL or source name]
2. [Fact] - Source: [URL or source name]
3. [Fact] - Source: [URL or source name]

### Market/Industry Context
[2-3 sentences summarizing relevant external factors]

### Gaps/Uncertainties
[What couldn't you verify? What remains unclear?]
```

**Checkpoint:**
- [ ] I've identified 3+ research needs
- [ ] I've gathered facts using Recon & Radar
- [ ] I've created a Fact Brief with citations
- [ ] I've noted any gaps or uncertainties

---

## Phase 3: Analysis (10-12 minutes)

### Task 3A: Determine Analysis Approach

Does your challenge involve quantitative data?

**If YES (data-based analysis):**
- Upload your data to Mission Control
- Use code execution for calculations
- Generate visualizations if helpful

**If NO (logical analysis):**
- Systematically compare options
- Identify and weigh pros/cons
- Apply structured decision frameworks

### Task 3B: Execute Analysis

**For data-based analysis:**

```xml
<data>
[Paste or upload your data]
</data>

<instructions>
Analyze this data to answer: [your key question]

1. Use Python to calculate relevant metrics
2. Identify key patterns or insights
3. Generate a visualization if it would clarify the findings
4. Document your methodology so I can verify

Output format: Summary of findings followed by methodology notes
</instructions>
```

**For logical analysis:**

```xml
<options>
Option A: [Description]
Option B: [Description]
Option C: [Description] (if applicable)
</options>

<criteria>
1. [Evaluation criterion 1]
2. [Evaluation criterion 2]
3. [Evaluation criterion 3]
</criteria>

<instructions>
Systematically evaluate each option against these criteria.
- Score each option on each criterion
- Identify key tradeoffs
- Recommend the best option with justification

Be balanced and identify genuine weaknesses in each option.
</instructions>
```

### Task 3C: Document Your Analysis

Record:
- **Methodology:** How did you/the AI approach this?
- **Key findings:** What did the analysis reveal?
- **Confidence level:** How certain are these conclusions?

**Checkpoint:**
- [ ] I've completed analysis (data-based or logical)
- [ ] I can explain the methodology used
- [ ] I have clear findings to support a recommendation

---

## Phase 4: Draft (8-10 minutes)

### Task 4A: Assemble Your Prompt

Create a structured prompt combining all phases:

```xml
<system_role>
You are helping me create a one-page strategic brief for [your audience - team, manager, executives].
</system_role>

<context>
[Paste your Phase 1 XML context]
</context>

<facts>
[Paste your Phase 2 Fact Brief]
</facts>

<analysis>
[Paste or summarize your Phase 3 analysis results]
</analysis>

<instructions>
Create a one-page brief that:
1. Opens with the key recommendation (bottom-line up front)
2. Provides 3-4 supporting points with evidence from the facts and analysis
3. Acknowledges 1-2 risks or limitations
4. Ends with specific, actionable next steps
5. Uses professional business tone

The recommendation should be:
- Clear and specific (not vague)
- Supported by evidence (not just opinion)
- Actionable (what should happen next)
</instructions>

<format>
- Executive brief format with headers
- No more than 500 words
- Bold key numbers and the recommendation
- Use bullet points for supporting evidence
</format>
```

### Task 4B: Generate Draft

Submit the prompt and review the output.

**Checkpoint:**
- [ ] I've assembled a complete structured prompt
- [ ] I've received a draft recommendation
- [ ] The draft addresses my original challenge

---

## Phase 5: Verify (8-10 minutes)

### Task 5A: Accuracy Check

Review the draft for accuracy:

- [ ] **Facts verified:** All factual claims match my Fact Brief sources
- [ ] **Numbers checked:** I've spot-checked 3+ data points manually
- [ ] **No hallucination:** Nothing appears that wasn't in my inputs
- [ ] **Logic sound:** Conclusions follow from evidence

**Issues found:** ________________________________________________

### Task 5B: Quality Check

Review the draft for quality:

- [ ] **Recommendation clear:** Someone can understand what to do
- [ ] **Evidence compelling:** Supporting points are strong
- [ ] **Tone appropriate:** Matches audience and context
- [ ] **Format correct:** Follows organizational standards

**Issues found:** ________________________________________________

### Task 5C: Governance Check

Review for governance compliance:

- [ ] **No Red zone data:** No credentials, API keys, or secrets
- [ ] **Yellow zone reviewed:** Any PII or sensitive content is appropriate
- [ ] **Ready to sign:** I would put my name on this

**Issues found:** ________________________________________________

### Task 5D: Red Team Check

Ask Mission Control to critique your own work:

```
Review this brief as a skeptical reader who needs to be convinced.

1. What are the strongest objections someone could raise?
2. Which evidence is weakest?
3. What assumptions might be wrong?
4. What's missing that would strengthen the argument?

Be genuinely critical—I want to improve this before sharing.
```

**Red Team findings:** ________________________________________________

### Task 5E: Revise and Finalize

Address issues from all checks:

1. Fix any accuracy errors
2. Strengthen weak points identified by Red Team
3. Adjust tone or format if needed
4. Confirm governance compliance

**Final Checkpoint:**
- [ ] All accuracy issues resolved
- [ ] Quality meets my standards
- [ ] Governance requirements satisfied
- [ ] Red Team concerns addressed
- [ ] I'm ready to use this brief

---

## Mission Debrief

### Reflection Questions

1. **Which phase was most challenging?** Why?

________________________________________________

2. **Where did AI add the most value?** What would have taken much longer without it?

________________________________________________

3. **Where did you need to intervene most?** What did the AI get wrong or miss?

________________________________________________

4. **How confident are you in the final output?** Would you share it as-is?

________________________________________________

5. **What would you do differently next time?**

________________________________________________

---

## Certification Checklist

Confirm you demonstrated each competency:

**Phase 1 (Capture):**
- [ ] Used voice or meeting notes as source material
- [ ] Structured context using XML tags
- [ ] Successfully briefed Mission Control

**Phase 2 (Research):**
- [ ] Identified research needs
- [ ] Used Recon & Radar for external information
- [ ] Created a Fact Brief with citations

**Phase 3 (Analysis):**
- [ ] Conducted systematic analysis (data or logical)
- [ ] Can explain methodology
- [ ] Generated actionable insights

**Phase 4 (Draft):**
- [ ] Assembled a complete structured prompt
- [ ] Generated a one-page recommendation
- [ ] Output addresses the original challenge

**Phase 5 (Verify):**
- [ ] Completed accuracy checks
- [ ] Completed quality checks
- [ ] Completed governance checks
- [ ] Executed Red Team review
- [ ] Produced final verified output

**If all boxes checked: Capstone complete. Congratulations, Squadron Leader!**

---

## Submission (Optional)

If your organization tracks certifications, save:
- Your final one-page brief
- This completed lab exercise
- Screenshots of key workflow steps (optional)

---

**End of Lab Exercise**
