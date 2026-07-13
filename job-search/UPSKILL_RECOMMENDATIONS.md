# Upskilling & Positioning Recommendations

Living doc, updated as part of the daily job-search routine. Goal: keep your Solidity/EVM +
TypeScript profile sharp for an AI-first web3 hiring market.

## You're already ahead on AI

Most Solidity engineers aren't shipping AI-native tooling. You already have:
- An AI-native CLI at Nunchi.trade that lets autonomous agents execute liquidation/TP-SL jobs.
- ERC-8004/ERC-8183 on-chain agent marketplace experience — this is a genuinely rare,
  in-demand combination (agent standards + perps infra).
- An agentic AI smart-contract auditor (LLM + MCP + Slither + exploit knowledge base).

Lead with these on your resume/LinkedIn headline, not just "Solidity engineer" — companies
going AI-first want to see you've already integrated AI into production trading
infrastructure, not just used ChatGPT to write code.

## Daily habits to stay sharp

1. **Use an agentic coding tool in your actual workflow** (Claude Code, Cursor) for at least
   one real task a day — writing tests, drafting NatSpec, triaging a Slither finding. Being
   able to talk fluently about *how* you use AI in a smart-contract workflow (and its
   limitations for security-critical code) is now a real interview topic.
2. **Read one audit report a day** from a recent Code4rena/Sherlock/Cantina contest. You
   already have real audit-lifecycle experience (Quantstamp, Zellic) — staying current on
   new exploit classes keeps that edge sharp.
3. **Track one perps/derivatives protocol's GitHub** (Hyperliquid, Drift, GMX, Vertex) for
   design decisions — directly relevant to your CLOB/liquidation-engine background.

## Skill gaps worth closing (nothing is "outdated," but these compound your strengths)

- **Formal verification / invariant testing** — Foundry fuzzing you likely already do; add
  Certora or Halmos for a project to show you can reason about protocol-level invariants,
  not just unit tests. High-value for perps/derivatives roles where a bug moves real capital.
- **Restaking / AVS design (EigenLayer)** — adjacent to your agent-marketplace and oracle
  work (Pyth/Stork); several EVM infra teams are hiring specifically for this.
- **Intents & solver architecture** (CoW Protocol, UniswapX-style) — increasingly replacing
  naive matching engines; your CLOB experience transfers directly, worth a weekend project.
- **Vyper** — a handful of perps protocols (Curve-adjacent teams) prefer it; even reading
  fluency is enough to not be screened out.
- **Deeper Rust/Anchor** — you have Solana experience via Hatchy.fun; if you want to keep SVM
  roles open (recommended given how much of the AI-agent-on-chain activity is happening on
  Solana right now), doing one more substantial Anchor program keeps that credible.

## Positioning

- Your resume line "I build products that move real capital" is strong — keep it as the
  headline everywhere (LinkedIn, cover letters).
- Pin the AI Smart-Contract Auditor repo and add a short demo video/GIF — recruiters at
  AI-first web3 shops filter on visible proof, not just resume bullets.
- Given the CLOB/liquidation/perps concentration in today's leads, consider a short
  (300-word) write-up on your Nunchi.trade matching-engine + liquidation design — this is
  exactly what perps protocols ask about in interviews, and having it written up saves you
  re-explaining it from scratch each time.

---
*This file grows over time — new entries get appended by later runs rather than rewriting
what's already here, unless something becomes stale.*
