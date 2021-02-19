-- Task
-- Write a query that prints a list of employee names for employees in the employee table having a salary greater than 2000$ per month
-- who have been employess for less than 10 months
-- sort by ascending employee_id

SELECT name from employee
WHERE salary > 2000 AND months < 10
ORDER BY employee_id ASC;