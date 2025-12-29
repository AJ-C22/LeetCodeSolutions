# Write your MySQL query statement below
WITH all_data AS (
    SELECT u.name, mo.title, rating, created_at
    FROM movieRating m
    LEFT JOIN users u 
        ON u.user_id = m.user_id
    LEFT JOIN movies mo
        ON mo.movie_id = m.movie_id
)

SELECT name AS results FROM (
    SELECT name, COUNT(name) as cnt FROM all_data
    GROUP BY name
    ORDER BY cnt DESC, name ASC
    LIMIT 1
) r1

UNION ALL

SELECT title AS results FROM (
    SELECT title, AVG(rating) AS avg FROM all_data
    WHERE created_at BETWEEN "2020-02-01" AND "2020-02-29"
    GROUP BY title
    ORDER BY avg DESC, title ASC
    LIMIT 1
) r2

