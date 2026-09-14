# Upskilling & Positioning Recommendations

Living notes, updated as the market shifts. Latest entry first.

## 2026-09-14

### Resume/skills are not outdated — but positioning can be sharper

The core stack (Solidity, Foundry/Hardhat, upgradeable contracts, ERC-4337,
ERC-4626, ERC-3643, audit-lifecycle ownership with Quantstamp/Zellic) is
current and in-demand. The two things worth tightening:

1. **Lead with the audit-lifecycle line, don't bury it.** "Owned full audit
   lifecycle" is rarer on a resume than "wrote smart contracts" — most
   Solidity engineers haven't sat on the other side of an audit triage.
   Security-track roles (Aave, Nethermind, Chainlink, Consensys Diligence)
   pay well and have less competition than general Solidity dev postings.

2. **The ERC-8004/8183 agent-marketplace line + OrgGPT is a genuine
   differentiator right now, not just a side project.** Very few Solidity
   engineers can also speak fluently about agentic RAG pipelines and
   on-chain agent-to-agent commerce. Companies going AI-first in web3
   (agent marketplaces, autonomous trading agents, AI-run DAOs) are
   actively looking for exactly this combination. Move the AGENTS section
   higher on the resume when applying to AI-adjacent web3 roles instead of
   treating it as an appendix.

### If companies go AI-first: what to actually add to the workflow

Not "learn AI" in the abstract — concretely:

- **Claude Code / Cursor in the Solidity loop**: use it for first-pass
  contract scaffolding, Foundry/Hardhat test-suite generation, and a
  first-pass security review before Slither/Trail of Bits — not to replace
  those tools, but to catch obvious issues earlier and spend the
  static-analysis budget on real findings. Being able to say "I use AI
  agents to accelerate audits, then verify with Slither/Trail of Bits" is a
  strong interview answer for 2026 hiring managers.
- **MCP servers for on-chain tooling**: there's a growing ecosystem (Foundry
  MCP, EVM MCP tools, Solidity static-analyzer MCPs) — spend a weekend
  wiring one into a real workflow (e.g., an MCP that pulls contract state /
  runs Foundry tests) and put it on GitHub. This directly extends the
  OrgGPT/agent work already on the resume and is a cheap, concrete
  portfolio addition.
- **Formal verification**: Certora Prover or Foundry's invariant/fuzz
  testing are not yet mentioned on the resume. Given the
  perpetuals/liquidation/settlement work, formal verification experience
  would meaningfully strengthen applications to protocols handling large
  TVL (this is the single highest-leverage skill gap found so far).

### Other skill-gap candidates worth 1-2 weeks each

- **Restaking / EigenLayer AVS development** — one of the hottest hiring
  categories in EVM right now; the oracle/Pyth/Stork integration
  experience transfers directly.
- **Cross-chain messaging (LayerZero, Chainlink CCIP)** — Chainlink
  experience exists (Keepers, price feeds) but not messaging; several
  senior postings list this explicitly.
- **Deepen the Solana/Anchor side** if staying open to SVM roles — currently
  listed as secondary experience; a couple of Anchor programs on GitHub
  would make it a credible "also do SVM" claim rather than a resume line.

### Daily habit suggestion

Spend 15 minutes/day on one of: reading a recent audit report (Sherlock/
Code4rena contest reports are free and high-signal), or shipping one small
addition to the MCP/agent-tooling side project above. Consistent small
audit-report reading compounds fast for the security-track applications.
