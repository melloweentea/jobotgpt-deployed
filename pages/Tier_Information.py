import streamlit as st 
from st_paywall_mod.aggregate_auth import add_auth

st.set_page_config(page_title="Tier Information", page_icon="ℹ️")
st.title("ℹ️ Tier Information")
st.markdown("Warning: Before upgrading your tier, please -cancel- your subscription, either through your stripe account, or through the button on the left sidebar.")

st.markdown("## Tier 1: JobotGPT Starter (4,560 บาท / 6 เดือน)")
st.write("The perfect entry-level subscription for beginner traders who are just starting to explore the world of AI-driven trading bots and strategies. This tier provides essential tools and tutorials to get you started on the right path.")
st.markdown("""**Tutorials Included:**
1) Introduction to JobotGPT and MT4/MT5 Basics
    - Overview of JobotGPT functionalities.
    - Setting up and navigating MT4 and MT5 platforms.
2) Fundamentals of Forex Trading
    - Understanding currency pairs, pips, and spreads.
    - Basic Forex trading strategies.
3) Creating Simple EAs with FXDreema
    - Step-by-step guide to creating your first Expert Advisor using FXDreema.
4) Basic Indicator Development
    - Writing and implementing simple indicators in MQ4/MQ5.
    - Converting Pine Script indicators to MQ4/MQ5.
5) Backtesting and Optimization Essentials
    - How to backtest your strategies in MT4/MT5.
    - Introduction to optimization techniques.
6) Introduction to Risk Management
    - Basic principles of money management and risk/reward ratios.
7) Access to AIGEN WorldBotRank Bots Catalog
    - Choosing and installing bots from the catalog.
8) Basic Market Analysis Techniques
    - Technical and fundamental analysis basics.
    - Identifying support and resistance levels.
""")

st.markdown("## Tier 2: JobotGPT Pro (7,890 บาท / 1 ปี)")
st.write("For intermediate traders who want to enhance their trading skills and explore more advanced strategies and tools. This tier offers comprehensive tutorials and resources to help you achieve consistent profitability.")
st.markdown("""**Tutorials included:**
1. All JobotGPT Starter Tutorials
2. Advanced EA Creation with FXDreema
    - Developing complex Expert Advisors using advanced FXDreema features.
3. Comprehensive Indicator Development
    - Creating and optimizing custom indicators for various trading scenarios.
    - Combining multiple indicators into powerful strategies.
4. Advanced Backtesting and Stress Testing
    - In-depth backtesting methods.
    - Conducting stress tests to evaluate EA performance under different market conditions.
5. Machine Learning for Trading
    - Introduction to machine learning concepts and their application in trading.
    - Developing simple machine learning models for trading signals.
6. Advanced Risk Management Techniques
    - Sophisticated money management strategies.
    - Implementing hedging and correlation-based risk mitigation.
7. Market Analysis and Trading Strategies
    - Advanced technical analysis techniques.
    - Implementing strategies like scalping, day trading, and swing trading.
8. AI-Driven Trading Bots
    - Creating and managing AI trading bots.
    - Introduction to arbitrage, grid, and martingale strategies.
9. Installing EAs on VPS
    - Step-by-step guide to setting up and managing a VPS for trading.
10. Access to Exclusive Bots from AIGEN WorldBotRank
    - Specially curated bots for Pro users.
            """)

st.markdown("## Tier 3: JobotGPT Elite (14,560 บาท / 2 ปี)")
st.write("The ultimate package for professional traders and those aspiring to become experts in AI-driven trading. This tier provides access to the most advanced tools, strategies, and exclusive resources.")
st.markdown("""**Tutorials included:**
1. All JobotGPT Pro Tutorials
2. Expert-Level EA and Indicator Development
    - Creating highly sophisticated Expert Advisors and indicators.
    - Integrating AI and machine learning models with your EAs.
3. Algorithmic Trading Strategies
    - Developing and implementing advanced algorithmic trading strategies.
    - Using Markov chains and other advanced mathematical models.
4. In-Depth Market Analysis and Trading Insights
    - Elliott wave theory.
    - Smart money concepts (SMC) and ICT (Inner Circle Trader) strategies.
    - Order block trading strategies.
5. Comprehensive Risk and Money Management
    - Advanced hedging techniques.
    - Complex risk/reward management systems.
6. Building and Managing EA Farms
    - Creating and maintaining multiple EAs for diversified trading.
    - Optimization and stress testing of EA farms.
7. Cutting-Edge AI Trading Bots
    - Developing and deploying state-of-the-art AI trading bots.
    - Advanced arbitrage, correlations, and hedging strategies.
8. Financial Statement Analysis and Stock Selection
    - Analyzing financial statements for stock selection.
    - Finding reversal stocks and implementing DCA (Dollar Cost Averaging).
9. Exclusive Access to Premium Bots and Strategies
    - Top-tier bots from the AIGEN WorldBotRank catalog.
    - Personalized bot and strategy development sessions.
10. Ongoing Support and Updates
    - Continuous updates to tutorials and resources.
    - Priority support and one-on-one coaching sessions.""")

add_auth(required=True)