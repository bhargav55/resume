# Daily Web3 Job Search Log

Tracks daily job leads and upskilling notes for Bhargav Kacharla's web3 job search
(Solidity/EVM smart contracts, TypeScript backend, Rust/SVM secondary).

Each day appends a new dated section below (newest first). Check a role off once applied.

---

## 2026-07-16

### Job leads found today

**Direct/strong fits (Solidity + EVM + perps/derivatives/AA — your core lane):**
- [ ] Smart Contract Engineer — Across Protocol (Risk Labs) — Remote — via [Paradigm Jobs](https://jobs.paradigm.xyz/companies/across-protocol-2/jobs/55077905-smart-contract-engineer)
- [ ] Sr. Smart Contract Engineer — Across Protocol — Remote — via [CryptoJobsList](https://cryptojobslist.com/jobs/sr-smart-contract-engineer-across-protocol-remote)
- [ ] Smart Contract Engineer — UMA — Remote (no geo restriction) — via [Cryptocurrency Jobs](https://cryptocurrencyjobs.co/engineering/uma-smart-contract-engineer/)
- [ ] Smart Contract Engineer — ZetaChain — Remote/NY/SF — via [Cryptocurrency Jobs](https://cryptocurrencyjobs.co/engineering/zetachain-smart-contract-engineer/)
- [ ] Smart Contract Engineer — Lemma — Remote — via [Cryptocurrency Jobs](https://cryptocurrencyjobs.co/engineering/lemma-smart-contract-engineer/)
- [ ] Smart Contract Security Engineer — Interop Labs (Axelar) — Remote — via [Cryptocurrency Jobs](https://cryptocurrencyjobs.co/engineering/interop-labs-smart-contract-security-engineer/)
- [ ] Smart Contract Engineer — Pond — Remote (Asia/Canada/US) — via [Cryptocurrency Jobs](https://cryptocurrencyjobs.co/engineering/pond-smart-contract-engineer/)
- [ ] Web3 Developer Experience Smart Contract Engineer (Solidity/EVM, Go) — IOTA Foundation — Remote, $105k-$120k — via [web3.career](https://web3.career/developer-experience-smart-contract-engineer-isc-solidity-evm-go-iota/61696)
- [ ] Staff Smart Contract Engineer (Solidity) — Phaxis — $76k-$100k — via [web3.career](https://web3.career/remote-staff-smart-contract-engineer-solidity-phaxis/55896)
- [ ] Protocol Engineer — LayerZero Labs — Remote, $120k-$250k — via [LayerZero careers](https://layerzero.network/careers) / [a16z jobs board](https://jobs.a16z.com/jobs/layerzero-labs)
- [ ] Solidity roles — Morpho — check [web3.career/solidity-jobs](https://web3.career/solidity-jobs) (listed as actively hiring, July 2026)

**Perps/derivatives DEX (closest match to your Nunchi.trade CLOB/liquidation work):**
- [ ] Hyperliquid Labs — protocol eng / backend / smart contracts — check [Ashby board](https://jobs.ashbyhq.com/Hyperliquid%20Labs) directly (couldn't confirm specific open reqs today, worth a daily check — they're ~70% of on-chain perp volume right now)
- [ ] Vertex/Ink Foundation — engineering team migrated to Ink (OP Stack L2) post VRTX sunset — worth watching Ink Foundation careers page for perps infra roles

**Job boards to re-check daily yourself (aggregators, not single listings):**
- [web3.career/remote+solidity-jobs](https://web3.career/remote+solidity-jobs) — 3 new remote Solidity roles as of this week
- [web3.career/solidity-jobs](https://web3.career/solidity-jobs) — 4 new this week, includes Anchorage Digital, Caldera, Sei Foundation, Ethereum Foundation, Chainlink Labs
- [cryptojobslist.com/solidity](https://cryptojobslist.com/solidity)
- [cryptocurrencyjobs.co/smart-contracts](https://cryptocurrencyjobs.co/smart-contracts/)

*Note: web3.career and cryptojobslist blocked direct scraping (403) today — the links above come from search snippets, so verify each listing is still open before applying.*

### Upskilling recommendations (reviewed against your current resume)

Your resume already leans into the "AI-first web3" trend harder than most Solidity candidates —
the AI Smart-Contract Auditor and the ERC-8004/8183 agent marketplace work at Nunchi.trade are
genuinely rare combinations right now (ERC-8004 only hit mainnet Jan 2026). Lean into that as your
differentiator rather than treating it as a side note. Concrete next steps:

1. **Turn production experience into public proof.** You've *shipped* an ERC-8004/8183 agent
   marketplace and an AI-native liquidation CLI — almost nobody else applying has this. Write one
   short technical post or open-source a stripped-down version of the AI smart-contract auditor.
   This is the single highest-leverage thing you can do this month for inbound recruiter interest.
2. **Build a public audit/security track record.** Enter a Code4rena or Sherlock contest, or do a
   couple of unpaid/public audits on smaller protocols. Senior Solidity roles ($150k-250k, e.g.
   LayerZero, Across) screen hard on security judgment — a public findings history beats "worked
   with Quantstamp/Zellic" as a line item.
3. **Deepen Rust/SVM given the current market.** Several of the biggest perps protocols to watch
   (Hyperliquid, Drift) are Rust/Solana-native. You already have Anchor experience from Hatchy.fun —
   push it further (e.g. rebuild a small CLOB or liquidation module in Anchor) so you can credibly
   cross-apply to SVM-side perps roles, not just EVM ones.
4. **AI-in-dev-workflow, applied to Solidity specifically.** Go beyond using LLMs for general coding —
   show LLM-assisted Foundry invariant/fuzz test generation, or an eval harness that catches known
   exploit classes (reentrancy, oracle manipulation) automatically. This directly extends your
   AI Smart-Contract Auditor project and is exactly what "AI-first" web3 teams are now asking about
   in interviews.
5. **Track EIP-7702 and intents (ERC-7683) alongside ERC-4337.** Account abstraction hiring is
   shifting toward EIP-7702 (EOA upgrade path) and cross-chain intents — your AA background at
   Xalts is valuable but worth a refresh given how fast this area is moving.
6. **Apply directly + warm channel, not just job boards.** Paradigm's job board and the a16z/Sequoia
   portfolio job boards surface roles at well-funded protocols before they hit general aggregators —
   worth checking those two boards daily in addition to web3.career.

### Daily process note
This log is meant to be appended to each day this routine runs, so you (and future runs) can see
what's already been surfaced and avoid re-notifying on the same listings. Mark items `[x]` once applied.
