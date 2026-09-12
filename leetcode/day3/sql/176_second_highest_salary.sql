"""
Problem: 176. Second Highest Salary
Link: https://leetcode.com/problems/second-highest-salary/
Solution: Write a SQL query to get the second highest salary from the Employee table.
If there is no second highest salary, return null.
We can use LIMIT and OFFSET, or use a subquery with MAX.
"""

SELECT 
    (SELECT DISTINCT Salary 
     FROM Employee 
     ORDER BY Salary DESC 
     LIMIT 1 OFFSET 1) AS SecondHighestSalary