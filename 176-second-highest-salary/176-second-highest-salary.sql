SELECT max(e2.salary) AS SecondHighestSalary
FROM Employee e1,Employee e2
WHERE e1.salary>e2.salary