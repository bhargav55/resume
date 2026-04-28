#!/usr/bin/env bash
# Run this each morning to generate a new daily digest via Claude Code.
# Usage: ./scripts/daily-digest.sh
#
# This launches Claude Code with a prompt to search today's job boards
# and generate a new digest file at daily-digest/YYYY-MM-DD.md

TODAY=$(date +%Y-%m-%d)
DIGEST_FILE="daily-digest/${TODAY}.md"

if [[ -f "$DIGEST_FILE" ]]; then
  echo "Digest for $TODAY already exists: $DIGEST_FILE"
  echo "Open it with: cat $DIGEST_FILE"
  exit 0
fi

echo "Generating digest for $TODAY..."
echo "Tip: run this inside a Claude Code session with the prompt below."
echo ""
echo "--------- PASTE THIS PROMPT INTO CLAUDE CODE ---------"
cat <<'PROMPT'
Search for new web3/DeFi/smart contract engineer job openings posted today or this week.
Focus on roles matching: Protocol Engineer, Smart Contract Engineer, DeFi Engineer, Blockchain Engineer.
Key skills to match: Solidity, EVM, perpetuals, AMM, CLOB, DeFi, TypeScript, smart contract security.
Search these boards: cryptojobslist.com, web3.career, crypto.jobs, remote3.co.
Also check career pages for: Ethena, Paradex, Uniswap, dYdX, Morpho, Euler, Hyperliquid, Autonolas.

Then generate a daily digest file at daily-digest/YYYY-MM-DD.md (today's date) following the
format of daily-digest/2026-04-28.md. Include:
1. Tier 1/2/3 job table with direct apply links
2. Today's one focused skill recommendation from recommendations.md (rotate weekly focus)
3. Any new protocols or companies worth tracking

Also do a quick scan: are there any new ERC standards, DeFi exploits in the news, or hot Twitter/X
threads in the Solidity/DeFi space worth knowing about? Add a "Today in Web3" section at the bottom.
PROMPT
echo "-------------------------------------------------------"
