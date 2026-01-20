# Write your MySQL query statement below
WITH data AS (
    SELECT *,
    CASE 
        WHEN amount % 2 = 0 THEN amount
        ELSE 0
    END AS "even_sum",
    CASE
        WHEN amount % 2 = 1 THEN amount
        ELSE 0
    END AS "odd_sum"
    FROM transactions
)

SELECT transaction_date, SUM(odd_sum) as odd_sum, SUM(even_sum) as even_sum
FROM data
GROUP BY transaction_date
ORDER BY transaction_date