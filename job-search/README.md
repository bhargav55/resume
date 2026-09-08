# Job Search Tracker

Automated daily digest of Web3/Solidity/EVM job leads for Bhargav Kacharla, run as a
scheduled Claude Code routine against this repo.

- `digests/YYYY-MM-DD.md` — one file per day the routine ran, with new job leads found
  that day plus notes on anything already surfaced on a previous day (deduped via
  `seen-jobs.md`).
- `seen-jobs.md` — running log of every job (company + title) already surfaced, so
  daily digests only highlight genuinely new postings as "new" and don't repeat stale
  ones every day. Old postings are still listed in digests as "still open" if
  re-confirmed, just not treated as new.
- `upskill-recommendations.md` — living document of skill-gap / positioning advice,
  updated when the market picture materially changes rather than every single day.

Note: this repo's sandbox blocks direct fetches of job-board domains (web3.career,
cryptojobslist.com, cryptocurrencyjobs.co, greenhouse/lever/ashby ATS pages), so leads
are gathered via web search snippets and cross-referenced company career pages where
reachable. Always verify a listing is still open and re-read the full JD before
applying — figures like salary ranges quoted by aggregator sites are often
platform-estimated, not confirmed by the employer.
