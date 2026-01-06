# Write your MySQL query statement below
WITH all_data AS (
    SELECT *,
    LEAD(people) OVER (ORDER BY id) AS NEXT,
    LEAD(people, 2) OVER (ORDER BY id) NEXT_2,
    LAG(people) OVER (ORDER BY id) AS PREV,
    LAG(people, 2) OVER (ORDER BY id) AS PREV_2
    FROM stadium
)

SELECT id, visit_date, people
FROM all_data
WHERE (people >= 100 AND NEXT >= 100 AND NEXT_2 >= 100)
OR (people >= 100 AND PREV >= 100 AND PREV_2 >= 100)
OR ((people >= 100 AND NEXT >= 100 AND NEXT_2 IS NULL) AND (PREV >= 100))
OR ((people >= 100 AND NEXT IS NULL AND NEXT_2 IS NULL) AND (PREV >= 100 AND PREV_2 >= 100))
ORDER BY visit_date ASC

