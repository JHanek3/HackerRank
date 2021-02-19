-- Task
-- Query the greatest value of the Northern Lat from STATION that is less than 137,2345
-- Truncate your answer to 4 decimal places

SELECT ROUND(MAX(LAT_N), 4) FROM Station
WHERE LAT_N < 137.2345;