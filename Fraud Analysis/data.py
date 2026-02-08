import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

np.random.seed(42)

n_transactions = 10000
n_users = 1000
n_merchants = 100
countries = ['US', 'UK', 'IN', 'NG', 'BR', 'DE', 'FR', 'CA', 'AU']
payment_methods = ['card', 'ach', 'wallet']

user_ids = [f'user_{i}' for i in range(1, n_users+1)]
users = pd.DataFrame({
    'user_id': user_ids,
    'signup_date': [datetime(2022,1,1) + timedelta(days=random.randint(0, 730)) for _ in range(n_users)],
    'country': np.random.choice(countries, n_users)
})


user_map = users.set_index('user_id')['country'].to_dict()
transactions = []

for i in range(n_transactions):
    user_id = random.choice(user_ids)
    home_country = user_map[user_id]
    
    if random.random() < 0.85:
        tx_country = home_country 
    else:
        tx_country = random.choice([c for c in countries if c != home_country])

    if tx_country != home_country:
        is_fraud = np.random.choice([0,1], p=[0.9,0.1])
    else:
        is_fraud = np.random.choice([0,1], p=[0.98,0.02])
    
    risk_score = 0.0
    
    if tx_country != home_country:
        risk_score += 0.3
    
    amount = round(np.random.exponential(100), 2)
    if amount > 500:
        risk_score += 0.2
    
    timestamp = datetime(2024,1,1) + timedelta(minutes=random.randint(0,525600))
    hour = timestamp.hour
    if hour in [0, 1, 2, 3, 4, 23]:
        risk_score += 0.15
    
    payment_method = random.choice(payment_methods)
    if payment_method == 'ach':
        risk_score += 0.1
    
    risk_score += 0.15 + np.random.uniform(-0.05, 0.05)
    risk_score = np.clip(risk_score, 0.0, 1.0)
    
    transactions.append({
        'transaction_id': f'tx_{i+1}',
        'user_id': user_id,
        'amount': amount,
        'merchant_id': f'merchant_{random.randint(1,n_merchants)}',
        'country': tx_country,
        'payment_method': payment_method,
        'device_id': f'device_{random.randint(1,3000)}',
        'is_fraud': is_fraud,
        'risk_score': round(risk_score, 2),
        'timestamp': timestamp
    })

transactions = pd.DataFrame(transactions)
os.makedirs('data', exist_ok=True)
transactions.to_csv('data/transactions.csv', index=False)
users.to_csv('data/users.csv', index=False)

