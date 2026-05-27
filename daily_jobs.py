#!/usr/bin/env python3
"""
Daily Web3 Job Hunt CLI — Bhargav Kacharla
Run: python daily_jobs.py
Optional: python daily_jobs.py --save   (saves report to reports/YYYY-MM-DD.md)
"""

import anthropic
import datetime
import argparse
import os
import sys

PROFILE = """
Name: Bhargav Kacharla
Role target: Senior Smart Contract / Blockchain Engineer (EVM-first, AI-native)
Years experience: ~9 years total, 5+ years web3

Core strengths:
- Solidity (EVM): CLOB matching engines, perpetuals/derivatives protocols, liquidation engines,
  risk engines, oracle integrations (Pyth, Stork), on-chain indexers (WebSocket)
- Smart contract standards: ERC-4337 (account abstraction), ERC-3643 (RWA), ERC-4626 (vaults),
  ERC-8004/8183 (agent marketplace), concentrated liquidity (Uniswap V3-style)
- Security: worked with Quantstamp & Zellic on formal audits, Slither, Trail of Bits tooling
- Rust/Solana (Anchor): launchpad (Hatchy.fun), secondary to EVM
- AI/Agents: RAG pipelines, multi-agent orchestration (LangChain/LangGraph), MCP tool calling,
  Anthropic SDK, autonomous on-chain agent execution, eval frameworks
- TypeScript/Node.js backend, Python, AWS/GCP, Postgres, Docker
- Recent role: Senior Engineer (Blockchain & Agents) at Nunchi.trade — built full perp DEX stack
  including CLOB, clearing house, risk engine, liquidation engine, and AI-native CLI

Target company types:
1. Perpetuals / derivatives DEXs (Hyperliquid, dYdX, Drift, Vertex, Paradex, RabbitX, Zeta)
2. DeFi protocols (EigenLayer, Uniswap, Aave, Morpho, Euler, Pendle, GMX)
3. AI + Web3 intersection (Autonolas/Valory, Giza, Bonsai, Marlin, Phala, Fetch.ai)
4. RWA / institutional (Ondo Finance, Maple Finance, Centrifuge, Plume Network)
5. Account abstraction infra (Biconomy, Pimlico, ZeroDev, Stackup, Alchemy)
6. Layer 2 / infra (Arbitrum, Optimism ecosystem, Base, zkSync, Starknet)

Location: India (remote strongly preferred, open to relocation for the right role)
"""

SEARCH_QUERIES = [
    "solidity smart contract engineer jobs hiring this week DeFi perpetuals",
    "EVM blockchain engineer senior remote jobs web3 2026",
    "AI agent blockchain engineer on-chain agents hiring",
    "EigenLayer Uniswap Aave Morpho smart contract engineer open positions",
    "web3 account abstraction ERC-4337 engineer jobs",
    "RWA tokenization blockchain engineer jobs 2026",
]

SYSTEM_PROMPT = """You are a senior web3 recruiter and career coach with deep knowledge of the
blockchain/DeFi job market. You help engineers find and land top-tier web3 jobs.
Be specific, actionable, and direct. No filler. Format output as clean markdown."""

def build_daily_prompt(date_str: str) -> str:
    return f"""Today is {date_str}.

Here is my profile:
{PROFILE}

Your job is to produce my DAILY JOB HUNT REPORT. Structure it exactly as follows:

---

# Daily Web3 Job Hunt Report — {date_str}

## 🎯 Profile Match Score & Today's Market Pulse
2-3 sentences: How strong is my profile for today's market? What's the single hottest demand signal right now?

## 🚀 Top Job Opportunities Today
List 8-10 SPECIFIC roles I should apply to TODAY. For each:
- **Company** — Role title
  - Why it's a match (1 line, specific to my profile)
  - Where to apply: [careers page or job board URL]
  - Salary range if known
  - Remote/location status

Focus on: perpetuals DEXs, DeFi protocols, AI+Web3 companies, RWA platforms, AA infra.
Include mix of: well-known protocols + emerging/growth-stage teams.
Prioritize roles that value CLOB/perp DEX experience, on-chain agents, and security audit experience.

## 📬 Outreach Targets (Cold Apply)
3-5 companies that aren't actively posting but would be a strong match.
For each: company name, why they'd want me, where to find their team (LinkedIn/Twitter/Discord).

## 🧠 Today's Skill Gap & Upskilling Recommendation
Based on current job descriptions and market trends, what is the ONE skill I should spend 30-60 mins on today?
- What skill / concept
- Why it matters right now (data point: e.g. "X% of job posts mention it")
- Specific resource to start with (GitHub repo, docs page, tutorial)

## 🤖 AI-First Signal: Should I Learn This?
Companies are going AI-first. Based on today's market:
- What specific AI skill is appearing in web3 job posts this week?
- Is it relevant to my profile or would it conflict?
- Concrete next step (tool to try, repo to read, thing to build)

## ⚡ Resume / Profile Optimization Tip
One specific change I should make to my resume OR GitHub/LinkedIn today.
Be surgical — point to exact section or bullet to improve.

## 📊 Skill Currency Check
Rate my core skills as: 🟢 Hot (actively demanded) | 🟡 Stable | 🔴 Fading
- Solidity / EVM
- CLOB / Perpetuals protocols
- ERC-4337 (Account Abstraction)
- ERC-3643 (RWA tokenization)
- Rust / Solana (Anchor)
- On-chain AI agents
- TypeScript backend
- Smart contract security (Slither, audit experience)
- LangChain / LangGraph
- Move language

## 🎯 Today's Action Checklist
5 specific actions ranked by priority. Each should take < 2 hours.
Format: [ ] Action — expected outcome

---
Keep the report tight and actionable. Every line should either open a door or close a skill gap."""


def run_daily_report(save: bool = False):
    client = anthropic.Anthropic()
    date_str = datetime.date.today().strftime("%B %d, %Y")

    print(f"\n🔍 Generating your daily job hunt report for {date_str}...\n")

    with client.messages.stream(
        model="claude-opus-4-7",
        max_tokens=4000,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": build_daily_prompt(date_str)}],
    ) as stream:
        full_response = ""
        for text in stream.text_stream:
            print(text, end="", flush=True)
            full_response += text

    print("\n")

    if save:
        reports_dir = os.path.join(os.path.dirname(__file__), "reports")
        os.makedirs(reports_dir, exist_ok=True)
        filename = datetime.date.today().strftime("%Y-%m-%d") + ".md"
        filepath = os.path.join(reports_dir, filename)
        with open(filepath, "w") as f:
            f.write(f"# Daily Web3 Job Hunt Report\n")
            f.write(f"*Generated: {date_str}*\n\n")
            f.write(full_response)
        print(f"✅ Report saved to: {filepath}\n")

    return full_response


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Daily Web3 job hunt report for Bhargav")
    parser.add_argument("--save", action="store_true", help="Save report to reports/YYYY-MM-DD.md")
    args = parser.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ Error: ANTHROPIC_API_KEY environment variable not set.")
        print("   export ANTHROPIC_API_KEY=your_key_here")
        sys.exit(1)

    run_daily_report(save=args.save)
