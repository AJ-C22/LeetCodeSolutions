# Write your MySQL query statement below
WITH table1 AS (
    SELECT customer_id, MIN(order_date) as min_order
    FROM delivery
    GROUP BY customer_id
),

table2 AS (
    SELECT d.delivery_id, d.order_date
     as order_date FROM delivery d
    INNER JOIN table1 t1 ON 
    d.order_date = t1.min_order
    AND d.customer_id = t1.customer_id
),

final AS(
    SELECT d.delivery_id, d.customer_id,
    CASE
        WHEN d.order_date = d.customer_pref_delivery_date THEN "Immediate"
        ELSE "Scheduled"
    END AS status
    FROM delivery d
    INNER JOIN table2 t2 ON 
    t2.delivery_id = d.delivery_id
),

counted AS (
    SELECT 
        SUM(CASE
            WHEN status = "Immediate" THEN 1
            ELSE 0
        END) AS imm_cnt,
        COUNT(status) as total_cnt
    FROM final
)

SELECT ROUND((imm_cnt / total_cnt) * 100, 2) AS immediate_percentage
FROM counted