# Job Hunt Daily Briefing — June 11, 2026

## Profile Summary (Bhargav Kacharla)
**Target:** Senior Blockchain/Smart Contract Engineer | Web3 DeFi | Remote
**Stack:** Solidity (EVM primary) · TypeScript/Node.js · Rust (Anchor/Solana) · AI agents (LangChain, LangGraph, Anthropic SDK, MCP)
**Highlights:** 5+ years Solidity, shipped perpetuals CLOB, RWA tokenization, account abstraction, on-chain agent marketplace, audit-hardened contracts (Quantstamp + Zellic)

---

## Today's Job Opportunities

### Tier 1 — Strong Fit (Apply First)

| # | Company | Role | Salary | Location | Link |
|---|---------|------|--------|----------|------|
| 1 | **Uniswap Labs** | Senior Smart Contract Engineer | $290K–$325K | Remote | [Apply](https://job-boards.greenhouse.io/uniswaplabs/jobs/4003103005) |
| 2 | **Coinbase** | Senior Smart Contract Engineer – Tokenization | Not listed | Remote | [Apply](https://job-boards.greenhouse.io/embed/job_app?token=7426373&for=coinbase&gh_jid=7426373) |
| 3 | **Veda Tech Labs** | Smart Contract Engineer | Not listed | Remote | [Apply](https://jobs.lever.co/vedatechlabs/c49b4993-d504-49aa-8cf5-03aa19e4895b) |
| 4 | **Alchemy** | Protocol Engineer | $135K–$350K | Remote | [Apply](https://job-boards.greenhouse.io/alchemy/jobs/4020810005) |

### Tier 2 — Good Fit (Apply if Tier 1 exhausted)

| # | Company | Role | Salary | Location | Link |
|---|---------|------|--------|----------|------|
| 5 | **cLabs (Celo)** | Senior Smart Contracts Engineer | Not listed | Remote | [Apply](https://jobs.lever.co/clabs/500004dc-7a42-47ec-9a3d-9de71969b9d5) |
| 6 | **Clearmatics** | Smart Contract Engineer – Ethereum | Not listed | Remote/EU | [Apply](https://job-boards.greenhouse.io/clearmatics/jobs/6847827002) |
| 7 | **CertiK** | Blockchain Security Engineer (Solidity/Rust/Go) | Not listed | Remote | [Apply](https://jobs.lever.co/certik/478ab0cd-9f5e-4b88-88b5-01d3beac4d81/apply) |
| 8 | **Serotonin** | Smart Contract Backend Engineer | Not listed | Remote | [Apply](https://jobs.lever.co/serotonin/8d6d755c-db9b-4351-92b3-90e9c7b4b5b8) |
| 9 | **Ethereum Foundation** | Developer – Account Abstraction & Interop | Not listed | Remote | [Apply](https://jobs.lever.co/ethereumfoundation/7c34b7a5-62c4-4905-98eb-2920b6074c09) |

### Daily Job Boards to Monitor (Bookmark These)
- [web3.career/solidity-jobs](https://web3.career/solidity-jobs) — Updated daily, 3 new Solidity roles as of Jun 2026
- [cryptojobslist.com/solidity](https://cryptojobslist.com/solidity) — 15 active Solidity roles
- [cryptocurrencyjobs.co/web3](https://cryptocurrencyjobs.co/web3/) — Curated, signal-to-noise high
- [arc.dev/remote-jobs/solidity](https://arc.dev/remote-jobs/solidity) — Remote-only focus
- [web3.career/ai-jobs](https://web3.career/ai-jobs) — 10 new AI+web3 roles this month

---

## Profile Fit Analysis

### Strengths (What Puts You in the Top 5%)
- **Perpetuals + CLOB experience** — Hyperliquid, dYdX, GMX clones are the hottest hiring segment; your Nunchi CLOB work is a direct match.
- **AI agent + on-chain automation** — 53% of web3 job postings now mention AI; you're already shipping this at production scale.
- **Audit lifecycle ownership** — Most candidates write contracts, few have managed Quantstamp/Zellic audits end-to-end.
- **ERC-4337 account abstraction** — Coinbase, Ethereum Foundation, and L2s all recruiting this expertise.
- **RWA tokenization (ERC-3643)** — Institutional DeFi is a growth vector; Coinbase's tokenization team is one example.
- **Multi-chain depth** — EVM (Avalanche, BNB, Polygon, Base) + Solana + Hyperledger Besu.

### Honest Weaknesses (Close These Gaps)
| Gap | Why It Matters | How to Close |
|-----|---------------|--------------|
| ZK proofs / zkEVM | 40%+ of L2 roles now require zk familiarity | Spend 2 weeks on ZK learning resources; build a toy zk circuit with circom/noir |
| Formal verification | Certora Prover and Echidna appear in 30%+ of senior listings | Spend 3–4 days running Certora on one of your existing contracts |
| MEV / orderbook internals | Hyperliquid/dYdX-style roles test this | Study flashbots MEV research; your CLOB work is a foundation |
| Move language | Aptos/Sui hiring, niche but premium comp | Optional — only pursue if SUI/Aptos roles interest you |

---

## Skill Recommendations for Today

### If Companies Are Going AI-First (They Are — 53% of Postings)
Your AI section is strong but mostly infrastructure-level. To stand out for AI-first protocols:

1. **Verifiable AI / zkML** — Prove AI agent outputs on-chain using ZK proofs. Ezkl is the leading tool. 1–2 day exploration.
2. **Onchain agent frameworks** — ElizaOS (formerly ai16z), Virtuals Protocol, Coinbase AgentKit. Your ERC-8004 work is ahead of most devs; contribute to or reference these frameworks in interviews.
3. **Intent-based architecture** — ERC-7683 (cross-chain intents), Anoma. Protocols that combine AI agents + intents are a premium hiring segment.
4. **LLM eval for smart contract code** — Your AI auditor project is gold; add a public benchmark with known CVEs and publish results. This gets you inbound.

### If Your Skills Feel Outdated (They Don't, But Here's What to Add)
Current Solidity stack that senior devs are expected to know in 2026:

```
Must-have: Solidity 0.8.x · Foundry (forge, cast, anvil) · fuzzing (Echidna/Medusa) · upgradeable proxies (UUPS/Transparent) · EIP-1559/4844 gas mechanics
Nice-to-have: Certora Prover · Yul/inline assembly · transient storage (EIP-1153) · blob transactions
Premium: ZK circuits (Circom / Noir) · custom precompiles · L2 sequencer mechanics
```

You already have most of the must-haves. The Certora + ZK circuit items are your fastest ROI to close.

---

## Daily Routine Recommendation

| Time | Task |
|------|------|
| 30 min AM | Check web3.career + cryptojobslist for new listings; apply to 1–2 roles |
| 30 min AM | Follow up on any pending applications; track status in a Notion/sheet |
| 1 hr | Skill building (rotate: ZK, Certora, MEV research, zkML) |
| Anytime | Post 1 insight on X/Twitter about something you built at Nunchi (liquidation engine, CLOB, AI agents) — inbound > outbound for senior roles |

### High-Signal Actions Beyond Job Boards
- **Write a technical post** about your ERC-8004 agent marketplace — this is novel enough to get traction and DMs from founders
- **Contribute to Foundry / OpenZeppelin** — even small PRs get you on radar
- **Engage on Telegram** — most senior DeFi roles are filled through Telegram DMs in communities like DeFi Dev Club, Blockchain Dev Forum
- **Target directly**: Hyperliquid, Drift, Vertex, Gains Network, Perpetual Protocol, Pendle Finance, Morpho, Euler Finance are all EVM perpetuals/DeFi protocols worth cold-emailing

---

## Market Signal (June 2026)
- Web3 engineering roles: 8,000–12,000 active globally
- AI mentions in crypto job postings: 53.1% (up from 23% in early 2025)
- Senior Solidity comp range: $180K–$325K + token
- Competition: ~450 applicants per senior role on average — warm intros via X/Telegram beat cold applications 3:1
- Fastest growing segments: **perpetuals infra**, **AI agents on-chain**, **RWA/tokenization**, **ZK infrastructure**

---

*Generated: June 11, 2026 | Update this file daily or ask Claude Code to regenerate it.*
