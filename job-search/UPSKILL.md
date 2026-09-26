# Upskilling & Positioning — living doc

Last updated: 2026-09-26

## Verdict: your core skills are not outdated

10 years backend + 6 years EVM/Solana, with ERC-4337, ERC-4626, ERC-3643,
ERC-8004/8183, real audit experience (Quantstamp/Zellic), and production
Kafka/Redis indexers is a strong, current profile — this is senior/staff
material, not something needing a rebuild. The gaps below are about widening
reach and pricing power, not catching up.

## You already have the "AI-first" differentiator most Solidity engineers lack

OrgGPT (RAG pipeline, Anthropic + OpenAI SDKs, agentic retrieve-then-answer)
plus the ERC-8004/8183 agent marketplace at Nunchi means you can credibly
say you've shipped both the AI stack and the on-chain agent-commerce stack.
**Lead with this combination explicitly in your resume summary and cover
letters** — most job posts asking for "AI-first" Web3 engineers mean
"comfortable using Copilot," and you're a tier above that.

## Daily 30–60 min improvement plan (rotate through these)

1. **AI-in-dev-workflow (do this one most days):**
   - Use Claude Code / Cursor for a real task in a personal or OSS Solidity
     repo — not just autocomplete, but agentic multi-file changes, and note
     what breaks so you can speak to it in interviews.
   - Try an AI-assisted fuzzing/invariant-testing pass with Foundry (write
     the invariant, let the model draft edge cases) — this is a concrete,
     demoable skill for "AI + smart contract security" roles.
   - Once a week: use an LLM to review a real diff for reentrancy/oracle
     manipulation/access-control bugs *before* running Slither, then compare
     — build a personal sense of where LLM review is reliable vs. not. This
     is a strong interview story for security-adjacent roles.

2. **Protocol-surface breadth (fill real gaps):**
   - **Formal verification** (Certora or Halmos) — you have Slither/Trail of
     Bits already; formal verification is the next tier up and is explicitly
     requested by top-paying protocol/security roles.
   - **Cross-chain intents (ERC-7683)** and **EIP-7702** — natural extension
     of your ERC-4337 account abstraction work at Novastro; several of the
     roles in today's digest (Chainlink CCIP, Wormhole) sit exactly here.
   - **Restaking/AVS (EigenLayer)** — adjacent to your risk-engine/oracle
     work at Nunchi; a fast-growing hiring category.
   - **x402 / agentic payments** — direct extension of your ERC-8004 work;
     worth a weekend project (a minimal x402-paying agent) since this niche
     has very few engineers with real on-chain + agent experience.

3. **Solana/Rust depth (secondary track, don't over-invest):**
   - You have Anchor experience — keep it warm with 1 small program/week
     rather than a deep dive, since your primary market and comp ceiling is
     EVM. Treat Solana roles as optionality, not the main track.

## Positioning changes to make now (not daily, but soon)

- Add a one-line resume bullet under Skills or Summary explicitly naming
  "AI-assisted smart contract development & review workflow" — recruiters
  and ATS keyword-match on this for "AI-first" postings.
- Consider a short public writeup (blog/X thread) on the ERC-8004 agent
  marketplace you built at Nunchi — this is a genuinely rare, timely
  portfolio piece and agentic-commerce teams (Coinbase x402, Virtuals
  Protocol, Olas/Autonolas) are actively hiring for exactly this overlap.
