#!/usr/bin/env python3
"""
Daily Web3 job hunter — tailored for Bhargav Kacharla's profile.

Fetches from multiple job-board RSS feeds, scores each listing against
profile keywords, deduplicates, and creates a GitHub Issue with today's
top matches plus a rotating daily skill tip.
"""

from __future__ import annotations

import hashlib
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime

try:
    import feedparser
    import requests
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "feedparser", "requests", "-q"])
    import feedparser  # type: ignore
    import requests    # type: ignore


# ── Profile keyword configuration ────────────────────────────────────────────

# Any one of these must appear in the listing for it to count as a dev role
ROLE_KEYWORDS = [
    "solidity", "smart contract", "evm", "blockchain engineer", "web3 engineer",
    "protocol engineer", "contract developer", "on-chain", "dapp developer",
    "ethereum", "polygon", "avalanche", "bnb chain", "blockchain developer",
]

# Each match adds +8 to score — these are Bhargav's strength areas
STRENGTH_KEYWORDS = [
    "perpetuals", "perps", "options", "clob", "liquidation", "clearing house",
    "account abstraction", "erc-4337", "rwa", "tokenization", "erc-3643",
    "ai agent", "autonomous agent", "security", "audit", "oracle integration",
    "pyth", "stork", "chainlink keeper", "gelato", "foundry", "hardhat",
    "typescript", "real-time indexer", "websocket", "defi",
]

# Each match adds +4 to score — secondary tech Bhargav knows
TECH_KEYWORDS = [
    "rust", "anchor", "solana", "svm", "layerzero", "ccip", "wormhole",
    "uniswap", "aave", "compound", "gmx", "hyperliquid", "dydx", "synthetix",
    "zk", "rollup", "l2", "eigenlayer", "restaking", "erc-4626",
    "move", "aptos", "sui", "mev", "flashbots",
]

# Matching any of these subtracts 20 — not Bhargav's target
EXCLUDE_TERMS = [
    "marketing", "sales", "community manager", "content writer",
    "graphic designer", "growth hacker", "recruiter", "hr ",
    "business development", "data analyst", "data scientist",
    "ios developer", "android developer",
    "senior frontend", "react developer",
    "intern", "entry level", "junior",
]

# Tier-1 protocol/fund names — +15 bonus
TIER1 = [
    "aave", "uniswap", "hyperliquid", "dydx", "gmx", "synthetix", "compound",
    "morpho", "pendle", "lido", "eigenlayer", "chainlink", "paradigm", "a16z",
    "arbitrum", "optimism", "base", "starkware", "aztec", "maker", "sky",
    "wintermute", "jump crypto", "dragonfly", "multicoin",
]


# ── Job board RSS feeds ───────────────────────────────────────────────────────

RSS_FEEDS = [
    ("web3.career/all",      "https://web3.career/feed"),
    ("web3.career/solidity", "https://web3.career/solidity-jobs/feed"),
    ("web3.career/defi",     "https://web3.career/defi-jobs/feed"),
    ("web3.career/remote",   "https://web3.career/remote-jobs/feed"),
    ("web3.career/security", "https://web3.career/security-jobs/feed"),
    ("cryptojobslist",       "https://cryptojobslist.com/feed/rss"),
    ("cryptocurrencyjobs",   "https://cryptocurrencyjobs.co/feed/"),
]

# Listed in the issue footer for manual browsing
BOARDS_TO_CHECK = [
    "https://web3.career/solidity-jobs",
    "https://cryptojobslist.com/solidity",
    "https://cryptocurrencyjobs.co/solidity/",
    "https://wellfound.com/role/smart-contract",
    "https://crypto.jobs/",
    "https://jobs.paradigm.xyz/",
    "https://jobs.a16zcrypto.com/",
    "https://immunefi.com/bug-bounty/",
]


# ── Daily skill tips (rotates by day-of-year) ────────────────────────────────

DAILY_TIPS = [
    "**Bug bounty hunting** — Submit a finding to Immunefi this week. A verified payout is stronger signal than any resume line.",
    "**ZK fundamentals** — Study Groth16 and PLONK proofs. L2 protocol roles in 2026 increasingly expect basic ZK literacy. Start at `zk-learning.org`.",
    "**Open-source contribution** — Make a PR to Morpho, Aave, or Uniswap. Even a doc fix gets your name in their commit log.",
    "**Write publicly** — Post a technical breakdown of your CLOB matching engine on Mirror or Substack. Your Nunchi.trade work is rare and worth documenting.",
    "**Foundry invariant tests** — Publish a repo of advanced Foundry invariant test suites. Hiring managers actively notice this.",
    "**MEV fundamentals** — Study the searcher → builder → proposer flow and Flashbots docs. Many perps roles expect this context.",
    "**EIP authorship** — Draft an EIP on the Ethereum Magicians forum. It's a strong signal of protocol-level thinking.",
    "**Cross-chain messaging** — Build a small CCIP or LayerZero cross-chain demo. Cross-chain fluency is now a checkbox at most DeFi protocols.",
    "**Gas optimization** — Write a blog post benchmarking SSTORE2, packed storage, and custom errors. Gas-optimization content gets shared widely.",
    "**Sherlock audit contest** — Participate in one contest this week. Even a low-severity finding builds a public auditor track record.",
    "**EVM Puzzles** — Solve 3 EVM Puzzles today (`github.com/fvictorio/evm-puzzles`). Bytecode-level intuition is tested in senior interviews.",
    "**Paradigm research** — Read the latest Paradigm research post and reproduce the code example. Posting your reproduction gets noticed by the right people.",
    "**Dune dashboard** — Build a Dune dashboard for one of your deployed protocols. It shows indexing depth beyond smart contracts.",
    "**Certora Prover** — Learn the basics of formal verification. Many top protocols now require it for senior hires. Start at `docs.certora.com`.",
    "**Document your AI agent work** — Write a detailed technical post on your ERC-8004/8183 agent marketplace. It's cutting-edge and almost no one has shipped this.",
    "**Ethereum Magicians** — Leave a thoughtful comment on an active EIP discussion thread. Protocol governance participation builds reputation.",
    "**Open-source your tooling** — Sanitize and publish your on-chain indexer or liquidation CLI. A public artifact beats a resume bullet.",
    "**Liquidation bot comparison** — Write about how liquidation bots differ across Aave, Compound, and your own perps protocol. Your firsthand knowledge is rare.",
    "**TypeScript SDK** — Wrap one of your deployed contracts in a TypeScript SDK and publish to npm. Ecosystem value is visible and searchable.",
    "**Protocol governance** — Track one major governance vote this week on Snapshot. Understanding protocol politics matters in senior roles.",
    "**Modular blockchain** — Read the Celestia whitepaper and EigenDA docs. Modular DA is required context for most infrastructure roles now.",
    "**Uniswap V4 hooks** — Build a simple V4 hook on a local fork. V4 hook architecture is the next AMM frontier and new roles are opening.",
    "**Certora specs** — Add a Certora spec to one of your open-source contracts. Formal verification proof is a rare and strong differentiator.",
    "**ERC-4626 strategy vault** — Deploy a novel yield strategy vault to testnet and write about the design. Concrete artifacts beat abstract claims.",
    "**Hyperliquid deep dive** — Study Hyperliquid's on-chain perp architecture. Comparing it to your Nunchi.trade implementation in writing is compelling content.",
    "**OP Stack internals** — Read the OP Stack derivation pipeline spec. L2 protocol roles increasingly expect familiarity with sequencer mechanics.",
    "**Halmos** — Run Halmos (`github.com/a16z/halmos`) on one of your Foundry test suites to explore symbolic execution. Write about what you find.",
    "**Quantstamp/Zellic audit post** — Write about the audit lifecycle you owned end-to-end. Security audit experience is rare; don't undersell it.",
    "**Apply to 3 roles today** — Quality over quantity. Customize your outreach for each role, referencing a specific protocol challenge or design choice.",
    "**Farcaster presence** — Post one technical insight on Farcaster (warpcast.com). The Web3 dev community is there and hiring managers are watching.",
]


# ── Data model ────────────────────────────────────────────────────────────────

@dataclass
class Job:
    title: str
    company: str
    url: str
    source: str
    published: datetime
    description: str = ""
    tags: list[str] = field(default_factory=list)
    score: int = 0

    @property
    def uid(self) -> str:
        return hashlib.md5(self.url.encode()).hexdigest()[:8]


# ── Core logic ────────────────────────────────────────────────────────────────

def normalize(text: str) -> str:
    return text.lower()


def score_job(job: Job) -> int:
    corpus = normalize(
        f"{job.title} {job.company} {job.description} {' '.join(job.tags)}"
    )
    score = 0

    # Must match at least one role keyword to be considered a dev role
    if any(kw in corpus for kw in ROLE_KEYWORDS):
        score += 10
    else:
        return 0  # Skip non-engineering roles entirely

    for kw in STRENGTH_KEYWORDS:
        if kw in corpus:
            score += 8

    for kw in TECH_KEYWORDS:
        if kw in corpus:
            score += 4

    if "remote" in corpus:
        score += 5

    if any(s in corpus for s in ["senior", "staff", "principal", "lead", "protocol engineer"]):
        score += 10

    for name in TIER1:
        if name in corpus:
            score += 15
            break  # one tier-1 hit is enough

    for term in EXCLUDE_TERMS:
        if term in corpus:
            score -= 20

    return max(0, score)


def parse_date(entry) -> datetime:
    for attr in ("published_parsed", "updated_parsed", "created_parsed"):
        t = getattr(entry, attr, None)
        if t:
            return datetime(*t[:6], tzinfo=timezone.utc)
    for attr in ("published", "updated"):
        s = getattr(entry, attr, None)
        if s:
            try:
                return parsedate_to_datetime(s).astimezone(timezone.utc)
            except Exception:
                pass
    return datetime.now(timezone.utc)


def fetch_feed(source: str, url: str, cutoff: datetime) -> list[Job]:
    try:
        feed = feedparser.parse(url, request_headers={"User-Agent": "web3-job-hunter/1.0"})
    except Exception as e:
        print(f"  [WARN] {source}: {e}")
        return []

    jobs: list[Job] = []
    for entry in feed.entries:
        published = parse_date(entry)
        if published < cutoff:
            continue

        title = entry.get("title", "").strip()
        link = entry.get("link", "").strip()
        if not title or not link:
            continue

        desc = re.sub(r"<[^>]+>", " ", entry.get("summary", entry.get("description", "")))
        desc = re.sub(r"\s+", " ", desc).strip()

        # Extract company from "Title at Company" pattern or author field
        company = ""
        m = re.search(r"\bat\s+(.+?)(?:\s*\||\s*[-–]|$)", title, re.IGNORECASE)
        if m:
            company = m.group(1).strip()
        elif entry.get("author"):
            company = str(entry.author).strip()

        tags = [t.get("term", "") for t in entry.get("tags", [])]

        jobs.append(Job(
            title=title,
            company=company,
            url=link,
            source=source,
            published=published,
            description=desc[:600],
            tags=tags,
        ))
    return jobs


def deduplicate(jobs: list[Job]) -> list[Job]:
    seen_urls: set[str] = set()
    seen_titles: set[str] = set()
    result: list[Job] = []
    for job in jobs:
        norm = re.sub(r"\s+", " ", normalize(job.title)).strip()
        if job.url in seen_urls or norm in seen_titles:
            continue
        seen_urls.add(job.url)
        seen_titles.add(norm)
        result.append(job)
    return result


def today_tip() -> str:
    day_of_year = datetime.now(timezone.utc).timetuple().tm_yday
    return DAILY_TIPS[day_of_year % len(DAILY_TIPS)]


# ── Issue formatting ──────────────────────────────────────────────────────────

def build_issue_body(top_jobs: list[Job], total_found: int) -> str:
    today = datetime.now(timezone.utc).strftime("%B %d, %Y")
    tip = today_tip()

    lines: list[str] = [
        f"# Web3 Job Report — {today}",
        "",
        f"Scanned 7 job boards. Found **{total_found}** new listings in the last 48 h. "
        f"Top **{len(top_jobs)}** matches for your profile (Solidity · EVM · DeFi · AI agents):",
        "",
    ]

    if not top_jobs:
        lines += [
            "> No strong matches today. Check the boards manually (links below).",
            "",
        ]
    else:
        for i, job in enumerate(top_jobs, 1):
            company_str = f" @ **{job.company}**" if job.company else ""
            date_str = job.published.strftime("%b %d")
            tag_str = "  ·  ".join(f"`{t}`" for t in job.tags[:5]) if job.tags else ""
            snippet = (job.description[:220] + "…") if len(job.description) > 220 else job.description

            lines += [
                f"### {i}. [{job.title}]({job.url}){company_str}",
                f"> 🎯 Score **{job.score}** &nbsp;|&nbsp; Source: `{job.source}` &nbsp;|&nbsp; Posted: {date_str}",
            ]
            if tag_str:
                lines.append(f"> {tag_str}")
            if snippet:
                lines.append(f"> {snippet}")
            lines.append("")

    lines += [
        "---",
        "",
        "## Browse More (check daily)",
        "",
        *[f"- {b}" for b in BOARDS_TO_CHECK],
        "",
        "---",
        "",
        "## Skill Tip of the Day",
        "",
        f"> {tip}",
        "",
        "---",
        "",
        "*Auto-generated by `.github/workflows/daily-jobs.yml` — runs every day at 09:00 IST.*",
    ]
    return "\n".join(lines)


# ── GitHub helpers ────────────────────────────────────────────────────────────

_GH_HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}


def ensure_label(token: str, repo: str) -> None:
    url = f"https://api.github.com/repos/{repo}/labels"
    h = {**_GH_HEADERS, "Authorization": f"Bearer {token}"}
    resp = requests.get(url, headers=h, timeout=10)
    names = [lb["name"] for lb in (resp.json() if resp.ok else [])]
    if "jobs" not in names:
        requests.post(url, headers=h, timeout=10,
                      json={"name": "jobs", "color": "0075ca",
                            "description": "Daily job hunt results"})


def create_issue(title: str, body: str) -> None:
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")

    if not token or not repo:
        # Local run — just print
        print(f"\n{'='*60}\nISSUE TITLE: {title}\n{'='*60}\n{body}")
        return

    ensure_label(token, repo)
    resp = requests.post(
        f"https://api.github.com/repos/{repo}/issues",
        headers={**_GH_HEADERS, "Authorization": f"Bearer {token}"},
        json={"title": title, "body": body, "labels": ["jobs"]},
        timeout=15,
    )
    if resp.status_code == 201:
        print(f"Issue created: {resp.json().get('html_url')}")
    else:
        print(f"ERROR creating issue: {resp.status_code}\n{resp.text}")
        sys.exit(1)


# ── Entry point ───────────────────────────────────────────────────────────────

def main() -> None:
    cutoff = datetime.now(timezone.utc) - timedelta(hours=48)
    print(f"Cutoff: {cutoff.strftime('%Y-%m-%d %H:%M UTC')}\n")

    raw: list[Job] = []
    for source, url in RSS_FEEDS:
        print(f"Fetching {source} …")
        new = fetch_feed(source, url, cutoff)
        print(f"  → {len(new)} recent entries")
        raw.extend(new)

    jobs = deduplicate(raw)
    print(f"\n{len(jobs)} unique jobs after dedup.")

    for job in jobs:
        job.score = score_job(job)

    relevant = sorted(
        [j for j in jobs if j.score >= 10],
        key=lambda j: j.score,
        reverse=True,
    )
    top = relevant[:20]
    print(f"{len(relevant)} relevant (score ≥ 10) → showing top {len(top)}.")

    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    create_issue(
        title=f"[Job Hunt] Web3 opportunities — {today_str}",
        body=build_issue_body(top, len(relevant)),
    )


if __name__ == "__main__":
    main()
