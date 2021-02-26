-- Task
-- Query the sum of the populations for all japenese cities in CITY. Country code is JPN
SELECT SUM(POPULATION) FROM CITY
WHERE COUNTRYCODE = 'JPN';