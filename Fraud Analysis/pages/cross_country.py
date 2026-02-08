import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Payment Method Analysis")

@st.cache_data
def load_data():
    df = pd.read_csv("data/combined_data")
    return df

df = load_data()

# -------- Executive Insight --------
st.success("""
Cross-country transactions account for:


14% of total volume


43.7% of total fraud


Fraud rate for cross-country transactions is 9.45%, compared to 2.03% for domestic transactions.


Cross-country transactions are approximately 4.6x more likely to be fraudulent.
""")


st.divider()


# -------- Visualization --------

cols_to_strip = ['transaction_country', 'payment_method']


col1, col2 = st.columns(2)

# Apply strip only to selected columns
for col in cols_to_strip:
    if col in df.columns and pd.api.types.is_string_dtype(df[col]):
        df[col] = df[col].str.strip()

with col1:
    fig, ax = plt.subplots(figsize=(4,4))

    fraud_rate_same_country = df.groupby('transaction_country')['is_fraud'].mean() * 100
    fraud_rate_same_country = fraud_rate_same_country.sort_values(ascending=False)
    ax.bar(fraud_rate_same_country.index, fraud_rate_same_country.values)
    ax.set_ylabel("Fraud rate")
    ax.set_title("Fraud Rate by Country")
    st.pyplot(fig, use_container_width=False)


with col2:
    fig, ax = plt.subplots(figsize=(4,4))
    fraud_rate_different_country = df.groupby('cross_country')['is_fraud'].mean() * 100
    fraud_rate_different_country = fraud_rate_different_country.sort_values(ascending=False)
    
    fraud_rate_different_country.index = fraud_rate_different_country.index.map({
    True: "Cross Country",
    False: "Domestic"
})

    ax.bar(fraud_rate_different_country.index.astype(str), fraud_rate_different_country.values)
    ax.set_ylabel("Fraud Rate (%)")
    ax.set_title("Fraud Rate by Cross Country")
    st.pyplot(fig, use_container_width=False)



cross_country_df = df[df['cross_country'] == True]
fraud_by_country = (
    cross_country_df.groupby('transaction_country')['is_fraud']
    .mean()
    .sort_values(ascending=False) * 100
)

fig, ax = plt.subplots()

ax.bar(fraud_by_country.index, fraud_by_country.values)
ax.set_ylabel("Fraud Rate (%)")
ax.set_title("Fraud Rate in Cross-Country Transactions by Transaction Country")
plt.xticks(rotation=45)

st.pyplot(fig, use_container_width=False)

st.divider()


# -------- Business Interpretation --------
st.subheader("📘 Business Interpretation")

st.write("""
Cross-border activity introduces increased fraud exposure due to identity verification challenges, regulatory differences, geographic spoofing, and international fraud rings. These transactions represent a highly concentrated fraud risk segment.
""")
st.divider()


# -------- Recommended Actions --------
st.subheader("🚨 Recommended Actions")

st.write("""
* Introduce step-up authentication (2FA, OTP, or KYC refresh) for cross-country transactions.


* Apply stricter transaction limits and velocity controls for cross-border activity.


* Deploy geolocation verification to detect location mismatches.


* Lower fraud scoring thresholds for cross-country transaction approval.


* Introduce real-time monitoring alerts for high-risk geographic corridors.
  
""")
