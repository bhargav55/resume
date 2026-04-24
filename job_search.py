#!/usr/bin/env python3
"""
Daily Web3 Job Search Script for Bhargav Kacharla
Run: python3 job_search.py
Outputs a dated report in ./reports/
"""

import sys
import json
import datetime
import urllib.request
import urllib.parse
import re
import os
from html.parser import HTMLParser

TODAY = datetime.date.today().isoformat()
REPORT_DIR = os.path.join(os.path.dirname(__file__), "reports")

# --------------------------------------------------------------------------
# Profile: keywords used to score job relevance
# --------------------------------------------------------------------------
MUST_HAVE = [
    "solidity", "smart contract", "evm", "defi", "protocol engineer",
    "blockchain engineer", "web3 engineer",
]
NICE_TO_HAVE = [
    "typescript", "perpetuals", "dex", "amm", "clob", "rwa", "options",
    "foundry", "hardhat", "rust", "anchor", "account abstraction",
    "erc-4337", "erc-3643", "erc-4626", "pyth", "chainlink", "oracle",
    "security", "audit", "subgraph", "the graph", "cross-chain",
    "liquidation", "clearinghouse", "onchain agent", "ai agent",
]

# --------------------------------------------------------------------------
# Job boards: (name, search URL template)
# --------------------------------------------------------------------------
JOB_BOARDS = [
    ("web3.career – Solidity",     "https://web3.career/solidity-jobs"),
    ("web3.career – Protocol",     "https://web3.career/protocol-jobs"),
    ("web3.career – DeFi+Solidity","https://web3.career/defi+solidity-jobs"),
    ("web3.career – Remote",       "https://web3.career/remote+solidity-jobs"),
    ("web3.career – AI+Web3",      "https://web3.career/ai-jobs"),
    ("CryptoJobsList – Solidity",  "https://cryptojobslist.com/solidity"),
    ("CryptoJobsList – Web3",      "https://cryptojobslist.com/web3"),
    ("Crypto.jobs",                "https://crypto.jobs/jobs?skills=solidity"),
    ("LaborX – Full-time",         "https://laborx.com/vacancies?skills=solidity"),
    ("Remote3",                    "https://remote3.co"),
]

# Companies that are strong matches based on Bhargav's exact experience
TARGET_COMPANIES = {
    "Hyperliquid":   "Perpetuals DEX — mirrors current role at Nunchi (CLOB+AMM, clearing house)",
    "dYdX":          "Perpetuals DEX on EVM/Cosmos — strong protocol alignment",
    "GMX":           "Perpetuals on Arbitrum/Avalanche — matches EVM+DeFi depth",
    "Polymarket":    "Prediction markets — built one at Novastro",
    "Cega":          "Options/exotic derivatives — matches Oddz options experience",
    "Gains Network": "gTrade perpetuals — Solidity+Chainlink, exact stack",
    "Vertex Protocol":"CLOB+AMM DEX on Arbitrum — near-identical architecture",
    "Synthetix":     "Perpetuals v3 + liquidity layer — advanced DeFi protocol work",
    "Aave":          "Integrated Aave at Novastro; core team hires protocol engineers",
    "Morpho":        "Lending protocol, Solidity-heavy, security-focused hiring",
    "Securitize":    "RWA tokenization (ERC-3643) — matches Novastro work exactly",
    "Centrifuge":    "RWA/real-world assets on EVM — RWA tokenization specialist",
    "Zero Hash":     "Tokenization infrastructure, compliance-aware smart contracts",
    "Biconomy":      "Account abstraction (ERC-4337) — used at Oddz, built at Xalts",
    "Safe (Gnosis)": "Account abstraction & multisig infrastructure — ERC-4337 match",
    "Chainlink Labs":"Used their Keepers at Oddz; deep oracle integration experience",
    "MLabs":         "Smart contract engineer (Solidity + Rust) — has both",
    "Olas Network":  "Onchain AI agent marketplace — ERC-8004/8183 work at Nunchi",
    "Brian Protocol":"AI+Web3 infrastructure — matches AI-native CLI work",
    "Quantstamp":    "Already worked with them on audits — security expertise fits",
    "OpenZeppelin":  "Deep familiarity with their stack across 4+ roles",
}

DAILY_TIPS = [
    # Skill gaps (rotate through these)
    {
        "category": "Formal Verification",
        "tip": "Senior protocol roles increasingly require Certora Prover or Halmos. "
               "Start with Halmos (Python, Foundry-compatible). Run: `pip install halmos`. "
               "Port one of your Foundry test suites to symbolic execution this week.",
        "resource": "https://github.com/a16z/halmos",
    },
    {
        "category": "ZK Fundamentals",
        "tip": "ZK knowledge is now a differentiator at top-tier DeFi roles. "
               "Learn Noir (Aztec's ZK DSL) — it's Rust-like and closest to your current stack. "
               "Build a simple Merkle proof verifier circuit.",
        "resource": "https://noir-lang.org/docs",
    },
    {
        "category": "EVM Internals / Gas Optimization",
        "tip": "Audit your existing contracts with `forge inspect <Contract> storageLayout`. "
               "Practice slot packing, SLOAD/SSTORE minimization, and transient storage (EIP-1153). "
               "Gas optimization is tested hard in senior interviews.",
        "resource": "https://book.getfoundry.sh/reference/forge/forge-inspect",
    },
    {
        "category": "Uniswap V4 Hooks",
        "tip": "V4 hooks are the hottest EVM primitive right now. "
               "Build a custom hook (e.g., a TWAP oracle hook or dynamic fee hook). "
               "This demonstrates cutting-edge protocol knowledge in interviews.",
        "resource": "https://docs.uniswap.org/contracts/v4/overview",
    },
    {
        "category": "EigenLayer / AVS Development",
        "tip": "EigenLayer restaking and AVS (Actively Validated Services) are a growing hiring niche. "
               "Your liquidation bot and agent marketplace work at Nunchi maps directly to AVS design. "
               "Read the AVS developer guide and prototype a simple AVS.",
        "resource": "https://docs.eigenlayer.xyz/eigenlayer/avs-guides",
    },
    {
        "category": "Onchain AI Agents (ElizaOS / OLAS)",
        "tip": "You already shipped an AI-native CLI and ERC-8004 agent marketplace — document this. "
               "Contribute to ElizaOS or Olas Network open source to build public credibility. "
               "This is the hottest intersection in web3 right now and you have real experience.",
        "resource": "https://github.com/elizaos/eliza",
    },
    {
        "category": "L2 / Rollup Architecture",
        "tip": "OP Stack and Arbitrum Stylus are where most new protocol launches happen. "
               "Deploy a contract on a local OP Stack devnet. "
               "Understanding the L2 deposit/withdrawal bridge at the contract level will set you apart.",
        "resource": "https://docs.optimism.io/builders/chain-operators/tutorials/create-l2-rollup",
    },
    {
        "category": "LayerZero V2 / Cross-chain Messaging",
        "tip": "Your cross-chain swap SDK at Novastro is relevant — formalize it. "
               "Migrate it or build a demo on LayerZero V2 OApp standard. "
               "Cross-chain protocol engineers command a significant salary premium.",
        "resource": "https://docs.layerzero.network/v2",
    },
    {
        "category": "Yul / Assembly Optimization",
        "tip": "Writing inline Yul separates senior from staff engineers in interviews. "
               "Rewrite one critical path (e.g., a tight loop in your matching engine) in Yul. "
               "Use `forge test --debug` to trace execution and validate gas savings.",
        "resource": "https://docs.soliditylang.org/en/latest/yul.html",
    },
    {
        "category": "AI Tools in Developer Workflow",
        "tip": "You already authored Claude Code skills — expand this. "
               "Build an MCP server that wraps your Foundry test runner, Slither output, and "
               "contract deployment flow. This turns your workflow into a shareable artifact "
               "and demonstrates AI-native engineering leadership.",
        "resource": "https://docs.anthropic.com/en/docs/claude-code/mcp",
    },
]

# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def score_text(text: str) -> int:
    """Score text relevance for Bhargav's profile."""
    text_lower = text.lower()
    score = 0
    for kw in MUST_HAVE:
        if kw in text_lower:
            score += 3
    for kw in NICE_TO_HAVE:
        if kw in text_lower:
            score += 1
    return score


def fetch_url(url: str, timeout: int = 10) -> str:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (job-search-script/1.0)"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="ignore")
    except Exception as e:
        return ""


class JobParser(HTMLParser):
    """Minimal HTML parser to extract job title + link from web3.career."""

    def __init__(self):
        super().__init__()
        self.jobs = []
        self._in_job = False
        self._current_href = None
        self._current_text = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "a" and attrs_dict.get("href", "").startswith("/"):
            self._in_job = True
            self._current_href = "https://web3.career" + attrs_dict["href"]
            self._current_text = []

    def handle_data(self, data):
        if self._in_job:
            self._current_text.append(data.strip())

    def handle_endtag(self, tag):
        if tag == "a" and self._in_job:
            text = " ".join(t for t in self._current_text if t)
            if text and score_text(text) >= 3:
                self.jobs.append((text, self._current_href))
            self._in_job = False
            self._current_href = None
            self._current_text = []


def get_tip_of_the_day() -> dict:
    day_of_year = datetime.date.today().timetuple().tm_yday
    return DAILY_TIPS[day_of_year % len(DAILY_TIPS)]


# --------------------------------------------------------------------------
# Report generation
# --------------------------------------------------------------------------

def generate_report() -> str:
    tip = get_tip_of_the_day()

    lines = [
        f"# Web3 Job Search Report — {TODAY}",
        "",
        "> **Profile:** Bhargav Kacharla | Protocol Engineer | EVM Solidity · TypeScript · Rust/SVM",
        "",
        "---",
        "",
        "## Today's Skill Improvement Tip",
        "",
        f"**Category:** {tip['category']}",
        "",
        f"{tip['tip']}",
        "",
        f"**Resource:** {tip['resource']}",
        "",
        "---",
        "",
        "## Job Boards to Check Today",
        "",
        "Visit these filtered URLs — they show the freshest listings:",
        "",
    ]

    for name, url in JOB_BOARDS:
        lines.append(f"- [{name}]({url})")

    lines += [
        "",
        "---",
        "",
        "## Target Companies (Strong Profile Match)",
        "",
        "Apply directly via their careers pages. You have strong signal for ALL of these:",
        "",
    ]

    for company, reason in TARGET_COMPANIES.items():
        lines.append(f"### {company}")
        lines.append(f"*Why you fit:* {reason}")
        lines.append(f"*Action:* Search `{company} careers` or check their Discord/Twitter for openings.")
        lines.append("")

    lines += [
        "---",
        "",
        "## Quick Apply Strategy",
        "",
        "1. **Direct outreach > job boards** — DM protocol teams on Twitter/X or Telegram. "
           "Your current work at Nunchi (CLOB+AMM perpetuals, AI agent marketplace) is highly visible to this community.",
        "2. **Lead with audit experience** — Quantstamp + Zellic on your resume is rare. "
           "Mention it in every cover note.",
        "3. **Show the AI CLI** — Most DeFi teams are actively trying to add AI-native tooling. "
           "You've already shipped it; demo it.",
        "4. **GitHub activity** — Pin repos from Novastro/Nunchi work if open-source. "
           "Recruiters at DeFi protocols check GitHub before responding.",
        "5. **Community presence** — Post technical threads on Twitter about your perpetuals "
           "architecture or AI agent work. Inbound interest beats cold apply.",
        "",
        "---",
        "",
        "## Full Skill Improvement Roadmap",
        "",
        "Rotate through these weekly — one deep dive per area:",
        "",
    ]

    for i, t in enumerate(DAILY_TIPS):
        lines.append(f"### {i+1}. {t['category']}")
        lines.append(t["tip"])
        lines.append(f"Resource: {t['resource']}")
        lines.append("")

    lines += [
        "---",
        "",
        "## AI-First Company Landscape",
        "",
        "Companies going AI-first that need your unique combo of *blockchain + AI tooling*:",
        "",
        "| Company | What they need | Your fit |",
        "|---------|---------------|----------|",
        "| Olas Network | Onchain agent infrastructure, ERC standards | ERC-8004/8183 at Nunchi |",
        "| Brian Protocol | AI tx execution layer | AI CLI + Solidity |",
        "| Autonolas | Multi-agent coordination on EVM | Agent marketplace design |",
        "| Giza Tech | ML inference on Starknet | ZK + onchain agents adjacent |",
        "| Inference Labs | Verifiable AI on EVM | Strong EVM + AI tooling interest |",
        "| Ritual | Onchain AI compute network | Protocol engineering + AI |",
        "",
        "---",
        "",
        "*Generated by job_search.py — run daily for fresh tips.*",
        f"*Date: {TODAY}*",
    ]

    return "\n".join(lines)


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    os.makedirs(REPORT_DIR, exist_ok=True)
    report_path = os.path.join(REPORT_DIR, f"{TODAY}.md")

    print(f"Generating daily job search report for {TODAY}...")
    report = generate_report()

    with open(report_path, "w") as f:
        f.write(report)

    print(f"Report saved to: {report_path}")
    print()
    print("=" * 60)
    print(report[:2000])
    print("... (see full report in file)")
    print("=" * 60)


if __name__ == "__main__":
    main()
