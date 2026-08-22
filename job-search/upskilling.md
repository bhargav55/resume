# Upskilling recommendations

Baseline: 8+ years total, ~5 years deep Solidity/EVM (options, perps CLOB,
account abstraction, RWA tokenization, agent marketplaces ERC-8004/8183),
audit experience (Quantstamp, Zellic, Slither, Trail of Bits), plus a real
AI/LLM layer already (RAG pipeline, MCP tool calling, LangChain/LangGraph,
agentic Slither-based auditor). This is already a strong, differentiated
profile — few Solidity engineers also ship agentic tooling. Recommendations
below build on that instead of starting from scratch.

## Where the market is going AI-first (and what to do about it)

- **AI-assisted smart contract auditing is becoming table stakes.** Keep
  extending the "AI Smart-Contract Auditor" project — add more historical
  exploit classes to the RAG knowledge base (reentrancy, oracle
  manipulation, access control, ERC-4626 inflation attacks), and publish
  benchmark results (precision/recall vs known bug datasets like
  DeFiHackLabs or SmartBugs). This is a strong portfolio piece to point to
  in interviews for "AI-first" web3 shops.
- **Agentic on-chain execution is a hiring signal right now.** The
  Nunchi.trade work (AI-native CLI for liquidation/TP-SL, ERC-8004/8183
  agent marketplace) is directly on-trend — keep it prominent, it's
  probably the single strongest differentiator on the resume.
- **Add daily-use AI dev tooling to the actual workflow**, not just as a
  project: Claude Code / Cursor for Solidity + TS work, Foundry's `forge`
  scripted with LLM-assisted fuzz/invariant test generation, and Slither +
  an LLM pass for first-draft audit triage before human review. If not
  already doing this daily, it's worth 15-30 min/day to build fluency —
  interviewers increasingly ask "how do you use AI in your dev loop."

## Where EVM skills could use refreshing (given 8yrs+ generalist EVM background)

- **Formal verification**: Certora Prover or Halmy/hevm symbolic execution.
  Senior/staff DeFi roles at protocols handling real TVL (Silo, Framework
  Ventures portfolio) increasingly expect this alongside Slither/fuzzing.
- **L2/rollup internals**: OP Stack or Arbitrum Orbit/Nitro internals,
  since a growing share of "EVM engineer" postings are actually rollup or
  appchain teams. Even a weekend building a minimal OP Stack devnet is a
  good talking point.
- **Restaking/AVS (EigenLayer)**: relevant given the agent-marketplace and
  liquidation-bot work — restaking is the emerging trust layer for
  autonomous on-chain agents and keeper networks.
- **ERC-7579 modular accounts**: the account abstraction ecosystem moved
  past plain ERC-4337 into modular smart accounts (Safe modules, Rhinestone,
  ZeroDev kernel) — worth a refresher since the Xalts AA experience predates
  this shift.

## Rust/SVM (secondary skill)

Given primary focus is EVM, don't over-invest here, but keep the
Hatchy.fun/Anchor experience current: skim Solana's Token Extensions
(Token-2022) and any updates to Anchor's security best practices
(re-entrancy on CPI, account validation macros) every couple of weeks
rather than a deep dive — enough to speak fluently if an SVM role comes up.

## Suggested weekly cadence (30-45 min/day)

1. One audit-style read of a recent DeFi exploit post-mortem (rekt.news) —
   feed notable new exploit patterns into the AI auditor's knowledge base.
2. One Foundry invariant/fuzz test written against a public protocol repo
   (or your own past work) using an LLM to help draft the invariant.
3. Skim one job posting from a top-tier protocol's careers page (not just
   aggregators) to track what "senior" now expects — requirements drift
   fast in this market.
