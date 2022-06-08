# Write your MySQL query statement below
SELECT user_id as buyer_id, join_date, COUNT(o.order_date) AS orders_in_2019
FROM Users u
LEFT JOIN Orders o ON o.buyer_id = u.user_id AND YEAR(o.order_date)='2019'
GROUP BY user_id
