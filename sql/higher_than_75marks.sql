-- Task
-- Query the name of any STUDENTS who scored higher than 75 marks.
-- Order the output by the last three characters of each, name
-- If two or more students have names ending in the same last characters order by ascending ID

SELECT Name FROM STUDENTS
WHERE Marks > 75
ORDER BY RIGHT(Name, 3), ID ASC;