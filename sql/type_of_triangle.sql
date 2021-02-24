-- Task
-- Write a query labeling triangles
-- Equilaterl 3 equal, Isoscleles 2 equal, Scalene 3 different lengths, and Not a triangle


SELECT
CASE
	WHEN A + B > C AND B + C > A AND A + C > B THEN
		CASE
			WHEN A=B AND B=C THEN "Equilateral"
            WHEN A=B OR B=C OR A=C THEN "Isosceles"
            Else 'Scalene'
		END
	ELSE 'Not A Triangle'
END as "Types of Triangles"
FROM Triangles ;