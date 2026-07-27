---
layout: post
title: The superhuman programmer from 1970s
pwd: posts
cmd: cat "The superhuman programmer from 1970s"
date: Jul 26 2026
tags: agents, code search, knowledge graph, AI
---

Take a good programmer from 1970s. Sit them in front of a terminal with `grep`, `find`, and a codebase they have never seen. They will get their bearings: search for a string, read the file, follow the call, search again. It works, because the thing running the loop is smart.

Now make them read a thousand times faster, never get bored, never lose the thread at 4pm, and run forty copies of themselves at once.

That is a coding agent, working like a superhuman from 1970s, which is the part worth staring at. Finding your way around a codebase is a problem we have been solving for fifty years, and are we going backwards now?

### Fifty years of finding things in code

Every generation of the problem has the same shape - somebody produces an index, somebody consumes it, somebody benefits.

| | Producer | Consumer | User |
|---|---|---|---|
| `grep`/`find` | string search | terminal | developer |
| `ctags`/`etags` | lexer/scanner | vim/emacs | developer |
| symbol-based codebase indexing | parser + symbol/dep graph | IDE (the JetBrains series) | developer |
| vector/embedding-based codebase indexing | embedding model | IDE (Cursor) / hosted service (Sourcegraph, Greptile) | developer |
| LLM agent | ??? | ??? | ??? |

Roughly on a timeline:

* **1970s** - `grep` and `find`. String search, no index at all.
* **1980s** - `ctags`/`etags`. A lexer walks the tree once and writes down where the names live.
* **2000s-2010s** - the IDEs. File-based, then AST-based. Famously "slow", because the index was local, and famously "dumb", until it finished building.
* **2016** - LSP, so nobody has to write that indexer once per editor.
* **2019** - LSIF, so the index can be precomputed on a server and the client doesn't have to build it at all.
* **2020** - vector and embedding retrieval, for the queries a symbol table can't answer.
* **2025** - `grep` and `find`.

### Running in circle?

**Era 1 - human as the index.** The developer holds the mental model. Navigation is manual: grep, read, follow the thread, grep again.

**Era 2 - precomputed symbolic index.** The machine holds the model. ctags → cscope → IDE indexes → LSP. Offload map-building to a persistent data structure. Behaviors are well-defined: find definition, find references.

**Era 3 - vector/semantic index.** The machine holds a *learned* model. Embedding retrieval for fuzzy queries.

**Era 4 - LLM agent + grep and find.** We are back in Era 1. The only difference is that the "human" doing the iterative exploration is an LLM. It reads a file, follows the imports, runs ripgrep, reads another file. Exactly what a developer did in the 1970s, just faster, in parallel, and without getting tired.

Line them up and the regression is hard to miss:

```
Era 1   code -> find/grep      -> index in a human brain -> write/review
Era 2   code -> parser/indexer -> symbolic index on disk -> index in a human brain (faster) -> write/review
Era 3   code -> embedding model-> neural index on disk   -> index in a human brain (faster) -> write/review
Era 4   code -> find/grep      -> index in an LLM context window -> write/review
```

Look like Era 4 is going backwards to Era 1? I don't think so, maybe just the tooling is, but the fact coding agents are so cheap and fast is a big step forward.

### The upward spiral

Given what we've discussed, it's not hard to see it's an upward spiral and where it's going:
1. Human's role: Human only needs to review code, which is arguably a thing that most people are never good at. Even at Google, I've seen the most rigorous reviews, and rubber stamps, and I have to say the former is rare.
2. Human's brain: There is no persistent layer like human brain, the coding agents rebuild their understanding every time in the context window.
3. Parallelism: Coding agents are so parallel, it brings up new problems on the old infra: is the filesystem fast enough? how to assign the tasks to reduce merge conflicts?

1 calls for the goverance layer, 2 calls for a persistent understanding and a memory layer, 3 calls for the agent-first infra.

Personally I am more interested in 2, specifically the persistent understanding.

### Outsource the understanding

<figure>
    <img src="../imgs/outsource-understanding-tweet.png" alt="Tweet asking whether understanding of a codebase can be outsourced"/>
    <figcaption>What if we can?</figcaption>
</figure>

A couple of pain points to incentivize us to solve the problem:

* **Context is built live, from scratch, every single time.** No session inherits anything from the last one.
* **That build *is* the work.** Half your tokens go to re-deriving what the codebase means before any code gets written, which means context rot.
* **You pay the full decoding cost per session.** Every session. Context switch is painful.
* **There's no way to supervise it.** The agent decided what your code means somewhere inside a 200k-token window, and neither you nor anyone else can inspect that decision, correct it, or make the correction stick.

I looked into the existing graph-based solutions, but they are not "upward" enough, feel like a product from Era 2 or Era 3. Sure, LLMs have abundant knowledge of graphs, they can navigate graphs well. But the end goal is to understand the code fast, if coding agents can just read the code 100x faster than human and understand, why do we need the code graphs? We need something new.
