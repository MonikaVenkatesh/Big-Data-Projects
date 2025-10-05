SELECT 
    c.customer_id,
    c.customer_name,
    SUM(CASE WHEN t.txn_type = 'DEBIT' THEN t.amount ELSE 0 END) AS total_debit,
    SUM(CASE WHEN t.txn_type = 'CREDIT' THEN t.amount ELSE 0 END) AS total_credit,
    CURRENT_DATE AS report_date
FROM transactions t
JOIN customers c ON t.customer_id = c.customer_id
WHERE t.txn_date = CURRENT_DATE
GROUP BY c.customer_id, c.customer_name;
