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

**Data**: yfinance + FRED + CoinGecko free + Finnhub (60 calls/min free)

**Paper Trading**:
- Alpaca (stocks, options, crypto)
- Interactive Brokers ($1M virtual cash)
- thinkorswim (best options simulator)

**Hosting**: Streamlit Community Cloud or Google Colab

**Backtesting**: vectorbt or backtrader locally
"""
)

st.success("**This tier is where you should spend months 1–3.**")

st.divider()

# --- Tier 2 ---
st.markdown("## Tier 2: Serious Hobby ($50–$150/month)")

st.markdown(
    """
Adding Polygon Starter ($29/month) unlocks unlimited API calls, WebSockets, and
5 years of history. A DigitalOcean droplet ($12/month) provides persistent
hosting for a trading bot.

Fund an Alpaca account with **$2,000–$5,000** for live trading — enough for 2–3
concurrent positions with fractional shares. At this capital level, expect
infrastructure costs to consume 40–80% of returns if you target 15% annually.

Commission-free trading on Alpaca means your primary cost friction is bid-ask
spreads (typically $0.01–$0.05/share).
"""
)

st.markdown("**Monthly Breakdown:**")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Polygon Starter", "$29")
col2.metric("VPS Hosting", "$12")
col3.metric("Domain / Misc", "$5–10")
col4.metric("Total", "~$50–65")

st.caption("Excluding trading capital")

st.divider()

# --- Tier 3 ---
st.markdown("## Tier 3: Semi-Professional ($500–$2,000/month)")

st.markdown(
    """
- **Polygon Advanced** ($199/mo) — real-time data, 20+ years history
- **Thetadata Standard** ($80/mo) — tick-level options data
- **ORATS** ($99/mo) — proprietary analytics
- **Dedicated infrastructure** — $100–$250/month

Trading capital of **$25,000–$100,000** unlocks day trading (FINRA's Pattern Day
Trader rule requires $25,000 equity for more than 3 day trades per 5 business
days) and makes options strategies viable (need $2,500+ per 100-share lot).

At $50,000 capital targeting 15% returns, infrastructure costs of $500–$850/month
are manageable but not trivial.
"""
)

st.markdown("**Monthly Breakdown:**")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Polygon Advanced", "$199")
col2.metric("Thetadata", "$80")
col3.metric("ORATS", "$99")
col4.metric("Infrastructure", "$100–250")
col5.metric("Total", "$500–850")

st.caption("Excluding trading capital")

st.divider()

# --- Tier 4 ---
st.markdown("## Tier 4: Professional ($2,000+/month)")

st.markdown(
    """
- **Bloomberg Terminal**: $2,305–$2,665/month on a 2-year lease (6.5% price
  increase in 2025)
- **Co-location at Equinix NY4**: ~$3,500/month per rack + $500–$2,000/month per
  exchange cross-connect
- **Direct data feeds**: $1,000–$3,000/month

All-in infrastructure for multi-venue presence: **$7,000–$15,000+/month**,
requiring $500K+ in trading capital to justify economically.
"""
)

st.markdown("**Monthly Breakdown:**")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Bloomberg", "$2,305–2,665")
col2.metric("Co-location", "$3,500+")
col3.metric("Cross-connects", "$500–2,000")
col4.metric("Data Feeds", "$1,000–3,000")
col5.metric("Total", "$7K–15K+")

st.caption("Requires $500K+ in trading capital to justify economically")
