/*
AND가 아닌 WHERE를 사용하면 안 되는 이유는 JOIN 후에 WHERE가 수행되기 때문
2019년도 주문만 선택한 후에 JOIN 해야 함
SELECT u.user_id AS buyer_id ,u.join_date ,COUNT(o.buyer_id) AS orders_in_2019 
FROM Users u LEFT JOIN Orders o
ON u.user_id = o.buyer_id WHERE YEAR(o.order_date) ='2019'
GROUP BY u.user_id
*/

SELECT user_id as buyer_id, join_date, COUNT(order_date) AS orders_in_2019
FROM Users u
LEFT JOIN Orders o ON u.user_id=o.buyer_id AND YEAR(order_date)='2019'
GROUP BY user_id
