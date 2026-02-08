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
* Multiple shared devices exhibit significantly elevated fraud rates.


* Certain devices demonstrate:


* 100% fraud rates (likely burner devices)


* Moderate fraud rates (50–67%) across multiple users, suggesting coordinated activity


* Lower fraud rates (25–40%) but high user counts, indicating systemic exposure risk


* Device sharing across unrelated users strongly correlates with fraud activity.

""")



st.divider()

# -------- Visualization --------



st.write("The following code shown was used for this calculation")

sql_code_transaction_amount = """
SELECT 
    COUNT(DISTINCT(user_id)) as user_count, SUM(is_fraud) as fraud_count, device_id,
    COUNT(*) as total_transactions, 
    AVG(CAST(is_fraud as FLOAT) * 100) as fraud_rates
FROM transactions
GROUP BY device_id 
HAVING fraud_count > 1 
    AND user_count > 1 
ORDER BY fraud_count DESC
"""


st.code(sql_code_transaction_amount, language="sql", line_numbers=True)


st.divider()

# -------- Business Interpretation --------
st.subheader("📘 Business Interpretation")

st.write("""
Device-level analysis reveals patterns consistent with organized fraud operations, account farming, and credential-sharing schemes. Device intelligence provides a high-signal indicator for fraud detection beyond user-level monitoring.
""")

st.divider()
# -------- Recommended Actions --------
st.subheader("🚨 Recommended Actions")

st.write("""
* Implement device reputation scoring integrated into transaction risk models.


* Block or step up authentication for devices with extreme fraud rates.


* Monitor high-reach devices serving multiple user accounts.




""")
