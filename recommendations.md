# Skill Analysis & Upskill Roadmap — Bhargav Kacharla

*Last updated: 2026-04-28*

---

## YOUR CURRENT POSITION IN THE MARKET

You are a **senior Protocol Engineer** with 4+ years of dedicated web3 experience and 9+ years total engineering. Your profile is genuinely strong. Key differentiators:

- **Perpetuals/CLOB depth**: Full stack — orderbook matching, clearing house, risk engine, liquidations. Very few engineers have built all of this.
- **Multi-chain breadth**: EVM (primary), Solana/Anchor, Aptos/Move — rare combination.
- **Security track record**: Worked with Quantstamp + Zellic on audits, uses Slither + Trail of Bits tooling. Most devs skip this.
- **AI-native tooling**: Shipped an AI CLI + on-chain agent marketplace (ERC-8004/8183). You're ahead of 95% of the market here.
- **RWA + compliance**: ERC-3643 work at Novastro — niche but growing fast.

**Salary range you should target**: $160k–$250k + token allocation (remote). Don't undersell.

---

## SKILL GAP ANALYSIS

### Critical Gaps (Fix These First)

#### 1. Zero Knowledge Proofs (ZK)
**Gap level: High | Timeline to fix: 3–6 months**

This is the biggest gap. Almost every major EVM protocol (Ethena, dYdX V4, Synthetix, Euler) is moving toward ZK settlement or ZK proofs for specific operations. Companies like Aztec, StarkWare, Scroll, Polygon zkEVM, zkSync are well-funded and hiring.

**What to learn:**
- **Noir** (by Aztec) — closest to Solidity syntax, best entry point for Solidity engineers
- **Circom** — most widely used today; Tornado Cash, Semaphore, Worldcoin use it
- **SP1 / Risc0** — zkVMs, write Rust programs that produce ZK proofs (your Rust background helps)
- **Halo2** — advanced, used by Zcash, PSE group. Skip for now unless going deep.

**Resources:**
- [Noir docs + tutorials](https://noir-lang.org/docs)
- [0xparc ZK Learning Group](https://learn.0xparc.org/)
- [ZK Whiteboard Sessions (YouTube)](https://www.youtube.com/playlist?list=PLj80z0cJm8QErn3akRcqvxUsyXWC81OGq)

**Action**: Build one ZK circuit this month. A simple proof of ownership or a hidden value range proof in Noir. Add it to your GitHub.

---

#### 2. Formal Verification
**Gap level: Medium | Timeline to fix: 4–8 weeks**

You use Slither and Trail of Bits tooling (good), but formal verification is the next level and is increasingly listed in senior/staff-level smart contract roles.

**What to learn:**
- **Certora Prover** — industry standard, used by Aave, Compound, Uniswap
- **Halmos** — symbolic testing for Foundry (closest to your current stack)
- **Echidna** — property-based fuzzing (you likely fuzz already; formalize it)

**Resources:**
- [Certora Tutorials](https://docs.certora.com/en/latest/docs/tutorial)
- [Halmos GitHub](https://github.com/a16z/halmos)

**Action**: Write Halmos invariant tests for one of your existing contracts. This takes a weekend and is immediately resume-worthy.

---

### High-Value Additions (Do These in Parallel)

#### 3. AI Agent Frameworks (Off-Chain Side)
**Gap level: Low-Medium | Timeline to fix: 2–4 weeks**

You already built the on-chain layer (ERC-8004/8183 agent marketplace, AI-native CLI). The gap is connecting that to mainstream off-chain AI agent frameworks. This makes you a complete "AI x Web3" candidate — a very small pool.

**What to learn:**
- **Claude API + tool use** — you're already using Claude Code; now build agents that call on-chain tools
- **LangChain / LangGraph** — most widely used, many web3 startups use it
- **Eliza (ai16z)** — popular in crypto-native AI agent projects
- **MCP servers** — you authored Claude Code skills; write an MCP server that wraps your smart contracts

**Action**: Build a demo: an AI agent that monitors on-chain positions and executes liquidations (you literally did this at Nunchi — document it publicly).

---

#### 4. Layer 2 / App-Chain Development
**Gap level: Medium | Timeline to fix: 1–2 months**

You deploy *on* L2s but haven't built the L2 infrastructure itself. The next wave of protocol engineering jobs involves customizing rollup stacks.

**What to learn:**
- **OP Stack** — Optimism's modular rollup framework; most widely forked
- **Arbitrum Orbit** — Arbitrum's app-chain framework
- **ZK Stack** (zkSync) — ZK-native app chains

**Action**: Spin up a local OP Stack devnet (one weekend). Understanding how sequencers, bridges, and fault proofs work adds depth to any protocol engineering interview.

---

#### 5. MEV / Searcher Mechanics
**Gap level: Medium | Timeline to fix: 2–4 weeks**

For perp protocols specifically, MEV is not optional knowledge. Liquidation bots (which you shipped), sandwich attacks, and oracle manipulation are attack vectors *and* revenue opportunities. Senior protocol engineers at perp DEXs are expected to reason about these.

**What to learn:**
- [MEV.wtf resources](https://github.com/flashbots/mev-research)
- [Flashbots docs](https://docs.flashbots.net/)
- How perp protocols protect themselves from oracle front-running (you may already know some of this from your Pyth/Stork integration)

---

### Nice to Have (Longer Term)

#### 6. Modern Indexing Alternatives
You know The Graph (subgraphs). Also learn:
- **Ponder** — TypeScript-native indexer, faster DX
- **Envio** — high-performance, multi-chain
- **Goldsky** — managed subgraphs + mirror pipelines

#### 7. Cross-chain Messaging Depth
Your Novastro cross-chain SDK work is good. Deepen:
- **LayerZero V2** — OApp standard
- **Chainlink CCIP** — increasingly required in enterprise/RWA contexts
- **Wormhole NTT** — native token transfers

---

## AI-FIRST MARKET REALITY

**Are your skills outdated? No. Are AI skills additive? Absolutely yes.**

The market in 2026 is splitting into two buckets:

| Bucket | Description | Your Fit |
|---|---|---|
| **Traditional Protocol Eng** | Deep Solidity, security, protocol design | You're already here |
| **AI x Web3 Protocol Eng** | All of the above + autonomous agents + AI-assisted security | You're 60% here already |

Companies going AI-first are NOT replacing smart contract engineers — they're looking for engineers who can build *agentic systems* that interact with contracts. Your ERC-8004/8183 agent marketplace puts you ahead. **Lean into this hard in every application.**

**Specific AI skills that matter for web3:**
1. **Prompt engineering for security analysis** — using LLMs to find vulnerabilities in Solidity code (you already use Claude Code; formalize this as a skill)
2. **Agentic transaction execution** — agents that sign, simulate, and submit txns autonomously (your liquidation CLI)
3. **Verifiable AI / zkML** — proving AI model outputs on-chain. Emerging, but Ritual.net, Giza, Ora Protocol are building here
4. **AI-assisted audit workflows** — using LLMs + static analysis together. Quantstamp and Trail of Bits are moving here

---

## WEEKLY UPSKILL SCHEDULE

| Day | Focus | Time |
|---|---|---|
| Monday | ZK study (Noir/Circom tutorial) | 1 hr |
| Tuesday | Apply to 3 jobs (from daily digest) | 45 min |
| Wednesday | Build something small (ZK circuit, Halmos test, MCP server) | 1.5 hr |
| Thursday | Read 1 DeFi/protocol paper or audit report | 45 min |
| Friday | Twitter/X engagement — reply to Uniswap, Aave, Ethena, Paradex threads | 30 min |
| Weekend | 1 open-source contribution OR personal project update | 2-3 hr |

---

## RESUME IMPROVEMENTS

Your resume is solid but missing:

1. **Numbers/scale** — Add TVL, transaction volume, or user counts wherever possible. "Prediction market protocol" vs "Prediction market protocol handling $5M TVL"
2. **Public GitHub links** — Link to specific repos for Oddz, your audit tools, your agent marketplace
3. **Security section** — Dedicated section: "Worked with Quantstamp + Zellic; secured using Slither, Echidna, Trail of Bits Manticore"
4. **AI skills** — Add to skills section: "AI agent tooling: Claude Code, MCP servers, ERC-8004/8183 on-chain agent standards"
5. **Move ERC-8004/8183 higher** — This is cutting-edge. It's buried in bullets. It should be a featured line.

---

## TARGET COMPANIES RANKED BY FIT

1. **Ethena Labs** — yield-bearing asset hedging is literally what Nunchi does
2. **Paradex** — CLOB + perps, Paradigm-backed, well-funded
3. **Autonolas/Valory** — on-chain agents, your ERC-8004/8183 is a direct conversation starter
4. **Uniswap Labs** — AMM depth, strong brand, remote
5. **dYdX** — perpetuals, proven protocol
6. **Morpho / Euler** — risk engine experience from your clearing house work
7. **Ritual.net** — AI x Web3, your CLI + agent work makes you relevant
8. **Hyperliquid** — dream job fit but Rust-heavy; invest 1 month in Rust before applying
