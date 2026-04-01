# Module 3: The Reasoning Engine
## Flashcards

---

### Card 1

**Front:**
What is "context bleeding" and why does it happen?

**Back:**
**Context bleeding** occurs when different parts of a prompt contaminate each other—when the AI confuses instructions with data, or includes constraint language in its output.

**It happens because:** Without clear separation (using tags, headers or labels), the AI processes everything as one continuous stream of text and can misinterpret what's an instruction vs. what's content.

**Example:** Writing "Don't use the word tracking" in a prompt and having the AI include that phrase in its response as if it were content.

---

### Card 2

**Front:**
What are the three format options for structuring prompts?

**Back:**
| Format | Syntax | Best For |
|--------|--------|----------|
| **XML Tags** | `<tag>content</tag>` | Complex prompts, nested data, templates, structured outputs |
| **Markdown Headers** | `## Section Name` | Narrative prompts, people uncomfortable with XML, documentation-style |
| **Clear Sections** | `LABEL: content` | Simple tasks, beginners, when formal structure feels like overkill |

**Key insight:** All three work—choose based on comfort level and task complexity. The goal is clear separation, not a specific syntax.

---

### Card 3

**Front:**
When is XML superior to other formatting options?

**Back:**
XML is superior when you need:

1. **Nesting complex data** - Tags inside tags (e.g., client_info, metrics, and communications all inside user_data)

2. **Structured output** - Asking Claude to return data in specific format signals you're comfortable with structured responses

3. **Reusable templates** - Clear placeholders like `[CLIENT_NAME]` work well in XML

4. **Edge cases with formatting conflicts** - When your data contains Markdown formatting that might confuse the structure

---

### Card 4

**Front:**
When do you NOT need formal structure in prompts?

**Back:**
**Skip formal structure when:**
- Task is simple and single-purpose
- You're having a back-and-forth conversation
- Your natural writing is already clear
- You're asking a quick question

**Use structure when:**
- Multiple data sources
- Several distinct requirements
- Getting inconsistent results
- Creating reusable templates

**Key principle:** The goal is clarity, not ceremony. Match complexity to the task.

---

### Card 5

**Front:**
How can you ask Claude to structure messy data for you?

**Back:**
Simply ask Claude to convert unstructured information into a structured format:

**Example prompt:**
> "Here are my rough notes from the client call. Please convert them into a structured format with these sections: Client Goals, Concerns Raised, Action Items, Next Steps. Use XML tags."

**When to use this:**
- Working with messy meeting transcripts
- Data scattered across multiple sources
- Creating consistent formats for recurring tasks

**Pro tip:** You can then use Claude's structured output as clean input for your next prompt.

---

### Card 6

**Front:**
What are the six standard components every structured prompt should include?

**Back:**
| Component | Purpose |
|-----------|---------|
| **Role** | Who the AI should be |
| **Context** | Background situation and goals |
| **Data** | The actual content to process |
| **Constraints** | What NOT to do |
| **Output Format** | Desired structure |
| **Examples** | (Optional) Sample outputs to emulate |

**The order matters:** Role/Context at the beginning, Data in the middle, Instructions/Format at the end (due to "Lost in the Middle" effect).

---

### Card 7

**Front:**
What are five common prompt mistakes and their fixes?

**Back:**
| Mistake | Fix |
|---------|-----|
| **Overloading** (research + write + critique) | Separate tasks across tools/conversations |
| **Vague outputs** ("make it better") | Specify exactly what "better" means |
| **Missing constraints** | Always include what to AVOID |
| **Buried instructions** | Place key instructions at the END |
| **Over-engineering** | Match structure complexity to task complexity |

---

### Card 8

**Front:**
What is meta-prompting and how can you use it?

**Back:**
**Meta-prompting** is asking AI to act as a prompt engineer and improve your prompts—using the tool to sharpen the tool.

**Simple approach:**
> "I have a prompt giving inconsistent results. Analyze it and suggest improvements: [paste prompt]"

**When to use:**
- Debugging prompts that give poor outputs
- Creating reusable templates for your team
- Learning why certain prompt structures work

**Key insight:** Works in any format—you don't need to use XML to meta-prompt.

---

## Study Tips

1. **Start simple:** Begin with Clear Sections format, graduate to Markdown or XML as needed
2. **Don't over-engineer:** A simple task deserves a simple prompt
3. **Remember the goal:** Clear separation of concerns, not specific syntax
4. **Use Claude to help:** Ask Claude to structure messy data or improve your prompts
5. **Place instructions last:** Takes advantage of the "Lost in the Middle" effect
