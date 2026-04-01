# Module 4: RAG Explainer Video Script
## "How Claude Projects Remember Without Memorizing"

**Duration:** ~6 minutes
**Visual Style:** Animated diagrams showing information flow
**Tone:** Clear, conversational, building understanding progressively

---

## SCRIPT

**[00:00 - Opening]**

Large language models like Claude. They're powerful tools.

They get some things amazingly right, and other things... well, interestingly wrong.

My name is [Your Name], and I work in Product Marketing at ActivTrak.

And I want to tell you about a framework that helps Claude be more accurate and more up to date when working with your company's information:

**Retrieval-Augmented Generation**, or **RAG**.

**[SCREEN: Title card - "RAG: Retrieval-Augmented Generation"]**

---

**[00:22 - The Generation Problem]**

Let's just talk about the "Generation" part for a minute. Forget the "Retrieval-Augmented" for now.

The generation refers to large language models, or LLMs, that generate text in response to your questions—what we call prompts.

These models can have some undesirable behavior. Let me give you an example.

**[00:38 - The Anecdote]**

Let's say someone on your sales team asks me this question:

*"What integrations does ActivTrak support for calendar and scheduling tools?"*

And my response is: "Oh, great question! I know this—I reviewed our integration documentation last quarter. We support Google Calendar, Outlook, and Office 365. That's the answer."

**[SCREEN: Visual of confident person giving answer with thought bubble showing "Last Quarter"]**

**[01:00 - Two Problems]**

Now, there are actually a couple of things wrong with my answer.

First, **I have no source** to support what I'm saying. Even though I confidently said "I reviewed the documentation," I'm not pointing to it. I'm giving the answer off the top of my head.

**[SCREEN: "Problem #1: No Source"]**

And second, I actually haven't kept up with this for a while, and **my answer is out of date**. In the past three months, we added Microsoft Teams scheduling integration and Slack status sync.

**[SCREEN: "Problem #2: Out of Date"]**

So we have two problems here: **no source**, and **out of date**.

**[01:30 - The Better Way]**

Now, what would have happened if I'd taken a beat and first gone to look up the answer in our current product documentation?

**[SCREEN: Person pausing, then searching documentation]**

Well, then I would have been able to say:

*"According to our latest integration docs, ActivTrak supports Google Calendar, Outlook, Office 365, Microsoft Teams scheduling, Slack status sync, and Zoom meeting detection. And this list keeps growing as our engineering team adds new integrations."*

**[SCREEN: Accurate, sourced answer with document icon]**

I have now **grounded my answer** in something more reliable. I have not hallucinated or made up outdated information.

---

**[02:00 - How Claude Without RAG Would Answer]**

All right, so what does this have to do with Claude?

Let's say you're in a standard Claude chat and you ask:

*"What integrations does ActivTrak support?"*

**[SCREEN: User asking question to Claude in standard chat]**

A standard large language model would confidently say:

*"Based on what I learned during my training, ActivTrak supports integrations with..."*

**[SCREEN: Claude responding with outdated information]**

The answer might be wrong or incomplete. But Claude is very confident in what it answered because that's what it learned during training—which ended months ago.

**[02:30 - Enter RAG]**

Now, what happens when you add this **retrieval-augmented** part?

That means that instead of just relying on what Claude learned during training, we're adding a **knowledge base**—a content store.

**[SCREEN: Diagram showing Claude + Knowledge Base]**

This could be open, like the internet. Or it can be closed, like a collection of your company's documents—product specs, pricing sheets, competitive briefs, customer success guides.

**[SCREEN: Folder icons representing uploaded documents]**

The point now is that Claude **first goes and talks to your knowledge base** and says:

*"Hey, can you retrieve for me information that is relevant to this user's question?"*

**[SCREEN: Animated arrow showing Claude querying the knowledge base]**

And now, with this retrieval-augmented answer, it's not outdated training data anymore. Claude pulls from **your current documentation** and gives an accurate, sourced response.

**[SCREEN: Updated, accurate answer with source citation]**

---

**[03:15 - How RAG Works Step-by-Step]**

So what does this look like in practice?

**Step 1:** You ask Claude a question inside your Project.

**[SCREEN: "What integrations does ActivTrak support?"]**

**Step 2:** Without RAG, Claude would just say: "Based on my training, here's what I know."

**[SCREEN: Standard generative response]**

But **with RAG** in a Claude Project, Claude has an instruction that says:

*"No, no, no. First, go and search the uploaded files. Find relevant content. Combine that with the user's question, and THEN generate the answer."*

**[SCREEN: Animated flow diagram]**
- Step 1: User question
- Step 2: Search knowledge base
- Step 3: Retrieve relevant chunks
- Step 4: Combine question + retrieved content
- Step 5: Generate grounded response

**[04:00 - The Three-Part Prompt]**

So the prompt Claude receives now has **three parts**:

1. **The instruction** to pay attention to retrieved content
2. **The retrieved content** from your uploaded files
3. **The user's question**

**[SCREEN: Visual breakdown of the three-part prompt]**

Now generate a response. And Claude can even give **evidence** for why its response was what it was, citing specific documents.

---

**[04:20 - How RAG Solves the Two Problems]**

So how does RAG solve the two challenges I mentioned earlier?

**Problem #1: Out of Date**

Instead of having to retrain Claude every time new information comes up—like when ActivTrak adds a new integration—all you have to do is **update your knowledge base** with the new product documentation.

**[SCREEN: Adding new document to Project]**

The next time someone asks the question, Claude automatically retrieves the most up-to-date information.

**Problem #2: No Source**

Claude is now being instructed to **pay attention to primary source data** before generating its response. It can cite which document it pulled from.

**[SCREEN: Response with "Source: ActivTrak_Integrations_Guide_Q1_2026.pdf"]**

This makes it **less likely to hallucinate** or make up information, because it's relying on your uploaded files instead of just its training data.

It also allows Claude to have a very positive behavior: **knowing when to say "I don't know."**

**[05:00 - Knowing When to Say "I Don't Know"]**

If your question can't be reliably answered based on the uploaded documents, Claude should say:

*"I don't see information about that in the uploaded files. Could you provide more context or upload the relevant documentation?"*

**[SCREEN: Claude declining to answer confidently without source]**

This is much better than making up something believable that could mislead you.

---

**[05:20 - How This Works in Claude Projects]**

This is exactly what happens when you create a **Claude Project**.

You upload your ActivTrak documentation—competitive briefs, product specs, pricing sheets, positioning guides.

**[SCREEN: Files being uploaded to a Claude Project]**

Claude automatically indexes these files—converting them into searchable "numerical fingerprints" called **embeddings**.

**[SCREEN: Visual of documents being converted to embeddings]**

When you ask a question, Claude searches semantically—not just for keywords, but for **meaning**.

If you ask *"How do we compare to Teramind on privacy?"*, Claude understands you're asking about competitive positioning, privacy philosophy, and differentiation—even if those exact words aren't in your files.

**[SCREEN: Semantic search visualization]**

It retrieves the most relevant chunks and synthesizes an answer grounded in your documentation.

---

**[05:50 - When RAG Activates]**

Claude automatically switches between two modes based on how much you've uploaded:

**Full Context Mode** (<200K tokens): Claude reads ALL your files into working memory.

**RAG Mode** (>200K tokens): Claude searches and retrieves relevant chunks on demand.

**[SCREEN: Visual showing the threshold and two modes]**

The transition is seamless. You don't need to do anything—Claude handles it automatically. This gives you a **10x capacity expansion**: instead of 20 files, you can upload 200.

---

**[06:10 - Optimizing for RAG]**

To get the best results from Claude Projects:

1. **Use Markdown when possible**—it's easier for Claude to parse than PDFs
2. **Structure documents with clear headers**—RAG retrieves by section
3. **Remove redundant content**—don't upload 200-page reports with repeated footers
4. **Keep file names descriptive**—Claude uses them as context clues
5. **Don't over-upload**—only include directly relevant files

**[SCREEN: Checklist visual with these 5 tips]**

---

**[06:30 - Potential Limitations]**

One limitation: if the retrieval step doesn't find the right information, Claude might say "I don't know" even when the answer is buried somewhere in your files.

This is why file organization matters. Clear headers, good structure, and relevant uploads help Claude retrieve accurately.

**[SCREEN: Well-organized vs poorly-organized document structure]**

---

**[06:45 - Conclusion]**

So that's **Retrieval-Augmented Generation**—the technology that lets Claude Projects give you accurate, sourced, up-to-date answers without retraining the model every time your company's information changes.

You're not just chatting with an AI. You're chatting with an AI that has **instant access to your Mission Headquarters knowledge base**.

**[SCREEN: Claude Projects interface with uploaded files]**

That's the power of RAG. And that's why Claude Projects eliminate the Context Rebuild Tax.

In the full lesson, you'll learn how to build your first Project, write custom instructions, and test that everything works.

**[SCREEN: "Ready to build your first Project? Let's go." with arrow pointing to full lesson]**

Thank you for watching, and let's get started.

**[END]**

---

## Visual Cues Summary

- **00:00**: Title card with "RAG: Retrieval-Augmented Generation"
- **00:38**: Animated person confidently giving outdated answer
- **01:00**: "Problem #1: No Source" and "Problem #2: Out of Date" on screen
- **01:30**: Person searching documentation before answering
- **02:00**: Standard Claude chat interface
- **02:30**: Diagram: Claude + Knowledge Base (folder icons)
- **03:15**: Animated flow diagram of RAG process
- **04:00**: Three-part prompt breakdown visual
- **04:20**: Adding document to Project animation
- **05:00**: Claude declining to answer without source
- **05:20**: Files uploading to Claude Project
- **05:50**: Full Context vs RAG Mode threshold diagram
- **06:10**: Optimization checklist (5 tips)
- **06:30**: Well-organized vs poorly-organized docs comparison
- **06:45**: Claude Projects interface closing shot

---

## Production Notes

- **Pace**: Slightly faster than conversational (aiming for 6 min total)
- **Pauses**: 1-2 second pauses after key concepts (RAG, retrieval, embeddings)
- **Emphasis**: Bold words in script indicate vocal emphasis
- **Tone**: Friendly, educational, building understanding progressively
- **Transitions**: Use "Now..." and "So..." to signal topic shifts
- **Visuals**: Each screen direction should appear for 3-5 seconds minimum for comprehension
