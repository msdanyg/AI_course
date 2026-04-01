# Module 10 Quiz
## Future Frontiers: Agents & MCP

**Instructions:** 7 questions. Mix of multiple choice, true/false with explanation, and scenario-based. Feedback provided for all answers.

---

### Question 1 (Multiple Choice)

**What is the key difference between "Tools" phase AI and "Agents" phase AI?**

A) Agents can access the internet; Tools cannot
B) Agents receive goals and autonomously execute multiple steps; Tools require human triggering for each action
C) Agents are faster than Tools
D) Tools can create files; Agents can only generate text

**Correct Answer:** B

**Feedback for B (Correct):**
Exactly right. The fundamental shift is operational autonomy:
- **Tools phase**: AI can do things (execute code, create files, search web), but humans trigger each action manually
- **Agents phase**: AI receives a goal, plans the approach, executes multiple steps, and iterates based on results

You define the mission objective; the agent executes the flight plan. This changes your role from "orchestrating every step" to "defining outcomes and reviewing results."

**Feedback for other answers:**
- **Option A**: Both Tools and Agents can access the internet (via Gemini grounding or MCP connections)
- **Option C**: Speed isn't the differentiator; operational autonomy is
- **Option D**: Both can create files; the difference is in autonomous vs. human-triggered execution

---

### Question 2 (True/False with Explanation)

**TRUE or FALSE: MCP (Model Context Protocol) allows AI to access external tools without requiring custom integration code for each tool.**

**Correct Answer:** TRUE

**Feedback if TRUE (Correct):**
Correct. MCP is like the "USB standard for AI." Before USB, every device needed a custom cable. Before MCP, every AI-to-tool connection required custom code.

MCP provides a standardized protocol so that:
- Tools built for MCP work with any MCP-compatible model
- Organizations can connect AI to databases, APIs, and file systems through standard interfaces
- The ecosystem of available capabilities grows much faster

This standardization is what makes scalable agent architectures practical.

**Feedback if FALSE (Incorrect):**
MCP's core purpose IS to eliminate the need for custom integration code. By providing a standardized protocol, MCP allows tools to be built once and work across MCP-compatible models. Think of it like USB—one standard connection instead of proprietary cables for every device. This standardization accelerates the ecosystem of agent capabilities.

---

### Question 3 (Multiple Choice)

**What is "goal thinking" in an agentic context?**

A) Setting ambitious targets for AI performance
B) Defining outcomes that may require multiple actions, rather than specifying individual tasks
C) Using visualization techniques to improve AI results
D) Planning AI implementation timelines

**Correct Answer:** B

**Feedback for B (Correct):**
Exactly. Goal thinking is the mindset shift required for working with agents.

**Task thinking** (traditional): "Summarize this document." "Create a chart." "Write an email."—single actions that you trigger and the AI executes.

**Goal thinking** (agentic): "Prepare me for my client meeting tomorrow." "Identify cost-saving opportunities in our software stack."—outcomes that may require multiple actions, where the agent determines the path.

The agent figures out what steps are needed. You define what success looks like.

**Feedback for other answers:**
Goal thinking isn't about ambition (A), visualization (C), or project timelines (D). It's specifically about defining outcomes rather than individual tasks, allowing agents to autonomously determine the execution path.

---

### Question 4 (Scenario-Based)

**Scenario:** You want to design an agent workflow for competitive monitoring. Which approach best demonstrates agent-ready design?

A) "Check competitor websites every Monday. If there are changes, notify me."
B) "Goal: Maintain current competitive intelligence. Success criteria: All competitor pricing changes detected within 24 hours; significant product announcements flagged with impact assessment; weekly summary generated automatically. Human checkpoint: Review before external distribution."
C) "Research competitors and write a report."
D) "Use Gemini to search for competitor news, then paste into Claude for analysis."

**Correct Answer:** B

**Feedback for B (Correct):**
This demonstrates proper agent-ready design:

1. **Goal-focused**: "Maintain current competitive intelligence" defines the outcome, not the steps
2. **Clear success criteria**: Specific, measurable outcomes the agent can evaluate
3. **Human checkpoint**: Defines where human review is required
4. **Autonomous scope**: Agent can determine how to achieve the criteria

This structure gives the agent clear direction while maintaining appropriate human oversight.

**Feedback for other answers:**
- **Option A**: Too task-focused (specifies "every Monday") and lacks success criteria
- **Option C**: Too vague—no success criteria, no human checkpoint
- **Option D**: Describes a manual workflow, not an agent-ready design

The key is defining outcomes and success criteria, not prescribing every action.

---

### Question 5 (Multiple Choice)

**Why does structured output (XML/JSON) become MORE important with agents?**

A) Agents can only read structured data
B) Structured output is faster to process
C) Agents need to pass information between steps reliably and interface with external systems that expect specific formats
D) Structured output uses fewer tokens

**Correct Answer:** C

**Feedback for C (Correct):**
Exactly. In agentic workflows, structure becomes essential because:

1. **Passing information between steps**: When an agent chains multiple actions, it needs to reliably transfer data from one step to the next
2. **Interfacing with external systems**: Databases, APIs, and other tools expect specific formats
3. **Making programmatic decisions**: If/Then logic requires parseable data

This is why your XML and structured prompting skills from Module 3 are agent-readiness skills. Structure is the programming language of autonomous workflows.

**Feedback for other answers:**
- **Option A**: Agents can process natural language, but structured data is more reliable
- **Option B**: Speed isn't the primary consideration
- **Option D**: Token usage isn't the key factor

The critical point is reliability in multi-step, multi-system workflows.

---

### Question 6 (True/False with Explanation)

**TRUE or FALSE: With AI agents, human oversight becomes less important because the AI can handle more autonomously.**

**Correct Answer:** FALSE

**Feedback if FALSE (Correct):**
Correct. Human oversight becomes MORE important with agents, not less.

Why? Because agents have greater capability to take actions with real-world consequences:
- They can access systems and data
- They can execute multi-step workflows
- Errors can cascade through chained actions
- The scope of potential impact increases

This is why agent design requires:
- **Permission boundaries**: What the agent can and cannot access
- **Human checkpoints**: Review points before consequential actions
- **Escalation triggers**: Conditions that stop automation and require human intervention
- **Audit trails**: Logs of what the agent did and why

The principle: "Agents execute. Humans remain accountable."

**Feedback if TRUE (Incorrect):**
Human oversight becomes MORE important with agents, not less. Greater autonomy means greater potential for impact—both positive and negative. Agent design requires careful permission boundaries, human checkpoints for consequential decisions, escalation triggers, and audit trails. The core principle: "You clear missions for takeoff and own what leaves the runway."

---

### Question 7 (Scenario-Based)

**Scenario:** You're designing an agent for Customer Success QBR preparation. The agent should analyze account data, identify trends, and generate a presentation draft. Where should you place the human checkpoint?

A) Before the agent starts—human should review the goal first
B) After data analysis but before presentation generation—human validates the insights
C) Only at the end—human reviews the final presentation
D) No checkpoint needed—the agent should handle everything autonomously

**Correct Answer:** B

**Feedback for B (Correct):**
Excellent choice. Placing the checkpoint after analysis but before deliverable creation is optimal because:

1. **Data gathering is low-risk**: The agent reading and analyzing data has limited downside
2. **Insights drive everything downstream**: If the analysis is wrong, the entire presentation will be wrong
3. **Early validation saves rework**: Catching a flawed insight before the presentation is built prevents wasted effort
4. **Final output inherits validated logic**: The presentation is built on human-approved conclusions

This "validate the thinking, not just the output" approach is a best practice in agent design.

**Feedback for other answers:**
- **Option A**: The goal has already been defined; reviewing it again adds friction without value
- **Option C**: Too late—if insights are wrong, you've wasted the agent's work generating a flawed presentation
- **Option D**: QBR presentations affect client relationships; human validation of insights is essential

The principle: Place checkpoints at decision points, not just at the end.

---

## Quiz Complete

**Score Interpretation:**

- **6-7 correct**: Future-ready. You understand the agentic paradigm and how to design for it.
- **4-5 correct**: Good foundation. Review the goal-thinking and governance concepts.
- **0-3 correct**: Revisit the lesson focusing on the Chat→Tools→Agents evolution and why human oversight increases with agent capabilities.

**Key Concepts to Master:**
1. Agents receive goals and autonomously execute; Tools require human triggering
2. MCP standardizes AI-to-tool connections (like USB for devices)
3. Goal thinking defines outcomes; task thinking specifies actions
4. Structured output is essential for reliable multi-step workflows
5. Human oversight becomes MORE important with increased autonomy
6. Place checkpoints at decision points, not just endpoints

---

**Proceed to Study Guide to consolidate your learning.**
