-- Task
-- Consider P1(a,c) and P2(b,d to be two points
-- a,b are min and max of LAT_N
-- c,d are min max of Long_W
-- Calculate the Euclidean distance
-- d(p,q) = sqrt (q1 -p1)2 + (q2 - p2)2

SELECT ROUND(SQRT(POWER((MAX(LAT_N) - MIN(LAT_N)),2) + POWER((MAX(LONG_W) - MIN(LONG_W)), 2)),4) AS "EUCLIDEAN DISTANCE" FROM STATION;
