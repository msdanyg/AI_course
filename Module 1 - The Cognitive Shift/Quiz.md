# Module 1: The Cognitive Shift
## Knowledge Check Quiz

**Instructions:** Answer all questions. Review feedback after each answer to reinforce learning.

---

### Question 1 (Multiple Choice)

What is the primary difference between a search engine and a reasoning engine?

A) Search engines are faster than reasoning engines
B) Search engines retrieve existing content; reasoning engines generate new content by predicting probable next words
C) Reasoning engines only work with structured data
D) Search engines require more context to produce results

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** Search engines like Google match keywords to existing indexed content and return links. Reasoning engines like Claude generate responses by predicting the most likely next token based on patterns learned during training. This fundamental difference changes how you should communicate with each tool.
- **Why A is wrong:** Speed varies by implementation and isn't the defining characteristic.
- **Why C is wrong:** Reasoning engines can work with unstructured text—that's one of their strengths.
- **Why D is wrong:** Actually, more context can *hurt* reasoning engine performance (the Water Glass Effect).

---

### Question 2 (True/False with Explanation)

**Statement:** Pasting more information into a Claude prompt always improves the quality of the response.

A) True
B) False

**Correct Answer:** B (False)

**Feedback:**
This is one of the most common mistakes when transitioning from search engines to reasoning engines. The "Water Glass Effect" demonstrates that irrelevant context actually *degrades* AI reasoning capability. Information in a prompt competes for the model's attention. Irrelevant details scatter attention away from the core task, leading to unfocused or off-topic responses. Squadron Leaders curate context ruthlessly, including only what's needed for the specific task.

---

### Question 3 (Multiple Choice)

A CSM pastes a 30-message email thread into Claude and asks "what should I do about this account?" The response fixates on a mention of a team lunch instead of addressing the renewal risk discussed in the thread. This is an example of:

A) The model lacking business knowledge
B) The Water Glass Effect
C) A context window limitation
D) The model being too creative

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** The Water Glass Effect occurs when irrelevant details in a prompt distract the model from the core reasoning task. The team lunch mention was a "distractor" that pulled attention away from the actual business question.
- **Why A is wrong:** The model likely has relevant business knowledge—the issue is attention allocation, not knowledge gaps.
- **Why C is wrong:** A 30-message thread wouldn't exceed Claude's context window. The problem is context *quality*, not *quantity*.
- **Why D is wrong:** This isn't about creativity—it's about the model not filtering noise effectively when reasoning.

**The fix:** Structure the prompt to explicitly state what to focus on ("Identify renewal risks") and what to ignore ("Ignore discussion of social events").

---

### Question 4 (Scenario-Based)

You need to prepare a competitive analysis comparing ActivTrak to a competitor. Which approach best reflects the Squadron Leader model?

A) Paste the competitor's website content and ActivTrak's feature list into Claude and ask for a comparison

B) Ask Claude to research the competitor, summarize findings, write the analysis, and critique its own work—all in one prompt

C) Use Gemini to gather verified competitor information, then feed that fact brief to Claude along with structured instructions to synthesize a strategic comparison

D) Use three separate Claude conversations: one for research, one for writing, one for editing

**Correct Answer:** C

**Feedback:**
- **Why C is correct:** This exemplifies the Squadron Leader approach—specialized tools for specialized tasks. Gemini (Recon) handles real-time research with grounded citations. Claude (Mission Control) handles strategic synthesis and writing. Each tool does what it's optimized for.
- **Why A is wrong:** This Solo Pilot approach dumps everything into one interaction without structure. It also relies on Claude for research when Gemini has better access to current web data.
- **Why B is wrong:** Asking one agent to research AND write AND critique creates an "identity crisis." These tasks require conflicting cognitive modes.
- **Why D is wrong:** While this separates tasks, it doesn't use the right tool for research. Claude can't access live web data the way Gemini can, so the "research" conversation would rely on training data that might be outdated.

---

### Question 5 (Multiple Choice)

What is the "Lost in the Middle" phenomenon, and how should it affect your prompt structure?

A) AI models forget information over long conversations, so keep conversations short
B) AI models pay less attention to information in the middle of the context window, so place critical instructions at the beginning or end
C) AI models can only process middle-complexity tasks, not simple or complex ones
D) Information in the middle of documents is usually less important, so AI correctly ignores it

**Correct Answer:** B

**Feedback:**
- **Why B is correct:** Research shows that attention mechanisms in language models assign higher weights to tokens at the beginning and end of the context window. Information in the middle receives diluted attention. This means prompt structure matters: put orientation at the beginning, data in the middle, and instructions at the end.
- **Why A is wrong:** While context can degrade over very long conversations, "Lost in the Middle" specifically refers to attention distribution within a single prompt, not across conversation turns.
- **Why C is wrong:** This misinterprets the phrase entirely—it's about positional attention, not task complexity.
- **Why D is wrong:** The phenomenon is about model behavior, not about what information is actually important.

---

### Question 6 (True/False with Explanation)

**Statement:** When analyzing ActivTrak workforce data with AI, framing your prompt as "Find who's underperforming" versus "Identify teams that might need additional support" will produce essentially the same output.

A) True
B) False

**Correct Answer:** B (False)

**Feedback:**
Prompt framing significantly shapes AI output. When you frame analysis as finding "underperformers," the AI adopts a surveillance/punitive lens—looking for individuals to blame, focusing on deficits, potentially reinforcing bias. When you frame it as identifying "teams needing support," the AI adopts a consultative lens—looking for systemic factors, focusing on resources and enablement, aligning with "Insights, Not Oversight."

This isn't just about optics. The framing changes what patterns the model looks for and how it interprets ambiguous data. A 15% drop in productivity could be framed as "concerning underperformance" or "expected transition cost during EHR implementation"—same data, radically different implications.

---

### Question 7 (Scenario-Based)

A colleague shares this prompt with you and asks why it's not working well:

> "Here's a bunch of stuff about our Q3 results and also the competitive landscape and I talked to some customers last week and there's a new product feature coming. Can you help me figure out the strategy and also write a summary and maybe suggest some KPIs?"

Identify TWO specific problems with this prompt and suggest a fix for each.

**Model Answer:**

**Problem 1: No clear single task**
The prompt asks for "strategy," "summary," AND "KPIs"—three different deliverables with different requirements. This creates an identity crisis where the AI tries to address everything shallowly.

*Fix:* Break into separate, focused prompts. Or, if one output is needed, specify priority: "Primary task: Identify top 3 strategic priorities. Secondary: Suggest one KPI for each priority."

**Problem 2: Unstructured context dump**
"A bunch of stuff" and "some customers" provide no structured data. The AI has no way to know what's relevant or how different pieces connect.

*Fix:* Use the mission briefing structure:
- [CONTEXT] Q3 performance summary: [specific data]
- [DATA] Competitive intelligence: [specific findings]
- [DATA] Customer feedback themes: [structured list]
- [TASK] Based on the above, identify the top 3 strategic priorities for Q4

**Additional issues participants might identify:**
- No role/persona specified
- No output format defined
- Vague language ("help me figure out")
- No constraints or focus areas

---

## Scoring Guide

- **7/7 correct:** Excellent! You've internalized the cognitive shift. Ready for Module 2.
- **5-6 correct:** Good foundation. Review the concepts you missed before the next module.
- **3-4 correct:** Rewatch the video and review flashcards, then retake the quiz.
- **0-2 correct:** Schedule time with your manager to discuss the module content before proceeding.

---

*Quiz complete. Proceed to the Study Guide for a quick reference summary.*
