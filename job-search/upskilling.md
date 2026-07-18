# Upskilling & AI-in-Workflow Recommendations

Living doc, revisited on each run. Prioritized by leverage for a senior
Solidity/EVM engineer (perpetuals, account abstraction, audits) moving into
an AI-first web3 market.

## 1. Push the audit-track credential (highest $ leverage)
Current experience (Quantstamp/Zellic audit lifecycle, Slither, Trail of
Bits tooling) is close to the $150k-$280k security-auditor tier used by
Trail of Bits, OpenZeppelin, Spearbit, Cantina, Sherlock. Gap to close:
- Formal verification: Certora, Halmos, Kontrol — none listed on resume yet.
- Fuzzing depth: Echidna, Foundry invariant testing beyond basic usage.
- Public track record: compete in Code4rena / Sherlock / Cantina contests —
  builds a verifiable portfolio and pays per finding while job hunting.

## 2. Lean into "AI x web3" as the differentiator, not a side note
The resume already has two strong AI projects (RAG pipeline, AI smart-contract
auditor with MCP + Slither). This is the rarest combination in the market
right now — most Solidity engineers have zero AI depth, most AI engineers
have zero Solidity depth. Recommendations:
- Ship the AI smart-contract auditor as a public tool/blog post with
  before/after findings on real contracts — turns a resume bullet into a
  demo link.
- Get hands-on with the on-chain AI agent frameworks web3 companies are
  actually shipping against: Coinbase AgentKit, ElizaOS, Virtuals Protocol
  GAME framework, Solana Agent Kit — directly relevant given the ERC-8004/8183
  agent marketplace work at Nunchi.
- Add an evals/observability layer to agent work (LangSmith, Braintrust
  evals, Arize Phoenix) — "how do you know your agent didn't hallucinate a
  liquidation" is exactly the question a perpetuals/agents team will ask.

## 3. Daily AI-in-developer-workflow habits (keep skills from going stale)
- Use an AI code-review pass (Claude Code / Cursor) on every PR before human
  review — cite this explicitly in interviews, teams going AI-first screen
  for it.
- Keep a running eval set of "known-bug" contracts and re-run the AI auditor
  against new Solidity CVEs/exploits monthly — mirrors what audit firms are
  starting to require internally.
- Use LLM-assisted gas-optimization and Slither triage as a daily habit, not
  a project artifact — makes it a demonstrable workflow in interviews.

## 4. Fill the resume gap: Vyper / Move
Move is already listed; Vyper shows up in several senior/lead postings
(Curve-adjacent protocols, Braintrust lead role). A week of Vyper syntax
familiarity is low-cost given Solidity depth already in place.

## 5. TypeScript backend — keep current, don't let it atrophy
Already strong (WebSocket indexers, event streaming). Web3 backend roles
(Gelato, Ondo Finance) increasingly want production experience scaling
these to multi-chain — worth a resume bullet quantifying indexer throughput/
latency numbers if available.
