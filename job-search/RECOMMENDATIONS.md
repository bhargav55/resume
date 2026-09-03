# Standing Recommendations

Last reviewed: 2026-09-03. This file changes only when the advice changes — check LEADS.md
for the daily job list.

## Where the resume is already strong
- 6 years of production DeFi/Web3 (perpetuals, options, prediction markets, tokenized vaults,
  account abstraction, RWA tokenization) across EVM + Solana is a senior, differentiated
  profile — most Solidity candidates don't have shipped-and-audited protocol experience at
  this depth.
- The audit lifecycle experience (Quantstamp, Zellic, Slither, Trail of Bits tooling) is a
  strong lever for security-focused roles, which pay a premium over general Solidity roles.
- AI/LLM line (Anthropic SDK, OpenAI SDK, RAG, multi-agent, OrgGPT) plus the ERC-8004/8183
  on-chain agent marketplace work is a genuine crossover most Solidity engineers can't claim —
  lean on this for "AI x crypto" roles, which are a growing, less-saturated niche.

## Daily habits while job-hunting
1. **Apply same-day to fresh postings.** Web3 roles at well-known protocols get 100+
   applicants within 48h; check LEADS.md each morning and apply before end of day for
   anything marked "Core Solidity / EVM" or "Security / Audit".
2. **Keep one open Code4rena or Sherlock contest running at all times.** Audit firms
   (Trail of Bits, Spearbit, Cyfrin, OpenZeppelin, Dedaub) hire primarily off contest
   history and public findings, not cold applications — 1-2 public placements materially
   changes response rates from these firms.
3. **Ship visible proof of the AI-crossover skill**, not just list it: a small public repo
   showing an agent that reads on-chain state / calls a contract via a tool (MCP or a custom
   tool schema) is a much stronger signal than the resume line alone, and takes a weekend.
4. **Warm outreach beats cold applications at this seniority.** With 10 years and named
   protocols (Oddz, Novastro, Nunchi.trade) on the resume, a short DM to an engineering
   lead/founder referencing a specific thing they shipped will outperform an ATS application
   for senior/staff roles.
5. **Tailor the resume summary line per role**: lead with "security + audit lifecycle" for
   audit-firm applications, lead with "perpetuals/CLOB + real-time indexing" for trading-
   protocol applications, lead with "AI agent marketplace + RAG" for AI x crypto roles.

## If AI-first hiring keeps expanding (recommended upskilling)
The resume's AI line is currently descriptive (used SDKs, built RAG) rather than
demonstrating AI-in-the-engineering-workflow. Companies going AI-first are increasingly
screening for the latter. Suggested additions, roughly in priority order:
1. **AI-assisted smart contract auditing tools** — get hands-on with LLM-based static analysis
   (e.g. running Slither + an LLM triage pass, or tools like the emerging "AI audit copilot"
   category) and be able to speak to where it catches real bugs vs. hallucinates. This is a
   direct extension of existing audit-lifecycle experience, not a new skill.
2. **Agentic dev workflow fluency** — daily use of Claude Code / Cursor with MCP servers wired
   to the actual repos you work in (not just chat use), plus writing your own MCP tool servers
   for on-chain data (indexer queries, contract state) — an easy showcase project given the
   existing Kafka/indexer background.
3. **Model Context Protocol (MCP)** specifically — it's becoming the default interface for
   agent-to-tool and agent-to-chain integration; the ERC-8004/8183 agent marketplace work is
   conceptually adjacent (agents registering/discovering capabilities on-chain), so drawing
   the explicit parallel in interviews is a strong story.
4. **Deeper agentic orchestration** (multi-agent eval harnesses, tool-use reliability, cost/
   latency tradeoffs at scale) beyond the RAG-pipeline level already listed — this is what
   separates "used OpenAI SDK" from "AI infrastructure engineer" in job descriptions.

## Skill-currency check (nothing urgent, but worth tracking)
- Solidity/Foundry/Hardhat, ERC-4337/4626/3643/8004, upgradeable-contract patterns, and
  Rust/Anchor are all current and in demand — no gap here.
- Watch **account abstraction evolution** (ERC-7702, EIP-4337 v0.8) and **L2/rollup-specific
  Solidity gotchas** (Arbitrum/Optimism/Base quirks) if targeting infra-heavy roles — these
  show up often in senior EVM job descriptions and aren't explicitly on the resume yet.
- Zero-knowledge fundamentals (circuit basics, zkVMs) are increasingly requested for senior
  protocol roles at newer chains — not urgent, but a gap versus the highest-paying frontier
  roles (Succinct, RiscZero-adjacent, zk-rollup teams).
