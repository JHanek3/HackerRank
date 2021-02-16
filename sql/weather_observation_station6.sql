-- Task
-- Query the list of CITY names starting with vowels from STATION, cannot contain duplicates

-- This worked
SELECT DISTINCT(CITY) FROM STATION
WHERE CITY LIKE 'A%' OR CITY LIKE 'E%' OR CITY LIKE 'I%' OR CITY LIKE 'O%' OR CITY LIKE 'U%';

-- This worked on W3, but did not work on mySQL workbench or hackerrank
SELECT DISTINCT(CITY) FROM STATION
WHERE CITY LIKE '[AEIOU]%';