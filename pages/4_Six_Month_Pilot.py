import streamlit as st

st.set_page_config(page_title="Six-Month Pilot", page_icon="🗓️", layout="wide")

st.markdown("# A Realistic Six-Month Pilot Starting From Scratch")

st.divider()

# --- Month 1 ---
st.markdown("## Month 1: Build Foundations at Zero Cost")

col1, col2 = st.columns([3, 1])
with col1:
    st.markdown(
        """
- Install **Python, VS Code, and Claude Code**
- Create free accounts on **Alpaca** (paper trading), **QuantConnect**,
  **TradingView**, and **Polygon** (free tier)
- Build your first data pipeline pulling S&P 500 prices with **yfinance**
- Implement three starter strategies on paper:
  1. **Buy-and-hold SPY** as your benchmark
  2. **50/200-day SMA crossover** (the "golden cross")
  3. **RSI mean reversion** (buy below 30, sell above 70)
- Read Ernest Chan's *Quantitative Trading* and Robert Carver's *Systematic Trading*
- **Start your GitHub repo** — this becomes your portfolio project
"""
    )
with col2:
    st.markdown("### Cost: $0")
    st.markdown("### Focus: Setup & Basics")

st.divider()

# --- Month 2 ---
st.markdown("## Month 2: Master Backtesting With Proper Methodology")

col1, col2 = st.columns([3, 1])
with col1:
    st.markdown(
        """
- Download **5+ years** of daily OHLCV data for S&P 500 constituents
- Build a data store (SQLite or CSV)
- Learn data cleaning: adjusting for splits, dividends, and **survivorship bias**
- Implement backtesting using **vectorbt** (fastest for parameter sweeps) or
  **backtrader** (more realistic event-driven simulation)

**Critical rule**: Always include commissions and slippage.

- Establish your validation framework:
  - **70/30** in-sample / out-of-sample split
  - Track **Sharpe ratio**, **max drawdown**, **profit factor**
  - Compare everything to **buy-and-hold SPY**
- Consider upgrading to Polygon Starter ($29/month) for better data
"""
    )
with col2:
    st.markdown("### Cost: $0–$29/mo")
    st.markdown("### Focus: Data & Validation")

st.divider()

# --- Month 3 ---
st.markdown("## Month 3: Develop and Stress-Test Strategies")

col1, col2 = st.columns([3, 1])
with col1:
    st.markdown(
        """
Test strategies in priority order:

1. **Simple Momentum** (SMA crossover) — Expected Sharpe 0.3–0.6 — Teaches
   trend-following
2. **Mean Reversion** (Bollinger Bands + RSI) — Expected Sharpe 0.4–0.8 — Teaches
   regime thinking
3. **Factor Investing** (rank by 12-month momentum + P/E, long top decile,
   rebalance monthly) — Introduces cross-sectional analysis
4. **Macro Trend Following** (MA rules on SPY, TLT, GLD, EEM with monthly
   rebalance) — Introduces multi-asset thinking

Keep parameters round (50-day, not 47-day) — **robustness matters more than
optimization**.
"""
    )
with col2:
    st.markdown("### Cost: $0–$29/mo")
    st.markdown("### Focus: Strategy Development")

st.divider()

# --- Month 4 ---
st.markdown("## Month 4: Go Live With Small Capital")

col1, col2 = st.columns([3, 1])
with col1:
    st.markdown(
        """
- Fund your Alpaca account with **$2,000–$5,000**
- Risk no more than **1–2% of capital per trade** ($50–$100 max loss on a
  $5,000 account)
- Limit to **2–3 concurrent positions**
- Use **limit orders** exclusively
- Set **hard stop-losses** on every position
"""
    )
    st.warning(
        "**Expect live results to be 20–40% worse than backtests** due to "
        "slippage, fill quality, and psychological pressure."
    )
    st.markdown(
        """
Track daily P&L against your paper trading results — the divergence teaches you
what backtests miss.
"""
    )
with col2:
    st.markdown("### Cost: ~$50–$65/mo")
    st.markdown("### Capital: $2K–$5K")
    st.markdown("### Focus: Live Execution")

st.divider()

# --- Month 5 ---
st.markdown("## Month 5: Expand Across Asset Classes")

col1, col2 = st.columns([3, 1])
with col1:
    st.markdown(
        """
- Add **crypto** (commission-free on Alpaca, 24/7 market, different dynamics)
- Start **options** with covered calls on existing positions
- Implement a **sector rotation** strategy using ETFs
- Run **2–3 uncorrelated strategies** simultaneously (momentum + mean reversion +
  trend following)
- Build **portfolio-level risk management**:
  - Correlation analysis
  - VIX-based regime filters
  - Aggregate risk tracking
"""
    )
with col2:
    st.markdown("### Cost: ~$50–$65/mo")
    st.markdown("### Focus: Multi-Asset")

st.divider()

# --- Month 6 ---
st.markdown("## Month 6: Evaluate Honestly and Decide")

col1, col2 = st.columns([3, 1])
with col1:
    st.markdown(
        """
Calculate every metric for each strategy:

- A strategy needs **100–200 trades minimum** for statistically meaningful
  metrics; ideally 300–500 across multiple market regimes
- **Walk-Forward Ratio** above 0.5 is acceptable; below 0.3 indicates overfitting

**Decision criteria:**
- If Sharpe exceeds 0.5 after costs
- Max drawdown is tolerable
- Live results are within 80% of backtest results

...then consider scaling up. If not, continue paper trading for another 3 months.
"""
    )
    st.info("**Most beginners lose money in year one. This is normal.**")
with col2:
    st.markdown("### Cost: ~$50–$65/mo")
    st.markdown("### Focus: Evaluation")
