# Write your MySQL query statement below
SELECT sub.customer_number
FROM (SELECT COUNT(customer_number) as cnt, customer_number
FROM Orders
GROUP BY customer_number) sub
ORDER BY sub.cnt DESC
LIMIT 1