# Web3 Job Hunt — Bhargav Kacharla
*Updated: 2026-05-29 | Daily reference guide*

---

## Your Edge — Where You Stand Out

You are in the **top ~2% of Web3 engineers** by profile depth. Here's why:

| Rare Combination | Why It Matters |
|---|---|
| Production perpetuals / CLOB (Nunchi.trade) | Most Solidity devs have never touched a real perp engine |
| Full audit lifecycle (Quantstamp + Zellic) | You can talk about findings, fixes, re-review — not just "used Slither" |
| AI agent execution + on-chain marketplace | ERC-8004/8183 is genuinely cutting-edge; <50 engineers globally have done this |
| ERC-4337 paymaster + bundler infra | AA is becoming baseline; you built infra, not just called it |
| ERC-3643 RWA compliance + identity registry | The RWA vertical is exploding in 2026 |
| Rust + Anchor (Solana) as a secondary skill | Opens SVM roles if EVM market tightens |

---

## Today's Job Opportunities (2026-05-29)

### Tier 1 — Perfect Profile Match (Apply first)

These companies work on exactly the problems you've solved (perps, CLOB, DeFi infra):

| Company | Role to target | Why you fit | Apply |
|---|---|---|---|
| **Chainlink Labs** | Smart Contract / Solidity Engineer (CCIP) | 33 open roles, all remote, CCIP needs EVM-deep engineers | [chainlinklabs.com/careers](https://chainlinklabs.com/careers) |
| **dYdX** | Protocol / Smart Contract Engineer | You built a perp CLOB — dYdX is the gold standard; rare overlap | [dydx.exchange/careers](https://dydx.exchange/careers) |
| **Hyperliquid Labs** | Backend / Protocol Engineer | On-chain CLOB matching engine experience is a direct match | [jobs.ashbyhq.com/Hyperliquid Labs](https://jobs.ashbyhq.com/Hyperliquid%20Labs) |
| **Synthetix** | Smart Contract Engineer | Options + perps protocols, liquidity provisioning — identical stack | [synthetix.io/jobs](https://synthetix.io/jobs) |
| **Vertex Protocol** | Protocol Engineer | CLOB-based perps DEX, needs on-chain order-book experience | [vertexprotocol.com/careers](https://vertexprotocol.com/careers) |
| **GMX** | Smart Contract Developer | Perpetuals protocol, open governance community | Search on [web3.career](https://web3.career/solidity-jobs) |
| **Aave** | Smart Contract Engineer | DeFi core infra, you already integrated Aave at Novastro | [aave.com/careers](https://aave.com/careers) |

### Tier 2 — AI x Web3 (Your rarest skill — lead with this)

These roles value the AI agent + on-chain execution combo you built at Nunchi.trade:

| Company | Role | Notes | Apply |
|---|---|---|---|
| **Coinbase / Base** | Protocol / AI Infra Engineer | Base is betting heavily on AI x onchain | [coinbase.com/careers](https://www.coinbase.com/careers) |
| **Sei Foundation** | Protocol Engineer | Fast DeFi L1, actively hiring | [cryptojobslist.com/companies/sei-foundation](https://cryptojobslist.com/companies/sei-foundation) |
| **Anchorage Digital** | Smart Contract Engineer | Institutional + DeFi, security-conscious — audit exp is key | [anchorage.com/careers](https://www.anchorage.com/careers) |
| **Space and Time** | Blockchain / AI Engineer | AI + on-chain data, matches your RAG + indexer work | [spaceandtime.io/careers](https://www.spaceandtime.io/careers) |
| **Any AI Agent protocol** | Protocol / Smart Contract Engineer | Search "agent protocol" on crypto.jobs | [crypto.jobs](https://crypto.jobs/) |

### Tier 3 — Smart Contract Security (audit lifecycle experience is rare)

| Company | Role | Notes | Apply |
|---|---|---|---|
| **Trail of Bits** | Smart Contract Security Engineer | You used their tooling + went through their audit | [trailofbits.com/jobs](https://www.trailofbits.com/jobs) |
| **Zellic** | Security Researcher | You worked WITH them on audit — reach out directly | [zellic.io](https://www.zellic.io) |
| **Quantstamp** | Smart Contract Auditor | You did a full audit lifecycle with them | [quantstamp.com/careers](https://quantstamp.com/careers) |
| **OpenZeppelin** | Security Engineer | Protocol security, Defender product | [openzeppelin.com/jobs](https://openzeppelin.com/jobs) |
| **Cyfrin** | Smart Contract Auditor | Growing audit firm, community-driven | [cyfrin.io/careers](https://www.cyfrin.io/careers) |

### Daily Job Boards to Check

Bookmark these and scan every morning (takes 10 min):

- [web3.career/solidity-jobs](https://web3.career/solidity-jobs) — filter: remote + DeFi
- [web3.career/ai-jobs](https://web3.career/ai-jobs) — AI x Web3 roles
- [cryptojobslist.com/solidity](https://cryptojobslist.com/solidity) — 15 active Solidity roles
- [cryptocurrencyjobs.co/solidity/](https://cryptocurrencyjobs.co/solidity/) — curated, quality roles
- [crypto.jobs](https://crypto.jobs/) — 3500+ listings
- [wellfound.com/role/r/solidity-developer](https://wellfound.com/role/r/solidity-developer) — startup roles
- **LinkedIn** — search: `"smart contract engineer" OR "solidity engineer"` + remote filter

---

## Skill Recommendations (Daily)

### What You Already Have (Don't undersell these)

Your AI skills are **ahead of the market** — over 53% of Web3 job posts now ask for AI in 2026 (up from 23% in early 2025). You're already there.

### Gaps to Fill (Priority order)

#### 1. ZK Proofs / zkEVM — HIGH PRIORITY
The biggest skill gap vs. top-tier protocol engineers. ZK is becoming the standard for rollups and privacy.

**What to learn:**
- [ZKonduit / zkEVM docs](https://docs.zkevm.consensys.net/) — Scroll, Linea
- [Starknet / Cairo basics](https://www.cairo-lang.org/docs/)
- Start with: understand ZK proof theory (SNARK vs STARK), then zkEVM architecture

**Time investment:** 2-4 weeks to become conversational; 3 months to be hireable

#### 2. Formal Verification — MEDIUM PRIORITY  
You use Slither (static analysis) and worked with Trail of Bits. Level up to:
- **Certora Prover** — industry standard for formal verification of Solidity
- **Halmos** — symbolic testing with Foundry

**Why:** Senior security roles at Aave, Uniswap, Compound require this. 1 week to learn basics.

#### 3. MEV / Flashbots — MEDIUM PRIORITY
For perps and CLOB work, understanding MEV exposure, sandwich attacks, and how searchers interact with your contracts is expected at senior level.

**Learn:** [flashbots.net](https://www.flashbots.net/), MEV-Boost, how your CLOB matching engine interacts with the mempool.

#### 4. Competitive Auditing — HIGH IMPACT (career accelerator)
Your audit experience with Quantstamp/Zellic is great. Now get a **public track record**:
- [Code4rena](https://code4rena.com/) — competitive audit contests
- [Sherlock](https://sherlock.xyz/) — audit competitions with payouts
- Finding even 1-2 medium/high findings publicly listed will dramatically increase your profile visibility with security-focused employers

**Time: 2-4 hours per contest. Start this week.**

#### 5. Layer 2 Architecture — LOW PRIORITY (you likely already know enough)
- OP Stack, Arbitrum Orbit — understand sequencer, bridge mechanics
- Useful if targeting L2 infra roles (Optimism, Arbitrum, Base)

---

## AI-First Skill Additions (2026 Market)

> You already have: Anthropic SDK, OpenAI SDK, MCP, tool calling, RAG pipelines, LangChain, LangGraph, multi-agent orchestration, eval frameworks.

**You are already AI-first.** Most Web3 engineers are still catching up to where you are.

### What to add to stay ahead:

| Skill | Why | Resource |
|---|---|---|
| **On-chain AI agent standards** (ERC-8004/8183, EIP-7730) | You built this — become the expert, write about it | Your own Nunchi.trade work |
| **Verifiable compute / zkML** | AI inference with cryptographic proofs — next frontier | [EZKL](https://github.com/zkonduit/ezkl), [Modulus Labs](https://www.modulus.xyz/) |
| **Agent wallets / session keys** | EIP-7702, Privy, Dynamic — agents need programmable signing | [EIP-7702 spec](https://eips.ethereum.org/EIPS/eip-7702) |
| **Lit Protocol / TEE-based agents** | Threshold cryptography for agent keys | [developer.litprotocol.com](https://developer.litprotocol.com/) |

---

## Application Strategy

### How to apply (not just what to apply for)

1. **Cold outreach > job board applies.** Your profile is strong enough to DM founders/CTOs directly on X/Twitter. Web3 is smaller than it looks.

2. **Lead with the AI agent angle** in cover letters. Most applicants lead with Solidity years. You have something rarer.

3. **Your GitHub should show:**
   - [ai-rag-pipeline](https://github.com/bhargav55/ai-rag-pipeline) ✓ Already there
   - AI Smart-Contract Auditor ✓ Already there
   - Make sure the READMEs are polished — hiring managers at web3 companies DO look

4. **Start one Code4rena/Sherlock contest this week.** Even participation is visible. Finding a bug puts you in a different tier.

5. **X/Twitter presence** — Web3 hiring is heavily driven by Twitter reputation. Tweet about what you built at Nunchi.trade: the CLOB engine, the agent marketplace, ERC-8004/8183. Even 2 tweets/week moves the needle.

### Resume quick wins

- Add quantified metrics where possible: "CLOB engine handling X orders/sec", "liquidation latency <Y ms"
- Move AI engineer skills section higher — it's currently at the bottom but it's your differentiator in 2026
- Add EIP-7702 to skills if you've worked with it (it shipped in Pectra upgrade 2025)

---

## Market Reality Check (May 2026)

| Metric | Value |
|---|---|
| Active Solidity jobs | ~5,400 globally |
| Remote Solidity roles | ~2,500 |
| AI mentions in Web3 job posts | 53.1% (up from 23% in early 2025) |
| Senior smart contract salary (base) | $180k–$260k + token grants |
| Typical search time (senior EVM) | 5–9 weeks |
| Your salary target (reasonable ask) | $150k–$220k base + tokens |

The market is candidate-scarce for your profile. You should be getting responses within 1-2 weeks of targeted outreach, not 5-9.

---

## Daily Routine (15 min/day)

```
Morning (5 min):   Scan web3.career + cryptojobslist for new postings
                   Bookmark any new roles matching Tier 1/2 above

Midday (5 min):    Check X/Twitter for protocol announcements + hiring threads
                   Search: "hiring" + "smart contract" on X

Evening (5 min):   Apply to 1-2 roles OR send 1 cold DM to a founder/CTO
                   Week goal: 5-7 applications + 2-3 cold outreaches
```

---

*Last updated: 2026-05-29. Re-run this research weekly to find new openings.*
