-- Task
-- Query the sum of the Northern Latitudes from STATION having values greater than
-- 37.880 and less than 137.2345

SELECT TRUNCATE(SUM(LAT_N), 4) FROM STATION
WHERE LAT_N BETWEEN 38.780 AND 137.2345;


-- I did the bottom, but found that you could use between
SELECT TRUNCATE(SUM(LAT_N), 4) FROM STATION
WHERE LAT_N > 38.780 AND LAT_N < 137.2345;
