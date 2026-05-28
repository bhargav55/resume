# Skill Analysis & Roadmap — Bhargav Kacharla

_Last updated: May 28, 2026_

---

## Your Current Stack vs. Market Demand

### Strengths (Strong / Keep Sharpening)

| Skill | Your Level | Market Demand | Notes |
|---|---|---|---|
| Solidity / EVM | Expert | Very High | Perpetuals, CLOB, liquidations — top 5% |
| Smart contract security | Strong | Very High | Audit lifecycle ownership is rare |
| ERC-4337 (Account Abstraction) | Strong | High | Ethereum Foundation is literally hiring for this |
| DeFi protocols | Expert | Very High | Options, perpetuals, AMM, yield — full coverage |
| TypeScript / Node.js | Strong | High | Standard backend pairing |
| AI agent integration | Growing | **Explosive** | 53% of Web3 jobs mention AI now |
| Rust / Anchor (Solana) | Intermediate | Medium-High | Good hedge, not primary yet |
| RAG / LLM tooling | Intermediate | Growing | Your AI projects show initiative |

---

## Gaps & What to Add (Prioritized)

### Priority 1 — High ROI, 2–4 weeks each

**1. ZK / Zero-Knowledge Proofs (Conceptual + Applied)**
- Why: ZK-EVMs (zkSync, Scroll, Polygon zkEVM, Linea) are mainstream. Jobs requiring ZK pay 30–40% premium.
- What to learn: Circom basics, ZK-SNARKs/STARKs concepts, how zkEVM works
- Resources: 0xPARC ZK learning, zkiap.com, RareSkills ZK book
- Time: 3–4 weeks for working knowledge
- Job unlock: zkSync, Polygon, Scroll, StarkWare, Aztec

**2. EigenLayer / AVS Development (Restaking)**
- Why: Restaking is the hottest infra category in 2026. Very few engineers understand it.
- What to learn: EigenLayer architecture, writing a custom AVS (Actively Validated Service)
- Resources: EigenLayer docs, their GitHub examples
- Time: 2 weeks
- Job unlock: EigenLayer, any protocol building on restaking

**3. Formal Verification (Certora / Halmos)**
- Why: Auditors and security engineers who can write specs earn top dollar. You already have Slither/Trail of Bits — this is the next level.
- What to learn: Certora Prover (CVL spec language), Halmos (symbolic execution)
- Resources: Certora tutorials, OpenZeppelin formal verification examples
- Time: 3 weeks
- Job unlock: OpenZeppelin, top audit firms, protocol security roles

---

### Priority 2 — Medium-term (1–2 months)

**4. Modular Blockchain / Rollup Architecture**
- OP Stack, Arbitrum Orbit, ZK Stack — how to deploy and customize your own rollup
- Increasingly required for infra roles at L2 ecosystems
- Resources: OP Stack docs, Arbitrum Orbit docs

**5. MEV / PBS (Proposer-Builder Separation)**
- Understanding MEV, block building, flashbots, private mempools
- Required for any role touching order flow, liquidations, or arbitrage
- You already do liquidation bots — this is the next logical step
- Resources: Flashbots docs, mev.wtf, EigenPhi analytics

**6. Cross-chain / Interoperability**
- LayerZero, Wormhole, Hyperlane — how to build omnichain apps
- Growing category as chains proliferate

---

### Priority 3 — AI-First Skills (Given 53% of jobs mention AI)

Your AI background is already strong for web3. Focus on:

**7. On-chain Verifiable AI / Agent Frameworks**
- Frameworks: ElizaOS, ZerePy, GAME (Virtuals Protocol)
- You've already built an agent marketplace (ERC-8004/ERC-8183) — this puts you ahead
- What to add: Verifiable inference (opML, zkML concepts), TEE-based agents
- Resources: Ritual Network docs, opML GitHub

**8. AI-assisted Smart Contract Security**
- Your AI auditor project is a killer portfolio piece — extend it:
  - Add fuzzing integration (Echidna, Medusa)
  - Add mutation testing
  - Benchmark against public audit reports
- This alone can get you into top audit firms

**9. Claude / GPT in Developer Tooling**
- MCP servers for blockchain: build one that wraps Etherscan, Tenderly, Foundry
- This is exactly what companies want — someone who ships AI-in-the-workflow tools

---

## What Is NOT Outdated

These concerns you raised are not issues:

- **Solidity**: Not going anywhere. Every new EVM chain needs Solidity devs.
- **TypeScript**: Still the dominant web3 backend language.
- **EVM focus over SVM**: Correct prioritization — EVM has 80%+ of total value locked.
- **DeFi protocols**: DeFi is expanding, not contracting.

---

## What Could Become Outdated (Watch These)

- **Hardhat** — Foundry is taking over. You already use Foundry — good.
- **LangChain** — still valid but fragmented. Keep LangGraph as the focus.
- **ERC-8004 / ERC-8183** — these are very new standards. Monitor if they get adopted or superseded.

---

## Daily Routine Recommendation

| Time | Activity |
|---|---|
| 15 min morning | Check the 6 job boards (links in today's jobs file) |
| 30 min / day | One upskill task (ZK, EigenLayer, formal verification) |
| 1 hour / week | Extend AI smart contract auditor project |
| 1 hour / week | Write one technical post (Twitter/X or Farcaster) about what you built |
| Ongoing | Star / follow: Paradigm, a16z crypto, Uniswap, EigenLayer GitHub repos |

---

## Your Strongest Job Titles to Target

1. **Senior Smart Contract Engineer** (highest volume, strong match)
2. **Protocol Engineer — DeFi / Perpetuals** (best salary, direct match)
3. **Blockchain Security Engineer** (audit experience differentiates you)
4. **AI + Blockchain / Onchain Agent Engineer** (emerging, low competition, premium pay)
5. **Staff / Principal Engineer — EVM** (5+ years experience qualifies you)

---

## Resume Edge Points to Emphasize More

1. **CLOB matching engine** — very few engineers have built one. Name-drop it in every cover letter.
2. **Audit lifecycle ownership** — Quantstamp + Zellic are top-tier firms. Recruiters know this.
3. **Agent marketplace (ERC-8004/8183)** — cutting-edge, almost no competition.
4. **Live mainnet deployments** — Polygon, Avalanche, BNB. Always say "production mainnet."
5. **AI auditor project** — frame it as: "built an AI system that replicates what a junior auditor does."
