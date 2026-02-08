import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Fraud By Transaction Amount")

@st.cache_data
def load_data():
    df = pd.read_csv("data/combined_data")
    return df

df = load_data()

# -------- Executive Insight --------
st.success("""
* user_812 recorded the highest fraud count with 4 incidents.

* Three users recorded 3 fraud incidents each.


* 23 users recorded two fraud attempts each.


* Repeat offenders represent early indicators of potential fraud rings or compromised accounts.
""")


# price_range = {
#     "Price Range": [
#         "$301 - $1000",
#         "$51 - $100",
#         "$0 - $50",
#         "$101 - $300",
#         "Unknown",
#     ],
#     "Fraud Rates": [
#         "3.414",
#         "3.369",
#         "3.192",
#         "2.726",
#         "2.439",
#     ]
# }

# df_price = pd.DataFrame(price_range)

# df_price["Fraud Rates (%)"] = df_price["Fraud Rates"].astype(float)

# price_order = ["$0 - $50", "$51 - $100", "$101 - $300", "$301 - $1000", "Unknown"]
# df_price["Price Range"] = pd.Categorical(df_price["Price Range"], categories=price_order, ordered=True)
# df_price = df_price.sort_values("Price Range")

# st.subheader("Fraud Rates by Price Range")
# st.table(df_price)


st.divider()

# -------- Visualization --------



st.write("The following code shown was used for this calculation")

sql_code_transaction_amount = """
SELECT u.user_id, 
COUNT(CASE WHEN is_fraud = 1 THEN 1 END) as fraud_count
FROM users u
JOIN transactions t ON t.user_id = u.user_id 
GROUP BY u.user_id
HAVING fraud_count > 1 
ORDER BY fraud_count DESC  
"""


st.code(sql_code_transaction_amount, language="sql", line_numbers=True)


st.divider()

# -------- Business Interpretation --------
st.subheader("📘 Business Interpretation")

st.write("""
Repeated attempts at fraud by individual users or clusters of users often signal coordinated fraud activity, credential compromise, or account takeover. Identifying early repeat behavior provides strong predictive fraud signals.
""")

st.divider()
# -------- Recommended Actions --------
st.subheader("🚨 Recommended Actions")

st.write("""
* Implement progressive account friction:


    * 1st fraud: Temporary enhanced verification


    * 2nd fraud: Manual review and temporary suspension


    * 3rd fraud: Permanent account restriction


* Develop cross-user linking analysis across:


    * Devices


    * Merchants


    * Geographic activity


    * Payment methods


* Deploy early-warning alerts when users approach repeat fraud thresholds.


* Conduct proactive outreach and security audits for impacted accounts.

""")
