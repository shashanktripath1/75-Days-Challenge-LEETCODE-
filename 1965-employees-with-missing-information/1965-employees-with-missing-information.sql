SELECT S.employee_id
FROM (SELECT * FROM Employees LEFT JOIN Salaries USING(employee_id)
     UNION
      SELECT * FROM Employees RIGHT JOIN Salaries USING(employee_id)
     )
AS S
WHERE S.salary is NULL or S.name is NULL
OrDER BY employee_id