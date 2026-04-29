#!/usr/bin/env bash
# Daily web3 job search for Bhargav Kacharla
# Run each morning: bash ~/resume/jobs/search.sh
# Opens curated job board URLs filtered for your exact skill set

DATE=$(date +%Y-%m-%d)
OUTPUT_DIR="$(dirname "$0")/logs"
mkdir -p "$OUTPUT_DIR"
LOG="$OUTPUT_DIR/$DATE.md"

echo "# Job Search — $DATE" > "$LOG"
echo "" >> "$LOG"

echo "## Your Target Boards (open in browser)" >> "$LOG"
cat >> "$LOG" << 'EOF'

### Tier 1 — Best signal-to-noise for your profile
- https://web3.career/solidity-jobs           ← Sort by "new", filter Remote
- https://web3.career/defi-jobs               ← Perpetuals, options, RWA roles here
- https://web3.career/ai-jobs                 ← AI+Web3 hybrid (your ERC-8004 work fits perfectly)
- https://cryptojobslist.com/solidity         ← Often has roles not on web3.career
- https://crypto.jobs                         ← 3500+ listings, search "protocol engineer"

### Tier 2 — Direct company career pages (updated weekly)
- https://aave.com/careers                    ← Staff Smart Contract Engineer open NOW
- https://jobs.lever.co/ondofinance           ← Senior SCE $140k-$220k open NOW
- https://jobs.ashbyhq.com/chainlink-labs    ← Senior Solidity SCE open NOW
- https://jobs.ashbyhq.com/polymarket        ← SCE open NOW
- https://job-boards.greenhouse.io/ritual    ← AI+blockchain SCE open NOW
- https://job-boards.greenhouse.io/gensyn    ← AI+blockchain SCE open NOW
- https://boards.greenhouse.io/layerzerolabs ← Cross-chain SCE open NOW
- https://jobs.lever.co/ondofinance          ← RWA tokenization (matches your Novastro work)

### Tier 3 — Aggregators for long-tail opportunities
- https://remote3.co                          ← 22k+ Web3 jobs
- https://web3vacancy.com/jobs/defi          ← DeFi focused
- https://cryptocurrencyjobs.co              ← Good for mid-size protocols

## Your LinkedIn Search Queries (copy-paste)
1. "Protocol Engineer" Solidity remote
2. "Smart Contract Engineer" DeFi remote
3. "Blockchain Engineer" perpetuals remote
4. "Staff Engineer" Solidity EVM remote

## Daily Checklist
- [ ] Check web3.career/solidity-jobs (sort by newest)
- [ ] Check web3.career/ai-jobs (AI+Web3 is your edge)
- [ ] Check direct career pages of target companies above
- [ ] Apply to 2-3 roles with tailored cover letter
- [ ] Log applications below

## Applications Today
| Company | Role | Applied | Status |
|---------|------|---------|--------|
| | | | |

EOF

echo "Log saved to: $LOG"
echo ""
echo "Opening job boards..."

# Detect OS and open browser
if command -v xdg-open &>/dev/null; then
    xdg-open "https://web3.career/solidity-jobs" 2>/dev/null
    xdg-open "https://web3.career/ai-jobs" 2>/dev/null
    xdg-open "https://cryptojobslist.com/solidity" 2>/dev/null
elif command -v open &>/dev/null; then
    open "https://web3.career/solidity-jobs"
    open "https://web3.career/ai-jobs"
    open "https://cryptojobslist.com/solidity"
fi

echo "Done. Edit $LOG to track your applications today."
