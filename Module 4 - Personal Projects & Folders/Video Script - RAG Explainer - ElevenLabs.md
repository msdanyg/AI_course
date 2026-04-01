# Module 4: RAG Explainer - ElevenLabs V3 Optimized
## "How Claude Projects Remember Without Memorizing"

**Duration:** ~6 minutes
**Optimized for:** ElevenLabs V3 Studio (Audio-only delivery)
**Voice Direction:** Professional but conversational, educational tech explainer, warm and approachable

---

<voice style="conversational-professional">

Large language models like Claude... they're powerful tools. They get some things amazingly right, and other things—well, <prosody rate="95%">interestingly</prosody> wrong.

I want to tell you about a framework that helps Claude be more accurate and more up to date when working with your company's information.

<break time="0.5s" />

It's called <emphasis level="moderate">Retrieval Augmented Generation</emphasis>... or <prosody rate="90%">R-A-G</prosody>.

<break time="1s" />

Let's just talk about the <emphasis level="moderate">generation</emphasis> part for a minute. Forget the retrieval augmented part for now. The generation refers to large language models, or LLMs, that generate text in response to your questions—what we call prompts. These models can have some undesirable behavior. Let me give you an example.

<break time="1s" />

Let's say someone on your sales team asks me this question. What integrations does ActivTrak support for calendar and scheduling tools?

And my response is, oh, great question. I know this. I reviewed our integration documentation last quarter. We support Google Calendar, Outlook, and Office three sixty five. That's the answer.

<break time="1s" />

Now, there are actually a couple of things wrong with my answer. First, I have <emphasis level="strong">no source</emphasis> to support what I'm saying. Even though I confidently said I reviewed the documentation, I'm not pointing to it. I'm giving the answer off the top of my head. And second, I actually haven't kept up with this for a while, and my answer is <emphasis level="strong">out of date</emphasis>. In the past three months, we added Microsoft Teams scheduling integration and Slack status sync.

So we have two problems here. <emphasis level="moderate">No source</emphasis>, and <emphasis level="moderate">out of date</emphasis>.

<break time="1s" />

Now, what would have happened if I'd taken a beat and <emphasis level="moderate">first</emphasis> gone to look up the answer in our current product documentation? Well, then I would have been able to say, according to our latest integration docs, ActivTrak supports Google Calendar, Outlook, Office three sixty five, Microsoft Teams scheduling, Slack status sync, and Zoom meeting detection. And this list keeps growing as our engineering team adds new integrations.

I have now <emphasis level="moderate">grounded</emphasis> my answer in something more reliable. I have not hallucinated or made up outdated information.

<break time="1s" />

All right, so what does this have to do with Claude? Let's say you're in a standard Claude chat and you ask, what integrations does ActivTrak support? A standard large language model would confidently say, based on what I learned during my training, ActivTrak supports integrations with, and then it lists some. The answer might be wrong or incomplete. But Claude is very confident in what it answered because that's what it learned during training, which ended months ago.

<break time="1s" />

Now, what happens when you add this <emphasis level="moderate">retrieval augmented</emphasis> part? That means that instead of just relying on what Claude learned during training, we're adding a <emphasis level="moderate">knowledge base</emphasis>—a content store. This could be open, like the internet. Or it can be closed, like a collection of your company's documents. Product specs, pricing sheets, competitive briefs, customer success guides.

The point now is that Claude <emphasis level="moderate">first</emphasis> goes and talks to your knowledge base and says, hey, can you retrieve for me information that is relevant to this user's question?

And now, with this retrieval augmented answer, it's not outdated training data anymore. Claude pulls from <emphasis level="strong">your current documentation</emphasis> and gives an accurate, sourced response.

<break time="1s" />

So what does this look like in practice? Here's how RAG works, step by step.

Step one. You ask Claude a question inside your Project. What integrations does ActivTrak support?

Step two. Without RAG, Claude would just say, based on my training, here's what I know.

But <emphasis level="moderate">with RAG</emphasis> in a Claude Project, Claude has an instruction that says, no, no, no. First, go and search the uploaded files. Find relevant content. Combine that with the user's question, and <emphasis level="moderate">then</emphasis> generate the answer.

<break time="1s" />

So the prompt Claude receives now has <prosody rate="95%">three</prosody> parts. First, the instruction to pay attention to retrieved content. Second, the retrieved content from your uploaded files. And third, the user's question. Now generate a response. And Claude can even give <emphasis level="moderate">evidence</emphasis> for why its response was what it was, citing specific documents.

<break time="1s" />

So how does RAG solve the two challenges I mentioned earlier? Let's talk about problem number one, <emphasis level="strong">out of date</emphasis>. Instead of having to retrain Claude every time new information comes up, like when ActivTrak adds a new integration, all you have to do is <emphasis level="moderate">update</emphasis> your knowledge base with the new product documentation. The next time someone asks the question, Claude automatically retrieves the most up to date information.

Problem number two, <emphasis level="strong">no source</emphasis>. Claude is now being instructed to <emphasis level="moderate">pay attention</emphasis> to primary source data before generating its response. It can cite which document it pulled from. This makes it <emphasis level="moderate">less likely</emphasis> to hallucinate or make up information, because it's relying on your uploaded files instead of just its training data.

It also allows Claude to have a very positive behavior, knowing when to say <emphasis level="strong">I don't know</emphasis>. If your question can't be reliably answered based on the uploaded documents, Claude should say, I don't see information about that in the uploaded files. Could you provide more context or upload the relevant documentation? This is much better than making up something believable that could mislead you.

<break time="1s" />

This is exactly what happens when you create a Claude Project. You upload your ActivTrak documentation. Competitive briefs, product specs, pricing sheets, positioning guides. Claude automatically indexes these files, converting them into searchable numerical fingerprints called <emphasis level="moderate">embeddings</emphasis>.

When you ask a question, Claude searches <emphasis level="moderate">semantically</emphasis>, not just for keywords, but for <emphasis level="moderate">meaning</emphasis>. If you ask, how do we compare to Teramind on privacy, Claude understands you're asking about competitive positioning, privacy philosophy, and differentiation, even if those exact words aren't in your files. It retrieves the most relevant chunks and synthesizes an answer grounded in your documentation.

<break time="1s" />

Claude automatically switches between two modes based on how much you've uploaded. <emphasis level="moderate">Full Context Mode</emphasis> activates when you have small knowledge bases, less than two hundred thousand tokens. In this mode, Claude reads <emphasis level="moderate">all</emphasis> your files into working memory. <emphasis level="moderate">RAG Mode</emphasis> activates when you have large knowledge bases, <emphasis level="moderate">more</emphasis> than two hundred thousand tokens. In this mode, Claude searches and retrieves relevant chunks on demand.

The transition is seamless. You don't need to do anything. Claude handles it automatically. This gives you a <emphasis level="strong">ten times</emphasis> capacity expansion. Instead of twenty files, you can upload two hundred.

<break time="1s" />

To get the best results from Claude Projects, follow these five optimization tips.

First, use Markdown when possible. It's easier for Claude to parse than PDFs.

Second, structure documents with clear headers. RAG retrieves by section.

Third, remove redundant content. Don't upload two hundred page reports with repeated footers.

Fourth, keep file names descriptive. Claude uses them as context clues.

And fifth, don't over upload. Only include directly relevant files.

<break time="1s" />

One limitation. If the retrieval step doesn't find the right information, Claude might say I don't know even when the answer is buried somewhere in your files. This is why file organization matters. Clear headers, good structure, and relevant uploads help Claude retrieve accurately.

<break time="1s" />

So that's <emphasis level="moderate">Retrieval Augmented Generation</emphasis>, the technology that lets Claude Projects give you accurate, sourced, up to date answers without retraining the model every time your company's information changes. You're not just chatting with an AI. You're chatting with an AI that has <emphasis level="strong">instant access</emphasis> to your mission headquarters knowledge base. That's the power of RAG. And that's why Claude Projects eliminate the context rebuild tax.

<break time="1s" />

Now that you understand how RAG works behind the scenes, you're ready to build your first Claude Project. In the full lesson, you'll learn how to upload files, write custom instructions that apply to every chat, and test that everything works correctly. The lab exercise will walk you through creating a LinkedIn Content Studio project, where you'll see RAG in action as Claude references your uploaded brand guidelines and past posts.

After you complete the lab, test your understanding with the knowledge check quiz. And remember, the study guide provides a one page quick reference for everything we covered today.

Let's get started building your first project.

</voice>
