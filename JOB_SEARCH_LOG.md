# Web3 Job Search Log

Daily log of open Solidity/EVM/Web3 job opportunities matched against Bhargav's
profile (Senior Solidity/EVM smart contract engineer, TypeScript backend,
Rust/Anchor on Solana, AI agent tooling). Updated automatically once per day.
Each entry lists new roles found that day — check off / strike through once
applied so future runs don't re-suggest them.

---

## 2026-08-09

**Strong matches (Solidity/EVM, senior level):**

- [ ] **Ondo Finance** — Senior Smart Contract Engineer (Solidity), Remote, ~$140k–$220k.
      RWA tokenization across multiple EVM chains — direct overlap with the
      ERC-3643 RWA/compliance work at Novastro. https://web3.career/senior-smart-contract-engineer-solidity-ondo-finance/13191
- [ ] **Prime Protocol** — Senior Solidity Engineer, Remote, ~$200k–$250k. Risk engines,
      interest-rate models, price oracles — near 1:1 match with the CLOB/risk-engine/
      Pyth-Stork oracle work at Nunchi.trade. https://web3.career/senior-solidity-engineer-prime-protocol/24583
- [ ] **GammaSwap Labs** — Senior Solidity Engineer, Remote, ~$120k–$230k. DeFi
      derivatives/LP protocol. https://web3.career/senior-solidity-engineer-gammaswap-labs/47740
- [ ] **NOYA Network** — Senior Solidity Engineer, Remote (GMT-friendly hours preferred),
      ~$120k–$200k. https://web3.career/senior-solidity-engineer-remote-noya-network/36506
- [ ] **Ellipsis Labs** — Senior Smart Contract Engineer (EVM), inaugural EVM hire —
      production EVM contracts + auditor coordination, matches the Quantstamp/Zellic
      audit-lifecycle ownership at Nunchi. https://jobs.electriccapital.com/companies/ellipsis-labs/jobs/34338324-senior-smart-contract-engineer-evm
- [ ] **STFX** — Smart Contract / Solidity Engineer, Remote-first, ~$100k–$160k + tokens.
      Perpetuals/trading product — overlap with CLOB & liquidation engine background.
      https://web3.career/smart-contract-solidity-engineer-stfx/33880
- [ ] **Framework Ventures portfolio (perps DEX)** — Senior/Lead Smart Contract Engineer,
      scaling a decentralized perpetuals exchange, ~$180k–$250k. Strongest thematic
      match to the perpetuals CLOB + liquidation flows shipped at Nunchi — worth
      tracking down the exact portfolio company via Framework's careers page.
- [ ] **GammaX** — Senior Blockchain/Solidity Engineer, Remote, ~$80k–$150k.
      https://web3.career/senior-blockchain-solidity-engineer-remote-gammax/36045

**Good matches (TypeScript/backend + Web3):**

- [ ] **Gelato Network** — Senior Web3 Backend Engineer (TypeScript/Node.js), Remote.
      Backend services around on-chain automation/keepers — direct overlap with the
      Chainlink Keepers/Gelato automation work at Oddz.
      https://cryptocurrencyjobs.co/engineering/gelato-network-senior-web3-backend-engineer/
- [ ] **Cool Cats** — Lead NodeJS Developer (Web3), Remote, ~$150k–$200k.
      https://cryptocurrencyjobs.co/engineering/cool-cats-lead-nodejs-developer-web3/
- [ ] **Paxos Labs** — Smart Contract Engineer, scaling DeFi protocol infra
      (Solidity + backend integration).

**Security/audit-adjacent (leverages Quantstamp/Zellic audit-lifecycle experience):**

- [ ] Firms actively hiring Solidity auditors per current market scan: **OpenZeppelin**,
      **Trail of Bits**, **Pashov Audit Group**, **Dedaub** — comp bands ~$130k–$280k
      base + bonus. Also worth entering **Code4rena** / **Sherlock** / **Cantina**
      contest audits in parallel — direct proof-of-skill that converts to firm offers
      and pairs naturally with the AI Smart-Contract Auditor side project.

**Boards to re-check daily for fresh EVM/Solidity postings:**
web3.career/remote+solidity-jobs, cryptojobslist.com/solidity,
cryptocurrencyjobs.co/remote/engineering, jobs.electriccapital.com (curated
VC-portfolio listings — high signal), wellfound.com/role/r/solidity-developer

---

## Skills / Upskilling Recommendations (living list, revisit weekly)

**AI-first hiring trend:** Web3 teams continue folding "AI agent" and "AI-assisted
dev workflow" experience into senior blockchain postings. Bhargav's RAG pipeline,
AI smart-contract auditor project, and the ERC-8004/8183 agent-marketplace work at
Nunchi are already differentiators — keep these prominent near the top of the
resume/LinkedIn headline, not buried after experience bullets.

1. **Ship the AI smart-contract auditor as a public tool.** Turn the Slither + LLM +
   exploit-KB project into something a hiring manager can try in under a minute
   (hosted demo, or a CLI + README with real sample findings on a known-vulnerable
   contract). Still the single highest-leverage resume item for "AI-first" web3 teams.
2. **Formal verification / advanced security tooling.** Add Certora or Foundry
   invariant/fuzz testing to the toolbelt (currently Slither + Trail of Bits tooling
   only) — senior/staff Solidity postings increasingly list this as a differentiator.
3. **Deepen Solana/SVM to a shippable level.** Rust/Anchor exists (Hatchy.fun) but
   reads as one line — EVM+SVM cross-chain roles pay a premium; one more substantial
   Anchor project would let this be pitched as a real second stack.
4. **Make the AI-agent dev workflow explicit in interviews/resume** (Claude Code /
   Cursor / MCP tool-calling in daily dev loop, agentic PR review) — teams going
   AI-first screen for this directly, and it's already true of how this repo itself
   is maintained.
5. **Daily sharpening habit:** rotate between (a) one Ethernaut/Damn-Vulnerable-DeFi/
   Cyfrin-Updraft challenge, (b) reading one rekt.news post-mortem and writing a
   one-paragraph "how I'd have caught this" note, (c) a Foundry fuzz/invariant test
   added to a personal repo. 20–30 min/day compounds fast and gives concrete talking
   points for audits/interviews.
6. **Zero-knowledge basics.** Not urgent, but zk-rollup/zkEVM familiarity (Circom or
   Noir fundamentals) shows up increasingly in senior EVM postings at L2 teams — a
   weekend project would be enough to speak to it credibly.
7. **EIP-7702 / newer account-abstraction surface.** The AA experience on the resume
   is ERC-4337-era (Xalts) — a short write-up or demo showing EIP-7702 (EOA
   upgradeability, now live post-Pectra) would keep the account-abstraction
   experience current rather than reading as slightly dated.
