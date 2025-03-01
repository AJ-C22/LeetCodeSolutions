# Write your MySQL query statement below
with t1 as (
    select email, count(email) as cnt from person group by email
)
select email from t1
where cnt > 1

