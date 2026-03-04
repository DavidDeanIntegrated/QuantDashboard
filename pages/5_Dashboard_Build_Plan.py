import streamlit as st

st.set_page_config(page_title="Dashboard Build Plan", page_icon="🔨", layout="wide")

st.markdown("# Building Your Dashboard With Claude Code")

st.divider()

# --- Why Streamlit ---
st.markdown("## Why Streamlit Wins for Beginners")

st.markdown(
    """
For someone with limited coding experience, **Streamlit is the unambiguous choice**:

- **Pure Python** — no HTML, CSS, JavaScript, or web development knowledge required
- A data scientist with zero web experience can go from Jupyter notebook to **live
  web app in under an hour**
- Apps are just Python scripts that run top-to-bottom
- Claude Code can generate complete Streamlit apps in single prompts since they're
  single-file Python programs
- Free deployment on Streamlit Community Cloud requires nothing more than a GitHub push

**When to graduate:**
- Move to **Dash (Plotly)** when you need more than 50 concurrent users
- Move to **Next.js + FastAPI** only if you're building a multi-user production platform
"""
)

st.divider()

# --- Claude Code Workflow ---
st.markdown("## The Claude Code Workflow")

st.markdown(
    """
Claude Code is Anthropic's terminal-native AI coding assistant — an agentic system
that reads your entire project, plans implementations, executes multi-file changes,
and runs tests. It holds **200,000 tokens of context** versus ~8,000 for Copilot.
"""
)

st.markdown("### The Four-Step Workflow")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("#### 1. Explore")
    st.markdown("Have Claude read relevant files")
with col2:
    st.markdown("#### 2. Plan")
    st.markdown('Use "think hard" for complex features')
with col3:
    st.markdown("#### 3. Code")
    st.markdown("Implement the solution")
with col4:
    st.markdown("#### 4. Commit")
    st.markdown("Explain what changed")

st.markdown(
    """
### Setting Up CLAUDE.md

Start by creating a `CLAUDE.md` file — Claude Code's project memory. Specify:

- Your **tech stack** (Streamlit, Plotly, Pandas, yfinance)
- **Coding standards** (type hints, docstrings, error handling for all API calls)
- Your **experience level** — tell Claude: *"I'm learning — explain every change you make."*

Use the prompts **"think"** / **"think hard"** / **"ultrathink"** for progressively
deeper reasoning on complex features.

*Claude Code requires a Claude Pro subscription ($20/month minimum).*
"""
)

st.divider()

# --- Project Structure ---
st.markdown("## Recommended Project Structure")

st.code(
    """
quant-dashboard/
├── CLAUDE.md              # Claude Code project memory
├── .env                   # API keys (never commit)
├── app.py                 # Main entry point
├── pages/                 # Streamlit multi-page app
│   ├── 1_Portfolio.py
│   ├── 2_Charts.py
│   ├── 3_Signals.py
│   ├── 4_Backtest.py
│   ├── 5_Risk.py
│   ├── 6_Macro.py
│   ├── 7_Crypto.py
│   └── 8_Options.py
├── src/                   # Core logic
│   ├── data/              # Market data, FRED, crypto wrappers
│   ├── analysis/          # Portfolio metrics, risk, signals, backtesting
│   ├── trading/           # Broker integration, orders, alerts
│   └── utils/             # Config, formatting, constants
└── tests/
""",
    language="text",
)

st.markdown(
    """
Each page should be thin — just Streamlit widgets calling functions from the logic
layer. Use `@st.cache_data` for all data-fetching functions. Store API keys in
`.env` files, never hardcoded.
"""
)

st.divider()

# --- Phased Build Plan ---
st.markdown("## Phased Build Plan")

st.markdown("### Phase 1 — Weeks 1–2: Foundation")
st.markdown(
    """
- Portfolio tracker with manual entry
- Candlestick charts via Plotly
- Basic metrics (returns, volatility)
- **Deploy to Streamlit Community Cloud**

*Claude Code can generate this in a single session.*
"""
)

st.markdown("### Phase 2 — Weeks 3–6: Analytics")
st.markdown(
    """
- Real-time data via Alpaca API
- Portfolio analytics (Sharpe, drawdown, correlation matrix using **quantstats**)
- Technical indicators (RSI, MACD via **pandas-ta**)
- Basic backtesting engine with **vectorbt**
"""
)

st.markdown("### Phase 3 — Weeks 7–12: Advanced Features")
st.markdown(
    """
- Options analytics (Black-Scholes via **py_vollib**, Greeks)
- Macro dashboard (yield curves from **FRED**)
- Crypto tracker (**ccxt**)
- Prediction market monitor (**Polymarket API**)
- VaR/CVaR risk metrics
- ML-based signals (**scikit-learn** Random Forest)
"""
)

st.markdown("### Phase 4 — Weeks 13+: Automation")
st.markdown(
    """
- Alpaca paper trading integration
- Telegram alert system
- Automated execution via **APScheduler**
- Performance attribution with **pyfolio**
"""
)

st.divider()

# --- Realistic Timelines ---
st.markdown("## Realistic Build Times With Claude Code")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("1 Week", "Working Dashboard", "Portfolio tracking + charts")
with col2:
    st.metric("1 Month", "Analytics Suite", "+ backtesting + macro data")
with col3:
    st.metric("3 Months", "Full Platform", "Multi-asset + paper trading + alerts")

st.caption("Without Claude Code, multiply these estimates by 2–3x.")

st.divider()

# --- Deployment ---
st.markdown("## Deployment Path")

st.markdown(
    """
1. **Start**: Streamlit Community Cloud (free, one-click from GitHub)
2. **Upgrade**: Railway or $6/month DigitalOcean droplet when you need persistent
   background jobs
3. **Live trading**: Docker on AWS/GCP free tier
"""
)
