import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Payment Method Analysis")

@st.cache_data
def load_data():
    df = pd.read_csv("data/transactions.csv")
    return df

df = load_data()

fraud_counts = df.groupby('payment_method')['is_fraud'].mean()

# -------- Executive Insight --------
st.success("""
Comparable transaction volumes across payment methods strengthen the reliability of these comparisons.
""")

st.write("""
Wallet payments have the highest fraud rate (3.68%) and highest total fraud volume.

ACH payments show moderate fraud exposure (3.11%).
         
Card payments demonstrate the lowest fraud rate (2.51%) despite the highest transaction volume.

Comparable transaction volumes across payment methods strengthen the reliability of these comparisons.

         """)
st.divider()


# -------- Visualization --------
fig, ax = plt.subplots(figsize=(3,3))
fig.savefig("payment_method_image.png")


ax.bar(fraud_counts.index, fraud_counts.values)

ax.set_title("Title")
ax.set_ylabel("Count")
ax.set_title("Fraud Counts")

st.pyplot(fig, use_container_width=False)

vol = df['payment_method'].value_counts()
st.write(vol)
st.divider()


# -------- Business Interpretation --------
st.subheader("📘 Business Interpretation")

st.write("""
Digital wallets may introduce additional vulnerabilities such as credential compromise, device spoofing, or reduced authentication friction. Traditional card payments likely benefit from mature fraud prevention infrastructure including chargeback systems, network-level monitoring, and authentication layers.
""")
st.divider()


# -------- Recommended Actions --------
st.subheader("🚨 Recommended Actions")

st.write("""
* Implement enhanced monitoring for wallet transactions:
    * Velocity checks
    * Device fingerprinting
    * Transaction limits


* Conduct root-cause analysis of wallet fraud by merchant, device, and geographic segmentation.
* Benchmark and adapt card-based security controls across other payment methods.
* Introduce risk-based pricing or transaction limits by payment type.
* Educate customers on wallet-specific fraud risks and protection practices.
  
""")
