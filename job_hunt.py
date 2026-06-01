#!/usr/bin/env python3
"""
Daily web3 job hunting automation for Bhargav Kacharla.
Searches job boards via Claude's built-in web_search tool,
scores matches against the candidate profile, and writes a
markdown report to reports/<YYYY-MM-DD>.md.
"""

import json
import os
import sys
from datetime import date
from pathlib import Path

import anthropic

# ---------------------------------------------------------------------------
# Candidate profile (cached across API calls)
# ---------------------------------------------------------------------------

PROFILE = """
## Candidate Profile: Bhargav Kacharla
Email: kacharlabhargav21@gmail.com
GitHub: github.com/bhargav55

### Primary Skills
- Solidity / EVM smart contract development (Foundry, Hardhat)
  - DeFi primitives: perpetuals, options, CLOBs, AMMs, lending protocols
  - ERC-4337 account abstraction, ERC-3643 RWA tokenization
  - Agent marketplace standards: ERC-8004 / ERC-8183
  - Oracle integration: Pyth, Stork, Chainlink
  - Auditing experience: Quantstamp, Zellic (security-aware development)
- TypeScript / Node.js backend
- Python (scripting, AI tooling)

### Secondary Skills
- Rust + Anchor (Solana / SVM)
- Move (Aptos/Sui familiarity)
- Cloud: AWS, GCP, Docker, Kubernetes basics

### AI / Agent Skills
- Anthropic SDK, OpenAI SDK, OpenRouter
- LangChain, LangGraph, RAG pipelines
- Model Context Protocol (MCP)
- On-chain autonomous agents, AI-native CLIs

### Experience Highlights
- Nunchi.trade (Current, July 2025–Present): Senior Blockchain & AI Engineer
  - Built on-chain CLOB matching engine for perpetuals
  - Integrated Pyth/Stork oracle pricing
  - Shipped AI-native CLI for autonomous liquidation agents
  - Designed on-chain agent marketplace (ERC-8004/8183)
- Novastro: RWA (ERC-3643), prediction markets on Polygon, Solana launchpad (Hatchy.fun)
- Xalts: ERC-4337 account abstraction, skandha bundlers
- Oddz: Options trading with concentrated liquidity on Avalanche/BNB

### Target Roles
- Smart Contract Engineer / Blockchain Engineer
- Protocol Engineer (DeFi)
- Blockchain + AI / Agent Engineer
- Senior/Staff Engineer at web3-native companies

### Target Companies
Hyperliquid, dYdX, Chainlink Labs, Uniswap Labs, LayerZero Labs,
GMX, Synthetix, Morpho, Euler Finance, EigenLayer, Ethereum Foundation,
Sei Foundation, Across Protocol, Aave, Compound, MakerDAO/Sky,
any AI-first web3 startup.

### Preferred: Remote-friendly, competitive comp, equity/tokens.
"""

# ---------------------------------------------------------------------------
# JSON schema for structured job listing output
# ---------------------------------------------------------------------------

JOB_LISTING_SCHEMA = {
    "type": "object",
    "properties": {
        "jobs": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "company": {"type": "string"},
                    "location": {"type": "string"},
                    "remote": {"type": "boolean"},
                    "url": {"type": "string"},
                    "match_score": {
                        "type": "integer",
                        "description": "0-100 score based on skill alignment",
                    },
                    "match_reasons": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "salary_range": {"type": "string"},
                    "key_requirements": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "missing_skills": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Skills the candidate lacks for this role",
                    },
                },
                "required": [
                    "title",
                    "company",
                    "location",
                    "remote",
                    "url",
                    "match_score",
                    "match_reasons",
                    "key_requirements",
                    "missing_skills",
                ],
            },
        },
        "skill_recommendations": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "skill": {"type": "string"},
                    "reason": {"type": "string"},
                    "priority": {
                        "type": "string",
                        "enum": ["high", "medium", "low"],
                    },
                    "resources": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                },
                "required": ["skill", "reason", "priority"],
            },
        },
        "market_summary": {"type": "string"},
        "ai_trends": {"type": "string"},
    },
    "required": ["jobs", "skill_recommendations", "market_summary", "ai_trends"],
}

# ---------------------------------------------------------------------------
# Search queries aimed at the best web3 job boards
# ---------------------------------------------------------------------------

SEARCH_QUERIES = [
    "site:web3.career solidity smart contract engineer jobs 2025",
    "site:cryptojobslist.com solidity OR \"smart contract\" OR EVM engineer",
    "site:cryptocurrencyjobs.co solidity OR protocol engineer remote 2025",
    "site:wellfound.com smart contract solidity engineer remote",
    "hyperliquid OR dydx OR chainlink OR uniswap OR layerzero \"smart contract\" OR solidity engineer jobs",
    "web3 DeFi protocol engineer AI agents solidity typescript remote jobs 2025",
    "EigenLayer OR Morpho OR Euler Finance OR Aave solidity engineer hiring",
]

# ---------------------------------------------------------------------------
# Core logic
# ---------------------------------------------------------------------------

def run_job_hunt(today: str) -> dict:
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    system_prompt = [
        {
            "type": "text",
            "text": PROFILE,
            "cache_control": {"type": "ephemeral"},  # cache the static profile
        },
        {
            "type": "text",
            "text": (
                "You are a career assistant specialising in web3/blockchain roles. "
                "Use the web_search tool to find real, currently open job postings. "
                "Score every job 0-100 against the candidate profile above. "
                "Only include jobs with a score >= 60. Aim for 10-20 high-quality listings. "
                "After the job search, produce skill recommendations and market insights. "
                "Return valid JSON that matches the provided schema exactly."
            ),
        },
    ]

    user_message = (
        f"Today is {today}. Search for open web3 / blockchain / DeFi engineering roles "
        "that match the candidate profile. Use multiple searches across different job boards "
        "and company career pages. Focus on: Solidity/EVM smart contract roles, "
        "Protocol Engineer positions, and any AI+blockchain hybrid roles. "
        "Also look for roles at the target companies listed in the profile. "
        "After gathering jobs, provide skill recommendations based on what you see "
        "companies asking for that the candidate might be missing or should deepen."
    )

    print(f"[{today}] Starting job search with {len(SEARCH_QUERIES)} planned queries...")

    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=16000,
        thinking={"type": "adaptive"},
        tools=[{"type": "web_search_20260209", "name": "web_search"}],
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
        output_config={
            "format": {
                "type": "json_schema",
                "name": "job_hunt_results",
                "schema": JOB_LISTING_SCHEMA,
                "strict": True,
            }
        },
    )

    # Extract text content from response
    text_content = ""
    for block in response.content:
        if hasattr(block, "text"):
            text_content += block.text

    data = json.loads(text_content)

    print(
        f"[{today}] Found {len(data.get('jobs', []))} jobs, "
        f"{len(data.get('skill_recommendations', []))} skill recs."
    )
    return data


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def render_report(data: dict, today: str) -> str:
    jobs = sorted(data.get("jobs", []), key=lambda j: j.get("match_score", 0), reverse=True)
    recs = data.get("skill_recommendations", [])
    market = data.get("market_summary", "")
    ai_trends = data.get("ai_trends", "")

    lines = [
        f"# Web3 Job Hunt Report — {today}",
        "",
        "## Market Summary",
        "",
        market,
        "",
        "## AI & Emerging Tech Trends",
        "",
        ai_trends,
        "",
        f"## Job Opportunities ({len(jobs)} matches)",
        "",
    ]

    for i, job in enumerate(jobs, 1):
        remote_tag = "Remote" if job.get("remote") else job.get("location", "Unknown")
        salary = job.get("salary_range", "Not listed")
        url = job.get("url", "#")
        lines += [
            f"### {i}. [{job['title']} — {job['company']}]({url})",
            f"**Location:** {remote_tag} | **Salary:** {salary} | **Match Score:** {job['match_score']}/100",
            "",
            "**Why it fits:**",
        ]
        for reason in job.get("match_reasons", []):
            lines.append(f"- {reason}")
        lines.append("")
        lines.append("**Key Requirements:**")
        for req in job.get("key_requirements", []):
            lines.append(f"- {req}")
        missing = job.get("missing_skills", [])
        if missing:
            lines.append("")
            lines.append("**Gaps to address:**")
            for sk in missing:
                lines.append(f"- {sk}")
        lines.append("")

    lines += [
        "## Daily Skill Recommendations",
        "",
    ]

    priority_order = {"high": 0, "medium": 1, "low": 2}
    recs_sorted = sorted(recs, key=lambda r: priority_order.get(r.get("priority", "low"), 2))

    for rec in recs_sorted:
        priority_emoji = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(rec["priority"], "⚪")
        lines += [
            f"### {priority_emoji} {rec['skill']} ({rec['priority'].upper()})",
            "",
            rec.get("reason", ""),
        ]
        resources = rec.get("resources", [])
        if resources:
            lines.append("")
            lines.append("**Resources:**")
            for r in resources:
                lines.append(f"- {r}")
        lines.append("")

    lines.append("---")
    lines.append(f"*Generated automatically on {today} via Claude claude-opus-4-8 + web_search*")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    today = date.today().isoformat()

    reports_dir = Path(__file__).parent / "reports"
    reports_dir.mkdir(exist_ok=True)
    report_path = reports_dir / f"{today}.md"

    try:
        data = run_job_hunt(today)
    except Exception as exc:
        print(f"ERROR during job hunt: {exc}", file=sys.stderr)
        sys.exit(1)

    report_md = render_report(data, today)
    report_path.write_text(report_md, encoding="utf-8")
    print(f"Report saved to {report_path}")

    # Also dump raw JSON for programmatic consumption
    json_path = reports_dir / f"{today}.json"
    json_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"JSON saved to {json_path}")


if __name__ == "__main__":
    main()
