-- Task
-- Consider P1(a,b) and P2(c, d)
-- A happens to be equal to the minimum value in the northen LAT_N
-- B happens to be equal to the minimul value in the Western LONG_W
-- C equals the maximum value in LAT_N
-- D equals the maximum value in LONG_W
-- Manhatten distance is abs(x1 - x2) + abs(y1-y2)

SELECT ROUND(ABS(MIN(LAT_N) - MAX(LAT_N)) + ABS(MIN(LONG_W) - MAX(LONG_W)), 4) as "Manhatten Distance" FROM STATION;
