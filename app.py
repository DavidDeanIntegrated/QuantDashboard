import streamlit as st

st.set_page_config(
    page_title="Hands-On Quant Finance 2025",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.markdown("## Navigation")
st.sidebar.markdown("Use the pages above to explore each section of the guide.")
st.sidebar.divider()
st.sidebar.markdown(
    "*Built as a portfolio project following the guide's own recommendations.*"
)

# --- Hero Section ---
st.markdown(
    """
# The Complete Guide to Hands-On Quant Finance in 2025

> **You can build a functioning quant trading system for $0–$79/month, paper trade
> every asset class, and deploy a portfolio-worthy dashboard in under a month
> using Claude Code and Streamlit.**

The math behind Renaissance Technologies' 66% annual returns and Bridgewater's
$150 billion All Weather fund is accessible through free Python libraries. The hard
truth: 76% of retail traders lose money, distinguishing skill from luck requires
2–4 years of live data, and your first year will almost certainly underperform the
S&P 500. But the infrastructure barrier has never been lower, and the portfolio
project you build along the way has standalone career value even if trading returns
disappoint.
"""
)

st.divider()

# --- Key Stats ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Medallion Fund", "66.1%", "Avg Gross Annual Return")
col2.metric("Retail Traders", "76%", "Are Unprofitable", delta_color="inverse")
col3.metric("Skill Validation", "~4 Years", "At Sharpe 1.0")
col4.metric("Min Live Cost", "$0/mo", "Paper Trading Tier")

st.divider()

# --- Guide Overview ---
st.markdown("## What This Guide Covers")

sections = {
    "1 — Real-World Examples": (
        "How Renaissance, Bridgewater, AQR, and others actually use probability, "
        "factor models, linear algebra, and stochastic calculus in production."
    ),
    "2 — Tools & Pricing": (
        "Every tool you need — data sources, brokerages, Python libraries, cloud "
        "hosting, and platforms — with exact 2025 pricing."
    ),
    "3 — Cost Tiers": (
        "Four tiers from $0/month (surprisingly capable) to $2,000+/month "
        "(professional). Most individuals never need Tier 3 or 4."
    ),
    "4 — Six-Month Pilot": (
        "A realistic month-by-month plan from zero to live trading, with honest "
        "expectations at every stage."
    ),
    "5 — Dashboard Build Plan": (
        "Step-by-step guide to building a Streamlit dashboard with Claude Code, "
        "including project structure and phased milestones."
    ),
    "6 — Success Metrics": (
        "How to tell if you're any good — the math of skill vs. luck, benchmarks, "
        "honest return expectations, and the eight pitfalls that destroy quant traders."
    ),
}

cols = st.columns(2)
for i, (title, desc) in enumerate(sections.items()):
    with cols[i % 2]:
        st.markdown(f"### {title}")
        st.markdown(desc)

st.divider()

# --- Conclusion ---
st.markdown(
    """
## The Bottom Line

The infrastructure for hands-on quant finance has democratized completely. Free data
APIs, commission-free brokerages with excellent APIs, open-source Python libraries
covering every quantitative method, and AI coding assistants that compress development
timelines by 2–3x mean the barriers are **capital, patience, and intellectual honesty**
— not technology or cost.

The most important number in this entire guide is **4 years** — the minimum track
record to statistically validate a strategy with Sharpe 1.0 at 95% confidence.
Everything before that is learning, and that learning has independent value as a
portfolio project, a demonstration of quantitative thinking, and a foundation for
understanding how the $3.26 trillion hedge fund industry actually operates.
"""
)
