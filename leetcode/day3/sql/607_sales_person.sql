"""
Problem: 607. Sales Person
Link: https://leetcode.com/problems/sales-person/
Solution: Write a SQL query to find the name of the sales person who did not have any deal with company 'RED'.
We can use a subquery or a left join.
"""

SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT sales_id
    FROM Orders
    WHERE com_id IN (
        SELECT com_id
        FROM Company
        WHERE name = 'RED'
    )
)