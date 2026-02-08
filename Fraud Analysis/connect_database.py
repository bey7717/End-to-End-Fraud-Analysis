import sqlite3
import csv
from tabulate import tabulate


DB = r'C:\Users\bey77\OneDrive\Desktop\Projects\FinanceProj\Fraud Analysis\fraud_database.db'
TRANSACTIONS = r'C:\Users\bey77\OneDrive\Desktop\Projects\FinanceProj\Fraud Analysis\data\transactions.csv'
USERS = r'C:\Users\bey77\OneDrive\Desktop\Projects\FinanceProj\Fraud Analysis\data\users.csv'




conn = sqlite3.connect(DB)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS USERS;")

cur.execute('''
CREATE TABLE users (
     user_id TEXT,
     signup_date DATE,
     country TEXT
)
''')


cur.execute("DROP TABLE IF EXISTS TRANSACTIONS;")

cur.execute('''
CREATE TABLE transactions (
    transaction_id TEXT,
    user_id TEXT,
    amount FLOAT,
    merchant_id TEXT,
    country TEXT,
    payment_method TEXT,
    device_id TEXT,
    is_fraud INTEGER,
    timestamp TIMESTAMP
);
''')

with open(USERS, 'r', newline='', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cur.execute('''
            INSERT INTO users (
                user_id, signup_date, country) VALUES (?, ?, ?)
        ''', (row['user_id'], row['signup_date'], row['country']))

with open(TRANSACTIONS, 'r', newline='', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cur.execute('''
            INSERT INTO transactions (
                transaction_id, user_id, amount, merchant_id, country, payment_method, device_id, is_fraud, timestamp) VALUES (?, ?, ?, ?,?,?,?,?,?)
        ''', (row['transaction_id'], row['user_id'], row['amount'], row['merchant_id'], row['country'],row['payment_method'],row['device_id'],row['is_fraud'],row['timestamp']))


conn.commit()

#testing to see if it works
# cur.execute("SELECT * FROM users LIMIT 5")
# rows = cur.fetchall()
# col = [description[0] for description in cur.description]
# print(tabulate(rows, headers=col, tablefmt='grid'))

# cur.execute("SELECT * FROM transactions LIMIT 5")
# rows = cur.fetchall()
# col = [description[0] for description in cur.description]
# print(tabulate(rows, headers=col, tablefmt='grid'))


# What is our baseline fraud rate, and how has it changed over time?
# cur.execute("SELECT AVG(CAST(is_fraud as FLOAT) * 100) as baseline_fraud, strftime('%Y-%W', date(timestamp, '-1 day')) as weekly_timestamp FROM transactions " \
# "GROUP BY weekly_timestamp " \
# "ORDER BY baseline_fraud ASC" \
# )
# rows = cur.fetchall()
# col = [description[0] for description in cur.description]
# print(tabulate(rows, headers=col, tablefmt='grid'))


# Which payment methods have the highest fraud rates relative to volume?
# cur.execute("SELECT payment_method, AVG(CAST(is_fraud as FLOAT) * 100) as fraud_rates, SUM(is_fraud) as fraud_count, COUNT(*) as transaction_volume FROM transactions " \
# "GROUP BY payment_method " \
# "ORDER BY fraud_rates DESC")
# rows = cur.fetchall()
# col = [description[0] for description in cur.description]
# print(tabulate(rows, headers=col, tablefmt='grid'))


# What percentage of fraud comes from cross-country transactions compared to their share of total volume?
# cur.execute("SELECT AVG(CAST(is_fraud as FLOAT) * 100) as fraud_rates, SUM(is_fraud) as fraud_count, COUNT(*) as transaction_volume, " \
# "CASE WHEN u.country <> t.country THEN 1 ELSE 0 END as transcation_type " \
# "FROM transactions t " \
# "JOIN Users u ON u.user_id = t.user_id " \
# "GROUP BY transcation_type " \
# "ORDER BY fraud_rates DESC")
# rows = cur.fetchall()
# col = [description[0] for description in cur.description]
# print(tabulate(rows, headers=col, tablefmt='grid'))




# Are higher transaction amounts more likely to be fraudulent?
# cur.execute("SELECT CASE WHEN amount BETWEEN 0 AND 50 THEN '$0 - $50' " \
# "WHEN amount BETWEEN 51 AND 100 THEN '$51 - $100' " \
# "WHEN amount BETWEEN 101 AND 300 THEN '$101 - $300' " \
# "WHEN amount BETWEEN 301 AND 1000 THEN '$301 - $1000' " \
# "WHEN amount > 1000 THEN '$1000+' " \
# "ELSE 'Unknown' END AS price_range, AVG(CAST(is_fraud as FLOAT) * 100) as fraud_rates " \
# "FROM transactions " \
# "GROUP BY price_range " \
# "ORDER BY fraud_rates DESC")
# rows = cur.fetchall()
# col = [description[0] for description in cur.description]
# print(tabulate(rows, headers=col, tablefmt='grid'))



# Are certain users responsible for multiple fraud attempts?
# cur.execute("SELECT u.user_id, COUNT(CASE WHEN is_fraud = 1 THEN 1 END) as fraud_count " \
# "FROM users u " \
# "JOIN transactions t ON t.user_id = u.user_id " \
# "GROUP BY u.user_id " \
# "HAVING fraud_count > 1 " \
# "ORDER BY fraud_count DESC")
# rows = cur.fetchall()
# col = [description[0] for description in cur.description]
# print(tabulate(rows, headers=col, tablefmt='grid'))





# Are there devices used by multiple users with elevated fraud rates?
cur.execute("SELECT COUNT(DISTINCT(user_id)) as user_count, SUM(is_fraud) as fraud_count, device_id, " \
"COUNT(*) as total_transactions, AVG(CAST(is_fraud as FLOAT) * 100) as fraud_rates " \
"FROM transactions " \
"GROUP BY device_id " \
"HAVING fraud_count > 1 " \
"AND user_count > 1 " \
"ORDER BY fraud_count DESC")
rows = cur.fetchall()
col = [description[0] for description in cur.description]
print(tabulate(rows, headers=col, tablefmt='grid'))





conn.close()