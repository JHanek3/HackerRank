-- Task
-- Samantha was tasked with calculating the average monthly salries for all employees in the
-- Employees table, but did not realize her keyboard's 0 key was broken unitl after completing
-- the calculation. She wants your help finding the difference between her miscalculations
-- Find the difference between her miscalculation using salaries with zeroes removed 
-- and the actual 

SELECT CEIL((AVG(SALARY)) - (AVG(REPLACE(SALARY, '0', '')))) FROM EMPLOYEES;
