-- Task
-- Query the LONG_W for the largest LAT_N in STATION that is less than 137.2345
-- Round answer to 4 decimal places
SELECT LONG_W FROM 
    (SELECT ROUND(MAX(LAT_N), 4) FROM Station
        WHERE LAT_N < 137.2345) as myalias;
-- This works on mySQL but not hackerrank so we have to use
-- SELECT ROUND(LONG_W,4) 
-- FROM STATION 
-- WHERE LAT_N < 137.2345 
-- ORDER BY LAT_N desc limit 1;