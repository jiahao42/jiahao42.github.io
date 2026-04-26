---
layout: post
title: The future of software is... Duck
pwd: posts
cmd: cat "The future of software is... Duck"
date: Apr 22 2026
tags: software, programming, AI
---

The code in your codebase, is never the knowledge itself. Instead, it's the encoded knowledge organized in a way that human prefers.

* Every time you read the code, you decode it into knowledge, in your head.
* Every time you launch a Claude Code session, Claude decodes the it into knowledge, in the context window.

But we have a problem.

### The problem

It's not a memory problem, of course human has long-term memory, can even organize the knowledge in dreams, huge advantages against LLM. But companies like Letta or mem0 will solve it.

It's also not a tooling problem, tooling will evolve - but the bottleneck was never the tools. Agents today do remarkable things with read, write, and grep<sup>*</sup>. The constraint isn't what they can do; it's what they can figure out in the context window.

*: I call them "super codes from 1970s" :)

To me, the problem is bigger - the shared decoded layer doesn't exist:      
*Human decodes privately, in their heads. Claude decodes privately, per session. No one is building a living, shared representation of what the codebase means - so every collaborator, human or AI, starts from zero.*

### Moving towards higher abstraction

Back in 2016, I was obsessed with reverse engineering, specifically binary analysis. One practice I had was - by looking at this C code, can I "compile" it in my head and imagine the corresponding disassembly code? It was hard but fun.

10 years later, LLM lifted the abstraction to a whole new level, everyone can "compile" human language to code. Put-ads-into-utility-app era is destined to end, everyone can one-shot utility app now. Customized, ad-free, all you need is a couple dollar of tokens.

However, the "compilation" is crumbling in many places. It's forcing people to take code review more seriously ([example](https://x.com/lukOlejnik/status/2031257644724342957)), but people will not be able to keep up with the exploded PRs.

*The paradigm shift of programming is in the right direction, but the shift is too lossy.*

### Re-thinking spec

Specs were supposed to be the shared truth. They weren't.

The reason isn't that engineers are lazy or that specs are a bad idea. It's structural. Specs were written for humans, consumed once, then abandoned - a communication artifact, not a living one. The moment code diverges from the spec (which happens `O(hour)`), the spec becomes historical fiction. Nobody updates it because nobody has to.

Text also turns out to be the wrong shape. A decoded codebase is a graph - nodes, edges, dependencies, rationale. Text forces you to linearize something that is fundamentally non-linear. You lose the structure the moment you write it down.

And so every reader - human or AI - starts from zero. Each session re-decodes the codebase from scratch. The decoded understanding is never written back in a richer form. There's no accumulation. The codebase never gets smarter about itself.

But the instinct behind specs was right. What if the spec is the decoded knowledge? What if it's a live graph, not a document?

*Text spec is dead. The live graph spec is just beginning.*

### Rust, but for business rules

Anthropic chose Rust to build a C compiler, because Rust is memory-safe by construction - once it compiles, it almost certainly doesn't have memory bugs.

The underlying principle is interesting: the Rust compiler is the precise, unambiguous oracle that says yes or no, and the model doesn't need to understand memory safety; it just needs to produce code that passes the check.     
*This is a model running probabilistic attacks against a deterministic gate*. It generates, fails, learns from the error, regenerates - thousands of times - until something gets through. The goal isn't comprehension, it's convergence.

*We need to build Rust at a higher abstraction, e.g. business rules, if it compiles, it never breaks your business.*

### What's next?

The next layer needs to do three things: cover the lossy translation between intent and code, preserve decoded knowledge in a form both human and AI can instantly use, and enforce ground truth against the probabilistic models generating code beneath it.

*A knowledge graph spec layer must emerge, it's where human and AI collaborate to shape the software, and it will be the foundation of AI-native software going forward.*

#### A tiny example

A new engineer adds a "care coordinator" role. They grep for patient record access, find 4 files saying slightly different things, pick the one that looks most recent. Claude Code adds a billing integration - misses the Notion doc, exposes records to billing admins. The PR looks fine. It ships. The HIPAA rationale lived in someone's head, and that person left.

But imagine a graph bootstraps from your code automatically - it already knows `patient.record` requires role in `["doctor", "nurse"]`. A senior engineer notices the HIPAA edge is missing, adds it once. Now the care coordinator PR hits that node - hard stop, with the exact regulation attached. Claude Code's billing integration, same. The rule is permanent. The rationale doesn't disappear when the engineer leaves, because it was never in their head to begin with.

Why does every reader have pay the full decoding cost every time, when we only need to pay it once with the new layer?

### The future of software is... Duck

In Python, if something walks like a duck and quacks like a duck, it's a duck.

That's our ultimate vision for software: you don't verify code. You verify behavior. If the graph shows the software does what you need, i.e. expresses the right intent, enforces the right rules, then the implementation is irrelevant. It's the compiled artifact that nobody needs to read.

We're not there yet. Nobody is. But every layer of abstraction in computing history looked impossible until it didn't - and then it looked inevitable. Assembly to C. C to Python. Python to prompts.

The next layer is the meaning layer. The decoded, shared, living representation of what software actually does and why.

That's what I call "duck software". And we are building it now.
