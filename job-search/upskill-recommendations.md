# Positioning & upskilling recommendations

Last updated: 2026-09-08. This is a living doc — update it when the market picture
changes materially, not on every daily run.

## Where you're already ahead (lean into this, don't undersell it)

Your resume already lists Anthropic SDK, OpenAI SDK, RAG pipelines, multi-agent
orchestration, and a shipped product (OrgGPT) with real architecture (durable
ingestion, code-aware chunking, Qdrant, agentic retrieve-then-answer with citations).
Most Solidity engineers do not have this. Two concrete moves:

- **Don't bury it under "AGENTS" as a side project.** Most web3 teams hiring in
  2026 explicitly want engineers who use AI tools well *and* can build agentic
  products, not just prompt a chatbot. Consider a one-line callout in your summary:
  "...plus production RAG/agent systems (OrgGPT)" so it's visible before a recruiter
  has to scroll.
- **Your ERC-8004/8183 agent marketplace work is the single hottest overlap of your
  two skill areas right now** — on-chain agent identity/commerce standards are a
  2026 growth area (agent-to-agent payments, x402-style flows, agentic DeFi). Very
  few candidates can credibly claim both "shipped a perps CLOB" and "shipped an
  on-chain agent marketplace + a RAG SaaS." Make this pairing the centerpiece of your
  pitch, not a footnote.

## Daily habit: put AI into the actual smart-contract workflow

Since you already have the AI tooling background, the fastest daily improvement is
using it *inside* the Solidity workflow itself, and being able to talk about it in
interviews as workflow, not just novelty:

- Use an agentic coding tool (Claude Code, Cursor) for Foundry test scaffolding and
  invariant-test generation, then hand-review — teams increasingly ask "how do you use
  AI day to day" as a real interview question, not small talk.
- Pair Slither/static-analysis output with an LLM triage pass to cut false-positive
  review time — directly extends the audit-lifecycle experience already on your
  resume (Quantstamp/Zellic).
- Try an LLM-assisted fuzzing/property-generation pass on top of Foundry invariant
  tests for one of your past protocols (vaults/perps) as a portfolio artifact you can
  discuss concretely.

This is a workflow upgrade, not a new skill to learn from scratch — you already have
the components (Foundry, Slither, RAG/agent tooling); the gap is just wiring them
together and having a specific story ready.

## Actual skill gaps worth closing (EVM market, 2026)

Your core EVM/DeFi depth (perps, options, AA, RWA, vaults, audits) is strong and
current. The gaps are more about breadth into adjacent hot areas that keep showing up
in senior JDs:

1. **ERC-7702** (EOA→smart-account upgrade path, live since Pectra) — a natural
   extension of your existing ERC-4337 experience. Worth a weekend building a small
   demo so you can speak to it specifically; it's becoming a common JD keyword.
2. **Cross-chain messaging** (Chainlink CCIP, LayerZero, Wormhole) — you already have
   the oracle-integration angle (Pyth/Stork/Chainlink); CCIP specifically is a short
   hop from that and shows up in the Chainlink Labs role above.
3. **Restaking / AVS development (EigenLayer)** — complements your security-review
   background; worth reading EigenLayer's AVS dev docs even before applying, since it
   comes up as its own interview topic.
4. **Formal verification** (Certora, Halmos, symbolic execution) — you list Slither +
   Trail of Bits tooling but not formal methods. Senior/audit-adjacent roles
   increasingly expect at least familiarity; a small Halmos exercise on one of your
   existing vault contracts would be a fast, concrete way to close this.
5. **L2/rollup internals** (OP Stack, Arbitrum Orbit, ZK rollups) — your work has been
   contract-level across chains, not rollup/infra-level. Not urgent, but roles like BOB
   (OP Stack bridge) sit right at this intersection with your AA background — worth
   skimming OP Stack docs before an interview there specifically.
6. **Intents/solvers (ERC-7683)** — smaller trend, lower priority, but keep it on the
   radar since it's showing up increasingly in DeFi protocol job descriptions.

None of these are "your skills are outdated" — your core stack is squarely what the
market is hiring for. Treat the list above as targeted breadth to pick up opportunistically
(ideally by building one small demo per item), not a sign you need to relearn
fundamentals.
