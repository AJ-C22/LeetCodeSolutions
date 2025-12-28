# Write your MySQL query statement below
SELECT stock_name, SUM(value) AS capital_gain_loss FROM (
    SELECT *,
        CASE 
            WHEN operation = "Buy" THEN price * -1
            ELSE price
        END AS value
    FROM stocks
    ORDER BY stock_name
) f
GROUP BY stock_name
