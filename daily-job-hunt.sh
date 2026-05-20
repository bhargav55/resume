#!/usr/bin/env bash
# Daily web3 job hunt script for Bhargav Kacharla
# Run each morning: bash daily-job-hunt.sh
# Fetches latest listings from RSS feeds matching your skill stack

DATE=$(date +"%Y-%m-%d")
OUTPUT_FILE="job-logs/${DATE}.md"
mkdir -p job-logs

echo "# Web3 Job Hunt - ${DATE}" > "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "_Skills: Solidity · EVM · TypeScript · Rust · DeFi · Perps · RWA · AA · AI Agents_" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# ──────────────────────────────────────────
# Fetch RSS feeds from major web3 job boards
# ──────────────────────────────────────────
fetch_rss() {
  local name="$1"
  local url="$2"
  local keywords="$3"

  echo "Fetching: $name ..."
  local raw
  raw=$(curl -s --max-time 10 "$url" 2>/dev/null)
  if [ -z "$raw" ]; then
    echo "  [WARN] Could not reach $name"
    return
  fi

  # Extract <title> and <link> pairs, filter by keywords (case-insensitive)
  local results
  results=$(echo "$raw" \
    | grep -oP '(?<=<title>)[^<]+|(?<=<link>)[^<]+' \
    | paste - - \
    | grep -iE "$keywords" \
    | head -10)

  if [ -n "$results" ]; then
    echo "## $name" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
    while IFS=$'\t' read -r title link; do
      echo "- [$title]($link)" >> "$OUTPUT_FILE"
    done <<< "$results"
    echo "" >> "$OUTPUT_FILE"
  fi
}

# web3.career – DeFi + Solidity feed
fetch_rss "web3.career – DeFi/Solidity" \
  "https://web3.career/feed/defi+solidity-jobs" \
  "solidity|protocol|smart.contract|engineer|defi"

# web3.career – Protocol Engineer feed
fetch_rss "web3.career – Protocol Engineer" \
  "https://web3.career/feed/protocol-engineer-jobs" \
  "solidity|evm|typescript|rust|defi|perp|rwa"

# web3.career – Remote Blockchain
fetch_rss "web3.career – Remote Blockchain" \
  "https://web3.career/feed/blockchain+remote-jobs" \
  "solidity|protocol|smart.contract|evm|defi"

# cryptojobslist.com – DeFi
fetch_rss "CryptoJobsList – DeFi" \
  "https://cryptojobslist.com/rss/defi" \
  "solidity|protocol|smart.contract|engineer"

# cryptojobslist.com – Solidity
fetch_rss "CryptoJobsList – Solidity" \
  "https://cryptojobslist.com/rss/solidity" \
  "protocol|engineer|senior|lead|defi|perp|rwa"

# crypto.jobs RSS
fetch_rss "crypto.jobs" \
  "https://crypto.jobs/jobs.rss" \
  "solidity|protocol.engineer|smart.contract|evm"

# ──────────────────────────────────────────
# Curated company career pages to check manually
# ──────────────────────────────────────────
cat >> "$OUTPUT_FILE" << 'EOF'
---

## Bookmark – Check These Career Pages Manually Each Day

| Company | Role Fit | Career Page |
|---------|----------|-------------|
| **Morpho Labs** | Protocol Engineer (lending, risk engine) | https://morpho.org/jobs |
| **Hyperliquid** | Backend/Smart Contract Eng (perps L1) | https://jobs.ashbyhq.com/Hyperliquid%20Labs |
| **Uniswap Labs** | Smart Contract Engineer | https://boards.greenhouse.io/uniswaplabs |
| **Aave** | Protocol/Smart Contract | https://aave.com/careers |
| **dYdX** | Protocol Engineer (perps) | https://dydx.exchange/careers |
| **Pendle Finance** | Smart Contract Eng (yield) | https://pendle.finance/careers |
| **Euler Finance** | Protocol Engineer (lending) | https://euler.finance/careers |
| **GMX** | Smart Contract (perps DEX) | https://gmx.io |
| **Circle** | Smart Contract Engineer | https://www.circle.com/en/careers |
| **Alchemy** | Protocol/Integration Engineer | https://www.alchemy.com/careers |
| **OpenZeppelin** | Smart Contract / Security | https://www.openzeppelin.com/jobs |
| **Chainlink Labs** | Smart Contract / Protocol | https://jobs.smartcontract.com |
| **Stader Labs** | Protocol Engineer | https://staderlabs.com/careers |
| **Pyth Network** | Protocol Engineer (oracle) | https://pyth.network/careers |
| **Anchorage Digital** | Protocol Engineer | https://anchorage.com/careers |

EOF

# ──────────────────────────────────────────
# Daily skill improvement reminder
# ──────────────────────────────────────────
cat >> "$OUTPUT_FILE" << 'EOF'
---

## Today's Skill Focus (Rotate Weekly)

### Week 1 – ZK Proofs Foundation
- [ ] Read RareSkills ZK Book Ch 1-2: https://www.rareskills.io/zk-book
- [ ] Understand PLONK vs Groth16 tradeoffs
- [ ] Try: https://github.com/iden3/circom (write a simple Circom circuit)

### Week 2 – Formal Verification
- [ ] Certora Prover tutorial: https://docs.certora.com/en/latest/docs/tutorials/
- [ ] Write one spec for a contract you know (ERC-20 or staking)
- [ ] Try Halmos: https://github.com/a16z/halmos

### Week 3 – Intent Architecture / Solver Design
- [ ] Read ERC-7521 (generalized intents): https://eips.ethereum.org/EIPS/eip-7521
- [ ] Read ERC-7683 (cross-chain intents): https://eips.ethereum.org/EIPS/eip-7683
- [ ] Study UniswapX solver architecture

### Week 4 – AI × Web3 (Already ahead – go deeper)
- [ ] Explore LangGraph for multi-agent workflows: https://langchain-ai.github.io/langgraph/
- [ ] Read Eigenlayer AVS spec – relevant for your agent marketplace
- [ ] Study TEE (Trusted Execution Environments) for verifiable AI agents

EOF

echo "" >> "$OUTPUT_FILE"
echo "_Generated: $(date)_" >> "$OUTPUT_FILE"

echo ""
echo "Done! Report saved to: $OUTPUT_FILE"
echo ""
cat "$OUTPUT_FILE"
