cur.execute("SELECT AVG(CAST(is_fraud as FLOAT) * 100) as fraud_rates, SUM(is_fraud) as fraud_count, COUNT(*) as transaction_volume, " \
"CASE WHEN u.country <> t.country THEN 1 ELSE 0 END as transcation_type " \
"FROM transactions t " \
"JOIN Users u ON u.user_id = t.user_id " \
"GROUP BY transcation_type " \
"ORDER BY fraud_rates DESC")
rows = cur.fetchall()
col = [description[0] for description in cur.description]
print(tabulate(rows, headers=col, tablefmt='grid'))