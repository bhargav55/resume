# Bhargav Kacharla — Web3 Job Search Strategy

## Profile Snapshot
**Core strengths:** Solidity/EVM (5+ yrs), perpetuals/CLOB/options protocols, account abstraction (ERC-4337), RWA tokenization (ERC-3643), AI agent integration (RAG, MCP, multi-agent), smart contract security (Quantstamp / Zellic audit lifecycle), Rust/Anchor (Solana), TypeScript/Node.js.

**Unique differentiator:** You sit at the intersection of on-chain protocol engineering AND AI agent tooling — this combination is rare and the market is actively paying a premium for it (53% of web3 job posts now require AI skills as of Q1 2026).

---

## Tier 1 — Best-Fit Targets (Apply First)

These companies build exactly what you've shipped: perpetuals, options, CLOB, DeFi automation.

| Company | Why You Fit | Careers Link |
|---|---|---|
| **Hyperliquid** | You built a CLOB matching engine, clearing house & liquidation flows — this is literally what Hyperliquid is | https://hyperliquid.xyz/careers |
| **dYdX** | Perpetuals protocol, chain-level engineering | https://dydx.exchange/careers |
| **Synthetix** | Derivatives/options, on-chain risk engine | https://synthetix.io/careers |
| **Lyra Finance** | Options protocol, concentrated liquidity, similar to Oddz | https://lyra.finance |
| **Drift Protocol** | Perps CLOB on Solana (you have Anchor/Rust) | https://driftprotocol.com/careers |
| **GMX / GLP** | Perpetuals, risk & liquidation | https://gmx.io |
| **Vertex Protocol** | Perps + spot CLOB, TypeScript infra | https://vertexprotocol.com |
| **Polynomial Protocol** | Options vaults + derivatives | https://polynomial.fi |
| **Gains Network** | Decentralized leveraged trading | https://gainsnetwork.io |

---

## Tier 2 — Strong Fit (Confirmed Open Roles as of June 2026)

These have verified live postings found today.

| Company | Role | Link |
|---|---|---|
| **Uniswap Labs** | Senior Smart Contract Engineer | https://job-boards.greenhouse.io/uniswaplabs/jobs/4003103005 |
| **Chainlink Labs** | Senior Smart Contract Engineer, Solidity | https://jobs.ashbyhq.com/chainlink-labs/842e9d47-982c-4dfb-8461-1080759c82d9 |
| **Aave Labs** | Staff Smart Contract Engineer | https://jobs.eu.lever.co/aavelabs/a3f47e26-ab0a-403d-8e59-ca2d7e5b4fe7 |
| **Monad Foundation** | Senior Software Engineer (Web3 Full Stack) | https://jobs.ashbyhq.com/monad.foundation/2242c712-d2cf-4fe5-8cc4-eae0ce2bc4f5 |
| **Hyphen Connect** | Full Stack Engineer (Crypto x AI) | https://job-boards.greenhouse.io/hyphenconnect/jobs/5022529007 |

---

## Tier 3 — AI x Blockchain (Emerging, High Growth)

Your on-chain agent marketplace work (ERC-8004/8183) puts you ahead of 99% of applicants here.

| Company | Focus | Link |
|---|---|---|
| **Ora Protocol** | On-chain AI inference (opML) | https://ora.io/careers |
| **Autonolas / Valory** | Autonomous agent services on-chain | https://olas.network |
| **Virtuals Protocol** | AI agent economy, tokenized agents | https://app.virtuals.io |
| **Story Protocol** | IP + AI provenance on-chain | https://storyprotocol.xyz/careers |
| **Semiotic.AI (Graph Protocol)** | AI-to-AI micropayments, agent infra | https://semiotic.ai |

---

## Daily Job Boards to Check (bookmark these)

- https://web3.career/solidity-jobs — updated daily
- https://cryptojobslist.com/solidity — filters for remote + senior
- https://cryptocurrencyjobs.co/smart-contracts/ — curated, high signal
- https://crypto.jobs/ — broad, 3500+ listings
- https://web3.career/ai-jobs — AI x Web3 specifically
- https://jobs.ashbyhq.com/uniswap — Uniswap board

---

## Skill Gap Analysis & Upskilling Plan

### Gaps vs. Current Market Demand

| Skill | Priority | Why | Where to Learn |
|---|---|---|---|
| **ZK fundamentals** (zkSNARKs, zkEVM, Circom basics) | HIGH | ZK is table stakes for senior EVM roles at L2 companies. StarkNet, zkSync, Linea all hiring. | Rareskills ZK book, 0xPARC circom course |
| **Cross-chain messaging** (LayerZero v2, Wormhole, Axelar) | HIGH | Most DeFi protocols are now multi-chain. You know single-chain deployment well. | LayerZero docs + build a cross-chain vault |
| **Formal verification** (Certora Prover, Halmos, Kontrol) | MEDIUM | Differentiates you as a security-first engineer. Zellic/Quantstamp experience helps but formal tools are what top protocols use now | Certora free certification program |
| **EIP-7702** (new AA standard) | MEDIUM | Replaces ERC-4337 in many contexts post-Pectra hardfork. You have 4337 depth, easy to extend. | Ethereum EIP-7702 spec + Alchemy blog |
| **viem + Wagmi** (modern TS web3 stack) | LOW-MEDIUM | ethers.js is aging out. Most new projects use viem. | viem.sh docs, replace ethers in one project |
| **MEV / searcher mechanics** | LOW | Good to know for perpetuals risk work, not a hard requirement | Flashbots docs, MEV-Share |

### You're Already Ahead On

- AI agent tooling (LangChain, LangGraph, MCP, RAG) — most blockchain engineers have zero of this
- Smart contract security (audit lifecycle with Quantstamp + Zellic is premium experience)
- ERC-4337 / account abstraction depth
- Production mainnet experience (Avalanche, BNB, Polygon — real TVL)
- Rust/Anchor (keeps Solana doors open)

---

## AI-First Positioning (What to Emphasize)

The market is bifurcating: pure Solidity devs vs AI-native blockchain engineers. You are the second, which is worth 30-40% more comp and opens far more doors.

**How to position yourself:**

1. **Lead with the agent work** in every application. Your on-chain agent marketplace (ERC-8004/8183) + AI-native CLI for liquidation automation is a narrative that almost no one else can tell.

2. **Reframe your title.** Instead of "Senior Blockchain Engineer", use: *"Blockchain Protocol Engineer with AI Agent Specialization"* — it matches the search terms hiring managers actually use in 2026.

3. **Build in public.** Post 1 thread/week on X/Twitter or Farcaster about one specific thing you built — agent marketplace mechanics, CLOB liquidation logic, etc. Your GitHub has the AI smart-contract auditor already; a short writeup on how it works drives inbound.

4. **The trifecta story:** You can build the protocol (Solidity/EVM), instrument it for AI consumption (indexers, TypeScript APIs), and build the agent that operates on it (LangGraph, MCP, eval frameworks). That full-stack capability is rare and what funded protocols are actively trying to hire.

---

## Daily Routine Recommendation (30–45 min/day)

| Time | Action |
|---|---|
| **Mon/Wed/Fri — 20 min** | Check the 3 job boards above, scan for new listings, add to `daily-leads/` in this repo |
| **Tue/Thu — 20 min** | Upskill block: work through one ZK or cross-chain concept. Keep notes. |
| **Daily — 10 min** | Engage on X/Farcaster/LinkedIn — reply to one DeFi or AI x crypto thread with something substantive |
| **Weekly — 1 hr** | Apply to 3–5 roles with tailored cover notes. Don't blast generic apps. |
| **Weekly — 1 hr** | Write one short post/thread about something you built or learned |

---

## Resume Strengths (Keep These Prominent)

- CLOB matching engine, clearing house, liquidation flows → rare production experience
- Audit lifecycle with Quantstamp + Zellic → proves security ownership
- On-chain agent marketplace (ERC-8004/8183) → cutting-edge, few people have shipped this
- Cross-chain yield (Aave + Stader integration) → shows DeFi composability knowledge
- AI projects (RAG pipeline, smart contract auditor) → the differentiator

## Resume Gaps to Address

- **No public TVL numbers.** If you can share any protocol TVL, trading volume, or transaction counts — add them. "Deployed to Avalanche mainnet" is weaker than "$2M TVL at launch" or "processing 500 liquidations/day".
- **GitHub link visible** — make sure pinned repos include your AI auditor and any public contract work.
- **Missing: ZK or cross-chain project.** One small public project (even a toy cross-chain vault using LayerZero) would signal awareness of where the market is heading.
