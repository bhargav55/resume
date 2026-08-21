# Upskilling Roadmap

Living doc, updated as the market shifts. Goal: stay ahead on both the
"pure EVM/Solidity" axis and the "AI-first web3 team" axis, since job
postings increasingly blend the two (see G-20 Group example in digests/).

## Where you're already strong (lead with these in interviews)
- Perpetuals/CLOB matching engines, liquidation & risk engines (Nunchi.trade) — rare, high-value skill.
- Account abstraction (ERC-4337) across multiple chains incl. Avalanche subnet, Hyperledger Besu (Xalts).
- RWA tokenization (ERC-3643) with compliance/identity registries (Novastro).
- Real audit lifecycle ownership (Quantstamp, Zellic) — most Solidity devs only get "reviewed," not "own remediation."
- Already building agentic AI tooling for Web3 (AI smart-contract auditor, on-chain agent marketplace ERC-8004/8183) —
  this combination (EVM + agentic AI) is still uncommon; market it explicitly rather than burying it under "AI projects."

## Gaps worth closing (ranked by ROI for your target roles)
1. **Security depth / formal methods** — you have practical audit experience but not much formal verification.
   - Do: Cyfrin Updraft security courses, Secureum bootcamp epochs, Damn Vulnerable DeFi (all levels), Certora basics.
   - Payoff: senior/staff Solidity roles increasingly expect "can lead audits," not just "pass them."
2. **Gas optimization & assembly/Yul** — a differentiator at senior level, comes up often in interviews for protocol teams (Ondo, Silo-tier).
   - Do: rebuild one of your existing contracts (e.g. a liquidation flow) in Huff or heavy Yul, benchmark gas.
3. **Cross-chain / intent-based architectures** — RWA and perps protocols are moving toward cross-chain settlement (LayerZero, Across, intents).
   - Do: ship a small demo integrating LayerZero or a solver/intents flow into an existing personal project.
4. **Solana/SVM depth** — you have Anchor experience (Hatchy.fun) but it's secondary; don't over-invest unless a specific
   role needs it, but keep it current enough to not fall behind (SVM is increasingly asked about even in EVM-primary roles).

## AI-in-developer-workflow (do this regardless of which company you join)
Companies going "AI-first" mostly mean: engineers who use AI tools to move faster and safer, not just people who
build AI products. Concretely:
- **Daily driver**: use Claude Code / Cursor for Solidity+Foundry workflows — test generation, fuzz harness scaffolding,
  PR review pre-pass before human review. Being able to talk about *how* you use these in an interview is now a real signal.
- **Extend your AI Smart-Contract Auditor project**: add a benchmark against a public exploit dataset (e.g. rekt.news
  incidents) and publish results — this becomes a portfolio piece that demonstrates both Solidity and AI-agent skill
  in one artifact, directly relevant to "AI-first" web3 teams.
- **MCP tooling**: you already list MCP tool calling — package the Slither+MCP auditor as an installable MCP server
  others can plug into their own agents. Turns a resume bullet into a public, checkable artifact (GitHub stars/usage).
- **Structured evals**: your resume already mentions eval frameworks — reuse that muscle to build a small eval suite
  for "does an LLM correctly flag reentrancy/access-control bugs in N sample contracts." Strong technical blog post material.

## Portfolio/visibility actions (do 1/week)
- Publish one write-up per month combining EVM security + AI agents (e.g. "using an LLM agent to triage Slither output").
- Keep GitHub repos (ai-rag-pipeline, AI Smart-Contract Auditor) documented with README + demo GIF — recruiters and
  hiring managers skim, they don't clone.
- Contribute one small PR/fix to a well-known open-source protocol repo (Foundry, OpenZeppelin, a DeFi protocol) —
  a merged PR is a stronger signal than another private project.

## Interview prep cadence
- 2x/week: one round of Damn Vulnerable DeFi or a Secureum-style CTF challenge.
- 1x/week: mock system design for a perps/derivatives or RWA protocol (your actual work areas) — practice explaining
  trade-offs out loud, since staff-level interviews weight this heavily.
