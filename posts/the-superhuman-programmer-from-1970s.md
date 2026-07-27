---
layout: post
title: The superhuman programmer from 1970s
pwd: posts
cmd: cat "The superhuman programmer from 1970s"
date: Jul 26 2026
tags: agents, code search, knowledge graph, AI
---

Take a good programmer from the 1970s. Sit them in front of a terminal with `grep`, `find`, and a codebase they have never seen. They will get their bearings: search for a string, read the file, follow the call, search again. It works.

Now make them read a thousand times faster, never get bored, never lose the thread at 4pm, and run forty copies of themselves at once.

That is a coding agent. And the analogy is flattering until you push on it one step further, because the 1970s programmer had something the agent does not: six months from now, they still know the codebase. The agent starts from zero at the beginning of every session, forever.

Finding your way around a codebase is a problem we have been working on for fifty years. It is worth asking what we kept and what we quietly threw away.

### Fifty years of finding things in code

Every generation of the problem has the same shape - somebody produces an index, somebody consumes it, somebody benefits.

| | Producer | Consumer | User |
|---|---|---|---|
| `grep`/`find` | string search | terminal | developer |
| `ctags`/`etags` | lexer/scanner | vim/emacs | developer |
| symbol-based codebase indexing | parser + symbol/dep graph | IDE (the JetBrains series) | developer |
| vector/embedding-based codebase indexing | embedding model | IDE (Cursor) / hosted service (Sourcegraph, Greptile) | developer |
| LLM agent | the agent | the same agent | the same agent |

That last row is the whole post. In every row above it, the producer and the consumer are different things, which means the index is an artifact: it survives the query that created it, and somebody other than its author can read it. In the last row, producer, consumer, and user collapse into one process, and the index it builds has a lifetime of one session.

Roughly on a timeline:

* **1970s** - `grep` and `find`. String search, no index at all.
* **1980s** - `ctags`/`etags`. A lexer walks the tree once and writes down where the names live.
* **2000s-2010s** - the IDEs. File-based, then AST-based. Famously "slow", because the index was local, and famously "dumb", until it finished building.
* **2016** - LSP, so nobody has to write that indexer once per editor.
* **2019** - LSIF, so the index can be precomputed on a server and the client doesn't have to build it at all.
* **2020** - vector and embedding retrieval, for the queries a symbol table can't answer.
* **2021-2024** - Copilot, then RAG over code as the default retrieval story.
* **2025** - `grep` and `find`.

### Running in circles?

**Era 1 - human as the index.** The developer holds the mental model. Navigation is manual: grep, read, follow the thread, grep again.

**Era 2 - precomputed symbolic index.** The machine holds the model. ctags → cscope → IDE indexes → LSP → LSIF. Map-building is offloaded to a persistent data structure. Behaviors are well-defined: find definition, find references.

**Era 3 - vector/semantic index.** The machine holds a *learned* model. Embedding retrieval for the fuzzy queries a symbol table was never going to answer.

**Era 4 - LLM agent + grep and find.** The iterative exploration is back, and the thing doing it is an LLM. It reads a file, follows the imports, runs ripgrep, reads another file. Exactly what a developer did in the 1970s, just faster, in parallel, and without getting tired.

Line them up and watch where the understanding ends up:

```
Era 1   code -> find/grep       -> index in a human brain                           -> write/review
Era 2   code -> parser/indexer  -> symbolic index on disk -> index in a human brain -> write/review
Era 3   code -> embedding model -> neural index on disk   -> index in a human brain -> write/review
Era 4   code -> find/grep       -> index in an LLM context window                   -> write/review
```

Brain, brain, brain, context window.

Eras 1 through 3 all end in the same place: a person who understands the code. The disk index was never the seat of that understanding, it was a cache that made loading it faster. Era 4 removed the cache *and* the thing it was caching for.

### The thing we threw away

* **Context is built live, from scratch, every single time.** No session inherits anything from the last one.
* **That build *is* the work.** Half your tokens go to re-deriving what the codebase means before any code gets written, which is also how you get context rot.
* **You pay the full decoding cost per session.** Every session. Context switching is expensive again.
* **There is no way to supervise it.** The agent decided what your code means somewhere inside a 200k-token window. Neither you nor anyone else can inspect that decision, correct it, or make the correction stick.

The last one is the real problem, and it is qualitatively different from the first three. Cheaper tokens fix cost. Bigger windows fix rot. Neither of them makes the agent's understanding of your codebase into something a second agent can read, a human can review, or a correction can be applied to.

Eras 1 through 3 had two durable stores, and it's worth separating them. The disk index held structure, and it was machine-readable, precomputable, shared across an org. The brain held meaning, and it was persistent, correctable, and transferable - you could ask the person, disagree with them in review, and have the correction stick.

Era 4 dropped both. Grep replaced the disk index. A context window replaced the brain. The brain was genuinely the bottleneck on speed and parallelism, and we fixed speed and parallelism by removing the only persistent thing in the pipeline.

### Outsource the understanding

<figure>
    <img src="../imgs/outsource-understanding-tweet.png" alt="Tweet asking whether understanding of a codebase can be outsourced"/>
    <figcaption>What if we can?</figcaption>
</figure>

Three things follow from Era 4:

**A governance layer.** The human's remaining job is review, which is a thing most people are never good at. At Google I saw the most rigorous reviews I have ever seen, and I saw rubber stamps, and the second was more common.

**Agent-first infrastructure.** Forty agents in parallel breaks assumptions that were fine for forty humans. Is the filesystem fast enough? How do you assign work to minimize merge conflicts?

**A persistent understanding layer.** Somewhere for the meaning of the codebase to live that isn't a context window.

I care most about the third one.

The obvious candidates already exist and none of them are it. Code graphs index structure - symbols, calls, imports - which is exactly the thing an agent now rederives in twenty seconds with ripgrep. AGENTS.md and its cousins are the right instinct on the wrong substrate: hand-written, unverifiable, stale the week after somebody writes them. Both rebuild the disk index. Neither replaces the brain.

The bar I'd set is a single sentence: correct the agent once, and have the correction survive the session. Not a better retrieval story - a store you can disagree with.

I don't think anyone has that right yet, myself included. But the shape of the thing is starting to look less like an index and more like a codebase's understanding of itself, kept somewhere you can read it.
