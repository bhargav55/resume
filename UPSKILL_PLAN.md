# Upskilling & Positioning Plan

Context: primary skills are Solidity/EVM smart contract engineering and
TypeScript backend, ~10 yrs experience, secondary Rust (Anchor/Solana).
Resume already shows real AI/agent work (RAG pipeline, agentic AI
smart-contract auditor, MCP tool calling, LangChain/LangGraph), so the base
"do I need to learn AI" question is mostly already answered — the gap is
depth, proof, and visibility, not starting from zero.

## Where you're already ahead

- Built an on-chain **agent marketplace (ERC-8004/8183)** — this is a 2025-2026
  bleeding-edge standard most Solidity engineers haven't touched. Very few
  candidates can say "I shipped ERC-8004" in an interview.
- Shipped an **agentic AI smart-contract auditor** (LLM + MCP + Slither +
  exploit-DB retrieval + eval harness) — this is exactly the kind of
  "AI-native security tooling" that audit firms and AI-first DeFi protocols
  are trying to build internally right now.
- Real production audit experience (Quantstamp, Zellic, Slither, Trail of
  Bits) — most Solidity-only candidates don't have the auditor-facing side.

## Gaps to close, ranked by leverage

1. **Make the AI auditor project legible and public.** The resume doesn't
   link a repo for it (RAG project has a GitHub link, the auditor doesn't).
   Priority this week:
   - Push a public repo + README with architecture diagram, eval harness
     results, and a short demo (Loom/video or GIF of it catching a known
     bug from a benchmark like DeFiHackLabs).
   - Write a short technical post ("I built an agentic AI auditor with
     Slither + MCP + eval harnesses") on X/Mirror/your site — this is the
     single highest-leverage thing you can do, since it converts a resume
     bullet into something a hiring manager can click and verify in 2 minutes.

2. **Depth over breadth on agent frameworks.** You already list LangChain/
   LangGraph/MCP/Anthropic SDK/OpenAI SDK. Don't chase more frameworks —
   instead go deep on the parts hiring teams actually probe:
   - Eval/observability tooling: Langfuse, Braintrust, or promptfoo — add
     one concretely to the auditor project so you can talk numbers (false
     positive rate, benchmark pass rate) in interviews, not just "I built evals."
   - Multi-agent orchestration failure modes (tool-call loops, context
     rot, cost control) — these are what separates "used LangGraph in a demo"
     from "ran this in production," which matches your "running 24/7 with
     self-evaluation pipelines" resume line — make sure you can back that
     claim with specifics (uptime, cost/run, failure recovery) in an interview.

3. **EVM depth for staff-level bar.** For $180k-$250k+ roles at top
   protocols, the bar above "shipped features" is: gas optimization at the
   bytecode/storage-layout level, fuzzing/invariant testing (Foundry
   invariants, Echidna), and increasingly formal verification (Certora,
   Halmos). Pick one (Foundry invariant testing is the highest ROI given
   you already use Foundry) and add a visible example to a public repo.

4. **Solana/Rust — keep as differentiator, not a pivot.** Since EVM is
   primary, don't invest heavily here. But your Hatchy.fun/Anchor experience
   already clears the bar for roles that want "EVM-primary, Solana-aware"
   (e.g., Circle's listing above) — mention it explicitly rather than
   burying it, since dual-chain candidates are genuinely rare.

5. **Outbound visibility for the AI x Web3 niche.** The "on-chain agent
   marketplace + LLM tooling" combination isn't a job title recruiters
   search for yet — you likely have to create the opening rather than find
   a listing:
   - Post about the ERC-8004 marketplace build and the auditor project
     regularly (weekly cadence beats one big post).
   - DM/apply directly to teams building agent-economy infra (e.g., teams
     around ERC-8004/x402/agent-payments, Coinbase's agent tooling efforts,
     Virtuals/other agent-launchpad projects) even without a live req —
     this segment hires off reputation and demos more than job posts.

## Daily habit (30-60 min, on top of applying)

- **Mon/Wed/Fri:** one Foundry invariant test or Slither/Echidna finding
  added to a public repo, or progress on the auditor project's eval suite.
- **Tue/Thu:** one audit contest finding submitted (Code4rena/Cantina/Sherlock)
  or one round of review on a live contest — compounds into both income and
  a public track record.
- **Daily, 10 min:** skim `job-search/README.md` boards + apply to anything
  in that day's `job-search/YYYY-MM-DD.md` list.
- **Weekly:** one build-in-public post (X/Mirror) about either the perps/CLOB
  work, the ERC-8004 agent marketplace, or the AI auditor project.

## If AI-first hiring keeps accelerating

Don't re-skill into a generalist "AI engineer" — that's a crowded lane and
throws away your differentiation. The winning position is **"Solidity/EVM
security engineer who builds AI tooling to audit and operate smart
contracts"** — a narrow, credible, hard-to-fake niche you already have two
real projects in. Double down on proof (repo, numbers, demo) over adding
more frameworks to the skills list.
