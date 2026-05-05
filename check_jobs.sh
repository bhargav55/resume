#!/usr/bin/env bash
# Daily web3 job check — opens fresh listings for Bhargav's profile
# Run: chmod +x check_jobs.sh && ./check_jobs.sh

DATE=$(date +%Y-%m-%d)
echo "=== Web3 Job Search — $DATE ==="
echo ""
echo "Opening job boards for: Solidity | Protocol Engineer | AI+Web3"
echo ""

BOARDS=(
  "https://web3.career/solidity-jobs"
  "https://web3.career/protocol-jobs"
  "https://web3.career/defi+solidity-jobs"
  "https://web3.career/ai-jobs"
  "https://cryptojobslist.com/solidity"
  "https://cryptocurrencyjobs.co/smart-contracts/"
)

DIRECT=(
  "https://jobs.ashbyhq.com/Hyperliquid%20Labs"
  "https://dydx.exchange/careers"
  "https://jobs.ashbyhq.com/ellipsislabs"
)

echo "--- Job Boards (check for new listings posted today) ---"
for url in "${BOARDS[@]}"; do
  echo "  $url"
done

echo ""
echo "--- Direct Protocol Careers Pages ---"
for url in "${DIRECT[@]}"; do
  echo "  $url"
done

echo ""
echo "--- Quick apply reminders ---"
echo "  Tier 1 (strong match):"
echo "  - Ellipsis Labs (EVM perps): https://jobs.ashbyhq.com/ellipsislabs/f5200c58-cada-4e8b-b398-67175ec4bd6b"
echo "  - Hyperliquid Labs: https://jobs.ashbyhq.com/Hyperliquid%20Labs"
echo "  - Ethereum Foundation (AA): https://jobs.lever.co/ethereumfoundation/7c34b7a5-62c4-4905-98eb-2920b6074c09"
echo "  - Pod Network (EVM): https://jobs.ashbyhq.com/pod-network/64ec90ae-a0d3-4175-b29d-27fc35eef85b"
echo "  - asymmetric.re (security): https://jobs.ashbyhq.com/asymmetric.re/5f84cc7d-7032-49e4-b434-3490d5fd153b"
echo ""
echo "=== Log your applications in JOB_SEARCH.md ==="
