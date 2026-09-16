# Daily Web3/Solidity Job Search Log

Automated daily scan for Bhargav Kacharla (Senior Blockchain/Backend Engineer — Solidity/EVM primary, Rust/SVM secondary, TypeScript backend). Each entry lists new leads found that day plus focused upskill recommendations. Older entries are kept for reference/dedup — don't re-list a company+title already logged below unless it's a materially different role.

---

## 2026-09-16

### Open roles worth applying to today

| Company | Role | Comp (as listed) | Source |
|---|---|---|---|
| NUMEUS (Amulet) | Lead Solidity Engineer, on-chain asset management protocol | $160k–$200k | [web3.career](https://web3.career/amulet-lead-solidity-engineer-remote-numeus/29353) |
| GammaSwap Labs | Senior Solidity Engineer | $120k–$230k | [web3.career](https://web3.career/senior-solidity-engineer-gammaswap-labs/47740) |
| NOYA Network | Senior Solidity Engineer | $120k–$200k | [web3.career](https://web3.career/senior-solidity-engineer-remote-noya-network/36506) |
| Austin Werner Ltd (recruiting for a funded DeFi startup) | Senior Solidity Engineer, Smart Contracts | $250k–$350k | [web3.career](https://web3.career/senior-solidity-engineer-smart-contracts-austinwernerltd/38445) |
| STFX | Smart Contract / Solidity Engineer | $100k–$160k + protocol tokens | [web3.career](https://web3.career/smart-contract-solidity-engineer-stfx/33880) |
| Interop Labs | Smart Contract Security Engineer (fully remote, no geo restriction) | — | [cryptocurrencyjobs.co](https://cryptocurrencyjobs.co/engineering/interop-labs-smart-contract-security-engineer/) |
| Advanced Blockchain | Smart Contract Auditor (5+ yrs, Solidity/EVM) | — | [cryptocurrencyjobs.co](https://cryptocurrencyjobs.co/engineering/advanced-blockchain-smart-contract-auditor/) |
| Ethereum Foundation | Web3 Developer, DevEx — Account Abstraction (ERC-4337) & Interop | — | [web3.career](https://web3.career/r/zkjM4ETM__h7utjd3a) |

**Best fits given your background:**
- **GammaSwap / NOYA / Austin Werner listing** — perpetuals/DeFi protocol work maps directly onto your Nunchi.trade CLOB/clearing-house/liquidation experience. Lead with the audit-lifecycle line (Quantstamp/Zellic) and the 1000 events/min indexer.
- **Interop Labs / Advanced Blockchain (security/audit)** — your Slither + Trail of Bits + adversarial review experience is a near-exact match; audit roles pay well and value production shipping experience over pure security-firm pedigree.
- **Ethereum Foundation AA/ERC-4337 role** — your Novastro account-abstraction work (smart accounts, paymasters, bundlers) is directly relevant; EF roles are prestigious and a strong resume signal even if compensation is below top DeFi protocols.

Also check daily (couldn't be scraped directly today — proxy blocked web3.career listing pages): [web3.career/remote+solidity-jobs](https://web3.career/remote+solidity-jobs), [cryptojobslist.com/solidity](https://cryptojobslist.com/solidity), [wellfound.com/role/r/solidity](https://wellfound.com/role/r/solidity).

### Daily improvement recommendations

**Your résumé is already unusually strong for the AI-first shift** — OrgGPT (RAG pipeline, Qdrant, agentic retrieve-then-answer) plus Anthropic/OpenAI SDK experience means you don't need to "add" AI skills from zero. Focus instead on making that experience legible to Web3-specific hiring managers and on closing real gaps:

1. **Surface AI-in-dev-workflow explicitly.** Add a line under Skills or a bullet under Nunchi.trade/OrgGPT calling out concrete AI-assisted engineering practice: e.g. using Claude Code/Cursor for Solidity test generation, invariant/fuzz test scaffolding, or audit-finding triage. Many DeFi teams now screen for "does this person actually use AI tools to ship faster," not just AI-as-product-feature.
2. **Formal verification is the biggest skill gap for top-tier protocol roles.** Certora, Foundry invariant/fuzz testing, and symbolic execution are increasingly required at protocols above $50M TVL. Spend 30–45 min/day working through Certora's tutorials or writing Foundry invariant tests against one of your own past contracts (e.g. the ERC-4626 vault).
3. **ERC-8004/ERC-8183 agent-commerce work is a differentiator — publish it.** On-chain agent marketplaces are a hot niche (agents transacting on-chain). A short writeup or public repo extract of that Nunchi.trade work would stand out on LinkedIn/GitHub and is very on-trend for "AI x crypto" roles.
4. **Rust/Anchor is currently secondary — decide if you want to invest or not.** If targeting SVM-heavy teams (e.g. perps/DeFi on Solana), 3–4 hours/week on Anchor test suites would move you from "have experience" to "can lead." If staying EVM-first, it's fine to leave as-is and market it as a secondary strength.
5. **Interview prep:** brush up on recent EVM upgrades (Pectra/Fusaka changes, EIP-7702) — expect these to come up in senior interviews given account-abstraction overlap with your background.

---
