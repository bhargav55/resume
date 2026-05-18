# Daily Job Search Digest — May 18, 2026

**Profile:** Bhargav Kacharla | Protocol Engineer | EVM/Solidity · TypeScript · Rust/SVM  
**Experience:** 5+ years web3, 8+ years total engineering  
**Specialization:** DeFi derivatives (perps, options), RWA tokenization, cross-chain, on-chain AI agents

---

## Today's Job Leads

### Tier 1 — Exact Matches (Apply Today)

#### 1. Nethermind — Founding Protocol Engineer (Web3 + AI)
**Why you fit:** This is a near-perfect match. Nethermind's role explicitly mentions ERC-8004 and on-chain agent infrastructure — you shipped a production ERC-8004/ERC-8183 agent marketplace at Nunchi. You also match their TypeScript/Ethers.js/Viem requirement and the "first engineering hire" archetype (you've operated at protocol architect level).

- **Role:** Full-time, 100% Remote Worldwide, Senior
- **Stack:** TypeScript, Node.js, Ethers.js/Viem, Fastify, Postgres, on-chain agents
- **What they build:** Triple-Verified Stack for autonomous agent workflows with cryptographic guarantees
- **Apply:** https://cryptojobslist.com/jobs/founding-protocol-engineer-web3-ai-at-nethermind
  - Also listed at: https://cryptocurrencyjobs.co/engineering/nethermind-founding-protocol-engineer-web3-ai/

---

#### 2. Hyphen Connect — Blockchain Tech Lead (RWA & Tokenization)
**Why you fit:** Your Novastro work is a direct match — ERC-3643 compliance, identity registry, Solidity tokenization, Chainlink oracles, Foundry. This role requires exactly that.

- **Role:** Full-time, Remote
- **Requirements:** 5+ years blockchain, 3+ years RWA/DeFi, Solidity/Rust, Hardhat, Foundry, Chainlink oracles
- **Apply:** https://job-boards.greenhouse.io/hyphenconnect/jobs/4956294007

---

#### 3. Chainlink Labs — Multiple Senior Engineering Roles
**Why you fit:** You've integrated Pyth and Stork oracles, used Chainlink Keepers extensively, and understand oracle-dependent protocol design from the consumer side. Chainlink Labs values engineers who've built production oracle integrations.

- **Role:** Various (475 open positions), 100% Remote
- **Notable opening:** Senior Engineering Manager, CCIP (Cross-Chain Interoperability Protocol)
- **Apply:** https://chainlinklabs.com/careers
- **Candidate guide for Solidity roles:** https://chainlinklabs.com/candidate-guide/solidity-smart-contract-engineer

---

### Tier 2 — Strong Matches (Apply This Week)

#### 4. THORChain — Senior Protocol Engineer
**Why you fit:** Cross-chain liquidity protocol, native asset swaps across 10+ chains. Your cross-chain SDK work at Novastro and multi-chain experience (EVM + Solana + Aptos) is directly relevant.

- **Find via:** https://web3.career/web3-companies/thorchain (check for active listings)

#### 5. MLabs — Smart Contract Engineer (Base/Arbitrum)
**Why you fit:** DeFi protocol work on Base and Arbitrum, Solidity + Rust requirement matches your stack.

- **Find via:** https://cryptojobslist.com/solidity

---

### Daily Job Boards to Monitor

Check these every day — they update with new listings constantly:

| Board | URL | Best Filter For You |
|-------|-----|-------------------|
| Web3.career | https://web3.career/defi+solidity-jobs | DeFi + Solidity |
| Web3.career | https://web3.career/protocol-jobs | Protocol roles |
| Web3.career | https://web3.career/ai-jobs | AI + Web3 |
| CryptoJobsList | https://cryptojobslist.com/solidity | Solidity roles |
| CryptoJobsList | https://cryptojobslist.com/remote | Remote roles |
| Crypto.jobs | https://crypto.jobs/ | Broad web3 |
| Remote3 | https://www.remote3.co/ | Remote-only |
| Wellfound | https://wellfound.com/role/blockchain | Startup roles |
| Glassdoor | https://www.glassdoor.com/Job/solidity-Remote | Glassdoor |

**Frequency:** Check Tier 1 boards (web3.career, cryptojobslist.com) daily at the same time. Set job alerts where available.

---

## Profile Assessment

### What's Working In Your Favor

Your profile is **genuinely strong** for the current market. Here's why:

1. **AI-native credentials are real** — You shipped an AI CLI for autonomous agent liquidation and an ERC-8004/ERC-8183 agent marketplace at Nunchi. AI mentions in web3 jobs hit 53.1% in March 2026 (up from 23% a year ago). You're already ahead of 90% of applicants on this dimension.

2. **Audit exposure is rare and valuable** — Worked with Quantstamp and Zellic, used Slither and Trail of Bits tooling. Most protocol engineers haven't sat in an audit room. This commands $20-40K premium at senior levels.

3. **DeFi breadth with depth** — Options (Oddz), perpetuals CLOB+AMM (Nunchi), RWA tokenization (Novastro), prediction markets, cross-chain SDK, launchpad, DEX on Aptos, Solana program — this range is unusual. Most engineers specialize in one.

4. **ERC-8004/8183 experience** — This standard finalized August 2025. Very few engineers have production experience with it. Nethermind's role explicitly cited it.

5. **Multi-chain reality** — EVM (primary), Solana/Anchor (Rust), Aptos (Move). Cross-chain is structurally where the money is.

---

## Skill Gaps & Daily Improvement Plan

### Priority 1 — Python (1-2 weeks to functional)
**Why:** Python is mandatory for AI/web3 convergence roles. It's the "power trio" alongside Solidity and Rust. Protocols building AI pipelines use LangChain, CrewAI, FastAPI. Your TypeScript transfers well — the patterns are familiar.

**Daily action:** 30 min/day on Python. Build a simple agent that reads on-chain data (Alchemy/Infura), runs an LLM decision (Claude API), and calls a contract function. This directly maps to your existing agent work at Nunchi — just in Python.

**Resources:**
- Python for JS devs: https://web3.career/learn-web3/web3-developer-2025-roadmap
- LangChain + Ethereum agent tutorial (search "langchain web3 agent tutorial 2026")

---

### Priority 2 — Formal Verification Basics (3-4 weeks)
**Why:** Formal verification roles pay $180K-$250K+ and are severely undersupplied. You already use Slither (static analysis). Next level is Echidna (fuzzing) and Certora Prover (formal proofs). Ethereum Foundation, Web3 Foundation, and Blockswap all have open roles here.

**Daily action:** Spend 45 min every other day:
- Week 1-2: Echidna fuzzing on your existing contracts (Foundry has invariant testing built in — you may already have this)
- Week 3-4: Certora Prover tutorial on a simple ERC-20 contract

**Resources:**
- Ethereum Foundation formal verification: https://web3.career/researcher-engineer-formal-verification-ethereum-foundation/107713
- Certora docs: certora.com/docs

---

### Priority 3 — ZK/zkEVM Fundamentals (ongoing, 1-2 months)
**Why:** ZK-rollups (zkSync, Scroll, StarkNet, Polygon zkEVM) are production now. Not knowing ZK basics is becoming a gap for senior EVM engineers. You don't need to write ZK circuits — just understand how zkEVMs differ in constraint handling, gas behavior, and what breaks when you port contracts.

**Daily action:** 20 min/day reading. Start with zkSync Era docs, then Scroll. Port one of your existing contracts to zkSync Era and note what changes.

---

### Priority 4 — Resume & Application Tweaks
Your resume is solid but missing a few things that would immediately improve recruiter response rates:

1. **Add metrics** — "Secured $X TVL", "Handled $Y volume", "Reduced gas by Z%". Even rough numbers signal scale.
2. **Highlight ERC-8004 work prominently** — Put it front and center in your summary. It's cutting-edge and very few people have it.
3. **Add a 3-line summary at the top** — Recruiters spend 6 seconds on a first scan. A summary like: _"Protocol Engineer specializing in DeFi derivatives (perps, options) and on-chain AI agent infrastructure. Audit experience with Quantstamp and Zellic. Multi-chain (EVM, Solana, Aptos)."_ dramatically improves first impressions.
4. **GitHub presence** — If you have OSS contributions or personal protocol forks, add them. Recruiters for protocol roles look at code.

---

## Market Context (May 2026)

- **53.1%** of web3 job postings mention AI skills (up from 23% in early 2025)
- **AI fluency premium:** 20-30% salary bump over standard blockchain salaries
- **Senior protocol engineers:** $180K-$250K base + token grants worth $100K-$300K
- **Market is hiring:** 5,429 Solidity jobs listed in May 2026
- **Trend:** Market is shifting from "do tasks" to "manage AI agents doing tasks" — your existing agent work at Nunchi positions you ahead of this curve
- **On-chain agents:** Surpassed 122,000 deployments on BNB Chain alone by March 2026

---

## AI Skills Roadmap (If Companies Go AI-First)

You already have a head start (shipped AI CLI + agent marketplace). Here's how to go deeper:

### What to add:
1. **Python** — See Priority 1 above. Not optional.
2. **MCP (Model Context Protocol)** — You already authored Claude Code skills. MCP is how AI agents talk to tools. Build an MCP server that wraps your contract interactions.
3. **Agent frameworks** — LangChain, CrewAI, ElizaOS (web3-native). Know one well.
4. **Verifiable compute** — TEE (Trusted Execution Environments), ZKML. Where on-chain AI verification is heading.
5. **x402 protocol** — Payment primitive for AI agents. Nethermind's role mentioned this alongside ERC-8004.

### What NOT to do:
- Don't chase every new AI buzzword. Your edge is the **web3 + AI intersection** — not pure AI/ML. Stay specialized.
- Don't learn PyTorch unless you want to build models. You want to **use** models via APIs, not train them.

---

## Application Strategy

1. **Personalize each cover note** — 3-4 sentences max. Reference the specific thing they build and a specific thing you built that maps to it.
2. **Cold outreach on LinkedIn** — Most protocol team leads respond to well-targeted DMs. Find the engineering lead or CTO, note a specific protocol decision you found interesting, ask one technical question.
3. **Be active in Discord** — Nethermind, Chainlink Labs, THORChain all have Discord. Answering technical questions in public channels is worth 5 cold applications.
4. **Contribute to OSS** — Even a small PR to a protocol you've integrated (Pyth, Aave, etc.) signals initiative.

---

*Next digest: Tomorrow — check web3.career/defi+solidity-jobs and cryptojobslist.com/solidity for new postings*
