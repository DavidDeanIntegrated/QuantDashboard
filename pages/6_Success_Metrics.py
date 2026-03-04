import streamlit as st

st.set_page_config(page_title="Success Metrics", page_icon="📈", layout="wide")

st.markdown("# When You Can Tell If You're Any Good")

st.divider()

# --- Skill vs Luck ---
st.markdown("## The Math of Distinguishing Skill From Luck")

st.markdown(
    """
The fundamental formula is:

### t-stat = Sharpe Ratio x sqrt(years)

Statistical significance at 95% confidence requires **t-stat > 2.0**.
"""
)

st.markdown(
    """
| Sharpe Ratio | Years Needed for 95% Confidence |
|:------------:|:-------------------------------:|
| 0.5 | ~16 years |
| 1.0 | ~4 years |
| 2.0 | ~1 year |
"""
)

st.markdown(
    """
Most retail strategies fall below Sharpe 1.0, meaning the required track record
extends painfully.

### The False Strategy Theorem

Lopez de Prado's **Deflated Sharpe Ratio** addresses a deeper problem: if you test
1,000 strategies and pick the best, the expected maximum Sharpe Ratio is **3.26
even if every strategy has zero true edge**.

Corrections for multiple testing (Bonferroni, FDR, Combinatorial Purged
Cross-Validation) are **not optional luxuries** — they're essential to avoid
self-deception.

Professional allocators typically require **3–5 years** of track record before
investing (66% of institutional investors per Preqin data). The industry standard
is 3 years of portable alpha plus $100M minimum AUM.
"""
)

st.divider()

# --- Benchmarks ---
st.markdown("## Benchmarks That Matter")

st.markdown(
    """
Your strategies should beat these baselines to demonstrate value:
"""
)

col1, col2 = st.columns(2)
with col1:
    st.markdown(
        """
### Broad Benchmarks

| Benchmark | Recent Performance | Long-Term |
|-----------|-------------------|-----------|
| **S&P 500** | +25.0% (2024), +17.9% (2025) | ~9.3%/yr average |
| **60/40 Portfolio** | ~16.8% (2024), ~15% (2025) | 8.18% CAGR (30yr), 34% max DD |
| **Risk-Free Rate** | 3-mo T-bills: ~4.2–4.3% | 10-yr Treasury: ~4.0–4.1% |
"""
    )
with col2:
    st.markdown(
        """
### Strategy-Specific Benchmarks

| Strategy Type | Benchmark |
|--------------|-----------|
| Momentum | MTUM ETF |
| Managed Futures | SG Trend Index |
| Options Selling | CBOE PutWrite Index |
"""
    )

st.divider()

# --- Return Expectations ---
st.markdown("## Honest Return Expectations by Year")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Year 1: Learning Curve")
    st.markdown("**Expected: -5% to -15%** (including infrastructure costs)")
    st.markdown(
        """
- 40% of day traders quit within one month
- Only 13% maintain profitability over 6 months
- **76% of retail traders are unprofitable** (ESMA data)
- Only 1–1.6% of day traders are consistently profitable net of fees
"""
    )

with col2:
    st.markdown("### Year 2: Stabilization")
    st.markdown("**Expected: -5% to +5%**")
    st.markdown(
        """
- You understand what *doesn't* work: overfitting, underestimated costs,
  regime changes
- Possibly approaching breakeven
"""
    )

with col3:
    st.markdown("### Year 3: Early Signal")
    st.markdown("**Expected: 0% to +10%**")
    st.markdown(
        """
- If you're still trading, you're in the **top percentile** of entrants
- Strategies may show consistent results
- Enough data to begin statistical validation
"""
    )

st.markdown(
    """
### Professional Fund Performance (2024)

| Fund / Benchmark | Returns |
|-----------------|---------|
| Professional quant funds (range) | 10–17% |
| QRT (Qube Research & Technologies) | 30% p.a. since 2017 |
| Top fund targets | Gross Sharpe 1.5–3.0, max DD 10–15% |

*They continuously rotate strategies — retirement based on drawdown thresholds
(-10% to -15%) rather than total return is more effective per Man AHL research.*
"""
)

st.divider()

# --- Eight Pitfalls ---
st.markdown("## The Eight Pitfalls That Destroy Quant Traders")

pitfalls = [
    (
        "Overfitting",
        "The #1 killer. If a strategy only works with RSI period 17 instead of "
        "round 15 or 20, it's fitting noise. Walk-Forward Ratio below 0.3 is a "
        "clear overfitting signal.",
    ),
    (
        "Survivorship Bias",
        "Backtesting only on currently existing stocks creates artificial positive "
        "bias. Include delisted stocks in your universe.",
    ),
    (
        "Look-Ahead Bias",
        "Using data not available at decision time is surprisingly easy to "
        "introduce. Always check that your signals use only past data.",
    ),
    (
        "Transaction Cost Underestimation",
        "Can slash real returns by 50%+ versus backtests. Always include "
        "commissions, spreads, slippage, and market impact.",
    ),
    (
        "Data Snooping",
        "Testing hundreds of ideas guarantees something will look great by pure "
        "chance. Record all trials and apply multiple testing corrections.",
    ),
    (
        "Regime Changes",
        "2022 broke stock-bond correlations; 2020 changed volatility regimes. "
        "Strategies that worked in one regime may fail in another.",
    ),
    (
        "Emotional Override",
        "The most common behavioral failure — overriding systematic rules based "
        "on gut feeling. Automate execution to eliminate it.",
    ),
    (
        "Insufficient Trade Count",
        "You need 100–200 trades minimum for statistically meaningful metrics; "
        "ideally 300–500 across multiple market regimes.",
    ),
]

for i, (title, desc) in enumerate(pitfalls, 1):
    with st.expander(f"**{i}. {title}**"):
        st.markdown(desc)

st.divider()

# --- Portfolio Project Value ---
st.markdown("## What Makes This a Great Portfolio Project")

st.markdown(
    """
**Employers value methodology over returns.** Showcase:

- Proper backtesting with out-of-sample validation
- Risk management awareness (drawdown analysis, position sizing, stop-losses)
- Statistical rigor (confidence intervals, significance tests, Walk-Forward ratios)
- Clean, documented code
- **Present losses and what you learned from them** — dishonesty is immediately
  disqualifying in quant interviews
- Compare results to relevant benchmarks, not just "made money"
- Show performance across different market conditions

Per analysis of 500+ quant job descriptions, **curiosity, demonstrated passion,
and work ethic** are the most underappreciated but highly valued traits.
"""
)
