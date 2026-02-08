import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Fraud By Transaction Amount")

@st.cache_data
def load_data():
    df = pd.read_csv("data/transactions.csv")
    return df

df = load_data()

# -------- Executive Insight --------
st.success("""
Fraud activity spikes during late-year shopping periods and specific high-risk weeks.
""")


price_range = {
    "Price Range": [
        "$301 - $1000",
        "$51 - $100",
        "$0 - $50",
        "$101 - $300",
        "Unknown",
    ],
    "Fraud Rates": [
        "3.414",
        "3.369",
        "3.192",
        "2.726",
        "2.439",
    ]
}

df_price = pd.DataFrame(price_range)

df_price["Fraud Rates (%)"] = df_price["Fraud Rates"].astype(float)

price_order = ["$0 - $50", "$51 - $100", "$101 - $300", "$301 - $1000", "Unknown"]
df_price["Price Range"] = pd.Categorical(df_price["Price Range"], categories=price_order, ordered=True)
df_price = df_price.sort_values("Price Range")

st.subheader("Fraud Rates by Price Range")
st.table(df_price)

st.write("""
* Transactions above $300 represent the highest fraud exposure.


* The $101–$300 range shows unexpectedly lower fraud rates, indicating potentially effective current controls.

         """)
st.divider()

# -------- Visualization --------



st.write("The following code shown was used for this calculation")

sql_code_transaction_amount = """
SELECT 
    CASE 
        WHEN amount BETWEEN 0 AND 50 THEN '$0 - $50'
        WHEN amount BETWEEN 51 AND 100 THEN '$51 - $100'
        WHEN amount BETWEEN 101 AND 300 THEN '$101 - $300'
        WHEN amount BETWEEN 301 AND 1000 THEN '$301 - $1000'
        WHEN amount > 1000 THEN '$1000+'
        ELSE 'Unknown' 
    END AS price_range,
    AVG(CAST(is_fraud as FLOAT) * 100) as fraud_rates
FROM transactions
GROUP BY price_range 
ORDER BY fraud_rates DESC   
"""


st.code(sql_code_transaction_amount, language="sql", line_numbers=True)

st.divider()

# -------- Business Interpretation --------
st.subheader("📘 Business Interpretation")

st.write("""
Fraudsters appear to target transaction sizes that balance payout potential with lower scrutiny. The lower fraud rate in the mid-tier range may reflect successful fraud controls or behavioral deterrence.
""")

st.divider()
# -------- Recommended Actions --------
st.subheader("🚨 Recommended Actions")

st.write("""
* Introduce tiered fraud control strategies:

    * Tier 1 ($0–$100): Standard automated verification


    * Tier 2 ($101–$300): Maintain current controls


    * Tier 3 ($301+): Mandatory step-up authentication and enhanced monitoring


* Implement manual review triggers when high-value transactions intersect with other risk signals.


* Investigate and resolve data issues driving "Unknown" transaction categories.


* Allocate fraud prevention resources proportionally across transaction tiers.

""")
