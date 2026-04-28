#!/usr/bin/env bash
# Opens all web3 job boards filtered for protocol/smart-contract engineer roles.
# Run each morning before applying.

BOARDS=(
  "https://cryptojobslist.com/solidity"
  "https://cryptojobslist.com/defi"
  "https://web3.career/protocol-engineer-jobs"
  "https://web3.career/solidity-jobs"
  "https://web3.career/defi+solidity-jobs"
  "https://crypto.jobs"
  "https://www.remote3.co"
  "https://cryptocurrencyjobs.co/engineering/"
  # Target company career pages
  "https://jobs.ashbyhq.com/Hyperliquid%20Labs"
  "https://job-boards.greenhouse.io/uniswaplabs"
  "https://paradex.trade/careers"
  "https://ethena.fi/careers"
  "https://morpho.org/careers"
  "https://euler.finance/careers"
  "https://olas.network/careers"
)

echo "Opening ${#BOARDS[@]} job boards..."

for url in "${BOARDS[@]}"; do
  if command -v xdg-open &>/dev/null; then
    xdg-open "$url" 2>/dev/null
  elif command -v open &>/dev/null; then
    open "$url"
  else
    echo "$url"
  fi
  sleep 0.3
done

echo "Done. Good luck today, Bhargav!"
