# Module 3: The Reasoning Engine
## Knowledge Check Quiz

**Instructions:** Answer all questions. Review feedback after each answer to reinforce learning.

---

### Question 1 (Multiple Choice)

What is "context bleeding" in AI prompts?

A) When the AI runs out of context window space
B) When different parts of a prompt contaminate each other, causing the AI to confuse instructions with data
C) When you copy-paste too much text into a prompt
D) When the AI forgets information from earlier in the conversation

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** Context bleeding occurs when the AI can't distinguish between different sections of your prompt—mixing instructions with content, including constraint language in outputs, or treating data as commands. Clear structure (whether XML, Markdown, or simple labels) solves this by creating separation.
- **Why A is wrong:** Running out of context window is a different problem (capacity, not clarity).
- **Why C is wrong:** The amount of text isn't the issue—it's the lack of structure.
- **Why D is wrong:** That describes context decay over long conversations, not bleeding within a single prompt.

---

### Question 2 (Multiple Choice)

Which statement about prompt structure formats is TRUE?

A) XML is required for Claude to understand structured prompts
B) Markdown headers and clear section labels can achieve similar results to XML tags
C) Only XML can prevent context bleeding
D) Unstructured prompts never work well

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** All three formats (XML tags, Markdown headers, clear section labels) create separation between prompt components. The goal is clarity and separation, not a specific syntax. Choose what feels comfortable.
- **Why A is wrong:** XML is one option, not a requirement. Claude understands all three formats.
- **Why C is wrong:** Markdown headers and clear labels also prevent context bleeding by creating visual and semantic separation.
- **Why D is wrong:** Simple, well-written unstructured prompts work fine for straightforward tasks.

---

### Question 3 (Multiple Choice)

When is XML superior to Markdown or clear section labels?

A) Always—XML is the only professional option
B) When you need nested data, structured outputs, reusable templates, or when your data contains Markdown formatting
C) Only when working with code
D) When prompts are longer than 500 words

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** XML has specific advantages: (1) nesting data hierarchically, (2) requesting structured output formats, (3) creating templates with placeholders, and (4) avoiding confusion when your data itself contains Markdown formatting.
- **Why A is wrong:** All three formats are valid professional options.
- **Why C is wrong:** XML is useful for many non-code scenarios.
- **Why D is wrong:** Length doesn't determine format—complexity and requirements do.

---

### Question 4 (True/False with Explanation)

**Statement:** You should always use formal structure (XML, Markdown headers, or clear labels) for every prompt you write.

A) True
B) False

**Correct Answer:** B (False)

**Feedback:**
Simple, single-purpose prompts often work fine without formal structure. For example: "Review this email and make it more concise. Keep it under 100 words."

**Use formal structure when:**
- Multiple data sources
- Several distinct requirements
- Getting inconsistent results
- Creating reusable templates

**Skip formal structure when:**
- Task is simple and single-purpose
- Back-and-forth conversation
- Your natural writing is already clear

The goal is **clarity, not ceremony**. Match complexity to the task.

---

### Question 5 (Multiple Choice)

What is a key benefit of asking Claude to structure messy data for you?

A) It makes Claude work faster
B) It converts unorganized notes or data into clean, structured format you can use in subsequent prompts
C) It reduces the cost of API calls
D) It only works with XML output

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** You can ask Claude to convert messy meeting notes, email threads, or raw data into structured format (with sections like "Action Items," "Key Concerns," etc.). This structured output then becomes clean input for your next prompt.
- **Why A is wrong:** Structuring data doesn't affect processing speed.
- **Why C is wrong:** This has no direct impact on API costs.
- **Why D is wrong:** You can ask for Markdown, XML, or any format you prefer.

**Example prompt:** "Here are my rough notes. Convert them into structured sections: Client Goals, Concerns, Action Items, Next Steps."

---

### Question 6 (Multiple Choice)

What is the correct order for prompt sections, and why?

A) Data → Instructions → Role → Constraints
B) Role → Context → Data → Constraints → Output Format
C) Instructions → Data → Role → Format
D) Any order works equally well

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** Role → Context → Data → Constraints → Output Format follows the principle of "orientation at the beginning, instructions at the end." The role primes the AI's persona, context sets the situation, data provides material to work with, and instructions/constraints at the end get highest attention due to the "Lost in the Middle" effect.
- **Why D is partially true but B is better:** While Claude can work with various orders, placing instructions at the end consistently produces better results due to attention patterns.

---

### Question 7 (Scenario-Based)

A colleague shows you this prompt and asks which format would work best:

> "I need to analyze three different data sources (client metrics, support tickets, and NPS scores) and produce a structured health assessment with specific sections for each area plus recommendations."

Which format would you recommend and why?

A) A simple unstructured paragraph would work fine
B) Markdown headers, because they're easier to read
C) XML tags, because nested data and structured output requirements favor explicit containers
D) Clear section labels, because they're the simplest option

**Correct Answer:** C

**Feedback:**
- **Why C is correct:** This scenario has multiple data sources that benefit from nesting (metrics, tickets, scores inside a parent data tag) and requires structured output (specific sections for each area). These are two of XML's specific advantages.
- **Why A is wrong:** Multiple data sources and structured output requirements call for formal structure.
- **Why B is wrong:** While Markdown would work, nested data is harder to represent clearly with headers alone.
- **Why D is wrong:** The complexity of this task warrants more explicit structure than simple labels.

**However:** If the colleague is uncomfortable with XML, a well-organized Markdown or labeled structure would still produce good results. The "best" answer depends partly on user comfort.

---

### Question 8 (Multiple Choice)

What is "meta-prompting"?

A) Writing very long, detailed prompts
B) Using AI to analyze and improve your prompts
C) Prompting about metadata in documents
D) A format that only works with XML

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** Meta-prompting is asking the AI to act as a prompt engineer—analyzing your prompts for weaknesses and suggesting improvements. It works in any format:
  - Simple: "Analyze this prompt and suggest improvements: [paste prompt]"
  - Structured: Use any format to organize your meta-prompt request
- **Why D is wrong:** Meta-prompting works regardless of what format you're analyzing or using.

---

## Scoring Guide

- **8/8 correct:** Excellent! You understand prompt architecture and format flexibility. Ready for Module 4.
- **6-7 correct:** Good understanding. Review the concepts you missed before proceeding.
- **4-5 correct:** Rewatch the video and focus on the three format options and when to use each.
- **0-3 correct:** Schedule time to review Module 3 content thoroughly before proceeding.

---

*Quiz complete. Review the Study Guide for a quick reference summary.*
