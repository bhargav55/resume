# Skill Recommendations & Daily Improvement Plan
**Profile:** Bhargav Kacharla — Protocol Engineer | EVM | DeFi
**Updated:** May 1, 2026

---

## Current Skill Assessment

### Strengths (Keep Sharpening)
| Skill | Evidence | Market Demand |
|-------|----------|---------------|
| Solidity / EVM | CLOB+AMM at Nunchi, options at Oddz, perps | Very High |
| DeFi Primitives | Perps, options, AMM, CLOB, orderbooks | Very High |
| Smart Contract Security | Quantstamp/Zellic audits, Slither, Trail of Bits | Very High |
| ERC Standards | 3643, 4337, 4626, 8004, 8183, 20, 721, 1155 | High |
| Oracle Integration | Pyth, Stork, Chainlink | High |
| Cross-chain | SDK, APIs, bridge integrations | High |
| Foundry + Hardhat | Testing frameworks | High |
| TypeScript/Node.js | Backend services | High |
| Rust/Anchor | Solana (secondary) | Medium-High |

### Skill Gaps vs Market Demand in 2026

---

## Priority 1 — AI-Native Development (URGENT — Market Shifting Fast)

**Why:** Companies are explicitly writing "AI+Web3 hybrid" in JDs now. Your Nunchi work (AI CLI, ERC-8004/8183 agent marketplace) is ahead of most candidates. Double down on this.

### What to Learn
1. **LLM Tool Use / Agent Frameworks**
   - Build agents using Claude API or OpenAI with tool_use/function calling
   - Learn LangChain, LangGraph for agentic workflows
   - Study: MCP (Model Context Protocol) — Claude Code already uses it; learn to build MCP servers for web3 tools
   - Resource: https://docs.anthropic.com/en/docs/agents-and-tools

2. **On-chain AI Agent Standards**
   - ERC-8004 / ERC-8183 you already know — extend this knowledge
   - Study EIP-7701 (native AA for EOAs) — upcoming standard
   - Follow: Coinbase AgentKit, Virtuals Protocol, ai16z/eliza framework

3. **Verifiable AI / zkML**
   - Modulus Labs, EZKL — proving ML model outputs on-chain
   - Not required immediately but a 6-month horizon skill
   - Study: RISC Zero, SP1 (succinct) for ZK proof systems

### Daily Action
- 30 min/day: Build one small AI+web3 integration per week (agent that reads on-chain data, executes a tx, reports back)
- Follow on X/Twitter: @AnthropicAI, @brian_armstrong (Coinbase AgentKit), @virtuals_io

---

## Priority 2 — ZK / Validity Proofs (High Impact, 6-12 Month Investment)

**Why:** ZK rollups (zkSync, Starknet, Scroll, Linea) are now production-scale. DeFi protocols on ZK chains need engineers who understand constraints.

### What to Learn
1. **ZK-EVM Differences** — understand what opcodes behave differently on zkSync Era vs Scroll vs Polygon zkEVM
2. **Cairo / Starknet** — if you want to expand beyond EVM; Starknet has significant DeFi activity
3. **Circom / Noir** — write ZK circuits for custom proof systems
4. **Practical start:** Deploy a Foundry project to zkSync Era, debug the differences

### Resources
- zkSync docs: https://docs.zksync.io/build/developer-reference/ethereum-differences
- Noir (Aztec): https://noir-lang.org/docs
- ZK whiteboard sessions (Dan Boneh on YouTube)

### Daily Action
- 1 hour/week: Work through ZK puzzles on https://zkhack.dev

---

## Priority 3 — Cosmos / CosmWasm (Moderate Impact, dYdX-specific)

**Why:** dYdX v4 runs on Cosmos SDK + Go. If targeting dYdX specifically, know the basics.

### What to Learn
- Cosmos SDK module structure
- CosmWasm for smart contracts on Cosmos
- Go basics (1-2 weeks of practice)

---

## Priority 4 — MEV & Protocol Economics (Deepen Existing)

**Why:** Any protocol hiring for perps/options/AMM will quiz you on MEV, liquidation mechanics, and economic security.

### What to Learn
1. **MEV Research** — read Flashbots research, understand sandwiching, backrunning, frontrunning mitigations
2. **Liquidation Economics** — Dutch auctions, bad debt scenarios, insurance funds
3. **AMM Math** — vAMM mechanics, funding rate formulas, mark price vs index price
4. Study: GMX v2 architecture, Hyperliquid whitepaper, dYdX v4 docs

### Resources
- Flashbots research: https://writings.flashbots.net
- EigenPhi MEV explorer: https://eigenphi.io
- Paradigm research: https://www.paradigm.xyz/writing

---

## Priority 5 — Skills That Are NOT Outdated (Reassurance)

Your stack is current. Here's why:
- **Solidity** — still the dominant smart contract language; will be for 5+ years
- **ERC-4337 (Account Abstraction)** — growing adoption; EIP-7702 is complementary, not replacing
- **Foundry** — industry standard, replaced Hardhat for most serious teams
- **Pyth/Stork oracles** — modern oracle stacks used by top protocols
- **Subgraph/The Graph** — still widely used for indexing

Things to deprioritize:
- **Hardhat** — still used but Foundry is now preferred for new projects; know both
- **OpenZeppelin Defender v1** — they've moved to Defender v2; update your knowledge
- **Biconomy v1 relayers** — gasless tx space has moved to ERC-4337; you're already ahead

---

## Daily Routine (30–60 min/day)

| Time | Activity |
|------|----------|
| Morning (15 min) | Check job boards: web3.career, cryptojobslist, LinkedIn |
| Morning (15 min) | Read 1 DeFi research post or protocol changelog |
| Evening (30 min) | Code: build AI+web3 integration OR ZK exploration |

### Weekly Cadence
- **Monday:** Apply to 2–3 jobs from Tier 1/2 list
- **Tuesday:** Read one protocol whitepaper (Hyperliquid, Morpho, Pendle, etc.)
- **Wednesday:** Build or contribute to an open-source DeFi project on GitHub
- **Thursday:** Write one short post on X/LinkedIn about something you built (visibility)
- **Friday:** Update job tracker, refresh boards for new listings

---

## Visibility Improvements (Non-Code)

Your GitHub and LinkedIn are linked in the resume — good. But:

1. **GitHub profile README** — add a pinned project showcasing the CLOB+AMM or agent marketplace work (if open-source possible)
2. **Write on Mirror.xyz or Substack** — 1 post/month on DeFi mechanics you've built (liquidation flows, funding rates, orderbook matching) — this gets you inbound recruiter messages
3. **X (Twitter) presence** — posting builder content (even short threads about EVM gotchas or security findings) dramatically increases recruiter visibility in web3
4. **Audit contest participation** — Code4rena, Sherlock, Cantina — even 1 valid finding signals security depth to hiring teams

---

## Red Flags to Fix in Resume

1. **Date inconsistency:** Nunchi.trade shows "July '25 - Present" — your current date is May 2026, which means ~10 months. Resume looks accurate.
2. **Move section** — "Developed smart contracts for Warpgate.pro in Aptos Move" is a differentiator; consider adding Move to your skills header.
3. **AI skills gap on resume** — You built an AI-native CLI and agent marketplace (ERC-8004/8183) at Nunchi. Add "AI-native tooling, autonomous agents, MCP" to the skills section explicitly — recruiters are searching for this.
4. **Security line needs more punch** — "Worked with Quantstamp and Zellic" is gold. Elevate this: "Managed full audit lifecycle with Quantstamp and Zellic; remediated findings and co-authored security review reports"
