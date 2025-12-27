# Write your MySQL query statement below
WITH table1 AS (
    SELECT *,
    CASE
        WHEN id % 2 = 1 THEN LEAD(student) OVER (ORDER BY id)
        ELSE LAG(student) OVER (ORDER BY id)
    END AS alt
    FROM seat
),

table2 AS (
    SELECT id, student,
        CASE
            WHEN alt IS NULL THEN student
            ELSE alt
        END AS alt
    FROM table1
)

SELECT id, alt AS student 
FROM table2