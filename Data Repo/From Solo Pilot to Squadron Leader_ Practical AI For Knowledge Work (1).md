---
aliases:
  - "(1) Curriculum Outline"
  - "Source 1"
tags:
  - content/source-material
  - curriculum
  - module-structure
  - learning-objectives
  - squadron-metaphor
  - governance/data-safety
related:
  - "[[Course Development Guide]]"
  - "[[Data Repo/00 - Source Material Index|Source Material Index]]"
  - "[[Data Repo/Concept Map|Concept Map]]"
---

# Source Material: Curriculum Outline

> [!info] Source Index
> This is **Source (1)** - the complete 12-module curriculum outline. See [[Data Repo/00 - Source Material Index|Source Material Index]] for all sources.

---

Here is the comprehensive, detailed course outline for the **"From Solo Pilot to Squadron Leader"** certification.

This curriculum is designed to transform ActivTrak employees from casual users into "AI Architects," capable of orchestrating complex reasoning workflows using the full ActivTrak tool stack (Claude, Gemini, Granola, and Mac/Google Ecosystems).

---

# **Course Title: From Solo Pilot to Squadron Leader**

Goal: Empower ActivTrak employees to orchestrate GenAI as a non-deterministic reasoning engine, leveraging internal data to drive verifiable business outcomes.

Format: Hybrid (Conceptual Strategy \+ Hands-on Labs)

Target Audience: General Staff (Managers, ICs, Sales, CS, Ops)

Prerequisites: Access to Claude Enterprise, Gemini for Workspace, and Granola.

---

### **Module 0: Pre-Flight Check (Setup, Policy & Boundaries)**

**Focus:** Removing friction and establishing the "Rules of Engagement."

* **Learning Objectives:**  
  * Configure the "Cockpit": Claude Desktop, Gemini (Workspace), Granola, and Apple Notes.  
  * Master the **ActivTrak PII Protocol**: Understanding the distinction between *Input* (Permissive) and *Output* (Gated).  
* **Core Concepts:**  
  * **The Toolchain:**  
    * **The Brain (Claude):** Reasoning, Strategy, Writing, Coding.  
    * **The Eyes (Gemini):** Real-time web search, grounding, Google Drive search.  
    * **The Memory (Granola):** Meeting transcription and structured notes.  
  * **The "Output Gate" Theory:** The risk is not in *analyzing* the customer data; the risk is in *sending* the unedited output.  
* **Topic Outline:**  
  * **Installation Party:** Setting up Claude Desktop, enabling "Extended Thinking" features, and syncing Gemini.  
  * **The Revised Traffic Light Protocol:**  
    * 🟢 **Green (Go):** PII (Names, Emails, Deal info), Internal Data. *Use freely for analysis, drafting, and prep.*  
    * 🟡 **Yellow (Review Required):** Marketing/Public Collateral. *PII usage requires PR/Legal review.*  
    * 🔴 **Red (No Go):** Secrets, API Keys, Passwords, Admin Credentials. *Never share.*  
* **Content & Aids:**  
  * *Handout:* **The Data Safety Traffic Light** (Visual Reference).  
  * *Scenario Card:* "Can I upload this?" (Quiz on specific data types).

---

### **Module 1: The Cognitive Shift (Understanding the Engine)**

**Focus:** Moving from "Search Engine" thinking to "Reasoning Engine" thinking.

* **Learning Objectives:**  
  * Understand LLMs as **Probabilistic Reasoning Engines** (Next-token prediction).  
  * Recognize the **"Water Glass" Effect:** How too much irrelevant context degrades intelligence.  
  * Differentiate between **Solo Pilot** (Single-shot prompting) and **Squadron Leader** (Multi-agent orchestration).  
* **Core Concepts:**  
  * **Token Prediction:** How the model traverses the "path of least resistance" in a semantic space.  
  * **Constitutional AI (CAI):** Why Claude minimizes "evasiveness" but prioritizes "harmlessness" (and how this differs from GPT).  
  * **Context Topology:** The "Lost in the Middle" effect—why putting instructions at the *end* often works best.  
* **Topic Outline:**  
  * **The "Stochastic Parrot" vs. The Reasoning Engine.**  
  * **The Context Budget:** How to manage the 200k context window effectively.  
  * **ActivTrak Ethics:** "Insights, not Oversight" in AI-generated analysis.  
* **Content & Aids:**  
  * *Visual Aid:* **The Context Window Map** (Priming \-\> Data \-\> Instructions).

---

### **Module 2: Model Selection & The "Thinking" Protocol**

**Focus:** Selecting the right "Brain" for the task and buying intelligence with latency.

* **Learning Objectives:**  
  * Select the correct model class (Opus, Sonnet, Haiku) based on task requirements.  
  * Master **"Extended Thinking"** (Claude Opus/Sonnet 4.5 with extended thinking and other thinking models) to solve complex logic and strategy problems.   
* **Core Concepts:**  
  * **The Model Taxonomy:**  
    * **Haiku:** Speed/Volume (Simple summaries, chat, translations).  
    * **Sonnet (4.5):** The Daily Driver (Coding, standard reasoning, speed, "Vibe Coding").  
    * **Opus (4.5):** The Strategist (Deep nuance, complex creative writing, highest logic).  
  * **System 1 vs. System 2:**  
    * *Standard Mode:* Fast, intuitive, prone to math errors.  
    * *Extended Thinking:* Slow, analytical, self-correcting.  
* **Topic Outline:**  
  * **The Decision Matrix:** When to trade speed for "Thinking Tokens."  
  * **Thinking Visibility:** Reading the collapsible "Thinking" block to verify the AI's logic.  
* **Content & Aids:**  
  * *Cheat Sheet:* **"Which Model When?" Matrix**.

---

### **Module 3: The Reasoning Engine (Advanced Prompt Architecture)**

**Focus:** "Programming in English" using XML and structure.

* **Learning Objectives:**  
  * Master **XML Tagging** (\<context\>, \<instructions\>, \<data\>) to "sandbox" PII and data.  
  * Apply **Chain of Thought (CoT)** principles to force logic before output.  
  * Use **Meta-Prompting** to have the AI write its own tools.  
* **Core Concepts:**  
  * **The XML Sandbox:** Using tags to prevent "Context Bleeding" (e.g., ensuring the AI doesn't confuse the *instructions* with the *text to be summarized*).  
  * **Structured Prompting:** The standard architecture: Role \-\> Context \-\> Data \-\> Instructions \-\> Output Format.  
* **Topic Outline:**  
  * **The ActivTrak XML Standard:**  
    * \<system\_role\>: Who are you?  
    * \<task\_context\>: What are we doing?  
    * \<user\_data\>: The PII/Data payload.  
    * \<constraints\>: What *not* to do.  
  * **The "Think" Tag:** Explicitly asking for \<thinking\> blocks inside the prompt (for models without native Extended Thinking).  
  * **Meta-Prompting:** "Act as a Prompt Engineer and improve this request."  
* **Content & Aids:**  
  * *Template:* **The "Mega-Prompt" Boilerplate** (Copy/Paste XML structure).

---

### **Module 4: Agentic Data Analysis (The "No Math" Rule)**

**Focus:** Doing math and analysis safely without hallucination.

* **Learning Objectives:**  
  * Understand **The Calculator Problem:** Why LLMs fail at basic arithmetic.  
  * Use **Code Execution (Python Sandbox)** for error-free financial and usage analysis.  
  * Generate visual assets (charts/graphs) from raw CSVs.  
* **Core Concepts:**  
  * **Probabilistic vs. Deterministic:** Text is guessed; Math must be calculated.  
  * **The Sandbox:** Asking Claude to "Write and run a Python script" to analyze data.  
  * **Claude for Excel:** Using AI to trace complex formula dependencies in uploaded spreadsheets.  
* **Topic Outline:**  
  * **The Hallucination Test:** Asking an LLM to multiply large numbers (and watching it fail) vs. using Python.  
  * **Vibe Coding for Analytics:** "Upload this CSV and show me a trend line of user activity."  
  * **Data Cleaning:** Using Claude to format messy text data into clean tables.  
* **Content & Aids:**  
  * *Lab:* **The "Account Review" Analysis** (Upload dummy account data \-\> Python Analysis \-\> Chart Output).

---

### **Module 5: The Sensory System (Gemini & Granola)**

**Focus:** Grounding the reasoning engine in reality.

* **Learning Objectives:**  
  * Use **Gemini** for "Grounding" (Real-time Retrieval) to prevent hallucinations.  
  * Use **Granola** for "Structured Listening" and meeting data capture.  
* **Core Concepts:**  
  * **The Trinity:** Brain (Claude) \+ Senses (Gemini) \+ Memory (Granola).  
  * **Context Injection:** The workflow of pasting Granola transcripts into Claude \<context\> tags for Call Prep.  
  * **Fact Briefs:** Using Gemini to generate a verified list of facts, then feeding that to Claude for writing.  
* **Topic Outline:**  
  * **Gemini Grounding:** Using the "Double Check" button and Google Workspace extensions.  
  * **Granola Templates:** Creating custom meeting templates (e.g., "Discovery Call," "QBR").  
  * **The Handoff:** Granola (Capture) \-\> Claude (Synthesis).  
* **Content & Aids:**  
  * *Template:* **The "Fact Brief" Format**.

---

### **Module 6: Decision Hygiene (Beating Sycophancy)**

**Focus:** Ensuring the AI tells you the truth, not what you want to hear.

* **Learning Objectives:**  
  * Identify and mitigate **Sycophancy** (The AI's bias to agree with the user).  
  * Execute **Red Teaming** and **Pre-Mortem** protocols for strategic decisions.  
* **Core Concepts:**  
  * **Neutral Framing:** Asking "Evaluate risks and benefits" instead of "Why is this a good idea?"  
  * **Persona Rotation:** "Critique this email as if you were the skeptical CFO of the target company."  
* **Topic Outline:**  
  * **The "Yes-Man" Trap:** Why models lie to be nice.  
  * **Red Teaming:** Explicitly instructing the AI to find flaws in your logic.  
  * **The Pre-Mortem Prompt:** "Imagine this project failed. Why?"  
* **Content & Aids:**  
  * *Activity:* **"Spot the Bias"** (Reviewing AI outputs for sycophancy).

---

### **Module 7: The Hybrid Agent (Mac, Mobile & Docs)**

**Focus:** Seamless workflows across devices and apps.

* **Learning Objectives:**  
  * Master the **"Ramble-to-Gold"** workflow (Voice Memos \-\> Apple Notes \-\> Claude).  
  * Utilize the **"HTML Bridge"** to paste AI tables into Google Docs without breaking formatting.  
* **Core Concepts:**  
  * **Zero-Friction Capture:** Eliminating the resistance to starting a task using voice.  
  * **The HTML Hack:** Asking Claude to "Output as an HTML table I can copy-paste" to preserve styling in G-Suite.  
* **Topic Outline:**  
  * **The Commuter’s Workflow:** Recording thoughts on the go, syncing via iCloud, and processing in Claude Desktop.  
  * **Cross-Platform Interoperability:** Formatting text for Slack (Markdown) vs. Docs (HTML) vs. Sheets (CSV).  
  * **Mac Power Moves:** Dragging screenshots and folders directly into the Claude Desktop input bar.  
* **Content & Aids:**  
  * *SOP:* **The "Ramble-to-Gold" Step-by-Step Guide**.

---

### **Module 8: Systemizing Intelligence (Projects, GPTs and Gems)**

**Focus:** Turning ad-hoc chats into reusable team assets.

* **Learning Objectives:**  
  * Use **Projects** to create "Department Brains" (Persistent Context Libraries).  
  * Use **Artifacts** for "Vibe Coding" (Interactive Dashboards) and Document drafting.  
* **Core Concepts:**  
  * **Knowledge Management:** Updating Project files to avoid "Context Rot."  
  * **Artifacts vs. Chat:** Knowing when to ask for a "Code Artifact" (React component) vs. a text response.  
* **Topic Outline:**  
  * **Building a Project:** Uploading the Employee Handbook, Brand Guidelines, and OKRs.  
  * **Artifact Types:** Documents, Code, SVG Graphics, and React Apps (Calculators).  
  * **Sharing Knowledge:** Exporting a chat or Project to share a workflow with a teammate.  
* **Content & Aids:**  
  * *Lab:* **Build Your "Squadron Base"** (Create a Project with 3 key knowledge files).

---

### **Module 9: Code execution and file creation** 

Focus: using code to analyze data,  creating excel, PPT, PDF, Markdown, and other file types for use outside of Claude.

* {Complete this as needed}

---

### **Module10: Future Frontiers (Agents & MCP)**

**Focus:** Preparing for the next wave of "Tool Use."

* **Learning Objectives:**  
  1. Understand the shift from "Chatting" to "Tool Use."  
  2. Prepare data structures for **Agentic Workflows**.  
* **Core Concepts:**  
  1. **MCP (Model Context Protocol):** A conceptual overview of connecting Claude to external databases/tools (future-proofing).  
  2. **Logic Flows:** Writing prompts as "If/Then" scripts (e.g., "If the data shows X, generate report Y; else, alert me").  
* **Topic Outline:**  
  1. **The Agentic Mindset:** Defining goals, not just tasks.  
  2. **Structured Output:** Why JSON/XML is the language of Agents.

---

### **Module 11: Capstone & Governance**

**Focus:** Accountability, ROI, and Certification.

* **Learning Objectives:**  
  * Track personal **AI ROI** (Time saved vs. Quality gained).  
  * Master the **Human-in-the-Loop** verification standard for PII outputs.  
* **Core Concepts:**  
  * **The "Send" Button is Yours:** Clarifying that AI drafts the content, but the human owns the consequences.  
  * **Success Metrics:** Accuracy, Speed, Logic.  
* **Capstone Project:**  
  * **"The Squadron Mission":** Participants must execute a multi-step workflow:  
    1. Record a voice memo (Idea).  
    2. Research facts via Gemini (Grounding).  
    3. Analyze data via Claude/Python (Logic).  
    4. Draft a final report using a Project/Persona (Strategy).  
    5. Verify PII safety (Governance).  
* **Content & Aids:**  
  * *Checklist:* **The PII Output Safety Check**.

