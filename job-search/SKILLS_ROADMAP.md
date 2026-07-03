# Upskilling & Positioning Roadmap

Living doc — updated as the daily job-search routine spots gaps between the resume and what postings
are asking for. Reviewed 2026-07-03 against current resume (Nunchi.trade, Novastro, Xalts, Oddz, Rakuten,
OpenText, TCS).

## Where you're already strong
- EVM depth: CLOB matching engines, liquidation/risk engines, oracle integration (Pyth, Stork), ERC-4337
  account abstraction, ERC-3643 RWA, options/derivatives (Oddz), Chainlink Keepers/Gelato automation.
- Audit lifecycle: real experience owning findings triage + fixes with Quantstamp and Zellic — most
  candidates only have "used Slither once," you've run the full external-audit process.
- AI-first differentiation: RAG pipeline + agentic Slither-based smart-contract auditor with eval
  harnesses is genuinely rare — most Solidity devs have zero shipped AI tooling. Lead with this.

## Gaps worth closing (in priority order)

1. **Public proof of security skill.** Job posts for senior/audit-adjacent roles (Spearbit-tier, $190k+)
   weight Code4rena / Sherlock contest results and public audit reports over resume bullets. Action:
   enter 1-2 Code4rena or Sherlock contests/month; publish findings on GitHub even if unranked.
2. **On-chain agent standards visibility.** You're building on ERC-8004/8183 (agent marketplace) at
   Nunchi — this is a very new, thin talent pool. Write 1-2 short technical posts/threads on what you
   built (matching engine + agent marketplace design tradeoffs). This converts internal work into an
   external signal that's hard to fake.
3. **Formal Solana/Rust depth.** You have Anchor experience (Hatchy.fun) but it's one line on the resume
   against companies increasingly hiring cross-chain. Not a pivot — a hedge. Low effort: rebuild one
   small program with newer Anchor + Solana Program Library patterns, note it explicitly as "secondary
   stack" so you don't get miscategorized as SVM-primary.
4. **Gas optimization / formal verification signal.** Postings at the DeFi-primitive tier (GammaSwap,
   Roci.fi) ask for "gas-optimized modular contracts." Add a concrete metric to resume bullets if you
   have one (e.g., "% gas reduction" on a shipped contract); if not, do a small optimization pass on an
   existing OSS contract and document before/after gas numbers.
5. **AI-in-workflow, not just AI-as-product.** Companies going AI-first care about devs who use AI tools
   to ship faster, not just devs who build AI products. Explicitly adopt and be ready to talk about:
   - Claude Code / Cursor for Solidity+TS day-to-day (test generation, refactors, PR review drafts).
   - MCP tool calling for internal workflows (you already have this pattern from the AI Smart-Contract
     Auditor project — reuse it as a talking point).
   - Slither/Foundry fuzzing hooked into an agent loop for pre-audit self-checks — you're close to this
     already; finishing it makes a strong portfolio piece and interview story.

## Recommended cadence
- **Daily:** 30-45 min — one Code4rena/Sherlock issue triage, or one small OSS contract read, or apply
  to 1-2 leads from `JOB_LEADS.md`.
- **Weekly:** ship a small, documented improvement to the AI Smart-Contract Auditor or RAG project and
  push it — keeps GitHub activity visible to recruiters who check contribution graphs.
- **Monthly:** one public write-up (blog/X thread) on something built at Nunchi or in a side project.

## Not needed right now
- Don't chase a full pivot to AI/ML engineering — your leverage is EVM+AI hybrid, which is scarcer and
  better paid than either skill alone. Keep AI as an amplifier on the resume, not the headline.
