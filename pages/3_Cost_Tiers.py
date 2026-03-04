import streamlit as st

st.set_page_config(page_title="Cost Tiers", page_icon="💰", layout="wide")

st.markdown("# Four Cost Tiers: From Zero to Professional")

st.info(
    "**Key insight**: Most individual quant traders never need Tier 3 or 4. "
    "The edge for retail comes from strategy quality, niche markets (prediction "
    "markets, small-cap crypto), and lower overhead — not from infrastructure "
    "arms races with Citadel."
)

st.divider()

# --- Tier 1 ---
st.markdown("## Tier 1: Free ($0/month) — Surprisingly Capable")

st.markdown(
    """
At zero cost, you can paper trade every asset class, backtest strategies on years
of historical data, and deploy a live dashboard.

| Category | What You Get |
|---|---|
| **Data** | yfinance + FRED + CoinGecko free + Finnhub (60 calls/min free) |
| **Paper Trading** | Alpaca (stocks, options, crypto), Interactive Brokers ($1M virtual cash), thinkorswim (best options simulator) |
| **Hosting** | Streamlit Community Cloud or Google Colab |
| **Backtesting** | vectorbt or backtrader locally |
| **Monthly Total** | **$0** |
"""
)

st.success("**This tier is where you should spend months 1–3.**")

st.divider()

# --- Tier 2 ---
st.markdown("## Tier 2: Serious Hobby ($50–$150/month)")

st.markdown(
    """
Adding Polygon Starter unlocks unlimited API calls, WebSockets, and 5 years of
history. A DigitalOcean droplet provides persistent hosting for a trading bot.

Fund an Alpaca account with **$2,000–$5,000** for live trading — enough for 2–3
concurrent positions with fractional shares. At this capital level, expect
infrastructure costs to consume 40–80% of returns if you target 15% annually.

Commission-free trading on Alpaca means your primary cost friction is bid-ask
spreads (typically $0.01–$0.05/share).

| Item | Monthly Cost |
|---|---|
| Polygon Starter | $29 |
| VPS Hosting | $12 |
| Domain / Misc | $5–$10 |
| **Total** | **~$50–$65** |

*Excluding trading capital.*
"""
)

st.divider()

# --- Tier 3 ---
st.markdown("## Tier 3: Semi-Professional ($500–$2,000/month)")

st.markdown(
    """
Trading capital of **$25,000–$100,000** unlocks day trading (FINRA's Pattern Day
Trader rule requires $25,000 equity for more than 3 day trades per 5 business
days) and makes options strategies viable (need $2,500+ per 100-share lot).

At $50,000 capital targeting 15% returns, infrastructure costs of $500–$850/month
are manageable but not trivial.

| Item | Monthly Cost |
|---|---|
| Polygon Advanced (real-time, 20+ years) | $199 |
| Thetadata Standard (tick-level options) | $80 |
| ORATS (proprietary analytics) | $99 |
| Dedicated infrastructure | $100–$250 |
| **Total** | **$500–$850** |

*Excluding trading capital.*
"""
)

st.divider()

# --- Tier 4 ---
st.markdown("## Tier 4: Professional ($2,000+/month)")

st.markdown(
    """
All-in infrastructure for multi-venue presence: **$7,000–$15,000+/month**,
requiring **$500K+** in trading capital to justify economically.

| Item | Monthly Cost |
|---|---|
| Bloomberg Terminal (2-year lease) | $2,305–$2,665 |
| Co-location at Equinix NY4 (per rack) | ~$3,500 |
| Exchange cross-connects | $500–$2,000 |
| Direct data feeds | $1,000–$3,000 |
| **Total** | **$7,000–$15,000+** |

*Bloomberg saw a 6.5% price increase in 2025.*
"""
)
