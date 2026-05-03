#!/usr/bin/env python3
"""
Daily Web3 Job Hunt Report Generator
Profile: Bhargav Kacharla — Solidity/EVM Protocol Engineer

Run daily: python3 job_hunt.py
"""

import os
import sys
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime

# ---------------------------------------------------------------------------
# Candidate profile — drives keyword scoring and recommendations
# ---------------------------------------------------------------------------
PROFILE = {
    "name": "Bhargav Kacharla",
    "keywords_high": [
        "protocol engineer", "solidity", "smart contract", "evm", "defi",
        "perpetuals", "perps", "derivatives", "options trading", "AMM",
        "CLOB", "orderbook", "rwa", "real world asset", "account abstraction",
        "erc-4337", "erc4337", "ai agent", "on-chain agent", "autonomous agent",
        "yield", "liquidation", "clearing house", "risk engine", "oracle",
        "pyth", "chainlink", "uniswap", "foundry",
    ],
    "keywords_medium": [
        "typescript", "blockchain", "web3", "rust", "hardhat", "cross-chain",
        "bridge", "layer2", "l2", "staking", "liquidity", "anchor", "solana",
        "subgraph", "indexer", "security", "audit", "slither",
    ],
}

# ---------------------------------------------------------------------------
# RSS feeds from major web3 job boards
# ---------------------------------------------------------------------------
RSS_FEEDS = {
    "web3.career": "https://web3.career/rss.xml",
    "cryptojobslist": "https://cryptojobslist.com/rss.xml",
    "remote3.co": "https://www.remote3.co/feed/",
}

# ---------------------------------------------------------------------------
# Pre-filtered search URLs — open these daily in the browser
# ---------------------------------------------------------------------------
SEARCH_LINKS = [
    ("web3.career — Solidity jobs",         "https://web3.career/solidity-jobs"),
    ("web3.career — Remote jobs (new)",     "https://web3.career/remote-jobs"),
    ("web3.career — AI + Web3",             "https://web3.career/web3-jobs-remote+ai"),
    ("web3.career — Protocol Engineer",     "https://web3.career/protocol-engineer-jobs"),
    ("CryptoJobsList — Solidity",           "https://cryptojobslist.com/solidity"),
    ("CryptoJobsList — Smart Contract",     "https://cryptojobslist.com/smart-contract"),
    ("CryptoJobsList — Remote",             "https://cryptojobslist.com/remote"),
    ("crypto.jobs",                         "https://crypto.jobs"),
    ("remote3.co",                          "https://www.remote3.co/"),
    ("LaborX — Web3",                       "https://laborx.com/vacancies"),
    ("Glassdoor — Solidity Remote",
     "https://www.glassdoor.com/Job/solidity-Remote-SRCH_KO0,8_IL.9,15_IS11047.htm"),
]

# ---------------------------------------------------------------------------
# Target companies — curated for Bhargav's exact experience
# ---------------------------------------------------------------------------
TARGET_COMPANIES = [
    # (Name, Why it fits, Careers URL, tier)
    ("dYdX",
     "Perpetuals DEX — CLOB + clearing house is exactly what you built at Nunchi.",
     "https://dydx.exchange/careers", "TIER1"),
    ("Hyperliquid Labs",
     "On-chain perps on HyperEVM. Your CLOB+AMM matching engine work is a direct signal.",
     "https://jobs.ashbyhq.com/Hyperliquid%20Labs", "TIER1"),
    ("Synthetix",
     "Derivatives / perps protocol. Deep Solidity stack, risk engine, oracles.",
     "https://jobs.synthetix.io", "TIER1"),
    ("GMX",
     "Decentralised perpetuals. Your liquidation + risk engine experience maps directly.",
     "https://gmx.io", "TIER1"),
    ("Ondo Finance",
     "RWA tokenization — you shipped ERC-3643 with on-chain compliance at Novastro.",
     "https://ondo.finance/careers", "TIER1"),
    ("Securitize",
     "Digital securities / RWA. ERC-3643, identity registry, compliance — exact match.",
     "https://securitize.io/about/careers", "TIER1"),
    ("Uniswap Labs",
     "AMM/DEX protocol. Your Uniswap V3-style concentrated liquidity work at Oddz.",
     "https://boards.greenhouse.io/uniswaplabs", "TIER1"),
    ("Aave",
     "Lending protocol. You integrated Aave for yield generation at Novastro.",
     "https://aave.com/careers", "TIER1"),
    ("Morpho",
     "Modular lending markets. Hot DeFi protocol, heavy Solidity, security-focused.",
     "https://www.morpho.org/careers", "TIER1"),
    ("Pendle Finance",
     "Yield trading on yield-bearing assets — mirrors your Nunchi perpetuals on YBAs.",
     "https://pendle.finance/careers", "TIER1"),
    ("Stader Labs",
     "Liquid staking. You integrated Stader at Novastro — they know the use case.",
     "https://staderlabs.com/careers", "TIER2"),
    ("EigenLayer / EigenLabs",
     "Restaking infrastructure, protocol engineering, very high comp.",
     "https://www.eigenlabs.org/careers", "TIER2"),
    ("Biconomy",
     "Account abstraction / gasless tx. You shipped gasless at Oddz + ERC-4337 at Xalts.",
     "https://biconomy.io/careers", "TIER2"),
    ("Particle Network",
     "Chain abstraction / account abstraction protocol.",
     "https://particle.network/careers", "TIER2"),
    ("Chainlink Labs",
     "Oracle infrastructure. You used Chainlink Keepers heavily at Oddz.",
     "https://chainlinklabs.com/careers", "TIER2"),
    ("Offchain Labs (Arbitrum)",
     "L2 protocol engineering — good fit if you move toward ZK/L2 infrastructure.",
     "https://offchainlabs.com/careers", "TIER2"),
    ("zkSync / Matter Labs",
     "ZK-EVM L2. If you upskill in ZK (recommended), this becomes Tier 1.",
     "https://matter-labs.io/careers", "TIER2"),
    ("Quantstamp",
     "You worked with them on audits at Nunchi — they hire experienced protocol engineers.",
     "https://quantstamp.com/careers", "TIER2"),
    ("Trail of Bits",
     "You used their tooling at Nunchi. Security-focused, high calibre team.",
     "https://www.trailofbits.com/careers", "TIER2"),
]

# ---------------------------------------------------------------------------
# Upskilling recommendations — cycled daily by weekday
# ---------------------------------------------------------------------------
UPSKILL_RECS = [
    {
        "skill": "ZK Proofs / ZK-EVM",
        "priority": "HIGH",
        "why": (
            "ZK is the #1 technical trend in EVM infra in 2026. zkSync, Starknet, Scroll, "
            "Polygon zkEVM are dominant L2s. Engineers who write ZK circuits command a 30-40% "
            "salary premium. This is your biggest gap."
        ),
        "action": (
            "Start with circom + snarkjs for circuit basics. Then study Halo2. "
            "Build a simple ZK proof for a DeFi primitive (e.g. prove a position is solvent "
            "without revealing collateral). Contribute to a ZK Hack challenge."
        ),
        "resources": [
            "https://zkiap.com (ZK Intensive Application Program)",
            "https://zkhack.dev (ZKHack puzzles)",
            "https://github.com/iden3/circom",
            "https://github.com/niclas-heun/Halo2-book",
        ],
        "time": "3-6 months to intermediate",
    },
    {
        "skill": "AI Agent Integration (on-chain)",
        "priority": "HIGH",
        "why": (
            "You already have a production edge here — ERC-8004/8183 agent marketplace + AI-native CLI "
            "at Nunchi. Engineers who can design on-chain agent incentive systems are extremely rare. "
            "Deepen and publicise this. AI-native protocols pay 20-30% premium."
        ),
        "action": (
            "Write a public blog post or GitHub repo showing your ERC-8004/8183 pattern. "
            "Extend your AI CLI to support MCP tool use (Anthropic's Model Context Protocol). "
            "Build an agent that autonomously manages a DeFi position end-to-end."
        ),
        "resources": [
            "https://docs.anthropic.com/claude/docs/tool-use",
            "https://modelcontextprotocol.io",
            "https://python.langchain.com/docs/modules/agents/",
        ],
        "time": "1-2 months — you already have the foundation",
    },
    {
        "skill": "EIP-7702 (EOA Delegation / Next-Gen AA)",
        "priority": "HIGH",
        "why": (
            "EIP-7702 shipped and is rapidly supplementing ERC-4337 for many account abstraction "
            "use cases. You have deep ERC-4337 experience (Xalts + Oddz gasless). "
            "Updating to EIP-7702 keeps your AA story current and relevant."
        ),
        "action": (
            "Read the EIP carefully. Build a demo: delegate an EOA to a smart contract, "
            "execute a batched transaction. Understand how EIP-7702 interacts with ERC-4337 "
            "bundlers and agent delegation patterns."
        ),
        "resources": [
            "https://eips.ethereum.org/EIPS/eip-7702",
            "https://github.com/ethereum/EIPs/blob/master/EIPS/eip-7702.md",
            "https://docs.alchemy.com/docs/eip-7702",
        ],
        "time": "2-4 weeks",
    },
    {
        "skill": "HyperEVM / Hyperliquid Ecosystem",
        "priority": "MEDIUM",
        "why": (
            "Hyperliquid is the dominant on-chain perps platform by volume in 2026. "
            "You build perps — knowing HyperEVM specifics (HyperCore precompiles, native order book "
            "interaction) makes you an obvious hire for them or any protocol building on HL."
        ),
        "action": (
            "Deploy contracts on HyperEVM testnet. Read HyperCore docs — understand how "
            "precompiles expose the native order book to Solidity. Build a simple integration "
            "that routes orders through HyperCore from a Solidity contract."
        ),
        "resources": [
            "https://hyperliquid.gitbook.io/hyperliquid-docs/",
            "https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/hyperevm",
        ],
        "time": "2-4 weeks",
    },
    {
        "skill": "Rust for EVM Infrastructure (revm / reth)",
        "priority": "MEDIUM",
        "why": (
            "Revm and Reth are the new EVM implementation layer written in Rust. "
            "You have Rust experience from Solana/Anchor. Applying it to EVM infra opens "
            "roles at L2 teams and tooling companies that pay significantly more."
        ),
        "action": (
            "Build a custom EVM inspector using revm — e.g. a gas profiler or storage diff tracer. "
            "Read the Reth book. Contribute a small PR to Reth. "
            "This bridges your Rust and EVM knowledge in a very marketable way."
        ),
        "resources": [
            "https://github.com/bluealloy/revm",
            "https://github.com/paradigmxyz/reth",
            "https://reth.rs/docs/",
        ],
        "time": "2-3 months (leverages existing Rust experience)",
    },
    {
        "skill": "Open-Source Presence & Technical Writing",
        "priority": "MEDIUM",
        "why": (
            "Protocol engineers at top DeFi firms are hired based on what they've shipped publicly. "
            "Your work at Nunchi (AI-native CLI, on-chain agent marketplace, audit-hardened contracts) "
            "is genuinely impressive — but if none of it is public, you can't leverage it in applications."
        ),
        "action": (
            "Pick one thing you've built and open-source it (a Foundry test template, "
            "a Solidity pattern for on-chain agent registration, your Claude Code skills for Slither). "
            "Write one technical post per week on Mirror, Substack, or your website. "
            "Tweet about what you're building — protocol engineers at top teams do this."
        ),
        "resources": [
            "https://mirror.xyz",
            "https://www.paradigm.xyz/writing (examples of what top protocol writing looks like)",
        ],
        "time": "Ongoing — start today",
    },
    {
        "skill": "Smart Contract Security / Competitive Auditing",
        "priority": "HIGH",
        "why": (
            "You have real audit experience (Quantstamp, Zellic, Slither, ToB tooling). "
            "Participating in competitive audit platforms (Code4rena, Sherlock, Cantina) "
            "builds public reputation AND pays. Top auditors earn $200k-$400k+. "
            "It also makes you a better protocol engineer."
        ),
        "action": (
            "Register on Code4rena and Sherlock. Join an audit contest this week. "
            "Even finding one medium-severity issue gets you on the leaderboard. "
            "Put your Code4rena/Sherlock profile in your resume and GitHub."
        ),
        "resources": [
            "https://code4rena.com",
            "https://www.sherlock.xyz",
            "https://cantina.xyz",
            "https://cyfrin.io/codehawks",
        ],
        "time": "Start immediately — ongoing",
    },
]


def fetch_rss(url: str, timeout: int = 10) -> list[dict]:
    """Fetch RSS feed and return list of job dicts."""
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "Mozilla/5.0 JobHuntBot/1.0"}
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            content = resp.read()
        root = ET.fromstring(content)
        items = []
        for item in root.findall(".//item"):
            def txt(tag):
                el = item.find(tag)
                return (el.text or "").strip() if el is not None else ""
            items.append({
                "title": txt("title"),
                "link": txt("link"),
                "description": txt("description"),
                "pubDate": txt("pubDate"),
            })
        return items
    except Exception:
        return []


def score_job(job: dict) -> tuple[int, list[str], list[str]]:
    text = (job.get("title", "") + " " + job.get("description", "")).lower()
    high_matched, medium_matched = [], []
    for kw in PROFILE["keywords_high"]:
        if kw.lower() in text:
            high_matched.append(kw)
    for kw in PROFILE["keywords_medium"]:
        if kw.lower() in text:
            medium_matched.append(kw)
    score = len(high_matched) * 3 + len(medium_matched)
    return score, high_matched, medium_matched


def stars(score: int) -> str:
    return "🔥" * min(score // 3 + (1 if score % 3 else 0), 5)


def generate_report(jobs_by_board: dict, date_str: str) -> str:
    weekday = datetime.now().weekday()  # 0=Mon … 6=Sun

    # Score and rank all fetched jobs
    all_jobs = []
    for board, jobs in jobs_by_board.items():
        for j in jobs:
            score, hi, med = score_job(j)
            if score > 0:
                all_jobs.append({**j, "score": score, "board": board,
                                  "hi": hi, "med": med})
    all_jobs.sort(key=lambda x: x["score"], reverse=True)

    lines = []

    lines += [
        f"# Daily Web3 Job Hunt Report — {date_str}",
        f"**Candidate:** {PROFILE['name']} | Solidity/EVM Protocol Engineer",
        "",
        "---",
        "",
    ]

    # ── Job Listings ──────────────────────────────────────────────────────────
    lines += ["## Job Listings Fetched Today", ""]
    if all_jobs:
        for i, j in enumerate(all_jobs[:25], 1):
            hi_preview = ", ".join(j["hi"][:5])
            lines += [
                f"### {i}. {j['title']}",
                f"**Board:** {j['board']}  ",
                f"**Match:** {stars(j['score'])} ({j['score']} pts)  ",
                f"**Skills hit:** {hi_preview}  ",
                f"**Apply:** {j['link']}",
                "",
            ]
    else:
        lines += [
            "_RSS feeds returned no results today (rate-limited or network issue)._",
            "_Use the direct search links below instead._",
            "",
        ]

    # ── Search Links ──────────────────────────────────────────────────────────
    lines += [
        "---",
        "",
        "## Job Boards — Open These Daily",
        "",
        "| Board | Link |",
        "|-------|------|",
    ]
    for name, url in SEARCH_LINKS:
        lines.append(f"| {name} | [Search]({url}) |")
    lines += [""]

    # ── Target Companies ──────────────────────────────────────────────────────
    tier1 = [c for c in TARGET_COMPANIES if c[3] == "TIER1"]
    tier2 = [c for c in TARGET_COMPANIES if c[3] == "TIER2"]

    lines += [
        "---",
        "",
        "## Target Companies",
        "",
        "### Tier 1 — Direct Experience Match",
        "",
    ]
    for name, reason, url, _ in tier1:
        lines += [f"**[{name}]({url})**  ", f"_{reason}_", ""]

    lines += ["### Tier 2 — Strong Fit", ""]
    for name, reason, url, _ in tier2:
        lines += [f"**[{name}]({url})**  ", f"_{reason}_", ""]

    # ── Daily Upskill Rec ─────────────────────────────────────────────────────
    rec = UPSKILL_RECS[weekday % len(UPSKILL_RECS)]
    lines += [
        "---",
        "",
        "## Today's Upskill Focus",
        "",
        f"### {rec['skill']}  _{rec['priority']} priority_",
        "",
        f"**Why:** {rec['why']}",
        "",
        f"**Action today:** {rec['action']}",
        "",
        f"**Time to competency:** {rec['time']}",
        "",
        "**Resources:**",
    ]
    for r in rec["resources"]:
        lines.append(f"- {r}")
    lines += [""]

    # ── Full skill matrix ─────────────────────────────────────────────────────
    lines += [
        "---",
        "",
        "## Skills vs Market Demand (May 2026)",
        "",
        "| Skill | Your Level | Market Demand | Status |",
        "|-------|-----------|---------------|--------|",
        "| Solidity / EVM | Expert (5+ yr) | Very High | ✅ STRONG |",
        "| Perpetuals / CLOB+AMM | Expert (Nunchi) | Very High | ✅ STRONG |",
        "| AI Agents on-chain | Advanced (ERC-8004/8183) | Very High | ✅ AHEAD OF CURVE |",
        "| RWA Tokenization | Advanced (ERC-3643, Novastro) | High | ✅ STRONG |",
        "| Account Abstraction ERC-4337 | Advanced (Xalts) | High | ✅ STRONG |",
        "| EIP-7702 (new AA standard) | Unknown | High | ⚠️ UPSKILL |",
        "| Security (Slither, ToB, audits) | Intermediate | Very High | 🟡 GOOD |",
        "| TypeScript / Node.js | Advanced | High | ✅ STRONG |",
        "| Rust / Solana SVM | Intermediate | High | 🟡 GOOD |",
        "| ZK Proofs / ZK-EVM | Beginner | Very High | ⚠️ UPSKILL |",
        "| HyperEVM specifics | Unknown | High (niche) | ⚠️ UPSKILL |",
        "| Competitive auditing (C4/Sherlock) | None public | High | ⚠️ START |",
        "| Open-source / public profile | Limited | High | ⚠️ INVEST |",
        "| Move / Aptos | Intermediate | Medium | 🟡 MAINTAIN |",
        "",
    ]

    # ── AI-first checklist ────────────────────────────────────────────────────
    lines += [
        "---",
        "",
        "## AI-First Company Checklist",
        "",
        "When applying to AI-first web3 protocols, make sure you can speak concretely to these:",
        "",
        "- [x] On-chain agent registration & incentive patterns (ERC-8004/8183 — you shipped this)",
        "- [x] Autonomous transaction execution (liquidation bots, TP/SL — Nunchi production)",
        "- [x] AI-assisted developer workflow (Claude Code skills — you authored them)",
        "- [x] AI-native CLI for autonomous agents (shipped at Nunchi)",
        "- [ ] MCP (Model Context Protocol) tool use for agents — extend your CLI",
        "- [ ] On-chain verifiable AI inference (ZKML) — research stage for most",
        "- [ ] Prompt engineering for smart contract generation / fuzz testing",
        "",
    ]

    # ── Daily checklist ───────────────────────────────────────────────────────
    lines += [
        "---",
        "",
        "## Today's Application Checklist",
        "",
        "- [ ] Scan job boards above for new postings (< 15 min)",
        "- [ ] Check 2 Tier 1 target companies' careers pages directly",
        "- [ ] Send 1-2 tailored applications (quality beats volume)",
        "- [ ] 30–60 min on today's upskill focus",
        f"- [ ] Write or post one technical insight online (rotate: Twitter/X, LinkedIn, Mirror)",
        "",
        "---",
        f"_Generated by job_hunt.py — {date_str}_",
    ]

    return "\n".join(lines)


def main():
    date_str = datetime.now().strftime("%Y-%m-%d")
    reports_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reports")
    os.makedirs(reports_dir, exist_ok=True)

    print(f"[{date_str}] Fetching job listings...")
    jobs_by_board: dict[str, list] = {}
    for board, url in RSS_FEEDS.items():
        print(f"  {board}: ", end="", flush=True)
        jobs = fetch_rss(url)
        jobs_by_board[board] = jobs
        print(f"{len(jobs)} jobs")

    print("Generating report...")
    report = generate_report(jobs_by_board, date_str)

    report_path = os.path.join(reports_dir, f"{date_str}.md")
    with open(report_path, "w") as f:
        f.write(report)

    total = sum(len(v) for v in jobs_by_board.values())
    print(f"\nDone. {total} jobs fetched. Report: {report_path}\n")
    print("Run daily with:  python3 job_hunt.py")
    return report_path


if __name__ == "__main__":
    main()
