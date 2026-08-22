# Job Search Tracker

Automated daily job search for Bhargav Kacharla — Senior Blockchain Engineer
(Solidity/EVM primary, TypeScript backend, Rust/Anchor on SVM as secondary).

## How this works

- `tracker.json` holds every job posting this routine has already surfaced
  (keyed by a stable id — usually the job board URL). On each scheduled run,
  newly found postings are compared against this file; only postings not
  already in it get pushed to the phone/email notification. This avoids
  re-notifying about the same listing every day it stays open.
- Search focuses on: Senior/Staff Solidity or Smart Contract Engineer roles,
  DeFi protocols (perps, options, lending, RWA tokenization), account
  abstraction (ERC-4337), agent/AI x web3 crossover roles, and Rust/Anchor
  Solana roles as a secondary filter.
- Note: `web3.career` and `cryptojobslist.com` are blocked by this
  environment's egress proxy, so listings are sourced via web search
  snippets/aggregators rather than direct page fetches. Always verify a
  listing is still open before applying — search-indexed postings can be
  stale by days or weeks.

## Upskilling notes

See `upskilling.md` for standing recommendations on where to invest daily,
given the current EVM/AI job market. Updated periodically, not every run.
