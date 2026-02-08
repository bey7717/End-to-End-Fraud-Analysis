import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Fraud Analytics Dashboard",
    layout="wide"
)

# ---------------------------
# HEADER
# ---------------------------

st.title("Fraud Analytics Business Intelligence Dashboard")
st.markdown("""
This dashboard analyzes financial transaction fraud patterns using SQL-driven analytics and feature engineering.
It is designed to help financial institutions identify high-risk behavior and optimize fraud detection strategies.
""")

st.divider()

# ---------------------------
# PROJECT OVERVIEW
# ---------------------------

col1, col2 = st.columns([2,1])

with col1:
    st.subheader("Project Overview")

    st.markdown("""
    This project explores fraud risk across several dimensions:

    - Transaction geography
    - Payment method risk
    - Transaction amount behavior
    - User fraud repetition
    - Shared device fraud networks

    The goal is to translate raw transaction data into **actionable business decisions**.
    """)

with col2:
    st.subheader("🛠 Tech Stack")
    st.markdown("""
    - Python
    - SQL
    - Pandas
    - Streamlit
    - AWS (Deployment)
    - Matplotlib
    """)

st.divider()

# ---------------------------
# KEY BUSINESS FINDINGS
# ---------------------------

st.subheader("Key Fraud Insights")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Cross-Country Fraud Risk",
        "4.6x Higher",
        "Major Risk Driver"
    )

with col2:
    st.metric(
        "Highest Risk Payment Method",
        "Digital Wallet",
        "3.68% Fraud Rate"
    )

with col3:
    st.metric(
        "Peak Fraud Season",
        "Weeks 43-52",
        "Holiday Surge"
    )

st.divider()

# ---------------------------
# NAVIGATION GUIDE
# ---------------------------

st.subheader("Dashboard Navigation")

st.markdown("""
Use the sidebar to explore detailed analytics pages:

###  Overview
• Baseline fraud rate trends  
• Seasonal fraud behavior  

###  Payment Methods
• Fraud comparison across payment channels  

###  Cross Country Transactions
• Geographic fraud concentration  
• Domestic vs international risk  

###  Transaction Amount
• Fraud likelihood by purchase size  

###  User Patterns
• Repeat offender analysis  
• Fraud escalation behavior  

###  Device Patterns
• Shared device fraud networks  
• Fraud ring detection  
""")

st.divider()

# ---------------------------
# BUSINESS IMPACT
# ---------------------------

st.subheader("Business Impact")

st.markdown("""
The insights generated from this dashboard support:

✔ Risk-based transaction monitoring  
✔ Fraud prevention resource allocation  
✔ Adaptive fraud detection thresholds  
✔ Early fraud ring identification  
✔ Customer security strategy development  
""")

st.divider()

# ---------------------------
# DATA DISCLAIMER
# ---------------------------

with st.expander("Data & Methodology"):
    st.markdown("""
    - Data generated using synthetic transaction simulation (Faker)
    - Fraud patterns modeled to reflect realistic fintech risk scenarios
    - Analysis performed using SQL aggregation and feature engineering
    - Dashboard visualizations built using Streamlit
    """)

st.caption("Fraud Analytics Dashboard — Portfolio Project")
