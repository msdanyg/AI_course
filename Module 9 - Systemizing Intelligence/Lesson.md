# Module 8: Systemizing Intelligence
## Projects, Skills, Gems & Custom GPTs

---

## Introduction: From Squadron Leader to Squadron Architect

You've spent seven modules learning to fly. You can capture intelligence on mobile, process it with Claude's reasoning engine, verify facts with Gemini's grounding, and deliver polished outputs to Google Workspace. You've mastered the tools.

But here's the uncomfortable truth: **you're still doing everything manually.**

Every time you start a new conversation, you're rebuilding context from scratch. Every time you need your competitive analysis framework, you're re-explaining it. Every time you want Claude to understand your role, your company, your preferences—you're typing the same instructions again.

This is like being an excellent pilot who builds a new cockpit before every flight.

Module 8 changes that. You're about to become a **Squadron Architect**—someone who builds persistent, reusable systems that work for you even when you're not actively prompting.

**The shift:** From giving instructions to building infrastructure.

---

## The Problem: Contextual Amnesia

Every AI conversation starts with a blank slate. Claude doesn't remember your last conversation. It doesn't know you prefer bullet points over paragraphs, that you work at ActivTrak, or that your competitive analysis should always include Teramind, Hubstaff, and Insightful.

This creates three problems:

1. **Repetition tax**: You spend the first 2-3 exchanges of every conversation re-establishing context
2. **Consistency drift**: Without persistent instructions, outputs vary based on how you happened to phrase things that day
3. **Expertise ceiling**: You can't build on previous work—every conversation starts at zero

The solution? **Persistent context systems**—tools that maintain knowledge, instructions, and specialized behaviors across sessions.

---

## The Three Pillars of Persistent Intelligence

Each AI platform offers its own approach to solving contextual amnesia:

| Platform | Persistence Tool | Best For |
|----------|-----------------|----------|
| Claude | Projects | Deep work requiring extensive context |
| Claude | Skills | Reusable prompt templates |
| Gemini | Gems | Research workflows with Google integration |
| ChatGPT | Custom GPTs | Shareable specialized assistants |

Let's examine each in detail.

---

## Pillar 1: Claude Projects — Your Mission Archives

### What Projects Are

A Claude Project is a persistent workspace that maintains:
- **Custom instructions**: How Claude should behave in this context
- **Knowledge files**: Documents Claude can reference (PDFs, CSVs, text files)
- **Conversation history**: Past chats that inform future responses

Think of it as giving Claude a dedicated office for a specific mission, complete with filing cabinets, reference materials, and standing orders.

### The Anatomy of a Well-Built Project

**Project Name**: Clear, specific, action-oriented
- ✅ "Q4 Competitive Intelligence"
- ✅ "Customer Success QBR Prep"
- ❌ "Work Stuff"
- ❌ "Research"

**Custom Instructions**: The persistent prompt that shapes all conversations
```
You are my competitive intelligence analyst for ActivTrak.

CONTEXT:
- I'm Senior Director of Product Marketing
- Our key competitors: Teramind, Hubstaff, Insightful, Time Doctor
- Our positioning: "Insights, Not Oversight"

BEHAVIOR:
- Always structure analysis as: Strengths | Weaknesses | Our Counter
- Flag any claims that need verification with [VERIFY]
- Use "users" not "customers" when referring to end-users

OUTPUT PREFERENCES:
- Lead with the strategic insight, then supporting evidence
- Use tables for comparisons
- Include "So What?" section explaining business implications
```

**Knowledge Files**: Upload relevant documents
- Competitive battle cards
- Product documentation
- Previous analyses
- Industry reports

### When to Create a New Project

Create a project when:
- You'll have **5+ conversations** on the same topic
- You need **consistent context** across sessions
- You have **reference documents** Claude should access
- The work requires **specialized behavior** (tone, format, terminology)

Don't create a project for:
- One-off questions
- Quick research tasks
- Experiments and exploration

### Project Architecture Patterns

**Pattern 1: The Client Hub**
One project per major client or account, containing:
- Account history and key contacts
- Previous meeting notes and QBRs
- Product configuration details
- Communication preferences

**Pattern 2: The Workflow Station**
One project per recurring workflow:
- "Weekly Competitive Roundup"
- "Customer Escalation Triage"
- "Content Review & Editing"

**Pattern 3: The Knowledge Base**
Centralized reference projects:
- "ActivTrak Product Knowledge"
- "Industry Terminology & Standards"
- "Brand Voice & Style Guide"

---

## Pillar 2: Claude Skills — Your Mission Cards

### What Skills Are

Skills are reusable prompt templates that you can invoke with a simple command. They're like pre-built mission cards—standardized procedures for common operations.

While Projects provide persistent context, Skills provide **portable methodology**.

### Creating Effective Skills

A Skill consists of:
1. **A clear trigger phrase** (how you'll invoke it)
2. **Structured instructions** (what Claude should do)
3. **Input placeholders** (where your specific content goes)
4. **Output format** (how results should be structured)

**Example Skill: Competitive Quick Analysis**
```
When I say "Quick comp on [COMPANY]", perform this analysis:

1. POSITIONING: Their core value proposition in one sentence
2. STRENGTHS: Top 3 competitive advantages
3. WEAKNESSES: Top 3 vulnerabilities we can exploit
4. COUNTER: How ActivTrak positions against each weakness
5. VERIFY: List any claims that need fact-checking

Format as a table I can paste into Slack.
```

**Example Skill: Meeting Prep Brief**
```
When I say "Prep me for [MEETING/CLIENT]", create:

1. CONTEXT REFRESH: Key facts about this client/topic
2. RECENT HISTORY: Last 2-3 relevant interactions
3. THEIR PRIORITIES: What they care about most
4. OUR OBJECTIVES: What we want to accomplish
5. WATCH OUTS: Potential landmines or sensitivities
6. QUESTIONS TO ASK: 3-5 strategic questions

Keep it to one page. Use bullet points.
```

**Example Skill: Brand Guidelines Application**
```
When I say "Apply brand to [CONTENT]", review and revise the content to follow ActivTrak brand guidelines:

TERMINOLOGY:
- Use "users" or "accounts" (never "customers" for end users)
- Use "flexible hours schedules" and "schedule adherence" (not "flex work")
- Use "Productivity Optimization" (not "Performance Optimization")

TONE:
- Lead with business outcomes, not features
- Emphasize "Insights, Not Oversight" philosophy
- Balance technical detail with accessibility

FORMATTING:
- No Oxford comma
- Avoid em-dashes unless necessary
- Use sentence case for headings

Output the revised content with [CHANGED] markers showing what was modified.
```

This kind of Skill ensures brand consistency across all AI-generated content—whether you're drafting emails, creating presentations, or writing documentation.

### Skills vs. Projects: When to Use Which

| Scenario | Use Project | Use Skill |
|----------|-------------|-----------|
| Ongoing client work | ✅ | |
| Quick formatting task | | ✅ |
| Research with documents | ✅ | |
| Repeatable analysis | | ✅ |
| Team-shared methodology | | ✅ |
| Deep strategic work | ✅ | |

**Best practice**: Combine them. Use Skills inside Projects for maximum efficiency.

---

## Pillar 3: Gemini Gems — Specialized Recon Units

### What Gems Are

Gemini Gems are custom AI assistants with persistent instructions, optimized for Google Workspace integration. Think of them as specialized reconnaissance units—pre-configured for specific intelligence-gathering missions.

### When Gems Excel

Gems are particularly powerful for:
- **Research workflows** requiring real-time web data
- **Google Workspace integration** (Docs, Sheets, Slides)
- **Collaborative scenarios** where others need access
- **Current information tasks** (news, trends, recent data)

### Building a Gem: The Configuration

**Gem Name**: Descriptive and role-based
- "Competitive Intel Researcher"
- "Meeting Notes Analyst"
- "Trend Spotter"

**Instructions**: Define behavior and focus
```
You are a competitive intelligence researcher for ActivTrak.

YOUR FOCUS:
- Workforce analytics and employee monitoring software
- Key competitors: Teramind, Hubstaff, Insightful, Time Doctor
- Industry trends in remote work, productivity, privacy

WHEN RESEARCHING:
- Always verify claims with multiple sources
- Include publication dates for all statistics
- Flag anything older than 6 months as potentially outdated
- Prioritize industry analyst reports and primary sources

OUTPUT FORMAT:
- Lead with key findings (3-5 bullets)
- Then provide detailed analysis
- End with "Confidence Assessment" rating
- Include source links for all claims
```

### The Gem Library: Recommended Builds

**Research Gem: "Market Intel"**
Focus: Industry trends, competitor news, market data
Use for: Weekly competitive roundups, trend analysis, market sizing

**Collaboration Gem: "Doc Analyst"**
Focus: Analyzing shared documents, creating summaries
Use for: Processing documents others share with you, collaborative editing

**Presentation Gem: "Slide Builder"**
Focus: Creating Google Slides content with proper formatting
Use for: Deck creation, presentation prep, visual content

---

## Pillar 4: Custom GPTs — Shareable Specialists

### What Custom GPTs Are

Custom GPTs are persistent assistants you build in ChatGPT that can be shared with others. They're like deployable specialists—AI teammates you can distribute to your organization.

### When Custom GPTs Make Sense

Use Custom GPTs when:
- **Others need access** to the same specialized assistant
- **Consistency matters** across multiple users
- **You want to distribute** a standardized workflow
- **ChatGPT's features** (DALL-E, browsing, code interpreter) are needed

### Building a Custom GPT

**Name**: Clear and professional
**Description**: What it does and who it's for
**Instructions**: Detailed behavior guidance
**Knowledge**: Upload relevant files
**Capabilities**: Enable/disable browsing, DALL-E, code interpreter
**Conversation Starters**: Suggested first prompts

**Example: "ActivTrak Battle Card Generator"**
```
Instructions:
You help ActivTrak sales team members create competitive battle cards.

PROCESS:
1. Ask which competitor they're facing
2. Pull relevant positioning from your knowledge base
3. Generate a structured battle card with:
   - Competitor overview
   - Key differentiators (us vs. them)
   - Common objections and responses
   - Discovery questions to ask
   - Closing arguments

TONE: Professional, confident, not disparaging
FORMAT: Single page, scannable, action-oriented
```

---

## The Squadron Playbook: Putting It All Together

Your AI arsenal now includes four persistence tools. Here's how they work together:

### The Decision Matrix

| Need | Primary Tool | Why |
|------|-------------|-----|
| Deep client work | Claude Project | Context + documents + history |
| Quick repeated tasks | Claude Skill | Portable methodology |
| Real-time research | Gemini Gem | Grounded, current data |
| Team-shared assistant | Custom GPT | Distributable, consistent |

### Workflow Integration Example

**Scenario**: Preparing a competitive presentation for the sales team

1. **Gemini Gem** ("Market Intel"): Gather latest competitor news and market data
2. **Claude Project** ("Competitive Intelligence"): Synthesize with existing battle cards and historical analysis
3. **Claude Skill** ("Presentation Outline"): Structure findings into slide framework
4. **Custom GPT** ("Battle Card Generator"): Create shareable asset for sales team

Each tool handles what it does best. No redundancy, maximum efficiency.

---

## Building Your First Project: Step-by-Step

Let's build a Claude Project together—your "Customer Intelligence Hub."

### Step 1: Define the Mission

**Purpose**: Central workspace for customer account intelligence
**Scope**: Top 10 accounts, QBR prep, escalation context
**Users**: Just you (for now)

### Step 2: Write Custom Instructions

```
You are my Customer Intelligence Analyst for ActivTrak.

CONTEXT:
- I manage relationships with enterprise accounts
- Key metrics: adoption rate, feature usage, renewal risk
- Our success philosophy: proactive, consultative, insight-driven

WHEN ANALYZING ACCOUNTS:
- Always check knowledge base for account history first
- Flag any renewal risks based on usage patterns
- Suggest proactive outreach when engagement drops
- Reference previous QBR outcomes when relevant

OUTPUT PREFERENCES:
- Lead with the insight, then the evidence
- Use traffic light system: 🟢 healthy, 🟡 attention, 🔴 risk
- Include "Next Best Action" recommendation
- Format for quick scanning (bullets, not paragraphs)

TERMINOLOGY:
- Use "users" not "customers"
- Use "adoption" not "usage"
- Use "insights" not "monitoring"
```

### Step 3: Upload Knowledge Files

Essential documents:
- Account profiles (one per key account)
- QBR templates and past QBR notes
- Product feature documentation
- Usage benchmarks by segment

### Step 4: Seed with Initial Conversations

Start 2-3 conversations to establish patterns:
- "Summarize the current state of [Account Name]"
- "What should I prioritize for next week's QBRs?"
- "Identify accounts showing early warning signs"

### Step 5: Refine Based on Output

After a week of use:
- Adjust instructions based on what's working
- Add documents you found yourself explaining
- Remove instructions that aren't helping

---

## Common Pitfalls and How to Avoid Them

### Pitfall 1: The Mega-Project

**Problem**: Cramming everything into one Project
**Symptom**: Claude's responses become unfocused, mixing contexts
**Solution**: Create purpose-specific Projects. "Customer Intelligence" ≠ "Competitive Analysis"

### Pitfall 2: Instruction Overload

**Problem**: Writing 2,000-word custom instructions
**Symptom**: Claude ignores or contradicts parts of your instructions
**Solution**: Keep instructions under 500 words. Be specific, not exhaustive.

### Pitfall 3: Stale Knowledge

**Problem**: Uploading documents once and forgetting them
**Symptom**: Outdated information in Claude's responses
**Solution**: Review and refresh knowledge files monthly. Date-stamp uploads.

### Pitfall 4: Tool Confusion

**Problem**: Using the wrong persistence tool for the task
**Symptom**: Friction, inefficiency, suboptimal outputs
**Solution**: Use the decision matrix. Match tool to task type.

---

## Maintenance and Evolution

Your Squadron infrastructure needs regular maintenance:

### Weekly
- Review Project conversations for patterns
- Update Skills that aren't working well
- Check Gem outputs for accuracy

### Monthly
- Refresh knowledge files with current documents
- Audit Custom Instructions for relevance
- Archive Projects that are no longer active

### Quarterly
- Evaluate which Projects deserve expansion
- Consider new Skills based on emerging workflows
- Share successful patterns with team

---

## The Transformation

You started this course as a Solo Pilot—typing prompts into a blank conversation, rebuilding context every time, hoping for good outputs.

Now you're a Squadron Architect. You build systems:
- **Projects** that remember everything about a domain
- **Skills** that standardize your best methodologies
- **Gems** that handle specialized research
- **Custom GPTs** that extend your capabilities to others

The AI does the same work. But your infrastructure makes it **consistent, efficient, and scalable.**

---

## Connection to Module 9

With your Squadron infrastructure in place, you're ready for the next level: **Code Execution**. In Module 9, you'll learn to have AI not just analyze data but create deliverables—Excel spreadsheets, PowerPoint presentations, PDF reports—all generated through code.

Your Projects will hold the context. Your Skills will define the process. And code execution will produce the artifacts.

From Squadron Architect to **Mission Output Commander.**

---

## Key Takeaways

1. **Projects provide persistent context**—use them for ongoing work requiring documents and history
2. **Skills provide portable methodology**—use them for repeatable tasks across contexts
3. **Gems excel at grounded research**—use them when current data and Google integration matter
4. **Custom GPTs enable distribution**—use them when others need access to your AI systems
5. **Maintenance matters**—review, refresh, and refine your infrastructure regularly

---

## The Architect's Creed

> "Don't just use AI—build systems that use AI for you. Infrastructure scales. Individual prompts don't."

---

**End of Module 8 Lesson**
