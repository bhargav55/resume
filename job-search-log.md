# Job Search Log — Bhargav Kacharla (Web3 / Solidity / EVM)

Automated daily scan for open roles matching: Solidity/EVM smart contracts, TypeScript backend,
Rust/Anchor (SVM), DeFi protocols (perps, options, vaults, RWA, account abstraction), smart
contract security. Each entry below is a day's findings — new run appends a new dated section
rather than repeating leads already logged, unless a listing is still open and worth a reminder.

---

## 2026-09-01

### Strong-fit leads (found via web search — verify still open before applying)

| Company | Role | Why it fits | Link |
|---|---|---|---|
| Chainlink Labs | Senior Smart Contract Engineer, Solidity | 5-8+ yrs eng, 3+ yrs smart contracts — owns architecture securing CCIP; matches your protocol-core + audit background | https://jobs.ashbyhq.com/chainlink-labs/842e9d47-982c-4dfb-8461-1080759c82d9 |
| Safe (SafeGlobal) | Solidity Engineer | Safe is THE account-abstraction/smart-wallet company — direct match to your ERC-4337 (Novastro) experience | https://jobs.ashbyhq.com/safe.global/ec342eb4-10dd-4ce0-8121-1f589aa20c14 |
| Stackup (YC) | Senior Blockchain Engineer, Account Abstraction | ERC-4337 bundler work, $100K-$200K, remote — direct overlap with paymaster/bundler work at Novastro | https://ycombinator.com/companies/stackup/jobs/bjKJNaR-senior-blockchain-engineer-account-abstraction |
| Sei Labs | Solidity / Smart Contracts Engineer | EVM L1, remote, protocol-level Solidity | https://jobs.lever.co/SeiLabs/64c40993-eaaf-41de-a73f-60d846f7393c |
| Aragon | Smart Contract Engineer | DAO/governance contracts, deep Solidity architecture | https://jobs.lever.co/aragon/09e50def-184c-433a-a94b-2c605fafd68b |
| Trust Wallet | Smart Contract Engineer | ERC-4337/6900/7579/7702, 3+ yrs, fully remote | via cryptocurrencyjobs.co / company careers page |
| Nethermind | Solidity Auditor | Fully remote, matches your Quantstamp/Zellic audit-lifecycle + Slither/Trail of Bits experience | https://cryptocurrencyjobs.co/engineering/nethermind-solidity-auditor/ |
| CertiK | Blockchain Security Engineer (Solidity/Rust/Golang) | Audit firm — leverages your security-review background directly | https://jobs.lever.co/certik/478ab0cd-9f5e-4b88-88b5-01d3beac4d81 |
| Veda Tech Labs | Smart Contract Engineer | Solidity architecture + delivery + security ownership | https://jobs.lever.co/vedatechlabs/c49b4993-d504-49aa-8cf5-03aa19e4895b |

### Job boards to check daily (fastest-moving, best signal for new postings)
- https://web3.career/evm+remote-jobs
- https://web3.career/defi+remote-jobs
- https://cryptojobslist.com/remote
- https://wellfound.com/role/r/solidity-developer
- https://www.remoterocketship.com/jobs/smart-contract-engineer/

### Market notes
- Senior smart-contract/protocol engineers with production audit experience are commanding
  $180K-$250K+ at well-funded protocols, sometimes with token allocations.
- Account-abstraction (ERC-4337 and successors 6900/7579/7702) is a hot, narrow niche right
  now — your Novastro work is a strong differentiator, lead with it.
- Security/audit-adjacent roles (CertiK, Nethermind, independent contest platforms) are
  actively hiring and value your Quantstamp/Zellic audit-lifecycle experience highly.

### Upskilling recommendations

**AI-in-workflow (companies going AI-first):**
- You're already ahead of most Solidity-only candidates — OrgGPT + Anthropic/OpenAI SDK + RAG
  experience is a genuine differentiator. Make it visible: add it explicitly to job applications
  as "AI-augmented smart contract engineer," not just a side project.
- Adopt AI-assisted security review as a daily habit: run Claude/Cursor over diffs before
  submitting PRs, specifically prompting for reentrancy, access-control, and oracle-manipulation
  patterns — then compare against Slither output. Firms are starting to ask about this workflow
  in interviews.
- Given your ERC-8004/8183 agent-marketplace work at Nunchi, position yourself for the emerging
  "agentic DeFi" niche (agents that trade, settle, or manage vaults on-chain) — very few
  candidates have shipped both sides (agent commerce standards + the AI agent stack).

**Skill gaps / upskilling if targeting top-tier protocols:**
- Formal verification: Certora or Foundry invariant/fuzz testing — increasingly a bar for senior
  hires at protocols handling large TVL.
- Restaking / LST ecosystem (EigenLayer, symbiotic) — adjacent to your vault and yield-routing
  experience, currently in high demand.
- Public audit track record: compete in Code4rena, Sherlock, Cantina, or CodeHawks contests.
  This is the single highest-leverage way to convert your existing audit experience into a
  public, verifiable reputation — many senior security hires come directly from contest
  leaderboards.
- Keep Rust/Anchor warm with one small SVM side-project shipped publicly, so SVM stays a real
  secondary option rather than "past exposure."

---
