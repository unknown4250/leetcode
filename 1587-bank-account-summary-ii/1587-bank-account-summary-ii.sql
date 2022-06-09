SELECT sub.name, sub.balance
FROM (SELECT u.name, SUM(t.amount) AS balance
FROM Transactions t
JOIN Users u ON u.account=t.account
GROUP BY t.account) sub
WHERE sub.balance > 10000