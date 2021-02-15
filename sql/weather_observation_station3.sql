-- Task
-- Query a list of CITY names from Station for cities that have an even ID number, exclude any duplicates
SELECT DISTINCT CITY FROM STATION
WHERE ID % 2 = 0; 