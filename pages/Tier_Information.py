import streamlit as st 
import stripe
from st_paywall_mod.aggregate_auth import add_auth

st.set_page_config(page_title="Tier Information", page_icon="ℹ️")
st.title("ℹ️ Tier Information")
if st.session_state.language == "english":
    st.markdown("Warning: Before upgrading your tier, please *cancel* your subscription, either through your stripe account, or through the button at the bottom of the page.")

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
    st.markdown("""*Tutorials included:*
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
11. **Prompt for Stock Market Trend Analysis (Stocks):**
    - Using JobotGPT to create an analysis of stock price trends in the Thai stock market: identifying factors influencing trends and making long-term forecasts.
    - Using JobotGPT to create an analysis of stock price trends in the US stock market: analyzing the impacts of monetary policy and the economy.
    - Using JobotGPT to create an analysis of stock price trends in the Chinese stock market: considering political factors and international relations.
12. **Prompt for Analyzing Investment Opportunities in the Derivatives Market:**
    - Using JobotGPT to create an analysis of investment opportunities in the Thai derivatives market: conducting risk analysis and portfolio management.
    - Using JobotGPT to create an analysis of investment opportunities in other derivatives markets: analyzing market conditions and employing advanced trading strategies.
    - Using JobotGPT to create an analysis of investment opportunities in the capital market: considering asset allocation and risk hedging.
13. **Prompt for Analyzing Bond Prices and Debt Instruments:**
    - Using JobotGPT to create an analysis of bond prices in the debt market: yield analysis and risk assessment.
    - Using JobotGPT to create an analysis of debt instrument prices in the capital market: analyzing interest rate trends and inflation.
    - Using JobotGPT to create an analysis of bond prices in the money market: considering liquidity and market conditions.
14. **Prompt for Analyzing Trading Signals and Investment Planning in the Stock Market (Stocks):**
    - Using JobotGPT to create an analysis of trading signals in the Thai stock market: applying technical and fundamental analysis.
    - Using JobotGPT to create an analysis of trading signals in the US stock market: news analysis and key events.
    - Using JobotGPT to create an analysis of trading signals in the Chinese stock market: analyzing economic and political factors.
15. **Prompt for Analyzing Property and Real Estate Price Trends:**
    - Using JobotGPT to create an analysis of property price trends in the property market: analyzing risk factors and opportunities.
    - Using JobotGPT to create an analysis of real estate price trends in the property market: considering the impact of government policies and the economy.
    - Using JobotGPT to create an analysis of real estate price trends in the REITs market: return analysis and risk assessment.
16. **Analyzing Price Trends in the Stock Market (Stocks):**
    - Using JobotGPT to analyze price trends in the Thai stock market: stock price movements and influencing factors.
    - Using JobotGPT to analyze price trends in the US stock market: considering the impact of monetary policy and economic events.
    - Using JobotGPT to analyze price trends in the Chinese stock market: analyzing economic shifts and political factors.
17. **Analyzing Support and Resistance Levels:**
    - Using JobotGPT to analyze support and resistance levels in the European stock market: considering economic and political factors.
    - Using JobotGPT to analyze support and resistance levels in the Indian stock market: analyzing market impact factors.
    - Using JobotGPT to analyze support and resistance levels in the Vietnamese stock market: analyzing liquidity and stock price movements.
18. **Investment Decision-Making:**
    - Using JobotGPT to assist in investment decision-making in the Thai stock market: considering risk and return.
    - Using JobotGPT to assist in investment decision-making in the US stock market: analyzing economic trends and political factors.
    - Using JobotGPT to assist in investment decision-making in the Chinese stock market: considering changes in monetary policy and the economy.
19. **Analyzing FOREX Market Directions:**
    - Using JobotGPT to analyze FOREX market directions in the derivatives market: considering factors influencing currency values.
    - Using JobotGPT to analyze FOREX market directions in FX derivatives: analyzing currency trends and the impact of monetary policy.
    - Using JobotGPT to analyze FOREX market directions in the capital market: considering the impact of economic and political events.
20. **Analyzing Investment Opportunities in Commodities Markets:**
    - Using JobotGPT to analyze investment opportunities in the commodity market, such as gold and oil: considering price factors and market trends.
    - Using JobotGPT to analyze investment opportunities in the agricultural commodities market: analyzing the impact of weather and government policies.
    - Using JobotGPT to analyze investment opportunities in other commodities markets: considering market demand and price factors.
21. **Analyzing Trading Signals for Cryptocurrency:**
    - Using JobotGPT to analyze trading signals in the cryptocurrency market: analyzing price impact factors and market movements.
    - Using JobotGPT to create an analysis of trading signals in the cryptocurrency market: analyzing trends and volatility.
    - Using JobotGPT to analyze investment opportunities in the cryptocurrency market: considering risk and return.
22. **Analyzing Investment Opportunities in Options:**
    - Using JobotGPT to analyze investment opportunities in options within the derivatives market: analyzing risk and return.
    - Using JobotGPT to analyze investment opportunities in options within the cryptocurrency market: analyzing trends and volatility.
    - Using JobotGPT to analyze investment opportunities in options within the stock market: considering investment factors and price movements.
                """)

    st.markdown("## Tier 3: JobotGPT Elite (14,560 บาท / 2 ปี)")
    st.write("The ultimate package for professional traders and those aspiring to become experts in AI-driven trading. This tier provides access to the most advanced tools, strategies, and exclusive resources.")
    st.markdown("""*Tutorials included:*
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
else:
    st.markdown("คำเตือน:ก่อนที่จะอัปเกรดระดับของคุณ กรุณา**ยกเลิก**การสมัครสมาชิกของคุณ ไม่ว่าจะผ่านบัญชี Stripe ของคุณ หรือผ่านปุ่มที่ด้านล่างของหน้านี้")
    
    st.markdown("## Tier 1: JobotGPT Starter (4,560 บาท / 6 เดือน)")
    st.write("แพ็คเกจเริ่มต้นที่เหมาะสำหรับนักเทรดมือใหม่ที่เริ่มต้นเข้าสู่โลกของบอทเทรดและกลยุทธ์การเทรดด้วย AI โดยจะได้รับเครื่องมือและคู่มือพื้นฐานที่จำเป็นในการเริ่มต้น")
    st.markdown("""คู่มือที่รวมอยู่:
1. การแนะนำ JobotGPT และพื้นฐาน MT4/MT5
    - ภาพรวมของฟังก์ชันการใช้งาน JobotGPT
    - การตั้งค่าและการใช้งานแพลตฟอร์ม MT4 และ MT5
2. พื้นฐานการเทรด Forex
    - การทำความเข้าใจคู่สกุลเงิน, pips และ spreads
    - กลยุทธ์การเทรด Forex พื้นฐาน
3. การสร้าง EA ง่ายๆ ด้วย FXDreema
    - คู่มือการสร้าง Expert Advisor แรกของคุณโดยใช้ FXDreema
4. การพัฒนาอินดิเคเตอร์พื้นฐาน
    - การเขียนและใช้งานอินดิเคเตอร์พื้นฐานใน MQ4/MQ5
    - การแปลง Pine Script จาก TradingView เป็น MQ4/MQ5
5. พื้นฐานการทดสอบย้อนหลังและการปรับแต่ง
    - วิธีการทดสอบย้อนหลังกลยุทธ์ของคุณใน MT4/MT5
    - แนะนำเทคนิคการปรับแต่ง
6. การบริหารจัดการความเสี่ยงเบื้องต้น
    - หลักการพื้นฐานของการบริหารจัดการเงินและอัตราส่วนความเสี่ยงต่อผลตอบแทน
7. การเข้าถึงแคตตาล็อกบอทจาก AIGEN WorldBotRank
    - การเลือกและติดตั้งบอทจากแคตตาล็อก
8. เทคนิคการวิเคราะห์ตลาดเบื้องต้น
    - การวิเคราะห์ทางเทคนิคและพื้นฐานเบื้องต้น
    - การระบุระดับแนวรับและแนวต้าน""")
    
    st.markdown("## Tier 2: JobotGPT Pro (7,890 บาท / 1 ปี)")
    st.write("สำหรับนักเทรดระดับกลางที่ต้องการพัฒนาทักษะการเทรดและสำรวจกลยุทธ์และเครื่องมือขั้นสูงเพิ่มเติม แพ็คเกจนี้ให้คู่มือและทรัพยากรที่ครอบคลุมเพื่อช่วยให้คุณทำกำไรได้อย่างต่อเนื่อง")
    st.markdown("""คู่มือที่รวมอยู่:
1. คู่มือทั้งหมดของ JobotGPT Starter
2. การสร้าง EA ขั้นสูงด้วย FXDreema
    - การพัฒนา Expert Advisor ที่ซับซ้อนโดยใช้ฟีเจอร์ขั้นสูงของ FXDreema
3. การพัฒนาอินดิเคเตอร์อย่างครอบคลุม
    - การสร้างและปรับแต่งอินดิเคเตอร์สำหรับสถานการณ์การเทรดต่างๆ
    - การผสมผสานหลายอินดิเคเตอร์เข้าด้วยกันเป็นกลยุทธ์ที่ทรงพลัง
4. การทดสอบย้อนหลังและการทดสอบความเครียดขั้นสูง
    - วิธีการทดสอบย้อนหลังอย่างละเอียด
    - การทดสอบความเครียดเพื่อประเมินประสิทธิภาพ EA ในสภาวะตลาดที่แตกต่างกัน
5. การใช้ Machine Learning ในการเทรด
    - แนะนำแนวคิด Machine Learning และการประยุกต์ใช้ในการเทรด
    - การพัฒนารูปแบบ Machine Learning อย่างง่ายสำหรับสัญญาณการเทรด
6. เทคนิคการบริหารจัดการความเสี่ยงขั้นสูง
    - กลยุทธ์การบริหารจัดการเงินที่ซับซ้อน
    - การใช้งานการป้องกันความเสี่ยงและการลดความเสี่ยงด้วยการวิเคราะห์ความสัมพันธ์
7. การวิเคราะห์ตลาดและกลยุทธ์การเทรดขั้นสูง
    - เทคนิคการวิเคราะห์ทางเทคนิคขั้นสูง
    - การนำกลยุทธ์เช่นการ Scalping, Day Trading และ Swing Trading มาใช้
8. การสร้างบอทเทรดด้วย AI
    - การสร้างและจัดการบอทเทรดด้วย AI
    - แนะนำกลยุทธ์ Arbitrage, Grid, และ Martingale
9. การติดตั้ง EA บน VPS
    - คู่มือการตั้งค่าและจัดการ VPS สำหรับการเทรด
10. การเข้าถึงบอทพิเศษจาก AIGEN WorldBotRank
    - บอทที่คัดสรรมาเป็นพิเศษสำหรับผู้ใช้ระดับ Pro
11. Prompt สำหรับวิเคราะห์แนวโน้มตลาดหุ้น (Stocks):
    - การใช้ JobotGPT เพื่อสร้างการวิเคราะห์แนวโน้มราคาหุ้นในตลาดหุ้นไทย: การระบุปัจจัยที่มีผลต่อแนวโน้มและการคาดการณ์ระยะยาว
    - การใช้ JobotGPT เพื่อสร้างการวิเคราะห์แนวโน้มราคาหุ้นในตลาดหุ้นอเมริกา: การวิเคราะห์ผลกระทบจากนโยบายการเงิน (Monetary Policy) และเศรษฐกิจ (Economy)
    - การใช้ JobotGPT เพื่อสร้างการวิเคราะห์แนวโน้มราคาหุ้นในตลาดหุ้นจีน: การพิจารณาปัจจัยทางการเมือง (Political Factors) และความสัมพันธ์ระหว่างประเทศ (International Relations)
12. Prompt สำหรับวิเคราะห์โอกาสการลงทุนในตลาดอนุพันธ์ (Derivatives):
    - การใช้ JobotGPT เพื่อสร้างการวิเคราะห์โอกาสการลงทุนในตลาดอนุพันธ์ในประเทศไทย: การวิเคราะห์ความเสี่ยง (Risk Analysis) และการจัดการพอร์ต (Portfolio Management)
    - การใช้ JobotGPT เพื่อสร้างการวิเคราะห์โอกาสการลงทุนในตลาดอนุพันธ์อีกซ์: การวิเคราะห์สภาวะตลาด (Market Conditions) และการใช้กลยุทธ์การเทรดขั้นสูง (Advanced Trading Strategies)
    - การใช้ JobotGPT เพื่อสร้างการวิเคราะห์โอกาสการลงทุนในตลาดเงินทุน: การพิจารณาการจัดสรรสินทรัพย์ (Asset Allocation) และการป้องกันความเสี่ยง (Risk Hedging)
13. Prompt สำหรับการวิเคราะห์ราคาพันธบัตรและตราสารหนี้ (Bonds):
    - การใช้ JobotGPT เพื่อสร้างการวิเคราะห์ราคาพันธบัตรในตลาดหนี้สิน (Debt Market): การวิเคราะห์ผลตอบแทน (Yield Analysis) และความเสี่ยง (Risk)
    - การใช้ JobotGPT เพื่อสร้างการวิเคราะห์ราคาตราสารหนี้ในตลาดเงินทุน: การวิเคราะห์แนวโน้มดอกเบี้ย (Interest Rate Trends) และอัตราเงินเฟ้อ (Inflation)
    - การใช้ JobotGPT เพื่อสร้างการวิเคราะห์ราคาพันธบัตรในตลาดเงินประจำวัน (Money Market): การพิจารณาสภาพคล่อง (Liquidity) และสภาวะตลาด (Market Conditions)
14. Prompt สำหรับวิเคราะห์สัญญาณการเทรดและการวางแผนการลงทุนในตลาดหุ้น (Stocks):
    - การใช้ JobotGPT เพื่อสร้างการวิเคราะห์สัญญาณการเทรดในตลาดหุ้นไทย: การใช้เทคนิคการวิเคราะห์ทางเทคนิค (Technical Analysis) และพื้นฐาน (Fundamental Analysis)
    - การใช้ JobotGPT เพื่อสร้างการวิเคราะห์สัญญาณการเทรดในตลาดหุ้นอเมริกา: การวิเคราะห์ข่าวสาร (News Analysis) และเหตุการณ์สำคัญ (Key Events)
    - การใช้ JobotGPT เพื่อสร้างการวิเคราะห์สัญญาณการเทรดในตลาดหุ้นจีน: การวิเคราะห์ปัจจัยทางเศรษฐกิจ (Economic Factors) และการเมือง (Political Factors)
15. Prompt สำหรับการวิเคราะห์แนวโน้มราคาทรัพย์สินและอสังหาริมทรัพย์ (Real Estate):
    - การใช้ JobotGPT เพื่อสร้างการวิเคราะห์แนวโน้มราคาทรัพย์สินในตลาดทรัพย์สิน (Property Market): การวิเคราะห์ปัจจัยเสี่ยง (Risk Factors) และโอกาส (Opportunities)
    - การใช้ JobotGPT เพื่อสร้างการวิเคราะห์แนวโน้มราคาอสังหาริมทรัพย์ในตลาดทรัพย์สิน (Real Estate Market): การพิจารณาผลกระทบจากนโยบายรัฐบาล (Government Policies) และเศรษฐกิจ (Economy)
    - การใช้ JobotGPT เพื่อสร้างการวิเคราะห์แนวโน้มราคาอสังหาริมทรัพย์ในตลาดอสังหาริมทรัพย์ (REITs): การวิเคราะห์ผลตอบแทน (Return Analysis) และความเสี่ยง (Risk)
16. วิเคราะห์แนวโน้มราคาในตลาดหุ้น (Stocks):
    - การใช้ JobotGPT เพื่อวิเคราะห์แนวโน้มราคาในตลาดหุ้นไทย: การวิเคราะห์การเคลื่อนไหวของราคาหุ้น (Stock Price Movements) และปัจจัยที่มีผล (Impact Factors)
    - การใช้ JobotGPT เพื่อวิเคราะห์แนวโน้มราคาในตลาดหุ้นอเมริกา: การพิจารณาผลกระทบจากนโยบายการเงิน (Monetary Policy) และเหตุการณ์ทางเศรษฐกิจ (Economic Events)
    - การใช้ JobotGPT เพื่อวิเคราะห์แนวโน้มราคาในตลาดหุ้นจีน: การวิเคราะห์การเปลี่ยนแปลงของเศรษฐกิจ (Economic Shifts) และปัจจัยทางการเมือง (Political Factors)
17. วิเคราะห์ระดับสนับสนุนและความต้านทางราคา (Support and Resistance Levels):
    - การใช้ JobotGPT เพื่อวิเคราะห์ระดับสนับสนุนและความต้านทางราคาในตลาดหุ้นยุโรป (European Stocks): การพิจารณาปัจจัยทางเศรษฐกิจ (Economic Factors) และการเมือง (Political Factors)
    - การใช้ JobotGPT เพื่อวิเคราะห์ระดับสนับสนุนและความต้านทางราคาในตลาดหุ้นอินเดีย (Indian Stocks): การวิเคราะห์ปัจจัยที่มีผลต่อแนวโน้มตลาด (Market Impact Factors)
    - การใช้ JobotGPT เพื่อวิเคราะห์ระดับสนับสนุนและความต้านทางราคาในตลาดหุ้นเวียดนาม (Vietnamese Stocks): การวิเคราะห์สภาพคล่อง (Liquidity) และการเคลื่อนไหวของราคาหุ้น (Price Movements)
18. การตัดสินใจการลงทุน (Investment Decision-Making):
    - การใช้ JobotGPT เพื่อช่วยในการตัดสินใจการลงทุนในตลาดหุ้นไทย (Thai Stocks): การพิจารณาความเสี่ยง (Risk) และผลตอบแทน (Return)
    - การใช้ JobotGPT เพื่อช่วยในการตัดสินใจการลงทุนในตลาดหุ้นอเมริกา (US Stocks): การวิเคราะห์แนวโน้มทางเศรษฐกิจ (Economic Trends) และการเมือง (Political Factors)
    - การใช้ JobotGPT เพื่อช่วยในการตัดสินใจการลงทุนในตลาดหุ้นจีน (Chinese Stocks): การพิจารณาการเปลี่ยนแปลงของนโยบายการเงิน (Monetary Policy) และเศรษฐกิจ (Economy)
19. การวิเคราะห์ทิศทางของตลาดฟอเร็กซ์ (FOREX):
    - การใช้ JobotGPT เพื่อวิเคราะห์ทิศทางของตลาดฟอเร็กซ์ในตลาดอนุพันธ์ (FOREX Derivatives): การพิจารณาปัจจัยที่มีผลต่อค่าเงิน (Currency Factors)
    - การใช้ JobotGPT เพื่อวิเคราะห์ทิศทางของตลาดฟอเร็กซ์ในตลาดอนุพันธ์อีกซ์ (FX Derivatives): การวิเคราะห์แนวโน้มค่าเงิน (Currency Trends) และผลกระทบจากนโยบายการเงิน (Monetary Policy)
    - การใช้ JobotGPT เพื่อวิเคราะห์ทิศทางของตลาดฟอเร็กซ์ในตลาดเงินทุน (Capital Market): การพิจารณาผลกระทบจากเหตุการณ์ทางเศรษฐกิจ (Economic Events) และการเมือง (Political Events)
20. การวิเคราะห์โอกาสการลงทุนในตลาดสินค้า (Commodities):
    - การใช้ JobotGPT เพื่อวิเคราะห์โอกาสการลงทุนในตลาดสินค้าโภคพันธ์ (Commodity Market) เช่น ทองคำ (Gold) และน้ำมัน (Oil): การพิจารณาปัจจัยที่มีผลต่อราคา (Price Factors) และแนวโน้มตลาด (Market Trends)
    - การใช้ JobotGPT เพื่อวิเคราะห์โอกาสการลงทุนในตลาดสินค้าเกษตร (Agricultural Commodities): การวิเคราะห์ผลกระทบจากสภาพอากาศ (Weather Impact) และนโยบายรัฐบาล (Government Policies)
    - การใช้ JobotGPT เพื่อวิเคราะห์โอกาสการลงทุนในตลาดสินค้าอื่นๆ (Other Commodities): การพิจารณาความต้องการในตลาด (Market Demand) และปัจจัยที่มีผลต่อราคา (Price Factors)
21. การวิเคราะห์สัญญาณการเทรด cryptocurrency (Cryptocurrency):
    - การใช้ JobotGPT เพื่อวิเคราะห์สัญญาณการเทรดในตลาด cryptocurrency: การวิเคราะห์ปัจจัยที่มีผลต่อราคา (Price Impact Factors) และการเคลื่อนไหวของตลาด (Market Movements)
    - การใช้ JobotGPT เพื่อสร้างการวิเคราะห์สัญญาณการเทรดในตลาด cryptocurrency: การวิเคราะห์แนวโน้ม (Trends) และความผันผวน (Volatility)
    - การใช้ JobotGPT เพื่อวิเคราะห์โอกาสการลงทุนในตลาด cryptocurrency: การพิจารณาความเสี่ยง (Risk)
22. การวิเคราะห์โอกาสการลงทุนในตัวเลือก (Options):
    - การใช้ JobotGPT เพื่อวิเคราะห์โอกาสการลงทุนในตัวเลือก (Options) ในตลาดอนุพันธ์ (Derivatives): การวิเคราะห์ความเสี่ยง (Risk) และผลตอบแทน (Return)
    - การใช้ JobotGPT เพื่อวิเคราะห์โอกาสการลงทุนในตัวเลือก (Options) ในตลาด cryptocurrency: การวิเคราะห์แนวโน้ม (Trends) และความผันผวน (Volatility)
    - การใช้ JobotGPT เพื่อวิเคราะห์โอกาสการลงทุนในตัวเลือก (Options) ในตลาดหุ้น (Stocks): การพิจารณาปัจจัยที่มีผลต่อการลงทุน (Investment Factors) และการเคลื่อนไหวของราคา (Price Movements)""")
    
    st.markdown("## Tier 3: JobotGPT Elite (14,560 บาท / 2 ปี)")
    st.write("แพ็คเกจสูงสุดสำหรับนักเทรดมืออาชีพและผู้ที่ต้องการเป็นผู้เชี่ยวชาญด้านการเทรดด้วย AI แพ็คเกจนี้ให้การเข้าถึงเครื่องมือ กลยุทธ์ และทรัพยากรพิเศษที่สุด")
    st.markdown("""คู่มือที่รวมอยู่:
1. คู่มือทั้งหมดของ JobotGPT Pro
2. การพัฒนา EA และอินดิเคเตอร์ระดับมืออาชีพ
    - การสร้าง Expert Advisor และอินดิเคเตอร์ที่ซับซ้อนอย่างมาก
    - การรวมโมเดล AI และ Machine Learning กับ EA ของคุณ
3. กลยุทธ์การเทรดด้วยอัลกอริทึม
    - การพัฒนาและใช้งานกลยุทธ์การเทรดด้วยอัลกอริทึมขั้นสูง
    - การใช้ Markov Chains และแบบจำลองทางคณิตศาสตร์ขั้นสูง
4. การวิเคราะห์ตลาดและกลยุทธ์การเทรดเชิงลึก
    - ทฤษฎี Elliott Wave
    - กลยุทธ์ SMC (Smart Money Concepts) และ ICT (Inner Circle Trader)
    - กลยุทธ์การเทรด Order Block
5. การบริหารจัดการความเสี่ยงและเงินทุนอย่างครอบคลุม
    - เทคนิคการป้องกันความเสี่ยงขั้นสูง
    - ระบบการบริหารจัดการความเสี่ยง/ผลตอบแทนที่ซับซ้อน
6. การสร้างและจัดการฟาร์ม EA
    - การสร้างและดูแลรักษา EA หลายตัวสำหรับการเทรดที่หลากหลาย
    - การปรับแต่งและการทดสอบความเครียดของฟาร์ม EA
7. บอทเทรดด้วย AI ขั้นสูงสุด
    - การพัฒนาและใช้งานบอทเทรดด้วย AI ขั้นสูง
    - กลยุทธ์ Arbitrage, Correlations และ Hedging ขั้นสูง
8. การวิเคราะห์งบการเงินและการเลือกหุ้น
    - การวิเคราะห์งบการเงินสำหรับการเลือกหุ้น
    - การหาหุ้นกลับตัวและการใช้งาน DCA (Dollar Cost Averaging)
9. การเข้าถึงบอทและกลยุทธ์พรีเมียม
    - บอทชั้นนำจากแคตตาล็อก AIGEN WorldBotRank
    - การพัฒนาบอทและกลยุทธ์เฉพาะบุคคล
10. การสนับสนุนและอัปเดตอย่างต่อเนื่อง
    - การอัปเดตคู่มือและทรัพยากรอย่างต่อเนื่อง
    - การสนับสนุนแบบ Priority และการฝึกอบรมแบบตัวต่อตัว""")
    
add_auth(required=True)

if st.session_state.user_subscribed == True:
    if st.button("Cancel subscription", type="primary"):
        if st.secrets.testing_mode == True:
            stripe.api_key = st.secrets.stripe_api_key_test
        else:
            stripe.api_key = st.secrets.stripe_api_key
        stripe.Subscription.cancel(st.session_state.subscriptions.data[0].id)