SELECT 
    t.txn_id,
    t.account_id,
    c.customer_name,
    t.txn_type,
    t.amount,
    t.txn_date
FROM transactions t
JOIN customers c ON t.customer_id = c.customer_id
WHERE t.amount > 100000
  AND t.txn_date = CURRENT_DATE;
