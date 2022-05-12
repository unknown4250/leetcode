# Write your MySQL query statement below
SELECT * FROM (
    SELECT product_id, 'store1' store, store1 price FROM products
    UNION
    SELECT product_id, 'store2' store, store2 price FROM products
    UNION
    SELECT product_id, 'store3' store, store3 price FROM products 
) sub
WHERE price IS NOT NULL