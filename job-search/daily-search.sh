#!/bin/bash
# Daily Web3 job search opener — run each morning
# Usage: bash daily-search.sh

DATE=$(date +%Y-%m-%d)
echo "=== Web3 Job Search — $DATE ==="
echo ""
echo "Opening job boards..."

# Core job boards
URLS=(
  "https://web3.career/defi+solidity-jobs"
  "https://cryptojobslist.com/solidity"
  "https://cryptocurrencyjobs.co/smart-contracts/"
  "https://web3.career/ai-jobs"
  "https://web3.career/tokenization-jobs"
)

# Priority company career pages
COMPANY_PAGES=(
  "https://chainlinklabs.com/open-roles"
  "https://jobs.ashbyhq.com/Hyperliquid%20Labs"
  "https://dydx.exchange/careers"
  "https://jobs.ashbyhq.com/cyfrin"
  "https://jobs.lever.co/openzeppelin"
)

for url in "${URLS[@]}"; do
  echo "Opening: $url"
  if command -v xdg-open &>/dev/null; then
    xdg-open "$url"
  elif command -v open &>/dev/null; then
    open "$url"
  fi
  sleep 0.5
done

echo ""
echo "Opening company career pages..."
for url in "${COMPANY_PAGES[@]}"; do
  echo "Opening: $url"
  if command -v xdg-open &>/dev/null; then
    xdg-open "$url"
  elif command -v open &>/dev/null; then
    open "$url"
  fi
  sleep 0.5
done

echo ""
echo "=== TODAY'S CHECKLIST ==="
echo "[ ] Scan job boards above for new listings"
echo "[ ] Check Hyperliquid/dYdX/Chainlink Labs for openings"
echo "[ ] 30 min: ZK learning (Noir) or Formal Verification (Halmos)"
echo "[ ] Post 1 technical tweet"
echo "[ ] Cold DM 1 engineering lead at a target company"
echo ""
echo "=== QUICK APPLY LINKS ==="
echo "Chainlink Labs CCIP: https://jobs.ashbyhq.com/chainlink-labs/842e9d47-982c-4dfb-8461-1080759c82d9"
echo "Hyperliquid Labs:    https://jobs.ashbyhq.com/Hyperliquid%20Labs"
echo "dYdX:               https://dydx.exchange/careers"
echo "Cyfrin:             https://jobs.ashbyhq.com/cyfrin"
echo "OpenZeppelin:       https://jobs.lever.co/openzeppelin"
echo "LangChain AI Eng:   https://jobs.ashbyhq.com/langchain/c75915ba-a32b-4e17-873d-19b47564170d"
echo ""
echo "=== UPSKILLING (pick one today) ==="
echo "ZK (Noir):          https://noir-lang.org"
echo "Formal Verify:      https://docs.certora.com  |  https://github.com/a16z/halmos"
echo "Intents/Solvers:    https://docs.uniswap.org/contracts/uniswapx/overview"
echo ""
echo "Done! Good luck today, Bhargav."
