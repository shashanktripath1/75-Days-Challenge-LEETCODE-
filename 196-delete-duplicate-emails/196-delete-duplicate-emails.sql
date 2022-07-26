# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
delete s from Person s,Person t
WHERE s.id>t.id and s.email=t.email