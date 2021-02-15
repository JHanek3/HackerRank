-- Task 
-- Find the difference between the toal number of city entries in the table and the number of distinct CITY entries in the table
SELECT COUNT(CITY) FROM STATION;
SELECT COUNT(DISTINCT CITY) FROM STATION;

SELECT (COUNT(CITY) - COUNT(DISTINCT CITY)) FROM STATION;