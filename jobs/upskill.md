# Upskilling Roadmap — Updated April 29, 2026

## Your Current Skill Assessment

### Strengths (keep sharpening)
- **Solidity / EVM** — Production-grade, security-audited, complex DeFi protocols. Top 5% of the market.
- **On-chain AI agents** — ERC-8004/8183 agent marketplace is ahead of the curve. 2026's hottest niche.
- **DeFi derivatives** — CLOB+AMM, perpetuals, options, clearing house. High-value, low-supply skill.
- **Smart contract security** — Slither, Trail of Bits, Quantstamp/Zellic audit experience. Most devs lack this.
- **Cross-chain** — EVM + Solana (Rust/Anchor) + Aptos (Move). Broad coverage is rare.

### Skills That Need Work (honest gaps vs. 2026 market)
See below for prioritized roadmap.

---

## PRIORITY 1 — Zero-Knowledge Proofs (biggest gap, biggest leverage)

**Why:** ZK is no longer research — it's production infra. zkEVMs (Polygon zkEVM, zkSync Era, Scroll), ZK coprocessors (Axiom, RiscZero), and ZK proofs for on-chain verification are now mainstream hiring requirements at top protocols. Companies like Starkware, Aztec, Scroll, and Espresso are hiring heavily.

**What to learn:**
- Circom + snarkjs (1-2 weeks to get basics)
- Noir language (Aztec's ZK language — simpler than Circom, growing fast)
- ZK coprocessors: Axiom and RiscZero for off-chain compute verified on-chain
- How zkEVMs differ from regular EVM (important for deployment)

**Resources:**
- 0xparc.org/circom — best Circom curriculum
- noir-lang.org/docs — Noir by Aztec
- docs.axiom.xyz — ZK coprocessor for Ethereum
- docs.risc0.com — zkVM for Rust (your Rust skills apply here!)

**Time investment:** 4–6 weeks for working knowledge that shows up on your resume.

---

## PRIORITY 2 — Intent-Based Protocols & Account Abstraction v2 (medium gap)

**Why:** You have ERC-4337 experience (Xalts). The next wave is ERC-7521 (generalized intents), ERC-7683 (cross-chain intents), and EIP-7702 (EOA-to-smart-account upgrade). Every major protocol is integrating intents in 2026.

**What to learn:**
- ERC-7521 — generalized intent standard
- ERC-7683 — cross-chain intents (Uniswap X, Across Protocol use this)
- EIP-7702 — EOA delegation (massive UX shift)
- Solver networks (how fillers/solvers work in intent architecture)

**Resources:**
- eips.ethereum.org — read ERC-7521, 7683, EIP-7702
- docs.across.to — production cross-chain intent system
- uniswap.org/whitepaper/uniswap-x.pdf — intent-based DEX

**Time investment:** 2–3 weeks. Your ERC-4337 foundation makes this fast to pick up.

---

## PRIORITY 3 — AI Developer Tooling Integration (already started — double down)

**Why:** You already shipped Claude Code skills and an AI-native CLI at Nunchi. Companies with "AI-first" engineering orgs want engineers who use AI tools in their actual workflow, not just who know about them. This is your biggest differentiator RIGHT NOW — make it louder.

**What to do:**
- Document and open-source your Claude Code skills (or write a blog post)
- Build/publish an MCP server for a web3 use case (e.g., Foundry test runner, contract deployment tool)
- Add AI-assisted formal verification to your workflow (Halmos + AI)
- Contribute to an open-source AI agent framework (ElizaOS, Olas, GAME by Virtuals)

**Why this matters:** Ritual, Gensyn, and any AI+crypto company will pay a 20-30% premium for engineers who can ship AI-native tooling. You're already there — make it visible.

---

## PRIORITY 4 — Formal Verification & Advanced Security (high value, less urgent)

**Why:** You've worked with external auditors. The next level is writing specs yourself — this unlocks audit firm roles ($150-$350/hr contract) and staff-level protocol roles.

**What to learn:**
- Halmos — symbolic execution for Foundry tests (Rust-based, fast)
- Certora Prover — formal verification (industry standard for top protocols)
- Echidna — property-based fuzzing (you may already use this)
- Mutation testing with Vertigo or similar

**Resources:**
- github.com/a16z/halmos
- docs.certora.com
- Secureum bootcamp (free, async)

**Time investment:** 4–8 weeks for Certora certification (adds significant resume weight).

---

## PRIORITY 5 — Restaking & AVS Development (emerging, medium urgency)

**Why:** EigenLayer restaking and Actively Validated Services (AVSs) are a new primitive. Symbiotic, Karak, and others are competing. Protocol engineers who understand how to build AVSs are rare and well-paid.

**What to learn:**
- EigenLayer AVS architecture
- EigenDA (data availability layer)
- Symbiotic vaults
- How your oracle/automation experience maps to AVS use cases

**Time investment:** 2–3 weeks to understand, then contribute to or fork an existing AVS.

---

## ARE YOUR SKILLS OUTDATED? — Honest Assessment

**No — your core skills are not outdated.** EVM/Solidity remains dominant. DeFi derivatives knowledge is more valuable in 2026 than 2024. Your RWA tokenization work (ERC-3643) is increasingly relevant as institutions enter DeFi.

**However, these are declining signals:**
- Hardhat as primary framework → Foundry has won. You list both which is fine, but emphasize Foundry.
- .Net/C#/jQuery (early career) — keep these off the resume entirely if possible; they suggest web2 and don't help.
- "Backend stack: MongoDB, Postgres" without mentioning your indexing work is underselling.

**These are rising signals you already have but should highlight more:**
- AI-native developer tooling (ERC-8004, Claude Code skills, AI CLI)
- Security audit involvement (Quantstamp, Zellic co-working)
- On-chain agent marketplace design

---

## RESUME QUICK WINS (do these today)

1. **Add metrics** — "Cleared $X in liquidations", "Protocol TVL of $X", "N audited contracts". Quantify impact.
2. **Rename "Protocol Engineer" at Nunchi to be more specific** — e.g., "Smart Contract Architect, Perpetuals & AI Agents" if accurate.
3. **Add a "Key Protocols & Tools" line** — Foundry, Hardhat, Slither, Echidna, Pyth, Stork, The Graph, Chainlink, EigenLayer (if applicable).
4. **Add GitHub links to open-source work** — Recruiters at top protocols check GitHub before interviews.
5. **Remove OpenText/TCS details** — these are web2 roles from 2015-2020. Keep company name + title only, or drop entirely. They dilute your web3 signal.
6. **Surface the agent marketplace work** — ERC-8004/8183 is niche and impressive. Give it its own bullet at the top of Nunchi.

---

## DAILY LEARNING SCHEDULE (30 min/day)

| Day | Focus |
|-----|-------|
| Mon | ZK proofs (Noir or Circom) — 1 circuit per week |
| Tue | Read 1 EIP/ERC (current: ERC-7521, 7683, EIP-7702) |
| Wed | Security: 1 CTF challenge on Ethernaut or Damn Vulnerable DeFi |
| Thu | AI tooling: build or extend an MCP server or agent integration |
| Fri | Read 1 audit report (Code4rena, Sherlock, Cantina) |
| Sat | Contribute to open source or write about your work |
| Sun | Review week, update job applications, track pipeline |

---

## TOP JOB BOARDS — bookmark these

| Board | Best for | URL |
|-------|----------|-----|
| web3.career | Freshest listings, good filters | https://web3.career/solidity-jobs |
| cryptojobslist.com | Salary-listed roles | https://cryptojobslist.com/solidity |
| crypto.jobs | High volume | https://crypto.jobs |
| remote3.co | Remote-only | https://remote3.co |
| web3vacancy.com | DeFi specific | https://web3vacancy.com/jobs/defi |
| Glassdoor | Salary data + corporate web3 | https://glassdoor.com |

---

*Last updated: 2026-04-29. Re-run `bash ~/resume/jobs/search.sh` daily for fresh links.*
