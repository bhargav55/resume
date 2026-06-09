# Web3 Job Hunt — Skill Recommendations for Bhargav Kacharla

> Updated: June 2026. Revisit monthly as the market shifts.

---

## Profile Assessment

### What's Strong ✅
These are rare in the market — lean into them in every application.

| Skill | Depth | Market Rarity |
|-------|-------|---------------|
| Solidity / EVM smart contracts | 5+ years, production mainnets | Common but depth is rare |
| DeFi protocol depth | Perpetuals, CLOB, options, liquidation engines, clearing house | Very rare |
| Smart contract security | Full audit lifecycle ownership with Quantstamp + Zellic, Slither/Trail of Bits tooling | Rare |
| Account abstraction | ERC-4337, paymaster, skandha bundlers | Uncommon |
| AI + Blockchain intersection | AI agents for on-chain execution, ERC-8004/8183 agent marketplace | Very rare (you're early) |
| On-chain indexing | Real-time WebSocket-based event streaming at low latency | Uncommon |
| TypeScript/Node.js backend | Paired with contract work — full-stack protocol engineering | Common |
| Rust / Anchor (Solana) | Secondary, but real production experience | Valuable for cross-chain roles |

---

## What's Becoming Table Stakes (Add Soon)

These are not gaps today, but will hurt you in 6–12 months if ignored.

| Skill | Why It Matters Now | Where to Start |
|-------|-------------------|----------------|
| **ZK fundamentals** | L2 and infrastructure roles now expect basic ZK literacy. Not writing circuits — just understanding Groth16/PLONK/STARKs. | [zk-learning.org](https://zk-learning.org), [zkiap.com](https://zkiap.com) |
| **Formal verification** | Certora Prover and Halmos are increasingly required for senior hires at top protocols. | [Certora Tutorials](https://docs.certora.com), [Halmos](https://github.com/a16z/halmos) |
| **Competitive auditing** | A public track record on Sherlock/Code4rena is more credible than a resume claim. One contest per month is enough. | [Sherlock](https://app.sherlock.xyz), [Code4rena](https://code4rena.com), [Cantina](https://cantina.xyz) |
| **L2 internals** | OP Stack (sequencer, derivation pipeline) and zkSync Era are common context for infrastructure protocol roles. | [OP Stack Specs](https://specs.optimism.io), [zkSync Era Docs](https://docs.zksync.io) |
| **Restaking / EigenLayer** | EigenLayer and AVS architecture is the dominant new primitive. Many roles now reference it. | [EigenLayer Docs](https://docs.eigenlayer.xyz) |

---

## AI Skills: Double Down or Branch Out?

**Double down on depth, not breadth.** You're already ahead of 95% of blockchain engineers on AI integration. The differentiated move is:

| What to Build | Why |
|---------------|-----|
| Open-source MCP tools for blockchain use cases | MCP is standard; publishing tools builds search visibility and GitHub rep |
| Evaluation harnesses for AI agent reliability | Structured evals show you ship production-quality agents, not demos |
| AI-assisted audit pipeline (make it public) | You've built this — document and open-source it. It's genuinely novel. |
| On-chain AI output verification (ZK + AI) | Emerging field. First movers will define the architecture. |

**What NOT to do:** Go deep into model training, fine-tuning, or GPU infrastructure. That's ML engineering, not your positioning. Stay at the application + agent orchestration layer.

**Verdict on AI-first companies:** Your existing AI skills (Anthropic SDK, MCP, RAG, LangGraph, structured outputs, evals) already match what AI-first companies need from a blockchain engineer. No major pivot required — just make it more visible on your GitHub and in writing.

---

## What's NOT Outdated (Keep)

- **Solidity** — Still the dominant smart contract language. No credible successor on EVM.
- **EVM** — Still the dominant execution environment. Not going anywhere.
- **TypeScript** — Evergreen. Nothing to change here.
- **Rust** — Growing importance as Solana/SVM expands and more ZK tooling uses Rust.
- **Foundry** — The dominant testing framework. Keep using it.

---

## What to Deprioritize

- **Move language** — Still niche. Low job count outside Aptos/Sui ecosystem.
- **Pure frontend Web3** (ethers.js integrations, wagmi) — Not your positioning. Mention fluency but don't lead with it.
- **Hyperledger/enterprise blockchain** — Your Xalts experience is fine on the resume, but the market for this is thin and not growing.

---

## Daily Routine (30 min/day)

| Time | Action |
|------|--------|
| **Morning** | Check the daily [Job Hunt Issue](../../issues) (auto-posted at 09:00 IST) |
| **Morning** | Apply to 1–3 roles with a *customized* outreach message (name a specific protocol challenge) |
| **Midday (15 min)** | Read one governance update: Aave, Morpho, Uniswap, or Hyperliquid |
| **Evening (15 min)** | Work on one visibility item: blog post, open-source commit, or audit contest |

---

## 30-Day Upskill Sprint

### Week 1 — Visibility (get found)
- [ ] Publish a technical post about your CLOB matching engine architecture on Mirror or Substack
- [ ] Make your AI smart-contract auditor GitHub repo public (sanitize company-specific data)
- [ ] Set up a Sherlock profile and join one live audit contest
- [ ] Post 3 technical takes on Farcaster (`warpcast.com`)

### Week 2 — ZK Literacy
- [ ] Complete modules 1–3 of [zk-learning.org](https://zk-learning.org)
- [ ] Read the Aztec and zkSync Era docs at a high level (architecture, not implementation)
- [ ] Implement one simple Circom circuit and write a short post about what you learned

### Week 3 — Formal Verification
- [ ] Run [Halmos](https://github.com/a16z/halmos) on an existing Foundry test suite and write about the results
- [ ] Add a basic Certora spec to one of your public contracts
- [ ] Write a comparison: invariant tests vs formal verification (when to use each)

### Week 4 — Network + Apply Blitz
- [ ] Connect with 5 protocol engineers on Farcaster / Twitter who work at target companies
- [ ] Submit at least 10 targeted applications with custom outreach
- [ ] Make one GitHub contribution (PR, issue, or discussion) to a major protocol repo

---

## Where to Be Visible

| Platform | What to Post |
|----------|--------------|
| **Farcaster** (`warpcast.com`) | Short technical takes on EVM, DeFi mechanisms, AI agents |
| **Twitter / X** | Thread about your AI agent + on-chain execution work |
| **Mirror.xyz** | Long-form technical articles (CLOB design, liquidation architecture) |
| **GitHub** | Open-source tools, audit contest artifacts, Foundry test libraries |
| **LinkedIn** | Job applications + professional updates (less signal in web3 but still useful) |
| **Ethereum Magicians** | EIP discussions — signals protocol-level thinking |
| **Immunefi** | Bug bounty submissions — verified payouts are permanent public credentials |

---

## Top Companies to Target

Based on your profile (perps, EVM depth, AI agents, security):

| Company | Why You Fit | Where to Apply |
|---------|-------------|----------------|
| Hyperliquid | On-chain perps, CLOB — exact match for your Nunchi.trade work | Direct contact / referrals |
| dYdX | Perpetuals protocol, Solidity + TypeScript | jobs.dydx.exchange |
| GMX | Perps, liquidation engine | their Discord / web3.career |
| Morpho | Protocol engineering, security, EVM depth | morpho.org/careers |
| Aave | Smart contract security, audits | aave.com/careers |
| Uniswap Labs | Protocol engineering, V4 hooks | uniswap.org/careers |
| Chainlink Labs | Oracle integration, smart contract depth | chain.link/careers |
| Eigenlayer / EigenDA | Restaking, EVM depth | eigenlayer.xyz/careers |
| Paradigm | Research + engineering hybrid | jobs.paradigm.xyz |
| Aztec | ZK + smart contracts, if you invest in ZK literacy | aztec.network/careers |

---

## Job Boards — Daily Check

The GitHub Action in this repo posts a ranked daily issue. Also check manually:

- [web3.career/solidity-jobs](https://web3.career/solidity-jobs)
- [cryptojobslist.com/solidity](https://cryptojobslist.com/solidity)
- [cryptocurrencyjobs.co/solidity](https://cryptocurrencyjobs.co/solidity/)
- [wellfound.com/role/smart-contract](https://wellfound.com/role/smart-contract)
- [crypto.jobs](https://crypto.jobs/)
- [Immunefi Bug Bounties](https://immunefi.com/bug-bounty/) — income + permanent public credential
- [Sherlock Audit Contests](https://app.sherlock.xyz/audits)
- [Code4rena](https://code4rena.com/audits)
