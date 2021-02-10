-- Query all columns for all American cities in the CITy table with populations larger than 100000, Country Code for America is USA
SELECT * FROM CITY
WHERE COUNTRYCODE="USA" AND POPULATION > 100000;