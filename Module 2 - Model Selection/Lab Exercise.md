# Module 2: Model Selection & The "Thinking" Protocol
## Lab Exercise: The Workforce Optimization Challenge

**Duration:** 15-20 minutes
**Tools Required:** Claude (claude.ai) with access to model selection

---

## Objective

Experience the dramatic difference between a fast model without deep reasoning and a strategic model with Extended Thinking. You'll see how the same prompt produces very different results—and learn to read the Thinking block to verify AI's work.

---

## The Challenge

A workforce manager needs to optimize labor allocation. This problem involves multiple variables, tradeoffs, and requires actual math—not just pattern-matching.

**Copy this prompt exactly:**

```
A workforce manager oversees a team of 12 employees who each work 8-hour shifts. She has budget to add 40 additional labor hours per week and wants to maximize productivity output. Historical data shows:

Morning shifts (6am-2pm) produce 15 units/hour per employee
Afternoon shifts (2pm-10pm) produce 12 units/hour per employee
Adding hours to already-scheduled employees reduces their productivity by 8% per overtime hour
New part-time hires produce at 70% efficiency for their first 4 weeks

Should she extend existing employee hours, hire part-time workers, or use a hybrid approach? What allocation maximizes output over the next 8 weeks?
```

---

## Part 1: Run with Haiku (No Extended Thinking)

1. Open Claude and select **Haiku**
2. Make sure Extended Thinking is **OFF**
3. Paste the prompt and submit
4. **Save or screenshot the response**

### Record Your Observations:

- Did Haiku give a recommendation? ☐ Yes ☐ No
- Did it show calculations? ☐ Yes ☐ Partial ☐ No
- Did it quantify the output for each option? ☐ Yes ☐ No
- How confident do you feel in the answer? ☐ High ☐ Medium ☐ Low

---

## Part 2: Run with Opus + Extended Thinking

1. Switch to **Opus**
2. Enable **Extended Thinking**
3. Paste the **same prompt** and submit
4. **Before reading the final answer**, expand the Thinking block

### Examine the Thinking Block:

This is the key learning moment. Open the collapsible Thinking section and observe:

**How did Opus approach the problem?**
- ☐ Broke down the problem into components
- ☐ Defined variables and assumptions
- ☐ Calculated output for each option separately
- ☐ Compared options quantitatively
- ☐ Considered the 8-week timeframe (part-timers improve after week 4)
- ☐ Self-corrected or revised calculations

**What assumptions did Opus make explicit?**
Write them here:
1. _________________________________
2. _________________________________
3. _________________________________

**Could you follow the math?** ☐ Yes ☐ Mostly ☐ No

---

## Part 3: Compare the Results

Now compare your two responses side-by-side.

| Question | Haiku | Opus |
|----------|-------|------|
| What recommendation did it give? | | |
| Did it calculate units produced per option? | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Did it account for the 8% overtime penalty? | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Did it account for 70% part-timer efficiency? | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Did it consider part-timers improving after week 4? | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Did it show its work? | ☐ Yes ☐ No | ☐ Yes ☐ No |

**Did both models reach the same conclusion?** ☐ Yes ☐ No

**If different, which answer do you trust more? Why?**

_________________________________________________________________

---

## Part 4: Reflection Questions

Answer these based on what you observed:

1. **Could you verify Haiku's answer?** If not, what would you need to do to trust it?

2. **What did the Thinking block reveal that the final answer didn't?**

3. **For a decision that affects real employees and budget, which response would you present to leadership?**

4. **How long did each model take?** Was the extra time for Opus worth it for this type of problem?

---

## Key Takeaways

1. **Haiku is fast but may skip steps.** For simple tasks, this is fine. For multi-variable optimization, you can't verify the reasoning.

2. **Extended Thinking shows the work.** You can follow the logic, catch errors, and understand the assumptions.

3. **The Thinking block is your audit trail.** When stakes are high, five seconds of reading it can save hours of fixing mistakes.

4. **Match the model to the mission.** This workforce problem has real consequences—it deserves the Strategist, not the Scout.

---

## Success Criteria

You've completed this lab successfully if you can:

- [ ] Explain why Haiku's answer was harder to verify
- [ ] Identify at least two things Opus considered that Haiku missed
- [ ] Read the Thinking block and follow the reasoning process
- [ ] Articulate when Extended Thinking is worth the extra time

---

*Lab complete. Proceed to the Module 2 Quiz when ready.*
