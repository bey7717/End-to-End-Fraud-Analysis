This README provides an overview of the Fraud Analytics Business Intelligence Dashboard, a project designed to analyze financial transaction patterns and identify high-risk fraudulent behavior.

Project Overview
The primary goal of this project is to translate raw synthetic transaction data into actionable business insights for financial institutions. By leveraging SQL-driven analytics and feature engineering, the project identifies patterns across several key dimensions:

Transaction Geography: Concentration of fraud by country and domestic vs. international risk.

Payment Method Risk: Comparison of fraud rates across different channels (e.g., Credit Card, Digital Wallet, ACH).

Transaction Amount Behavior: Likelihood of fraud based on purchase size.

User Patterns: Identification of repeat offenders and escalation behaviors.

Device Intelligence: Detection of shared device networks and potential fraud rings.

Tech Stack
Language: Python

Database: SQL (SQLite)

Data Analysis: Pandas, NumPy

Visualization: Matplotlib, Streamlit


Key Insights
Payment Methods: Digital wallet payments exhibit the highest fraud rate (~3.68%), while credit cards show the lowest (~2.51%) despite higher transaction volumes.

Seasonality: Fraud activity significantly spikes during late-year holiday shopping periods (Weeks 43–52), reaching rates up to 6.17%.

Transaction Amount: Fraudsters frequently target specific transaction tiers (e.g., $301–$1000) to balance payout potential with lower scrutiny.

Repeat Offenders: A small number of users are responsible for multiple incidents; for example, one specific user recorded 4 separate fraud incidents.

Device Risk: Devices shared across unrelated users strongly correlate with fraud, with some "burner" devices showing 100% fraud rates.

Repository Structure
connect_database.py: Python script for initializing the SQLite database and importing raw CSV data into users and transactions tables.

analysis.ipynb: Jupyter notebook containing exploratory data analysis (EDA), data cleaning, and initial fraud pattern hypothesis testing.

app.py: The main entry point for the Streamlit Business Intelligence dashboard.

Feature Modules:

payment_methods.py: Analyzes risk by transaction channel.

seasonality.py: Examines weekly and seasonal fraud trends.

transcation_amount.py: Bins transactions by size to find high-risk price ranges.

user_patterns.py: Uses SQL joins to track repeat offenders.

device_intelligence.py: Detects suspicious shared device networks.

Recommended Actions for Businesses
Based on the analysis, financial institutions should:

Introduce Tiered Controls: Apply standard verification for low-value transactions and enhanced multi-factor authentication for high-risk price tiers ($300+).

Monitor Wallets: Implement stricter velocity checks and device fingerprinting specifically for digital wallet transactions.

Dynamic Thresholds: Deploy adaptive fraud scoring that lowers friction during low-risk mid-year periods and tightens during peak holiday seasons.

Device Scoring: Integrate device reputation scoring into existing risk models to identify shared hardware used in farming schemes.
