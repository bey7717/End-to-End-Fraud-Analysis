import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Fraud Seasonality Analysis")

@st.cache_data
def load_data():
    df = pd.read_csv("data/transactions.csv")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["week"] = df["timestamp"].dt.isocalendar().week
    return df

df = load_data()

weekly = df.groupby("week")["is_fraud"].mean() * 100

# -------- Executive Insight --------
st.success("""
Fraud activity spikes during late-year shopping periods and specific high-risk weeks.
""")

st.write("""
         Fraud rates vary significantly throughout the year, ranging from ~0.56% (Week 24) to ~6.17% (Week 43) — nearly an 11x difference.


* High-risk periods:
    * Weeks 43–52: Sustained elevated fraud rates (5.82%–6.17%), likely tied to holiday shopping and increased transaction volume.
    * Week 11: Early-year spike (~5.82%).


* Low-risk periods:
    * Week 24 shows the lowest fraud rate (~0.56%).
    * Weeks 1–2 and 16 remain below 1.2%.

Mid-year generally represents the lowest baseline fraud risk.
         """)
st.divider()

# -------- Visualization --------
fig, ax = plt.subplots(figsize=(3,3))
weekly.plot(ax=ax)

ax.set_ylabel("Fraud Rate (%)")
ax.set_xlabel("Week of Year")

st.pyplot(fig, use_container_width=False)
st.divider()


# -------- Business Interpretation --------
st.subheader("📘 Business Interpretation")

st.write("""
Fraud activity follows predictable seasonal patterns driven by transaction volume surges, promotional events, and increased digital payment usage during peak shopping periods. Static fraud detection thresholds may lead to under-detection during peak seasons and over-friction during low-risk periods.
""")
st.divider()

# -------- Recommended Actions --------
st.subheader("🚨 Recommended Actions")

st.write("""
* Implement seasonal fraud monitoring escalation plans during peak weeks.


* Deploy dynamic fraud scoring thresholds based on time-of-year risk levels.


* Align fraud investigation staffing and resources with historical seasonal peaks.


* Incorporate seasonality risk scoring into real-time transaction models. 
""")
