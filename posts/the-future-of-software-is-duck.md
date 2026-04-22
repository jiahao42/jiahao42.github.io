---
layout: post
title: The future of software is... Duck
pwd: posts
cmd: cat "The future of software is... Duck"
date: Apr 22 2026
tags: software, programming, AI
---

The code in your codebase, is never the knowledge itself. Instead, it's the encoded knowledge organized in a way that human prefers.

Every time you read the code, you decode it into knowledge, in your head.
Every time you launch a Claude Code session, Claude decodes the it into knowledge, in the context window.

But we have a problem.

### The problem

It's not a memory problem, of course human have long-term memory, can even organize the knowledge in dreams, that's huge advantage against LLM. But companies like Letta or mem0 will solve it.

It's also not a tooling problem, human has built Integrated Development Environment (IDE), leveraging various tools to speed up the "knowledge decoding". But coding agents have been proven to do amazing things with simple tools (i.e. read, write, grep), they are like the super coders with 1970s' tools. I doubt the agents will need complex harness in the future, and even if they do, Anthropic will know and fix it first.

To me, the problem is bigger - there's no shared decoded layer:      
Human decodes privately, in their heads. Claude decodes privately, per session. No one is building a living, shared representation of what the codebase means - so every collaborator, human or AI, starts from zero.

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

But what if the spec is the decoded knowledge? What if **the spec is a graph**, not text?

### 

### Rust for business rules

### Duck software


And that, is what I am building for the future.
