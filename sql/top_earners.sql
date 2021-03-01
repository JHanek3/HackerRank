-- Task
-- Total Earnings = salary * month, maximum total earnings to be the maximum total
-- earnings for any employee in the Employee table
-- Write a query to find the maximum total earnings for all employees, as
-- well as the total number of employeees who have maximum earnings

-- This was my submission
-- This works but Hackerrank says it fails because it shows the max_salary variable along with the final output
-- I dont know how to only show the final output, I like my waym its easier to read.
SELECT 
    @max_salary:= MAX(salary * months)
FROM
    Employee;

Select
	@max_salary, COUNT(@max_salary)
FROM Employee
WHERE salary * months = @max_salary;

-- This was the final submission
SELECT (salary * months) as earnings, count(*)
FROM employee
GROUP BY 1
ORDER BY earnings DESC
LIMIT 1;