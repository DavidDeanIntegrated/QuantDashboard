import streamlit as st

st.set_page_config(page_title="Tools & Pricing", page_icon="🛠️", layout="wide")

st.markdown("# Every Tool You Need and Exactly What It Costs")
st.markdown(
    """
The quant trading ecosystem in 2025 offers free or low-cost alternatives at every
layer. Below is the complete pricing landscape across data, brokerages, libraries,
infrastructure, and platforms.
"""
)

st.divider()

# --- Market Data ---
st.markdown("## Market Data: From Free to Institutional")

tab_stocks, tab_options, tab_crypto, tab_macro, tab_prediction = st.tabs(
    ["Stocks & ETFs", "Options", "Crypto", "Macro", "Prediction Markets"]
)

with tab_stocks:
    st.markdown(
        """
| Source | Free Tier | Paid Tiers | Notes |
|--------|-----------|------------|-------|
| **yfinance** | Unlimited (unofficial) | — | No API key needed; breaks periodically, no SLA |
| **Polygon.io** ("Massive") | 5 calls/min, 2yr history | $29/mo (unlimited, 5yr, WebSockets) → $79/mo (10yr, trades) → $199/mo (20yr+, real-time) | Best tiered pricing |
| **Alpha Vantage** | 25 requests/day | From $49.99/mo | — |
| **Tiingo** | 50 symbols/hr, 30yr+ EOD | $10/mo expanded | Exceptional data quality |
| ~~IEX Cloud~~ | — | — | **Permanently shut down Aug 31, 2024** |
"""
    )

with tab_options:
    st.markdown(
        """
| Source | Free Tier | Paid Tiers | Notes |
|--------|-----------|------------|-------|
| **Thetadata** | 1yr EOD | $40/mo (4yr, real-time) → $80/mo (8yr, tick) → $160/mo (12yr, full depth) | Market disruptor |
| **ORATS** | — | $99/mo | 800+ proprietary indicators |
| **OptionMetrics** | — | $10,000+/yr | Institutional only |
"""
    )

with tab_crypto:
    st.markdown(
        """
| Source | Free Tier | Notes |
|--------|-----------|-------|
| **Binance / exchange APIs** | Free real-time + historical | Direct from exchanges |
| **CoinGecko** | 10,000 calls/mo, 13,000+ assets | — |
| **ccxt** (open source) | Unlimited | Unified Python interface to 100+ exchanges |
"""
    )

with tab_macro:
    st.markdown(
        """
| Source | Free Tier | Notes |
|--------|-----------|-------|
| **FRED** | 800,000+ series, 120 req/min | The gold standard for economic data |
| **World Bank** | Free | — |
| **BLS / Treasury.gov / IMF** | Free | — |
| **Trading Economics** | — | $49–$149/mo for compiled global data |
"""
    )

with tab_prediction:
    st.markdown(
        """
| Source | Trading Fees | API Access | Notes |
|--------|-------------|------------|-------|
| **Polymarket** | ~0% | REST + WebSocket, free | $9B cumulative 2024 volume |
| **Kalshi** | 0.7–3.5% per contract | REST + FIX protocol, free | US-regulated |
"""
    )

st.divider()

# --- Brokerages ---
st.markdown("## Brokerages for Algorithmic Trading")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
### Stocks & Options

| Broker | Commissions | Key Features |
|--------|------------|--------------|
| **Alpaca** | $0 stocks/ETFs/options; 0.25% crypto | API-first, no minimum, excellent Python SDK, free paper trading |
| **Interactive Brokers** | IBKR Lite: $0 / Pro: $0.0035/share | 170+ markets, 40+ countries, broadest access |
| **Charles Schwab** | Varies | New Trader API (replaced TD Ameritrade, shut down May 2024), still maturing |
| **Tradier** | $10/mo subscription → $0 commissions | Full API access |
| ~~Robinhood~~ | — | No public API — avoid for systematic trading |
"""
    )

with col2:
    st.markdown(
        """
### Crypto Exchanges

| Exchange | Maker/Taker Fees | Notes |
|----------|-----------------|-------|
| **Binance** | 0.10% / 0.10% | Largest global exchange |
| **Coinbase Advanced** | 0.40% / 0.60% | US-regulated |
| **Kraken** | 0.25% / 0.40% | Strong API |
"""
    )

st.divider()

# --- Python Stack ---
st.markdown("## The Essential Python Stack (All Free & Open Source)")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
### Data & Math
- **pandas** / **numpy** — data manipulation
- **scipy** / **statsmodels** — statistics, ARIMA, GARCH
- **scikit-learn** — machine learning
- **PyTorch** — deep learning
- **cvxpy** — portfolio optimization
- **QuantLib** — derivatives pricing
"""
    )

with col2:
    st.markdown(
        """
### Backtesting
- **vectorbt** — blazing-fast vectorized testing
- **backtrader** — event-driven simulation
- **zipline-reloaded** — Quantopian's legacy

### Visualization
- **plotly** — interactive charts
- **streamlit** — dashboards
"""
    )

with col3:
    st.markdown(
        """
### Data Access
- **yfinance** — Yahoo Finance
- **fredapi** — FRED economic data
- **ccxt** — 100+ crypto exchanges
- **alpaca-py** — Alpaca brokerage

### All of these are free, open-source, and pip-installable.
"""
    )

st.divider()

# --- Cloud Hosting ---
st.markdown("## Cloud Hosting: Starts at Zero")

st.markdown(
    """
| Provider | Free Tier | Paid | Best For |
|----------|-----------|------|----------|
| **Streamlit Community Cloud** | Free for public apps | — | Dashboard hosting (one-click GitHub deploy) |
| **AWS Free Tier** | t3.micro (1 vCPU, 1GB, 750 hr/mo) for 12 months | — | Basic trading bot |
| **Google Cloud** | Always-free e2-micro VM | — | Basic trading bot |
| **DigitalOcean** | — | From $6/mo | Persistent hosting |
| **Render** | — | From $7/mo | Easy deploy |
| **Railway** | — | ~$15–$40/mo | Small bot hosting |
| **Vercel** | Free tier | — | Frontend only (no persistent backend) |
"""
)

st.divider()

# --- Research Platforms ---
st.markdown("## Backtesting and Research Platforms")

col1, col2 = st.columns(2)
with col1:
    st.markdown(
        """
### QuantConnect
- Free tier: 8 hours backtesting/month
- Paid from $10/month
- 400TB+ historical data across all asset classes
- Underlying **LEAN engine** is fully open-source
"""
    )
with col2:
    st.markdown(
        """
### TradingView
- Pine Script for quick visual testing
- From $14.95/month
- Great for prototyping and visual analysis
"""
    )
