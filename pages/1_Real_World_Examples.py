import streamlit as st

st.set_page_config(page_title="Real-World Examples", page_icon="🏦", layout="wide")

st.markdown("# How Renaissance, Bridgewater, and AQR Actually Use the Math")
st.markdown(
    """
The gap between textbook quant finance and production trading systems is smaller
than most people think. Every major concept from probability theory through
stochastic calculus has a direct, measurable application in fund management today.
"""
)

st.divider()

# --- Probability & Bayesian Thinking ---
st.markdown("## Probability and Bayesian Thinking Generate Billions")

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown(
        """
Renaissance Technologies' Medallion Fund averaged **66.1% gross annual returns**
from 1988–2018, turning $100 into $398.7 million versus $1,815 for the S&P 500.
Robert Mercer's famous insight:

> "We're right 50.75% of the time, but we're 100% right 50.75% of the time."

This is pure probabilistic edge at massive scale — a casino model applied to
securities. Medallion uses **Hidden Markov Models** (inherited from speech
recognition research at IBM), mean reversion on correlated pairs, and non-linear
pattern detection across thousands of instruments. During the 2008 financial
crisis, the fund returned **74.6% net** while markets collapsed.
"""
    )
with col2:
    st.markdown("### Medallion Fund Performance")
    st.markdown(
        """
| Metric | Value |
|--------|-------|
| Avg Gross Return | 66.1%/yr |
| $100 → (1988–2018) | $398.7M |
| S&P 500 same period | $1,815 |
| 2008 Crisis Return | +74.6% net |
| Edge per trade | ~50.75% |
"""
    )

st.markdown(
    """
### The Kelly Criterion

The Kelly Criterion — **f\\* = (bp − q) / b** — governs position sizing at many
systematic funds. Ed Thorp pioneered its application from blackjack to markets.

In practice, most funds use **fractional Kelly** (half or quarter) because full
Kelly produces 50–70% drawdowns. A 55% win rate with 1.5:1 reward/risk yields a
Kelly allocation of 25%; professionals would trade at 6–12%.
"""
)

st.markdown(
    """
### Bayesian Updating in Real-Time

Bayesian updating is visible in real-time on prediction markets. When Fed Chair
Powell signaled a policy shift in late 2024, Polymarket's "December rate cut"
contract jumped from $0.65 to $0.78 within **8 seconds** — thousands of traders
simultaneously updating their probability estimates.

Polymarket crossed **$9 billion** in cumulative 2024 trading volume with 314,500
active traders in December, though only 0.51% of wallets realized profits
exceeding $1,000.
"""
)

st.divider()

# --- Factor Models ---
st.markdown("## Factor Models and Regression Drive Trillions in AUM")

st.markdown(
    """
The **Fama-French three-factor model** explains over **90% of diversified portfolio
return variation** versus 70% for CAPM alone. The five-factor extension (adding
profitability and investment factors) explains 71–94% of cross-sectional variance.

**Dimensional Fund Advisors**, where Fama and French serve as board consultants,
manages hundreds of billions using these models directly — constructing proprietary
indexes targeting size, value, and profitability premiums while acting as a patient
liquidity provider rather than tracking external benchmarks.
"""
)

col1, col2 = st.columns(2)
with col1:
    st.markdown(
        """
### AQR Capital Management ($153B AUM)

Extends factor investing across every asset class. Their landmark paper
*"Value and Momentum Everywhere"* documented consistent premiums across eight
markets and asset classes with negatively correlated returns — powerful
diversification. They buy stocks that score well on multiple factors
simultaneously (cheap AND trending upward AND high quality) rather than mixing
standalone factor portfolios.
"""
    )
with col2:
    st.markdown(
        """
### Bridgewater's All Weather Portfolio

Balances risk across four economic environments (rising/falling growth ×
rising/falling inflation) using **risk parity** — equalizing risk contributions
rather than capital allocations. A traditional 60/40 portfolio concentrates
roughly 90% of risk in equities.

In March 2025, State Street launched the ALLW ETF: ~79% global bonds, 43%
equities, 38% inflation-linked bonds, 37% commodities via derivatives.
"""
    )

st.divider()

# --- Linear Algebra ---
st.markdown("## Linear Algebra Is the Backbone of Fixed Income and Portfolio Construction")

st.markdown(
    """
### PCA on Yield Curves

Litterman and Scheinkman (1991) showed that **three principal components** explain
**99%+ of total variance** in bond returns:
"""
)

col1, col2, col3 = st.columns(3)
col1.metric("Level", "88.5%", "All rates moving together")
col2.metric("Slope", "8.5%", "Short vs. long rates diverging")
col3.metric("Curvature", "2.1%", "Middle maturities vs. extremes")

st.markdown(
    """
Every major fixed income desk uses PCA for P&L attribution, hedging, and
relative value analysis.

### Portfolio Optimization & Random Matrix Theory

For portfolio optimization, Markowitz mean-variance requires estimating the
covariance matrix — for 500 stocks, that means **125,250 unique parameters**.

Random Matrix Theory (Laloux et al.) revealed that **94% of the eigenvalue
spectrum** of an empirical S&P 500 correlation matrix is indistinguishable from
pure noise. The Marcenko-Pastur distribution identifies which eigenvalues carry
real signal. Denoising correlation matrices using this approach reduces portfolio
standard deviation by over **22%**.

*López de Prado's "Machine Learning for Asset Managers" is the standard reference.*
"""
)

st.divider()

# --- Stochastic Calculus ---
st.markdown("## Stochastic Calculus Powers Modern Options Markets")

st.markdown(
    """
**Black-Scholes (1973)** remains the common language but not the final word. Real
markets exhibit volatility smiles, fat tails, and stochastic volatility that the
model ignores.
"""
)

col1, col2 = st.columns(2)
with col1:
    st.markdown(
        """
### Heston Model (1993)
Captures volatility skew through correlated stochastic volatility with mean
reversion — widely used on equity derivatives desks.
"""
    )
with col2:
    st.markdown(
        """
### SABR Model
The market standard for interest rate derivatives, producing self-consistent
smiles across all strikes. In 2025, deep neural network calibration provides
arbitrage-free calibration for maturities up to 30 years.
"""
    )

st.markdown(
    """
Market-making firms like Citadel Securities, Optiver, and Jane Street continuously
construct **volatility surfaces** and hedge not just standard Greeks but
higher-order cross-sensitivities. ML-powered surface interpolators using Gaussian
Processes produce surfaces **25% smoother** than spline methods for illiquid strikes.
"""
)

st.divider()

# --- Macro, Crypto, Prediction Markets ---
st.markdown("## Extensions: Macro, Crypto, and Prediction Markets")

tab1, tab2, tab3 = st.tabs(["Managed Futures", "Crypto Quant", "AI/ML in 2024–2025"])

with tab1:
    st.markdown(
        """
**Managed futures** (CTAs) apply time-series momentum across bonds, FX, and
commodities — a **$340 billion AUM** industry.

The SG CTA Trend Index delivered **+27% in 2022** going long USD and commodities
while short global bonds, though it returned −11% YTD through May 2025 in
range-bound markets.

The core signal is simple (e.g., 20/120-day moving average crossover), with
position sizing via inverse volatility scaling.
"""
    )

with tab2:
    st.markdown(
        """
**Crypto quant strategies** exploit 24/7 markets, higher volatility, and
on-chain data.

A 2025 ML-driven multi-factor model for Ethereum combining technical indicators,
on-chain metrics, and social sentiment produced **97% annualized returns with a
Sharpe ratio of 2.5** in backtesting — though live simulated trading showed
+33% in a bull quarter and −10% in a bear quarter.
"""
    )

with tab3:
    st.markdown(
        """
**AI/ML** has moved from experimental to production:

- **LLMs** like FinBERT and FinLlama provide sentiment classification used
  directly as trading factors
- **Reinforcement learning** agents learn dynamic portfolio allocation policies
- An **NBER working paper (2025)** found that AI-powered speculators using RL
  can autonomously sustain collusive supra-competitive profits without
  communication or intent — raising novel regulatory concerns
"""
    )
