# Write your MySQL query statement below
select user_id,max(time_stamp) as last_stamp
from Logins
where time_stamp Between '2020-01-01' and '2021-01-01' 
group by user_id

