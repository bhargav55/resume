# Job Search Log — Bhargav Kacharla

Daily tracking of web3 job leads (Solidity / EVM smart contracts, TypeScript backend, Rust/SVM secondary) and upskilling notes. Newest entries at top.

---

## 2026-08-29

### Target profile
Senior Solidity/EVM engineer (perpetuals, liquidation engines, account abstraction, RWA tokenization, protocol security) + TypeScript backend. Secondary: Rust/Anchor on Solana. Growing AI-agent/LLM tooling skillset (RAG, MCP, agentic auditing).

### New/still-open high-fit leads
1. **Almanak — Senior Blockchain Engineer (EVM, Remote)** — ~$74K–$100K. AI + simulation for DeFi protocol optimization — direct overlap with the on-chain agent marketplace (ERC-8004/8183) work at Nunchi.trade.
   https://web3.career/senior-blockchain-engineer-evm-almanak/67141
2. **Polymarket — Smart Contract Engineer, Prediction Markets (Remote)** — designing/deploying Solidity contracts for the largest prediction market platform. Direct match to the prediction-market protocol work at Novastro.
   (search via https://web3.career/remote+solidity-jobs — "Polymarket Smart Contract Engineer")
3. **Solana Labs — Senior Backend Engineer, Solana Mobile (Remote, US/EMEA)** — $175K–$180K. Strong TypeScript/Node.js bar; good stretch role to activate the Rust/Anchor/SVM side skill alongside primary TS backend strength.
   https://web3.career/senior-backend-engineer-solana-mobile-solanalabs/149602
4. **Upside — Senior Solidity Engineer (Remote, North America)** — $100K–$150K.
5. **Fuel Labs — Senior TypeScript Engineer (Remote)** — ~$130K–$141K. Infra/SDK-flavored TS role, good fit for the backend/indexer side of the profile.
   https://web3.career/senior-typescript-engineer-fuellabs/60168

### Still open from prior sweeps (re-verify before applying — first logged 2026-08-24)
- **MLabs — Senior/Lead Smart Contract Engineer, Perpetuals Exchange (Remote)** — $250K–$500K. Largest perp exchange on Arbitrum; direct match to CLOB/liquidation/clearing-house work at Nunchi.trade. https://web3.career/senior-lead-smart-contract-engineer-mlabs/139661
- **Ondo Finance — Senior Smart Contract Engineer, Solidity (Remote)** — $140K–$220K. RWA tokenization — matches ERC-3643 work at Novastro. https://web3.career/senior-smart-contract-engineer-solidity-ondo-finance/13191
- **GammaSwap Labs — Senior Solidity Engineer (Remote)** — $120K–$230K. https://web3.career/senior-solidity-engineer-gammaswap-labs/47740
- **NOYA Network — Senior Solidity Engineer (Remote, GMT-friendly)** — $120K–$200K. https://web3.career/senior-solidity-engineer-remote-noya-network/36506
- **STFX — Smart Contract/Solidity Engineer (Remote)** — $100K–$160K + tokens. https://web3.career/smart-contract-solidity-engineer-stfx/33880

### Lower priority (comp below target or narrower scope — skip unless nothing else lands)
- Braintrust — Lead Solidity/Vyper Engineer (Remote) $70K–$80K
- InBillo — Blockchain/Solidity Engineer (Remote) $20K–$35K
- Horizon Blockchain Games — Senior Backend Engineer (Go, Remote) $43K–$56K

### Boards to re-sweep daily
- https://web3.career/remote+solidity-jobs
- https://web3.career/typescript-jobs
- https://cryptojobslist.com/solidity · https://cryptojobslist.com/remote
- https://cryptocurrencyjobs.co/evm/

### Market notes
- **AI agents are now autonomously exploiting smart contracts.** OpenAI + Paradigm released *EVMbench* (Feb 2026), a benchmark for AI agents detecting/patching/exploiting EVM vulnerabilities — GPT-5.3-Codex reportedly autonomously exploits 70%+ of critical historical Code4rena bugs. This is the clearest signal yet that "AI-augmented security engineer" is becoming table stakes, not a nice-to-have, for senior Solidity roles. Teams will increasingly expect candidates to already use LLM agents as a first-pass auditor before human review.
- Research-grade LLM auditing tools (iAudit — 91% F1 on real vulns; GPTScan combining GPT with static analysis) are moving from academic papers toward production tooling (Slither/Echidna + LLM orchestration). Worth tracking as these get productized.
- Comp spread remains wide ($20K–$500K) — filter aggressively by base comp and scope; the $250K+ roles (MLabs-tier) cluster around perps/derivatives protocols, which is Bhargav's strongest specialization from Nunchi.trade and Oddz.

### Upskilling recommendations
**AI-in-workflow (highest leverage right now):**
- Build a small demo wiring an LLM agent to run Slither/Echidna, triage findings, and draft a fix PR against a Foundry repo — directly answers the "AI-augmented security engineer" bar that EVMbench signals is coming. This is more valuable on a resume right now than another vanilla protocol integration.
- Publish the "AI Smart-Contract Auditor" side project (still the single highest-leverage resume item) as a public write-up with a before/after finding — carry this forward until it's actually shipped.
- Get comfortable narrating Claude Code / Cursor + custom MCP tool workflows in interviews — several EVM teams are now asking about AI-assisted code review/audit tooling specifically, not generic "do you use ChatGPT."

**Core EVM (ongoing, keep sharp):**
- ERC-7579 modular smart accounts — postings increasingly ask for this on top of bare ERC-4337.
- EIP-7702 (EOA→smart-account upgrades) — natural extension of the account-abstraction work at Novastro; worth a short study spike.
- Formal verification / invariant testing (Certora, Foundry invariant tests) — pairs directly with the Quantstamp/Zellic audit-lifecycle experience and is one of the top-paying niches right now.

**Not urgent:**
- Core Solidity, Foundry/Hardhat, ERC-4337/3643/4626, and TypeScript backend fundamentals remain squarely in demand — resume doesn't read as outdated on fundamentals.

### Next run
Re-check the boards above for genuinely new postings, diff against links already logged in this file (and prior dated entries), and only surface what's new or has changed status.
