-- Task
-- Query the two cities in STATION with the shortest and longest names as well as there lengths
-- More than one choose the first when ordered alphabetically

-- SELECT CITY, LENGTH(CITY) FROM STATION
-- WHERE LENGTH(CITY) = (
-- 	SELECT MIN(LENGTH(CITY)) FROM STATION
--     ) ORDER BY CITY LIMIT 1;

-- SELECT CITY, LENGTH(CITY) FROM STATION
-- WHERE LENGTH(CITY) = (
-- 	SELECT MAX(LENGTH(CITY)) FROM STATION
-- 	) ORDER BY CITY LIMIT 1;