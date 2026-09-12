"""
Problem: 1045. Customers Who Bought All Products
Link: https://leetcode.com/problems/customers-who-bought-all-products/
Solution: Write a SQL query to find the customer ids that bought all the products.
We can use a double NOT EXISTS or compare counts.
"""

SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product)