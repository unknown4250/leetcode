SELECT name, balance
FROM 
(SELECT name, SUM(amount) AS balance
FROM Users u
LEFT JOIN Transactions t ON u.account = t.account
GROUP BY u.account) s
WHERE balance > 10000