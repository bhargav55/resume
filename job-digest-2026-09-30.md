# Web3 job digest: 2026-09-30

Profile: Senior backend/blockchain engineer, 10 yrs total, 6 in DeFi/Web3. Strongest on EVM Solidity, TypeScript backend, indexers (Kafka/Redis/subgraphs), audits (Quantstamp, Zellic), ERC-4337/4626/3643/8004. Some Solana/Rust.

Caveat: web3.career and cryptojobslist.com are blocked from this environment, so I could not open listings and check posting dates. The roles below come from search snippets. Check each one is still open before you apply. Salaries are aggregator estimates, not employer-stated.

## Open roles found today

| Company | Role | Fit | Link |
|---|---|---|---|
| Ondo Finance | Senior Smart Contract Engineer (Solidity), multi-chain EVM + tooling | Strong: RWA (ERC-3643), vaults | https://builtin.com/job/senior-smart-contract-engineer-solidity/2269178 , https://dynamitejobs.com/company/ondofinance/remote-job/senior-smart-contract-engineer-solidity |
| Ondo Finance | Blockchain Engineer (RWA tokenization). The listing wants US time zones (PT/MT/CT/ET), so check whether that rules out India | Strong on skills, location uncertain | https://web3.career/senior-smart-contract-engineer-ondofinance/82521 |
| Mantle | Senior Smart Contract Engineer (audits, gas optimization) | Strong | search "Mantle careers" |
| Windranger Labs | Remote Senior Smart Contract Engineer | Good | https://remoteok.io/remote-engineer+senior+solidity-jobs |
| LayerZero | Backend engineer (TypeScript), est. $120k-$200k | Good: TS + indexers | https://web3.career/typescript-jobs |
| Ihsan Pay | Senior backend + blockchain engineer (Go, TS, Postgres, Solana) | Medium: Go is missing | https://web3.career/backend+blockchain-jobs |
| CertiK, Paxos Labs, Binance, Galaxy Digital, Morpho Labs | Solidity roles listed on the boards | Check each careers page | https://cryptojobslist.com/remote_solidity , https://web3.career/solidity-jobs |

Boards to check daily: web3.career, cryptojobslist.com, wellfound.com/role/r/solidity, cryptocurrencyjobs.co, remote3.co.

## Improvement recommendations (today's focus)

1. AI in the dev workflow (the biggest gap to close):
   - Use Claude Code or Codex CLI with Foundry via MCP for test scaffolding, invariant and fuzz generation, and PR review.
   - Try Certora AI Composer, which combines AI codegen with formal verification.
   - Add AI-assisted audit passes on top of Slither and Trail of Bits tools. Keep a human review of every finding.
   - Put a "how I use AI safely on contracts" bullet in the resume and interviews.
2. Foundry depth: stateful invariant testing, fork tests, differential fuzzing. Confirm the resume says Foundry, not only "tests".
3. Formal verification: learn Certora CVL or Halmos. Few candidates have it, and it sets you apart at audit-heavy teams.
4. Public audit track record: post Code4rena, Sherlock or Cantina contest results. Hiring managers value these highly.
5. Newer standards to add or keep: ERC-4337 (done), ERC-7702, transient storage / Cancun-Pectra changes, Uniswap v4 hooks, intent-based systems, ERC-8004 (done).
6. Resume: put the summary line at the top with your target role ("Senior Smart Contract Engineer, EVM"). Add numbers (TVL, volume, audit findings resolved). Keep the ERC-8004/8183 agents work, since AI-agent-on-chain is a hiring theme.
7. Skills to keep sharp on the TypeScript side: viem/wagmi, Ponder or subgraphs, NestJS/Fastify, Postgres, Kafka.

Daily habit (30 min): one Ethernaut, Damn Vulnerable DeFi or Capture the Ethernaut challenge, one audit report read, and one AI-tool experiment.
