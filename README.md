# Bhargav Kacharla — Job Search System

Daily job digest + skill tracker for web3/DeFi Protocol Engineer roles.

## Daily Routine (15 minutes each morning)

```bash
# 1. Generate today's digest (inside Claude Code session — paste the prompt from the script)
./scripts/daily-digest.sh

# 2. Open all job boards in browser
./scripts/open-job-boards.sh

# 3. After applying, log it
./scripts/apply-tracker.sh add "Ethena Labs" "Smart Contract Engineer" "https://..." "Applied"

# 4. View all applications
./scripts/apply-tracker.sh list
```

## Files

| File | Purpose |
|---|---|
| `daily-digest/YYYY-MM-DD.md` | Daily job listings + skill tip |
| `recommendations.md` | Full skill gap analysis + upskill roadmap |
| `applications.csv` | Application tracker |
| `scripts/daily-digest.sh` | Prompt to generate today's digest in Claude Code |
| `scripts/open-job-boards.sh` | Opens all job boards in browser |
| `scripts/apply-tracker.sh` | CLI application tracker |

## Target Companies (Priority Order)

1. **Ethena Labs** — yield-bearing assets, direct Nunchi overlap
2. **Paradex** — CLOB perp DEX, Paradigm-backed
3. **Autonolas/Valory** — on-chain AI agents, ERC-8004/8183 match
4. **Uniswap Labs** — AMM depth, ~$308k remote
5. **dYdX** — perpetuals, mature protocol
6. **Morpho / Euler** — risk engine, lending
7. **Ritual.net / Giza** — AI x Web3
8. **Hyperliquid** — dream role; prep Rust first

## Current Skill Priorities

1. Zero Knowledge (Noir → Circom → SP1)
2. Formal verification (Halmos → Certora)
3. AI agent frameworks (Claude API, LangGraph, Eliza)
4. MEV / searcher mechanics
5. L2 app-chain dev (OP Stack)
