"""
Problem: 595. Big Countries
Link: https://leetcode.com/problems/big-countries/
Solution: Write a SQL query to report the name, population, and area of big countries.
A country is big if it has an area of at least 3,000,000 km2 or a population of at least 25,000,000.
"""

SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000