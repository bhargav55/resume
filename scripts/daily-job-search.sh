#!/usr/bin/env bash
# Run this every morning to open all job boards in your browser
# Usage: bash scripts/daily-job-search.sh

DATE=$(date +%Y-%m-%d)
echo "=== Daily Web3 Job Search — $DATE ==="
echo ""

echo "Opening primary job boards..."

BOARDS=(
  "https://web3.career/solidity-jobs"
  "https://web3.career/defi+solidity-jobs"
  "https://web3.career/protocol-engineer-jobs"
  "https://cryptojobslist.com/solidity"
  "https://cryptocurrencyjobs.co/smart-contracts/"
  "https://wellfound.com/role/smart-contract"
  "https://www.remote3.co/"
  "https://web3vacancy.com/jobs/defi"
)

echo ""
echo "Direct company career pages to check:"
echo "  - Ellipsis Labs:  https://jobs.ashbyhq.com/ellipsislabs"
echo "  - Chainlink Labs: https://chainlinklabs.com/open-roles"
echo "  - dYdX:           https://dydx.exchange/careers"
echo "  - Hyperliquid:    https://jobs.ashbyhq.com/Hyperliquid%20Labs"
echo "  - Morpho:         https://morpho.org/careers"
echo "  - Aave:           https://aave.com/careers"
echo "  - GMX:            https://gmx.io/#/jobs"
echo "  - Synthetix:      https://synthetix.io/jobs"
echo "  - Pendle:         https://pendle.finance/careers"
echo ""
echo "Search keywords to use on LinkedIn today:"
echo "  \"Protocol Engineer\" Solidity DeFi"
echo "  \"Smart Contract Engineer\" EVM remote"
echo "  \"Blockchain Engineer\" perpetuals"
echo "  \"DeFi Engineer\" solidity audit"
echo ""
echo "Log applications in: jobs/opportunities-$(date +%Y-%m-%d).md"
echo ""

# Open all boards if on a desktop environment
if command -v xdg-open &> /dev/null; then
  for url in "${BOARDS[@]}"; do
    xdg-open "$url" &
    sleep 0.5
  done
elif command -v open &> /dev/null; then
  for url in "${BOARDS[@]}"; do
    open "$url"
    sleep 0.5
  done
else
  echo "Copy and open these URLs in your browser:"
  for url in "${BOARDS[@]}"; do
    echo "  $url"
  done
fi

echo "=== Done. Apply to 2-3 positions today. ==="
