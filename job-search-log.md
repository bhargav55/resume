# Job Search Log — Bhargav Kacharla

Daily tracking of web3 job leads (Solidity / EVM smart contracts, TypeScript backend, Rust/SVM secondary) and upskilling notes. Newest entries at top.

---

## 2026-08-24

### Target profile
Senior Solidity/EVM engineer (perpetuals, liquidation engines, account abstraction, RWA tokenization, protocol security) + TypeScript backend. Secondary: Rust/Anchor on Solana. Growing AI-agent/LLM tooling skillset (RAG, MCP, agentic auditing).

### High-fit leads (apply first)
1. **MLabs — Senior/Lead Smart Contract Engineer, Perpetuals Exchange (Remote)** — $250K–$500K. Building the largest perp exchange on Arbitrum (~$20B+ cumulative volume). Direct match to the CLOB/liquidation/clearing-house work at Nunchi.trade.
   https://web3.career/senior-lead-smart-contract-engineer-mlabs/139661
2. **Ondo Finance — Senior Smart Contract Engineer (Solidity, Remote)** — $140K–$220K. RWA tokenization focus — directly matches the ERC-3643 compliance/identity-registry work at Novastro.
   https://web3.career/senior-smart-contract-engineer-solidity-ondo-finance/13191
3. **GammaSwap Labs — Senior Solidity Engineer (Remote)** — $120K–$230K. AMM/leveraged-liquidity protocol; concentrated-liquidity + risk-engine background from Oddz is a strong fit.
   https://web3.career/senior-solidity-engineer-gammaswap-labs/47740
4. **NOYA Network — Senior Solidity Engineer (Remote, GMT-friendly)** — $120K–$200K.
   https://web3.career/senior-solidity-engineer-remote-noya-network/36506
5. **STFX — Smart Contract/Solidity Engineer (Remote)** — $100K–$160K + protocol tokens. Trading-adjacent product, EVM security best practices emphasized.
   https://web3.career/smart-contract-solidity-engineer-stfx/33880

### Also worth a look
- Anchorage Digital, Caldera, Sei Development Foundation, Ethereum Foundation, Chainlink Labs — all listing multiple open Solidity/protocol roles (via CryptoJobsList): https://cryptojobslist.com/solidity
- ZKX — Senior Software Developer (Solidity/Cairo), derivatives protocol on Starknet: https://web3.career/senior-software-developer-solidity-cairo-zkx/27983
- Phaxis — Remote Staff Smart Contract Engineer (Solidity, values JS/TS too): https://web3.career/remote-staff-smart-contract-engineer-solidity-phaxis/55896
- TypeScript-in-web3 board (infra/SDK roles, good fit for the backend side): https://web3.career/typescript-jobs
- Full aggregator sweep boards to re-check daily: https://web3.career/remote+solidity-jobs · https://cryptojobslist.com/remote · https://cryptocurrencyjobs.co/evm/

### Market notes
- Smart-contract security auditing demand is up ~250% since 2023; auditors fluent in Slither/Echidna/MythX + fuzzing are commanding top comp (some >$400K). Bhargav's Quantstamp/Zellic audit-lifecycle experience at Nunchi.trade is a strong differentiator worth foregrounding in applications.
- "AI + blockchain integration" is called out as one of the fastest-growing hiring categories ($140K–$250K), but the note from recruiters is that generic "AI + web3" is oversaturated — the scarce, well-paid profile is AI-augmented security engineers and protocol architects who use AI effectively, not people bolting on chatbot demos. Bhargav's agentic Slither-based smart-contract auditor project fits this exact scarce profile if positioned correctly.

### Upskilling recommendations
**AI-in-workflow (near-term, 1-2 weeks each):**
- Turn the "AI Smart-Contract Auditor" side project into a public case study/writeup with concrete before/after findings — this is the single highest-leverage resume item for "AI-first" companies right now. A blog post + short demo video would do more than the GitHub link alone.
- Add Claude Code / Cursor + custom MCP tool usage to the resume's AI/LLM skills line explicitly — many EVM teams are now asking about AI-assisted code review and audit-support tooling in interviews, not just usage of ChatGPT.
- Get hands-on with an AI-driven fuzzing/invariant-testing workflow (e.g., LLM-assisted Foundry invariant test generation) — bridges the audit experience with the AI angle recruiters are pricing highest.

**Core EVM (ongoing, keep sharp):**
- ERC-7579 modular smart accounts — the ecosystem has moved past bare ERC-4337; several AA-focused postings now explicitly ask for ERC-7579 experience on top of ERC-4337.
- EIP-7702 (EOA-to-smart-account upgrades) — increasingly referenced in account-abstraction job specs; worth a short study spike since it's a natural extension of the AA work at Xalts.
- Formal verification / invariant testing depth (Certora or Foundry invariant testing) — pairs well with the audit-lifecycle experience and is explicitly called out as a top-paying niche.

**Not urgent / no action needed:**
- Core Solidity, Foundry/Hardhat, ERC-4337/3643/4626, and TypeScript backend skills remain squarely in demand as-is — resume does not read as outdated on fundamentals.

### Next run
Re-check the boards above for new postings and diff against links already logged here before reporting anything new.
