# Write your MySQL query statement below
SELECT name as Customers from Customers
LEFT JOIN orders
on Customers.id=Orders.customerid
WHERE orders.customerid is NULL
