# Write your MySQL query statement below
WITH all_data AS (
    SELECT s.user_id, c.action
    FROM signups s
    LEFT JOIN confirmations C ON 
    c.user_id = s.user_id
),

count_data AS (
    SELECT user_id, 
    SUM(
        CASE
            WHEN action = "confirmed" THEN 1
            ELSE 0
        END
    ) AS confirmed_cnt,
    COUNT(user_id) AS total
    FROM all_data
    GROUP BY user_id
)

SELECT user_id, 
ROUND(confirmed_cnt / total, 2) AS confirmation_rate
FROM count_data

    
