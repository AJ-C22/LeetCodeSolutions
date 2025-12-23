# Write your MySQL query statement below
SELECT DISTINCT num AS ConsecutiveNums 
    FROM (
        SELECT num FROM (
            SELECT *,
            LAG(num) OVER (ORDER BY id) AS prev_one,
            LAG(num,2) OVER (ORDER By id) AS prev_two
            FROM logs
        ) l
        WHERE num = prev_one 
            AND num = prev_two
            AND prev_one IS NOT NULL
    ) c

