SELECT user_id as buyer_id, join_date, COUNT(order_date) AS orders_in_2019
FROM Users u
LEFT JOIN Orders o ON u.user_id=o.buyer_id AND YEAR(order_date)='2019'
GROUP BY user_id
