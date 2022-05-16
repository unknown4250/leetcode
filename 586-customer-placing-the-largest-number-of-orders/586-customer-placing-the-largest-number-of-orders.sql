# Write your MySQL query statement below

SELECT S.customer_number
FROM (SELECT COUNT(customer_number) AS orders, customer_number
FROM Orders
GROUP BY customer_number 
ORDER BY orders DESC
LIMIT 1) S
