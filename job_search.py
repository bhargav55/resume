#!/usr/bin/env python3
"""
Daily Web3 Job Search Tool for Bhargav Kacharla
Run: python3 job_search.py
Requires: pip install requests beautifulsoup4
"""

import urllib.request
import urllib.parse
import json
import datetime
import re
import sys
from xml.etree import ElementTree as ET


TODAY = datetime.date.today().isoformat()

PROFILE_KEYWORDS = [
    "solidity", "smart contract", "defi", "perpetual", "clob", "liquidation",
    "evm", "account abstraction", "erc-4337", "rwa", "ai agent", "on-chain agent"
]

# Curated target companies with direct career page URLs
TARGET_COMPANIES = [
    {"name": "Uniswap Labs",       "careers": "https://careers.uniswap.org/",                            "note": "Your V3-style AMM + CLOB experience is a direct match"},
    {"name": "Hyperliquid Labs",   "careers": "https://jobs.ashbyhq.com/Hyperliquid%20Labs",              "note": "You built a CLOB perp engine — this IS their product"},
    {"name": "Eigen Labs",         "careers": "https://jobs.ashbyhq.com/eigen-labs",                      "note": "ERC-4337 + security = restaking infra fit"},
    {"name": "Risk Labs / Across", "careers": "https://jobs.ashbyhq.com/risklabs",                        "note": "Intent-based cross-chain — AA + cross-chain background"},
    {"name": "LI.FI",             "careers": "https://jobs.ashbyhq.com/li.fi",                            "note": "Multi-chain EVM bridge/aggregator"},
    {"name": "Ethereum Foundation","careers": "https://ethereum.org/en/community/grants/",                "note": "Account abstraction & interop team"},
    {"name": "dYdX",              "careers": "https://dydx.exchange/careers",                             "note": "Leading perpetual DEX, 64+ roles"},
    {"name": "Coinbase",          "careers": "https://www.coinbase.com/careers/positions",                "note": "AgentKit + AI applications — your AI×chain angle"},
    {"name": "CertiK",            "careers": "https://jobs.lever.co/certik",                              "note": "Your Quantstamp/Zellic audit experience is direct cred"},
    {"name": "Ellipsis Labs",     "careers": "https://jobs.ashbyhq.com/ellipsislabs",                    "note": "Phoenix Perpetuals on Solana — perp + Anchor"},
    {"name": "Drift Protocol",    "careers": "https://jobs.solana.com/companies/drift-protocol",          "note": "Solana perp DEX, Anchor smart contracts"},
    {"name": "Monad Foundation",  "careers": "https://jobs.ashbyhq.com/monad.foundation",                "note": "New EVM L1, senior full stack web3"},
    {"name": "Chainlink Labs",    "careers": "https://chainlink.com/careers",                             "note": "You used Keepers + Gelato at Oddz, they know the domain"},
    {"name": "Aevo",              "careers": "https://aevo.xyz/",                                         "note": "Options + perps on OP Stack — your options background"},
]

# Job board RSS/API feeds (boards that allow programmatic access)
JOB_BOARD_SEARCHES = [
    {
        "name": "web3.career — DeFi + Solidity",
        "url": "https://web3.career/defi+solidity-jobs",
        "type": "manual"
    },
    {
        "name": "CryptoJobsList — Solidity",
        "url": "https://cryptojobslist.com/solidity",
        "type": "manual"
    },
    {
        "name": "crypto.jobs — Smart Contract",
        "url": "https://crypto.jobs/",
        "type": "manual"
    },
    {
        "name": "remote3.co — Remote Web3",
        "url": "https://www.remote3.co/",
        "type": "manual"
    },
    {
        "name": "web3vacancy.com",
        "url": "https://web3vacancy.com/",
        "type": "manual"
    },
]

# Twitter/X searches (manual — open these in browser)
TWITTER_SEARCHES = [
    "https://x.com/search?q=%22smart+contract+engineer%22+%22hiring%22&src=typed_query&f=live",
    "https://x.com/search?q=%22solidity%22+%22we+are+hiring%22+%22defi%22&src=typed_query&f=live",
    "https://x.com/search?q=%22web3%22+%22hiring%22+%22solidity%22&src=typed_query&f=live",
]

SEPARATOR = "=" * 70


def print_header():
    print(SEPARATOR)
    print(f"  BHARGAV'S WEB3 JOB SEARCH — {TODAY}")
    print(SEPARATOR)


def print_section(title: str):
    print(f"\n{'─' * 70}")
    print(f"  {title}")
    print(f"{'─' * 70}")


def print_companies():
    print_section("TARGET COMPANIES — Check These Career Pages Today")
    for i, company in enumerate(TARGET_COMPANIES, 1):
        print(f"\n  [{i:02d}] {company['name']}")
        print(f"       → {company['careers']}")
        print(f"       ★  {company['note']}")


def print_job_boards():
    print_section("JOB BOARDS — Open These in Browser")
    for board in JOB_BOARD_SEARCHES:
        print(f"\n  {board['name']}")
        print(f"  → {board['url']}")


def print_twitter():
    print_section("X/TWITTER — Live Hiring Posts (open in browser)")
    for url in TWITTER_SEARCHES:
        print(f"  → {url}")
    print()
    accounts_to_follow = [
        "@HyperliquidX", "@UniswapLabs", "@EigenLayer", "@Chainlink",
        "@dydxprotocol", "@CoinbaseCloud", "@paradigm", "@a16zcrypto",
        "@DriftProtocol", "@AevoXYZ", "@LiFi_Project"
    ]
    print("  Follow for job announcements:")
    print("  " + "  ".join(accounts_to_follow))


def print_skills_reminder():
    print_section("TODAY'S UPSKILL FOCUS (rotate daily)")
    schedule = {
        0: ("Monday",    "ZK Proofs",          "30 min Circom tutorial → https://rareskills.io/post/circom-intro"),
        1: ("Tuesday",   "EIP-7702",            "30 min → build a session key delegation contract"),
        2: ("Wednesday", "Intent Protocols",    "30 min → read ERC-7683 spec, understand solver mechanics"),
        3: ("Thursday",  "Formal Verification", "30 min → Certora/Halmos docs → https://docs.certora.com"),
        4: ("Friday",    "AI Agent Evals",      "30 min → LangSmith evals, add eval harness to agent project"),
        5: ("Saturday",  "ZK Portfolio",        "Build time — implement a ZK circuit for a DeFi primitive"),
        6: ("Sunday",    "Review + Apply",      "Apply to 3 new positions, update resume metrics"),
    }
    weekday = datetime.date.today().weekday()
    day_name, focus, action = schedule[weekday]
    print(f"\n  Today ({day_name}) → {focus}")
    print(f"  Action: {action}")

    print("\n  Full weekly rotation:")
    for day_num, (day, topic, _) in schedule.items():
        marker = "◀ TODAY" if day_num == weekday else ""
        print(f"    {day:10s} — {topic} {marker}")


def print_application_checklist():
    print_section("APPLICATION CHECKLIST — Before You Hit Send")
    checklist = [
        "Tailor your headline to the company (CLOB for Hyperliquid, AA for Eigen, etc.)",
        "Add TVL/volume numbers if available in your bullet points",
        "Move AI projects section above Skills in resume for AI-first companies",
        "Mention specific ERC standards that match their stack",
        "Include GitHub link to AI auditor project prominently",
        "Write a 2-sentence cover note: what you've shipped + why their specific protocol",
        "Connect on X/Twitter before applying — many web3 hires come through DMs",
    ]
    for item in checklist:
        print(f"  ☐ {item}")


def print_market_snapshot():
    print_section("MARKET SNAPSHOT — June 2026")
    stats = [
        ("Active web3 job listings",          "74,000+ (web3.career)"),
        ("AI mentions in web3 job posts",      "53.1% (up from 23% in early 2025)"),
        ("AI fluency salary premium",          "+20–30% over non-AI peers"),
        ("Senior Solidity engineer base",      "$180K–$325K + tokens"),
        ("Solidity in blockchain job postings","~40% of all postings"),
        ("Remote opportunities",               ">60% of blockchain roles"),
    ]
    for metric, value in stats:
        print(f"  {metric:<45} {value}")


def main():
    print_header()
    print_market_snapshot()
    print_companies()
    print_job_boards()
    print_twitter()
    print_skills_reminder()
    print_application_checklist()

    print(f"\n{SEPARATOR}")
    print("  Full job search guide → JOB_SEARCH.md")
    print(f"{SEPARATOR}\n")


if __name__ == "__main__":
    main()
