---
aliases:
  - "(3) Prompt Frameworks"
  - "Source 3"
tags:
  - content/source-material
  - prompt/costar
  - prompt/prep
  - prompt/care
  - concept/context-window
  - prompt/few-shot
  - capability/projects
  - skill/gems
related:
  - "[[Data Repo/00 - Source Material Index|Source Material Index]]"
  - "[[Module 3 - Prompt Architecture/Lesson|Module 3 Lesson]]"
  - "[[Module 6 - Decision Hygiene/Lesson|Module 6 Lesson]]"
---

# Source Material: Prompt Engineering Frameworks

> [!info] Source Index
> This is **Source (3)** - COSTAR, PREP, CARE frameworks. See [[Data Repo/00 - Source Material Index|Source Material Index]] for all sources.

---

## **Module 1: The Strategic Intersection of AI and Workforce Analytics**

### **1.1 Introduction: The Evolution of "Insights, Not Oversight"**

The modern digital workplace is characterized by a deluge of data and a scarcity of attention. At ActivTrak, our mission has always been to cut through the noise, providing organizations with workforce analytics that illuminate how work happens—not to police employees, but to empower them.1 We champion the philosophy of "Insights, not oversight," distinguishing our platform from invasive surveillance tools by focusing on productivity trends, burnout prevention, and workload balance rather than keystroke logging or camera access.2

As we integrate Generative AI (GenAI) into our internal workflows, we face a parallel transformation. Just as ActivTrak helps customers move from raw data to actionable workforce intelligence, GenAI enables our own teams to move from manual content creation and basic information retrieval to high-level strategic orchestration. This module serves as a foundational guide for ActivTrak employees—across Human Resources, Customer Success, Product, and Sales—to master the art of prompt engineering. By leveraging tools like Claude, Gemini, ChatGPT, and Granola, we can embody the very efficiency and insight-driven decision-making we promise our customers.

The focus of this curriculum is strictly non-technical. We are not building software; we are building *competence* in information retrieval, content synthesis, and automated reasoning. We will explore how to use "Projects" in Claude to maintain context over long strategic initiatives 4, how to use Gemini "Gems" to standardize communication styles 5, and how to use Granola to turn meetings into structured data assets.6

### **1.2 The Shift to Intent-Based Computing**

To understand prompt engineering, one must first recognize the fundamental shift in computing paradigms. Traditional software requires the user to know *how* to do something—which menu to click, which formula to write. Generative AI operates on *intent*. The user provides the *what* (the goal) and the *why* (the context), and the AI determines the *how*.7

However, this shift introduces a new skill gap: the ability to articulate intent with precision. An LLM (Large Language Model) is a probability engine, not a truth engine. It predicts the next likely token based on its training data. Without specific guidance, it reverts to the average, generic response found in that training data. "Prompt Engineering" is, therefore, the skill of constraining the model's infinite possibilities down to the specific, high-quality output required for a business task.

For an ActivTrak Customer Success Manager (CSM), this means the difference between asking an AI to "write an email about low utilization" (which might produce a generic, possibly offensive message) and prompting it to "analyze the attached usage report to draft a consultative email to a VP of Ops, highlighting that low utilization in the Engineering team might signal 'deep work' rather than disengagement, aligning with our 'Privacy-first' core value".3 The latter requires an understanding of both the tool's capabilities and ActivTrak’s strategic narrative.

### **1.3 The ActivTrak AI Ecosystem**

Our internal toolkit has been selected to provide a balance of reasoning power, ecosystem integration, and specialized utility.

| Tool | Primary Use Case | Key Features for ActivTrak |
| :---- | :---- | :---- |
| **Claude (Anthropic)** | Complex reasoning, long-form writing, coding assistance, and knowledge management. | **Projects:** Knowledge bases for specific clients or products. **Artifacts:** Creating interactive tools or visual documents. 8 |
| **Gemini (Google)** | Integrated workflow acceleration within Google Workspace (Docs, Sheets, Slides). | **Gems:** Custom personas for repetitive tasks. **Drive Integration:** Seamless access to internal docs. 5 |
| **ChatGPT (OpenAI)** | Ad-hoc data analysis and quick structured data manipulation. | **Advanced Data Analysis:** Uploading CSVs for instant visualization and outlier detection. 11 |
| **Granola** | Meeting intelligence and structured note-taking. | **Templates:** Customizing meeting outputs. **Integrations:** Sending summaries to Slack/Notion. 12 |

---

## **Module 2: The Cognitive Science of Prompt Engineering**

### **2.1 The Probability Trap and Hallucinations**

When an ActivTrak employee types a prompt into Claude or Gemini, they are engaging with a neural network that has compressed a vast portion of the internet's text. The model does not "know" facts in the way a database does; it stores associations. If you ask about "employee monitoring," the model's training data might associate that term with "surveillance" or "spying."

Because ActivTrak explicitly differentiates itself *against* spying—emphasizing "Insight, not oversight" 3—our prompts must actively steer the model away from these probabilistic defaults. If we fail to provide the correct context (e.g., "we are a privacy-first workforce analytics platform"), the AI will likely hallucinate or generate content that conflates us with the "bossware" tools we compete against.

**Key Insight:** Prompt engineering for ActivTrak is often an exercise in *negative constraint*—telling the AI what *not* to say just as much as what to say. We must explicitly instruct models to avoid terms like "tracking" or "policing" and prioritize terms like "optimization," "burnout prevention," and "resource allocation".1

### **2.2 The Context Window: Your Working Memory**

One of the most critical concepts for business users is the "Context Window." This is the amount of information the AI can hold in its "working memory" at one time. Early models had small windows (like a single sheet of paper). Modern tools like Claude and Gemini Pro have massive windows (equivalent to hundreds of books).14

For an analyst at ActivTrak, this is revolutionary. It means you can upload the entire "State of the Workplace 2025" report 3, the "ActivTrak Agent Technical Specifications," and a client's "Q3 Quarterly Business Review" PDF into a single chat session. You can then ask the AI to "Synthesize a strategy for Q4 based on the technical constraints in the specs and the trends in the Workplace report."

However, filling the context window requires strategy. "Garbage in, garbage out" still applies. If you fill the window with irrelevant data, the model's reasoning capability (its "attention mechanism") gets diluted. We must learn to curate the "Context" we provide—a skill we will develop using the "Projects" feature in Claude later in this report.

### **2.3 Zero-Shot vs. Few-Shot Prompting**

To move from novice to expert, one must understand the difference between Zero-Shot and Few-Shot prompting.15

* **Zero-Shot Prompting:** Asking the AI to do something without examples.  
  * *Prompt:* "Write a job description for a Sales Engineer."  
  * *Result:* A generic, vanilla description that could apply to any company.  
* **Few-Shot Prompting:** Providing examples of the desired output within the prompt.  
  * *Prompt:* "Write a job description for a Sales Engineer. Here are three examples of previous high-performing ActivTrak job descriptions \[paste examples\]. Note the tone is 'empowering' and 'technical yet accessible'. Mimic this style."  
  * *Result:* A highly tailored output that matches our employer brand voice.

**Application:** When using Gemini to draft responses to customer tickets regarding "Privacy Concerns," do not just ask for a draft. Paste two examples of "Gold Standard" responses from our internal wiki. This "Few-Shot" technique forces the model to align with our specific messaging regarding non-invasive analytics.3

---

## **Module 3: Advanced Prompting Frameworks**

Effective prompting is not about memorizing "magic words"; it is about structural engineering of the request. We will adopt three primary frameworks: **COSTAR**, **PREP**, and **CARE**. Using these frameworks ensures consistency and reduces the rate of error (hallucination) significantly.

### **3.1 The COSTAR Framework**

The COSTAR framework is the industry standard for complex task generation.17 It breaks the prompt into six essential components. Using COSTAR is non-negotiable for high-stakes content, such as client-facing communications or strategic reports.

| Component | Definition | ActivTrak Context Example |
| :---- | :---- | :---- |
| **C**ontext | Background information necessary to ground the model. | "You are an expert Productivity Coach using ActivTrak data. The client is a healthcare provider worried about nurse burnout." |
| **O**bjective | The specific goal of the task. | "Analyze the attached work pattern data to identify shifts exceeding 12 hours and create a summary for the Chief Nursing Officer." |
| **S**tyle | The writing style to emulate. | "Consultative, data-driven, yet empathetic to the high-stress environment." |
| **T**one | The emotional inflection of the output. | "Professional, urgent but not alarmist. Avoid 'monitoring' language; use 'support' language." |
| **A**udience | Who will consume the output? | "Executive leadership (C-Suite). They care about retention and patient safety, not just hours." |
| **R**esponse | The required format. | "A one-page executive memo in Markdown, with a table for 'At-Risk Departments'." |

Deep Dive Analysis:

Why is the Audience parameter so critical here? If we omitted it, the AI might write a technical report suitable for an IT admin, detailing "agent uptime" or "active window titles." By specifying "Executive Leadership," the AI shifts its focus to outcomes—retention and safety—which aligns with the value proposition of ActivTrak's "Workforce Planning" features.1

### **3.2 The PREP Framework**

PREP is a lighter framework, ideal for quick iterations, internal Slack messages, or refining a thought process.17

* **P**rompt: State the direct request.  
* **R**ole: Assign a persona.  
* **E**xplicit Instructions: Give constraints.  
* **P**arameters: Define the format.

**Scenario:** An HR Manager needs to quickly explain the "Location Insights" feature to a department head.

* **Prompt:** "Explain 'Location Insights'.19"  
* **Role:** "Act as an Internal Change Management Consultant."  
* **Explicit Instructions:** "Emphasize that we use this for real-estate planning (right-sizing the office), not for checking if people are at their desks."  
* **Parameters:** "Keep it to 3 bullet points, suitable for a Slack message."

**Implication:** The **Role** assignment here is vital. A "Change Management Consultant" persona inherently understands that new technology can cause anxiety. The AI will therefore soften the language and focus on the *benefit* (office planning) rather than the *feature* (location tracking), effectively mitigating internal resistance.20

### **3.3 The CARE Framework**

CARE is designed for persuasive communication and reporting results.21 It is the preferred framework for our Customer Success team when conducting QBRs (Quarterly Business Reviews).

* **C**ontext: The situation or problem.  
* **A**ction: What we did (or what the software did).  
* **R**esult: The outcome.  
* **E**xample: A specific proof point.

**Scenario:** Demonstrating the value of the "Productivity Coaching" module.1

* **Context:** "The engineering team was reporting high fatigue levels in Q1."  
* **Action:** "We used ActivTrak's 'Workload Balance' report to identify three developers who were consistently working 55+ hour weeks."  
* **Result:** "Manager reallocated two projects. Burnout risk scores dropped by 40% in Q2."  
* **Example:** "Developer A returned to 'Healthy' status and shipped the new API integration on time."

Using CARE ensures that every interaction with AI generates a narrative that links *features* to *value*, a core requirement for driving adoption in the ActivTrak "Productivity Lab" methodology.2

---

## **Module 4: Mastery of Claude (Anthropic)**

Claude is ActivTrak's "Heavy Lifter." It is the tool of choice for processing large documents, coding assistance (for non-coders), and maintaining long-term project context.

### **4.1 Claude Projects: The Knowledge Management Engine**

"Projects" in Claude are arguably the most powerful feature for enterprise users. They allow you to create a "walled garden" of context that persists across multiple chat sessions.4

#### **4.1.1 The Architecture of a Project**

Instead of uploading the "ActivTrak User Guide" every time you have a question, you create a **Project** named "ActivTrak Expert."

1. **Project Knowledge:** You upload the core documents: "ActivTrak Features List" 19, "Privacy Principles" 3, and "Employee Monitoring vs. Analytics Guide".23  
2. **Custom Instructions:** You set the "System Prompt" for the entire project. For example: *"You are an ActivTrak Solutions Engineer. You always prioritize privacy. You never recommend using the tool for punitive measures. Your goal is organizational health."*

#### **4.1.2 Integration with Google Drive**

Claude allows direct integration with Google Drive.24 This means you can connect a live Google Doc (e.g., "Q3 Roadmap") to a Project.

* **Workflow:**  
  * Open Project "Q3 Planning."  
  * Click "Add Content" \> "Google Drive."  
  * Select the "Q3 Roadmap" Google Doc.  
* **Benefit:** As the Roadmap changes in Google Docs, Claude (mostly) stays up to date when it re-scans for a new session. This eliminates version control nightmares where you are pasting old text into the AI.25

**Warning:** Claude only reads the text of the Doc. It does not see comments, suggested edits, or images within the Doc.24

### **4.2 Artifacts: The "App Builder" for Non-Coders**

"Artifacts" allow Claude to generate standalone windows for code, diagrams, or documents.9 This feature transforms Claude from a chatbot into a content generator.

#### **4.2.1 Use Case: Visualizing Workflow**

Scenario: A Product Manager wants to visualize the user journey for the "Personal Insights" dashboard.1

Prompt: "Create a Mermaid flowchart diagram showing the user journey from logging in to viewing their 'Focus Time' score. Include decision nodes for 'Is user a Manager?' vs 'Is user an Employee?'."

Output: Claude generates a visual diagram in the right-hand window (Artifact). The PM can then say, "Change the color of the Manager path to Blue," and the diagram updates instantly. This allows non-technical staff to create technical-grade documentation.

#### **4.2.2 Use Case: Interactive Calculators**

Scenario: Sales wants an ROI calculator for a prospect.

Prompt: "Create a React-based interactive calculator Artifact. Inputs: 'Number of Employees', 'Average Hourly Wage', 'Hours Saved per Week'. Output: 'Annual Savings'. Use ActivTrak branding colors."

Output: A working calculator app appears in the side panel. The Sales rep can screen-share this with a client.

### **4.3 Practical Exercise: Building the "Competitor Battle Card" Project**

**Objective:** Create a Claude Project that helps Sales Reps position ActivTrak against competitors.

1. **Create Project:** Name it "Competitive Intel."  
2. **Knowledge:** Upload PDF comparisons or text files containing data on competitors (e.g., "Competitor A focuses on surveillance," "Competitor B lacks burnout detection").  
3. **Instructions:** "You are a Competitive Strategy Consultant. When asked about a competitor, provide a 3-column table: 'Their Feature', 'Our Advantage', 'Talking Point'. Always emphasize our 'Insights not Oversight' philosophy."  
4. **Test:** Ask the Project: "How do we beat a competitor who offers keylogging?" (Note: Claude should reference our privacy stance 3 as a differentiator).

---

## **Module 5: Mastery of Gemini (Google Workspace)**

Gemini is the "Orchestrator" embedded in our daily tools. Its strength lies not in deep reasoning (where Claude excels) but in workflow acceleration and integration with our corporate data ecosystem.26

### **5.1 Gemini Gems: Scaling Expertise**

"Gems" are custom versions of Gemini that can be given specific instructions and—crucially—shared with the team.5 This allows us to "clone" the expertise of our best employees.

#### **5.1.1 The "Proposal Generator" Gem**

Problem: Sales reps spend hours customizing proposals.

Solution: A "Proposal Generator" Gem.27

* **Instructions:** "You are a Senior Proposal Writer. I will paste a rough meeting transcript. You will extract the client's 'Pain Points' and 'Success Metrics'. Then, draft a proposal introduction using the 'ActivTrak Value Framework'. Reference 'Workforce Planning' 1 and 'Technology Optimization' 19 where relevant."  
* **Knowledge:** Upload high-performing past proposals as examples (Few-Shot Prompting).  
* **Impact:** This Gem is shared with the entire sales team. A junior rep can now generate a proposal that sounds like a top performer.

#### **5.1.2 The "Tone & Compliance" Gem**

Problem: Ensuring all external communication complies with our "Privacy First" messaging.

Solution: A "Compliance Check" Gem.

* **Instructions:** "Review the following text. Flag any words that imply surveillance (e.g., 'spying', 'tracking', 'watching'). Suggest alternatives that emphasize 'analytics', 'visibility', and 'insight'."  
* **Use Case:** Before sending a newsletter, the Marketing team runs the draft through this Gem.

### **5.2 Gemini in Docs, Sheets, and Slides**

#### **5.2.1 Google Sheets: Categorizing Feedback**

For Product Managers dealing with thousands of rows of customer feedback:

* **Action:** Open the Gemini sidebar in Sheets.  
* **Prompt:** "Analyze the feedback in Column C. Categorize each row into 'Feature Request', 'Bug', or 'Pricing'. Put the category in Column D."  
* **Benefit:** Gemini automates the tedious tagging process, allowing the PM to focus on the *insights* (e.g., "Why are pricing complaints rising?").

#### **5.2.2 Google Slides: Visualizing Concepts**

* **Action:** "Create Image" feature.  
* **Prompt:** "Create an image of a diverse team collaborating in a modern, sunlit office, with abstract data visualizations floating in the air. Style: Corporate Memphis, Blue and White palette."  
* **Benefit:** Custom assets that match our brand, created in seconds.28

### **5.3 Advanced Data Analysis in Gemini**

Gemini can analyze uploaded files to find correlations.11

* **Task:** Analyzing the "State of the Workplace" report.3  
* **Prompt:** "Based on the uploaded report, what is the correlation between 'Meeting Time' and 'Burnout Risk'? Create a chart summarizing this."  
* **Insight:** Gemini can extract the data points from the PDF and generate a visualization, proving the hypothesis that excessive meetings drive burnout.

---

## **Module 6: Granola and the Art of Meeting Intelligence**

Granola represents a shift from "recording" to "structured listening." It does not use a bot that joins the call (which can be intrusive); it records system audio and uses AI to transcribe and summarize.29

### **6.1 The "Template" is the Prompt**

The most underutilized feature in Granola is the **Custom Template**.12 The default template gives a generic summary. A custom template acts as a sophisticated prompt that runs against the transcript.

#### **6.1.1 Creating the "Customer Discovery" Template**

For our Sales team, a generic summary is insufficient. We need specific data points to populate Salesforce.

* **Template Structure:**  
  1. **Tech Stack:** "List all software tools mentioned (e.g., Jira, Slack, Salesforce)."  
  2. **Competitors:** "Did they mention \[Competitor X\] or?"  
  3. **Privacy Objections:** "Quote any questions asked about employee privacy or data security."  
  4. **Buying Timeline:** "Extract dates mentioned regarding budget approval or implementation."  
* **Mechanism:** When the meeting ends, Granola executes this "prompt" against the transcript. The result is not a summary; it is a structured dataset ready for CRM entry.

### **6.2 Integrations: The "Ripple Effect"**

Granola integrates with Slack and Notion.13 This allows for automated information dissemination.

**Scenario:** The "Productivity Lab" team holds a weekly research call.

* **Setup:** Connect Granola to the \#productivity-research Slack channel.  
* **Workflow:** When the call ends, Granola posts the "Key Takeaways" directly to Slack.  
* **Result:** The entire company can see the latest research findings without attending the meeting. This reduces the need for "update meetings," directly improving our own "Meeting Time" metrics.32

### **6.3 Chat with Transcript**

Post-meeting, you can query the Granola chat interface.29

* **Query:** "What was the exact phrase the client used when describing their burnout problem?"  
* **Granola:** "They said: 'Our teams are fried because they feel like they have to be green on Teams all day.'"  
* **Application:** This quote can be copy-pasted directly into the proposal to show deep listening and empathy.

---

## **Module 7: ChatGPT and Structured Data Analytics**

While Claude and Gemini are excellent for text, ChatGPT (specifically with the "Advanced Data Analysis" tool enabled) remains the premier tool for quick, ad-hoc analysis of structured data (CSV/Excel).33

### **7.1 The HR Analytics Workflow**

HR teams often have exports of "Productivity Data" that are too large for manual scanning but too small for a Data Science project.

#### **7.1.1 Step-by-Step Analysis**

1. **Data Prep:** Anonymize the data\! (Replace names with ID numbers).  
2. **Upload:** Upload the CSV to ChatGPT.  
3. **Prompt 1 (Exploratory):** "Analyze this dataset. Provide descriptive statistics for 'Focus Time' and 'Collaboration Time'."  
4. **Prompt 2 (Hypothesis Testing):** "Test the hypothesis that employees with higher 'Collaboration Time' have lower 'Focus Time'. Visualize this relationship with a scatter plot."  
5. **Prompt 3 (Actionable Insight):** "Identify the top 10% of users with the highest 'Passive Time'. Based on ActivTrak principles, suggest 3 non-punitive reasons this might be happening (e.g., long meetings, offline work)." 35

### **7.2 Creating Excel Formulas**

ChatGPT is also an expert at generating complex Excel formulas for non-technical users.36

* **Prompt:** "I have a sheet where Column A is 'Start Time' and Column B is 'End Time'. Write a formula to calculate the duration in hours, but exclude weekends and holidays listed in range K1:K10."  
* **Result:** ChatGPT generates the precise NETWORKDAYS formula, saving the HR analyst hours of Googling.

---

## **Module 8: Role-Specific Application Scenarios**

To demonstrate the versatility of these tools, we will explore three comprehensive "Day in the Life" scenarios.

### **8.1 Scenario A: The HR Business Partner (HRBP)**

**Goal:** Address a department head's concern about "Quiet Quitting" without resorting to invasive monitoring.

1. **Information Retrieval (Gemini):**  
   * *Action:* The HRBP opens the "State of the Workplace" report in Drive.  
   * *Prompt:* "Summarize the section on 'Quiet Quitting' vs. 'Healthy Boundaries'. What metrics differentiate them?"  
   * *Insight:* The report clarifies that lower hours often mean better efficiency, not quitting.  
2. **Data Analysis (ActivTrak \+ ChatGPT):**  
   * *Action:* Export the department's "Productivity Trends" (anonymized). Upload to ChatGPT.  
   * *Prompt:* "Analyze the trend of 'Productive Hrs/Day' over the last 6 months. Is it declining? Also check 'Focus Quality'. Are they working fewer hours but with higher focus?"  
   * *Result:* ChatGPT reveals that hours are down 5%, but Focus Quality is up 15%. This is efficiency, not quitting.  
3. **Content Generation (Claude):**  
   * *Action:* Use the "Coaching Script" Project.  
   * *Prompt (COSTAR):* "Context: Managers suspect quiet quitting. Data shows increased efficiency. Objective: Write a talking point script for the HRBP to give to the Manager. Audience: Skeptical Manager. Tone: Data-driven, reassuring. Result: A script that reframes the narrative from 'Quitting' to 'Optimization'."

### **8.2 Scenario B: The Customer Success Manager (CSM)**

**Goal:** A customer is up for renewal but has low feature adoption.

1. **Meeting Prep (Granola):**  
   * *Action:* Review past meeting notes using "Chat with Transcript."  
   * *Query:* "What were the customer's stated goals for Q1?"  
   * *Result:* "They wanted to reduce overtime costs."  
2. **Strategy Generation (Claude):**  
   * *Action:* Upload the customer's "Usage Report" (PDF) to Claude.  
   * *Prompt:* "The customer wanted to reduce overtime. Look at this Usage Report. Have overtime hours trended down? If not, which feature (that they aren't using) should I recommend?"  
   * *Result:* Claude notices they aren't using the "Workload Balance" dashboard 1, which is the primary tool for solving their problem.  
3. **Content Creation (Gemini):**  
   * *Action:* "Help me write" in Gmail.  
   * *Prompt:* "Draft a renewal email. Highlight that while overtime is still high, they have an unused tool ('Workload Balance') that can fix it. Propose a training session."

### **8.3 Scenario C: The Product Marketer**

**Goal:** Launch a campaign for the new "Personal Insights" dashboard.37

1. **Ideation (Gemini Gems):**  
   * *Action:* Use the "Brainstorming Gem."  
   * *Prompt:* "Generate 10 blog post titles about 'Personal Insights' that appeal to employees, not just managers. Focus on 'Autonomy' and 'Self-Improvement'."  
2. **Drafting (Claude Artifacts):**  
   * *Action:* "Create an HTML mockup of a landing page for this feature. Include a 'Before/After' comparison table: 'Before: Manager tells you how you work. After: You tell your Manager how you work best'."  
   * *Result:* A visual artifact of the landing page to share with the web team.  
3. **Refinement (Granola Integration):**  
   * *Action:* Present the mockup in a team meeting recorded by Granola.  
   * *Post-Meeting:* Granola summarizes the team's feedback ("Change the headline," "Make the table blue").  
   * *Action:* Feed the Granola summary back into Claude: "Update the Artifact based on this feedback."

---

## **Module 9: Ethics, Privacy, and Governance**

As employees of ActivTrak, our usage of AI must reflect our product's core values: Privacy, Transparency, and Trust.3

### **9.1 The "Privacy-First" Prompting Protocol**

We must treat AI prompts with the same rigor as we treat our database security.

1. **Anonymization is Mandatory:** Never enter PII (Personally Identifiable Information) into *any* AI tool.  
   * *Bad Prompt:* "Analyze the performance of John Smith, email j.smith@client.com."  
   * *Good Prompt:* "Analyze the performance of Employee\_001, Role: Senior Dev."  
2. **Exclude Confidential Secrets:** Do not upload unreleased code, API keys, or unannounced financial results into public models. Use the Enterprise versions (Claude Team, Gemini Enterprise) where data privacy is contractually guaranteed, but still practice minimization.  
3. **The "Surveillance" Check:** Before acting on AI advice regarding workforce data, ask: "Does this action feel like 'Insight' or 'Oversight'?" If the AI suggests "Monitor their screen every 5 minutes to see if they are active," **discard that advice**. It violates our core philosophy.2

### **9.2 Avoiding Bias in AI Analysis**

LLMs can perpetuate biases found in their training data. When analyzing workforce data:

* **Prompt for Objectivity:** "Analyze this performance data. Be aware of potential bias. Ensure that 'time of day' work habits (e.g., parents working late after kids sleep) are not penalized as 'unproductive'."  
* **Human in the Loop:** AI is a decision *support* tool, not a decision *maker*. Never allow an AI to make a final determination on hiring, firing, or promotion.

---

## **Module 10: Hands-On Assignments**

To complete this module, you must submit the following three assignments. These are designed to prove your competency in the tools and frameworks discussed.

### **Assignment 1: The "Project" Builder (Claude)**

**Objective:** Demonstrate the ability to create a persistent knowledge base.

1. **Task:** Create a Claude Project named "ActivTrak Onboarding Assistant."  
2. **Input:** Upload the text from the "ActivTrak Features" page 1 and the "Privacy Policy".3  
3. **Prompt:** Use the Project to generate a "Welcome Email" for a new customer that explains the "Privacy-First" approach.  
4. **Submission:** A screenshot of the Project settings (showing the uploaded knowledge) and the generated email.

### **Assignment 2: The "Meeting to Action" Loop (Granola \+ Gemini)**

**Objective:** Demonstrate workflow automation.

1. **Task:** Record a 5-10 minute meeting (or mock meeting) using Granola. Use a custom template to extract "Action Items."  
2. **Action:** Copy the "Action Items" from Granola.  
3. **Prompt:** Paste them into Gemini (Google Docs) with the prompt: "Convert these action items into a 'Next Steps' project table. Columns: Task, Owner, Due Date (assume 1 week from now), Priority."  
4. **Submission:** The link to the Google Doc containing the formatted table.

### **Assignment 3: The Framework Challenge (ChatGPT/Claude)**

**Objective:** Demonstrate mastery of the COSTAR framework.

1. **Task:** You need to explain to a client why their "Productivity Score" dropped. (Reason: They hired 5 new interns who are still learning).  
2. **Constraint:** Write a prompt using the **COSTAR** framework to generate this explanation.  
3. **Submission:** The full COSTAR prompt you wrote, and the AI's output.

---

## **Conclusion**

This guide has moved from the theoretical underpinnings of Generative AI to the practical, daily application of tools like Claude, Gemini, and Granola. By mastering these technologies, we do more than just save time; we model the future of work that ActivTrak advocates for. We demonstrate that with the right "Insights," we can achieve extraordinary results without "Oversight."

You are now equipped to be an "AI Orchestrator." The tools are your orchestra. The prompt is your baton. Lead with intent.

