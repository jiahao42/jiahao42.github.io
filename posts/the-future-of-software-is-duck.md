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

It's also not a tooling problem, human has built Integrated Development Environment (IDE) to speed up the "knowledge decoding". But coding agents have been proven to do amazing things with simple tools (i.e. read, write, grep), they are the super coders with 1970s' tools. I doubt the agents will need complex harness in the future, and even if they do, Anthropic will know and fix it first.

To me, the problem is bigger - the shared decoded layer doesn't exist:      
*Human decodes privately, in their heads. Claude decodes privately, per session. No one is building a living, shared representation of what the codebase means - so every collaborator, human or AI, starts from zero.*

### Moving towards higher abstraction

Back in 2016, I was obsessed with reverse engineering, specifically binary analysis. One practice I had was - by looking at this C code, can I "compile" it in my head and imagine the corresponding disassembly code? It was hard but fun.

10 years later, LLM lifted the abstraction to a whole new level, everyone can "compile" human language to code. Put-ads-into-utility-app era is destined to end, everyone can one-shot utlility app now. Customized, ad-free, all you need is a couple dollar of tokens.

However, the "compilation" is crumbling in many places. It's forcing people to take code review more seriously ([exmaple](https://x.com/lukOlejnik/status/2031257644724342957)), but people will not be able to keep up with the exploded PRs.

*We believe that the paradigm shift of programming is in the right direction, but the shift is too lossy.*

### The spec-driven is dead, long live the spec-driven

For years, we've been building specs, but it's not well adopted. A couple of reasons:

1. Specs are written for humans, consumed once, then abandoned
They're a communication artifact, not a living artifact. The moment code diverges from the spec - which happens immediately - the spec becomes historical fiction.
2. Text is the wrong shape
A decoded codebase is a graph, but text forces you to linearize a non-linear thing, the reader has to reconstruct the graph in their head every time.
3. The "why" is never encoded
Text specs capture what at best. But the decisions - why this architecture, why this tradeoff - live in people's heads. The spec is a shadow of the actual knowledge.
4. Every reader starts from zero
Human or AI, each session re-decodes the codebase from scratch. The decoded understanding is never written back in a richer form. There's no accumulation. The codebase never gets smarter about itself.

But what if the spec is the decoded knowledge? What if *the spec is a graph*, not text?

*We believe that text spec is dead, and the journey of graph spec has just begun.*

### Rust, but for business rules

Anthropic chose Rust to build a C compiler, because Rust is memory-safe by construction - once it compiles, it almost certainly doesn't have memory bugs.

The underlying principle is interesting: the Rust compiler is the precise, unambiguous oracle that says yes or no, and the model doesn't need to understand memory safety; it just needs to produce code that passes the check.
This is the model running probabilistic attacks against a deterministic gate. It generates, fails, learns from the error, regenerates - thousands of times - until something gets through. The goal isn't comprehension, it's convergence.

*We believe that we need to build the Rust at a higher abstraction, e.g. business rules, if it compiles, it never breaks you business.*

### The missing layer

A new layer must emerge, and it should be able to:
* cover the lossy part towards higher abstraction
* preserve the decoded knowledge in a way that both human and AI can instantly understand
* be able to enforce ground truth on the probablistic models

*We believe a knowledge graph spec layer must exist, it's where human and AI collaborate to shape the software, and it will be the foundation of many AI-native software from the future.*

### The future of software is... Duck

In Python, if something walks like a duck and quacks like a duck, it's a duck.

In our ultimate vision, people don't interact with code anymore, they ask about software - if the graph spec shows the software does what you want, this is the software you need. I call it "duck software".

And that, is what we are building for the future.
