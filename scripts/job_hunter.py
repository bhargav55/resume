#!/usr/bin/env python3
"""
Daily Web3 Job Hunter for Bhargav Kacharla
Skills: Solidity/EVM, TypeScript, AI agents, ERC-4337, DeFi/perpetuals, RWA, Rust/Anchor
Uses only stdlib + requests — no feedparser dependency.
"""

import os
import sys
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime

try:
    import requests
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "-q"])
    import requests

# ─── Profile keywords ────────────────────────────────────────────────────────

MATCH_KEYWORDS = [
    "solidity", "smart contract", "evm", "defi", "blockchain engineer",
    "protocol engineer", "web3 engineer", "account abstraction", "erc-4337",
    "perpetual", "perp dex", "clob", "rwa", "tokenization", "on-chain",
    "rust", "anchor", "ai agent", "autonomous agent", "llm", "langchain",
    "foundry", "hardhat", "security audit", "liquidation", "dex",
    "typescript", "node.js", "layer 2", "l2", "zk", "zero knowledge",
]

WEAK_ONLY_KEYWORDS = [
    "frontend", "marketing", "designer", "graphic", "community manager",
    "sales", "legal", "recruiter", "data analyst",
]

TARGET_COMPANIES = [
    "hyperliquid", "dydx", "gmx", "drift", "vertex", "synthetix",
    "aave", "compound", "uniswap", "chainlink", "alchemy", "biconomy",
    "pimlico", "safe", "zerodev", "mantra", "ondo", "centrifuge",
    "maple", "goldfinch", "superfluid", "paraswap", "1inch",
    "starkware", "polygon", "arbitrum", "optimism", "base", "scroll",
    "circle", "bitgo", "anchorage", "fireblocks", "gauntlet", "chaos labs",
    "quantstamp", "openzeppelin", "cyfrin", "trail of bits", "sherlock",
    "immunefi", "code4rena",
]

# ─── Job board RSS sources ────────────────────────────────────────────────────

JOB_SOURCES = [
    {
        "name": "Web3.Career – Solidity Remote",
        "rss": "https://web3.career/remote+solidity-jobs.rss",
        "url": "https://web3.career/remote+solidity-jobs",
    },
    {
        "name": "Web3.Career – DeFi Solidity",
        "rss": "https://web3.career/defi+solidity-jobs.rss",
        "url": "https://web3.career/defi+solidity-jobs",
    },
    {
        "name": "Web3.Career – Smart Contract",
        "rss": "https://web3.career/smart-contract-jobs.rss",
        "url": "https://web3.career/smart-contract-jobs",
    },
    {
        "name": "CryptoJobsList – Solidity",
        "rss": "https://cryptojobslist.com/solidity.rss",
        "url": "https://cryptojobslist.com/solidity",
    },
    {
        "name": "CryptoJobsList – DeFi",
        "rss": "https://cryptojobslist.com/defi.rss",
        "url": "https://cryptojobslist.com/defi",
    },
    {
        "name": "CryptoJobsList – Remote",
        "rss": "https://cryptojobslist.com/remote.rss",
        "url": "https://cryptojobslist.com/remote",
    },
    {
        "name": "CryptoCurrencyJobs – Smart Contracts",
        "rss": "https://cryptocurrencyjobs.co/smart-contracts/feed/",
        "url": "https://cryptocurrencyjobs.co/smart-contracts/",
    },
    {
        "name": "CryptoCurrencyJobs – DeFi",
        "rss": "https://cryptocurrencyjobs.co/defi/feed/",
        "url": "https://cryptocurrencyjobs.co/defi/",
    },
    # Remotive — open RSS, good blockchain/remote coverage
    {
        "name": "Remotive – Blockchain/Software",
        "rss": "https://remotive.com/remote-jobs/rss/software-dev",
        "url": "https://remotive.com/remote-jobs/software-dev?search=blockchain",
    },
    # WorkInWeb3 — Atom feed
    {
        "name": "WorkInWeb3",
        "rss": "https://workinweb3.com/feed.xml",
        "url": "https://workinweb3.com/jobs",
    },
]

# ─── Daily skill rotation (7 days, Mon–Sun) ───────────────────────────────────

SKILL_TIPS = [
    {
        "title": "ZK Proofs — Your biggest gap & highest-value upskill",
        "why": "ZK engineer salaries hit $250k–$350k. Starknet (Cairo) and Aztec (Noir) are scarce-talent markets. Your EVM + security background transfers directly.",
        "action": [
            "**Start**: [Noir by Example](https://noir-lang.org/docs) — Aztec's Rust-like ZK DSL, easiest ramp for Rust devs",
            "**Then**: [Cairo Book](https://book.cairo-lang.org/) for Starknet contracts",
            "**Project**: Port your AI smart-contract auditor to flag ZK circuit bugs",
            "**Target roles**: ZK Protocol Engineer @ Aztec, StarkWare, Scroll, Linea",
        ],
    },
    {
        "title": "EIP-7702 — Next-gen Account Abstraction (your ERC-4337 is the launchpad)",
        "why": "EIP-7702 ships EOA delegation without a full smart wallet. Infra companies built on 4337 are migrating now. Your Xalts + Skandha bundler experience is rare context.",
        "action": [
            "**Read**: EIP-7702 spec + Viem's `wallet_sendCalls` implementation",
            "**Build**: A 7702 delegation example that wraps your existing 4337 paymaster",
            "**Publish**: '4337 vs 7702 trade-offs' — a short article gets you noticed",
            "**Target**: Alchemy, Pimlico, Safe, ZeroDev, Biconomy — all actively hiring",
        ],
    },
    {
        "title": "Formal Verification — The next tier above Slither + Trail of Bits",
        "why": "Your Quantstamp + Zellic audit experience is gold. Certora is asked for in senior auditor JDs — it separates you from 90% of Solidity devs.",
        "action": [
            "**Tool**: [Certora Prover](https://docs.certora.com) — write CVL specs for your CLOB engine",
            "**Tool**: Foundry invariant testing + symbolic execution with Halmos or Medusa",
            "**Project**: Add Certora proofs to your liquidation contracts at Nunchi",
            "**Target**: Gauntlet, Chaos Labs, Trail of Bits, OpenZeppelin, Cyfrin",
        ],
    },
    {
        "title": "Cross-chain Protocols — CCIP, LayerZero, Wormhole",
        "why": "Perpetual DEXs and RWA protocols are going multi-chain. Your Polygon + Avalanche + BNB mainnet experience needs a cross-chain bridge layer.",
        "action": [
            "**Start**: [Chainlink CCIP Docs](https://docs.chain.link/ccip) — build a cross-chain token transfer",
            "**Then**: LayerZero OFT (Omnichain Fungible Token) standard",
            "**Project**: Make your Novastro prediction market cross-chain with CCIP",
            "**Target**: Chainlink Labs, LayerZero Labs, Wormhole, deBridge — all hiring",
        ],
    },
    {
        "title": "Verifiable AI Agents — Deepen what you already have",
        "why": "53% of web3 JDs mention AI in 2026. You're ahead with LangChain/LangGraph + MCP. The frontier is: on-chain verifiability of agent actions via TEEs.",
        "action": [
            "**Study**: TEE-based agent execution — TLSNotary, Phala Network, Marlin",
            "**Study**: Agent wallets + ERC-4337 session keys for self-funding agents",
            "**Build**: Add TEE attestation to your AI liquidation CLI at Nunchi",
            "**Target**: Lit Protocol, Phala, Privy, Dynamic.xyz, Coinbase Developer Platform",
        ],
    },
    {
        "title": "MEV + Gas Optimization — The sharp edge for perp DEX senior roles",
        "why": "Your CLOB matching engine at Nunchi is the exact domain. MEV knowledge + gas optimization is what separates mid-level from staff-level at perp DEXs.",
        "action": [
            "**Read**: Flashbots research blog + MEV-Share docs",
            "**Tool**: Foundry gas snapshots + `forge snapshot` diffs",
            "**Deep dive**: EVM assembly JUMPDEST optimization in your matching engine hot path",
            "**Target**: Hyperliquid, dYdX, GMX, Vertex, Drift — senior protocol roles",
        ],
    },
    {
        "title": "Move Language — Turn a resume line into a real portfolio piece",
        "why": "Move is already on your resume. Sui TVL grew 4x in 2025. One deployed project makes this a real differentiated skill vs. 'familiar with Move'.",
        "action": [
            "**Read**: [Sui Move docs](https://docs.sui.io/build/move) — object-centric ownership model",
            "**Port**: Your staking contract from Solidity to Move as a portfolio piece",
            "**Target**: Sui Foundation, Mysten Labs, Cetus Protocol, Turbos Finance",
        ],
    },
]

# ─── Greenhouse / Lever company career APIs (open, no auth) ──────────────────
# These APIs are designed for public job board embeds — no Cloudflare blocking.

GREENHOUSE_COMPANIES = [
    # Perpetuals / DeFi
    ("dYdX", "dydx"),
    ("Synthetix", "synthetix"),
    ("Paraswap", "paraswap"),
    # Account Abstraction infra
    ("Alchemy", "alchemyplatform"),
    ("Safe", "safe"),
    # RWA / tokenization
    ("Circle", "circle"),
    ("Centrifuge", "centrifuge"),
    # Infrastructure / oracles
    ("Chainlink Labs", "chainlink"),
    ("LayerZero Labs", "layerzero"),
    ("Wormhole", "wormhole"),
    # Security
    ("OpenZeppelin", "openzeppelin"),
    ("Trail of Bits", "trailofbits"),
    # General crypto
    ("Coinbase", "coinbase"),
    ("Anchorage Digital", "anchoragedigital"),
    ("BitGo", "bitgo"),
]

LEVER_COMPANIES = [
    # Perpetuals / DeFi
    ("GMX", "gmx"),
    ("Drift Protocol", "drift-protocol"),
    ("Aave", "aave"),
    ("Compound", "compound-labs"),
    ("Uniswap", "uniswap"),
    # Account Abstraction
    ("Biconomy", "biconomy"),
    ("Privy", "privy"),
    # RWA
    ("Ondo Finance", "ondo-finance"),
    ("Maple Finance", "maple-finance"),
    # AI + Web3
    ("Lit Protocol", "lit-protocol"),
    ("Dynamic", "dynamic"),
    # Security
    ("Cyfrin", "cyfrin"),
    ("Quantstamp", "quantstamp"),
    # Infrastructure
    ("Polygon Labs", "polygon-labs"),
    ("Arbitrum Foundation", "offchainlabs"),
    ("Optimism", "optimism-pbc"),
]


def fetch_greenhouse(company_name: str, slug: str) -> list[dict]:
    url = f"https://boards-api.greenhouse.io/v1/boards/{slug}/jobs"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=12)
        resp.raise_for_status()
        data = resp.json()
        jobs = []
        for job in data.get("jobs", []):
            title = job.get("title", "")
            link = job.get("absolute_url", "")
            location = job.get("location", {}).get("name", "")
            score = score_job(title, location, company_name)
            if score >= 10:
                jobs.append({
                    "title": title,
                    "company": company_name,
                    "link": link,
                    "score": score,
                    "source": f"Greenhouse ({company_name})",
                    "published": "recent",
                })
        return jobs
    except Exception:
        return []


def fetch_lever(company_name: str, slug: str) -> list[dict]:
    url = f"https://api.lever.co/v0/postings/{slug}?mode=json"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=12)
        resp.raise_for_status()
        postings = resp.json()
        jobs = []
        for post in postings:
            title = post.get("text", "")
            link = post.get("hostedUrl", "")
            description = post.get("descriptionPlain", "")
            score = score_job(title, description, company_name)
            if score >= 10:
                jobs.append({
                    "title": title,
                    "company": company_name,
                    "link": link,
                    "score": score,
                    "source": f"Lever ({company_name})",
                    "published": "recent",
                })
        return jobs
    except Exception:
        return []


def fetch_all_company_jobs() -> tuple[list[dict], list[dict]]:
    """Fetch from Greenhouse + Lever APIs in parallel-ish."""
    all_jobs: list[dict] = []
    status: list[dict] = []

    print("  Fetching Greenhouse company boards...")
    for name, slug in GREENHOUSE_COMPANIES:
        jobs = fetch_greenhouse(name, slug)
        all_jobs.extend(jobs)
        if jobs:
            status.append({"name": f"Greenhouse/{name}", "ok": True, "count": len(jobs)})

    print("  Fetching Lever company boards...")
    for name, slug in LEVER_COMPANIES:
        jobs = fetch_lever(name, slug)
        all_jobs.extend(jobs)
        if jobs:
            status.append({"name": f"Lever/{name}", "ok": True, "count": len(jobs)})

    return all_jobs, status


# ─── XML / RSS parsing ────────────────────────────────────────────────────────

NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "dc": "http://purl.org/dc/elements/1.1/",
}


def _text(el, *tags) -> str:
    """Safely extract text from nested XML elements."""
    cur = el
    for tag in tags:
        if cur is None:
            return ""
        cur = cur.find(tag) if ":" not in tag else cur.find(tag, NS)
    return (cur.text or "").strip() if cur is not None else ""


def parse_rss_xml(content: bytes) -> list[dict]:
    """Parse RSS 2.0 or Atom 1.0 XML into a list of item dicts."""
    items = []
    try:
        root = ET.fromstring(content)
    except ET.ParseError:
        return items

    # Atom feed
    if root.tag in ("{http://www.w3.org/2005/Atom}feed", "feed"):
        ns = "http://www.w3.org/2005/Atom"
        for entry in root.findall(f"{{{ns}}}entry"):
            link_el = entry.find(f"{{{ns}}}link")
            link = (link_el.get("href", "") if link_el is not None else "")
            pub = _text(entry, f"{{{ns}}}published") or _text(entry, f"{{{ns}}}updated")
            items.append({
                "title": _text(entry, f"{{{ns}}}title"),
                "link": link,
                "description": _text(entry, f"{{{ns}}}summary") or _text(entry, f"{{{ns}}}content"),
                "author": _text(entry, f"{{{ns}}}author", f"{{{ns}}}name"),
                "pubDate": pub,
            })
        return items

    # RSS 2.0
    channel = root.find("channel")
    if channel is None:
        channel = root
    for item in channel.findall("item"):
        author = (
            _text(item, "author")
            or _text(item, "{http://purl.org/dc/elements/1.1/}creator")
        )
        items.append({
            "title": _text(item, "title"),
            "link": _text(item, "link"),
            "description": _text(item, "description"),
            "author": author,
            "pubDate": _text(item, "pubDate"),
        })
    return items


def parse_pub_date(raw: str) -> datetime | None:
    if not raw:
        return None
    try:
        return parsedate_to_datetime(raw).astimezone(timezone.utc)
    except Exception:
        pass
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%d"):
        try:
            dt = datetime.strptime(raw[:19], fmt[:len(raw[:19])])
            return dt.replace(tzinfo=timezone.utc)
        except Exception:
            pass
    return None


# ─── Scoring ─────────────────────────────────────────────────────────────────

def strip_html(html: str) -> str:
    return re.sub(r"<[^>]+>", " ", html)


def score_job(title: str, description: str, company: str) -> int:
    text = (title + " " + strip_html(description) + " " + company).lower()
    title_lower = title.lower()

    score = 0
    for kw in MATCH_KEYWORDS:
        if kw in title_lower:
            score += 15
        elif kw in text:
            score += 3

    for co in TARGET_COMPANIES:
        if co in (company + " " + text).lower():
            score += 20
            break

    weak_hits = sum(1 for kw in WEAK_ONLY_KEYWORDS if kw in title_lower)
    strong_title_hits = sum(1 for kw in MATCH_KEYWORDS if kw in title_lower)
    if weak_hits > 0 and strong_title_hits == 0:
        score -= 50

    return max(0, min(100, score))


# ─── Feed fetching ────────────────────────────────────────────────────────────

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
}


def fetch_feed(source: dict, cutoff_hours: int = 72) -> tuple[list[dict], bool]:
    cutoff = datetime.now(timezone.utc) - timedelta(hours=cutoff_hours)
    jobs = []
    try:
        resp = requests.get(source["rss"], headers=HEADERS, timeout=15)
        resp.raise_for_status()
        raw_items = parse_rss_xml(resp.content)

        for item in raw_items:
            title = item.get("title", "")
            link = item.get("link", "")
            description = item.get("description", "")
            company = item.get("author", "")
            pub_raw = item.get("pubDate", "")
            published = parse_pub_date(pub_raw)

            if published and published < cutoff:
                continue

            score = score_job(title, description, company)
            if score >= 10:
                jobs.append({
                    "title": title,
                    "company": company,
                    "link": link,
                    "score": score,
                    "source": source["name"],
                    "published": published.strftime("%Y-%m-%d") if published else "recent",
                })
        return jobs, True
    except Exception as e:
        print(f"  Warning: {source['name']}: {e}", file=sys.stderr)
        return [], False


def deduplicate(jobs: list[dict]) -> list[dict]:
    seen_links, seen_titles, unique = set(), set(), []
    for job in jobs:
        lk = job["link"] or job["title"]
        tk = job["title"].lower().strip()
        if lk not in seen_links and tk not in seen_titles:
            seen_links.add(lk)
            seen_titles.add(tk)
            unique.append(job)
    return unique


# ─── Issue formatting ─────────────────────────────────────────────────────────

def get_daily_tip() -> dict:
    return SKILL_TIPS[datetime.now().weekday() % len(SKILL_TIPS)]


def format_issue(jobs: list[dict], sources_status: list[dict]) -> tuple[str, str]:
    today = datetime.now().strftime("%A, %B %d %Y")
    tip = get_daily_tip()
    jobs_sorted = sorted(jobs, key=lambda j: j["score"], reverse=True)

    title = f"🔍 Web3 Jobs — {today}"
    lines = [
        f"# 🔍 Daily Web3 Job Hunt — {today}",
        "",
        "> Auto-generated for **Bhargav Kacharla**  ",
        "> Skills: Solidity · EVM · TypeScript · AI Agents · ERC-4337 · Perpetuals · RWA · Rust/Anchor",
        "",
    ]

    # Jobs
    if jobs_sorted:
        lines += [f"## 💼 {len(jobs_sorted)} Matching Jobs (last 72 h)", ""]
        for j in jobs_sorted[:25]:
            icon = "🔥" if j["score"] >= 60 else "⭐" if j["score"] >= 30 else "·"
            co = f" @ **{j['company']}**" if j["company"] else ""
            lines.append(
                f"- {icon} [{j['title']}]({j['link']}){co} — `{j['source']}` · {j['published']}"
            )
        lines.append("")
    else:
        lines += [
            "## 💼 Jobs",
            "",
            "No new filtered listings found in the last 72 h — use the direct search links below.",
            "",
        ]

    # Quick search links
    lines += [
        "## 🔗 Direct Job Board Links (updated hourly)",
        "",
        "| Board | Best filter for your profile |",
        "|---|---|",
        "| [web3.career — Remote Solidity](https://web3.career/remote+solidity-jobs) | Senior / Staff roles |",
        "| [web3.career — DeFi + Solidity](https://web3.career/defi+solidity-jobs) | Protocol / DeFi roles |",
        "| [CryptoJobsList — Solidity](https://cryptojobslist.com/solidity) | Broad Solidity market |",
        "| [CryptoJobsList — Remote](https://cryptojobslist.com/remote) | Remote only |",
        "| [CryptoCurrencyJobs — DeFi](https://cryptocurrencyjobs.co/defi/) | DeFi-native companies |",
        "| [Wellfound — Smart Contract](https://wellfound.com/role/smart-contract) | Startups + equity |",
        "| [Crypto.Jobs](https://crypto.jobs/) | Community-driven listings |",
        "| [Immunefi Bounties](https://immunefi.com/bug-bounty/) | Security bounties (side income) |",
        "",
    ]

    # Skill tip of the day
    lines += [
        f"## 🧠 Today's Skill Recommendation — {tip['title']}",
        "",
        f"> **Why now?** {tip['why']}",
        "",
        "**Action steps:**",
    ]
    for step in tip["action"]:
        lines.append(f"- {step}")
    lines.append("")

    # Market pulse
    lines += [
        "## 📊 Market Pulse (2026)",
        "",
        "| Signal | Data |",
        "|---|---|",
        "| AI mentions in web3 job postings | **53%** (up from 23% in early 2025) |",
        "| Hybrid AI + Blockchain engineer demand | **+150% YoY** |",
        "| Senior Solidity salary range | **$180k–$250k + token grants** |",
        "| AI + Web3 hybrid engineer range | **$140k–$300k** |",
        "| Blockchain talent shortage | **Critical** — supply is the bottleneck |",
        "",
    ]

    # Target companies
    lines += [
        "## 🎯 Companies to Watch for Your Profile",
        "",
        "**Perpetuals / DeFi** — dYdX, Hyperliquid, Drift, Vertex, Synthetix, GMX",
        "",
        "**Account Abstraction infra** — Alchemy, Biconomy, Pimlico, Safe, ZeroDev, Privy",
        "",
        "**RWA / Tokenization** — MANTRA, Ondo Finance, Centrifuge, Maple Finance, Circle",
        "",
        "**AI + Web3** — Lit Protocol, Phala Network, Coinbase Developer Platform, Dynamic.xyz",
        "",
        "**Security / Audit** — Cyfrin, Trail of Bits, Quantstamp, OpenZeppelin, Immunefi",
        "",
        "**Infrastructure** — Chainlink Labs, LayerZero Labs, Wormhole, Base (Coinbase)",
        "",
    ]

    # Feed status
    lines += [
        "<details>",
        "<summary>📡 Feed status</summary>",
        "",
    ]
    for s in sources_status:
        icon = "✅" if s["ok"] else "⚠️"
        lines.append(f"- {icon} {s['name']} — {s['count']} listings fetched")
    lines += ["", "</details>", ""]

    lines += [
        "---",
        "*Auto-generated by [Daily Web3 Job Hunt](../../actions/workflows/daily-job-hunt.yml) · runs every day at 8 AM IST*",
    ]

    return title, "\n".join(lines)


# ─── GitHub issue creation ────────────────────────────────────────────────────

def create_github_issue(title: str, body: str) -> bool:
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY", "bhargav55/resume")

    if not token:
        print("No GITHUB_TOKEN — printing output:\n")
        print(f"TITLE: {title}\n")
        print(body)
        return True

    url = f"https://api.github.com/repos/{repo}/issues"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    # Try with labels first; fall back without if they don't exist yet
    for payload in [
        {"title": title, "body": body, "labels": ["job-hunt", "daily"]},
        {"title": title, "body": body},
    ]:
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=30)
            resp.raise_for_status()
            print(f"✅ Issue created: {resp.json()['html_url']}")
            return True
        except requests.HTTPError:
            if resp.status_code != 422:
                print(f"❌ GitHub API error {resp.status_code}: {resp.text}", file=sys.stderr)
                return False
            # 422 = labels don't exist, retry without
            continue
    return False


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    print("🔍 Starting daily web3 job hunt...")
    all_jobs: list[dict] = []
    sources_status: list[dict] = []

    # 1. RSS / Atom feeds (may be blocked by Cloudflare on some IPs)
    print("\n[1/2] RSS feeds...")
    for source in JOB_SOURCES:
        print(f"  {source['name']}...")
        jobs, ok = fetch_feed(source)
        sources_status.append({"name": source["name"], "ok": ok, "count": len(jobs)})
        all_jobs.extend(jobs)

    # 2. Company career APIs (Greenhouse + Lever — always open, no auth)
    print("\n[2/2] Company career boards (Greenhouse + Lever)...")
    company_jobs, company_status = fetch_all_company_jobs()
    all_jobs.extend(company_jobs)
    sources_status.extend(company_status)

    unique = deduplicate(all_jobs)
    matched = len([j for j in unique if j["score"] >= 10])
    print(f"\n✅ {matched} matching jobs found (from {len(unique)} unique listings)\n")

    title, body = format_issue(unique, sources_status)
    create_github_issue(title, body)


if __name__ == "__main__":
    main()
