# Write your MySQL query statement below
SELECT customer_id FROM (
    SELECT customer_id, COUNT(DISTINCT product_key) AS cnt 
    FROM customer c
    GROUP BY customer_id
    HAVING cnt = (SELECT COUNT(product_key) FROM product)
) f

