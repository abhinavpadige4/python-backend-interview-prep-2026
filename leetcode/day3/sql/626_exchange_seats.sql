"""
Problem: 626. Exchange Seats
Link: https://leetcode.com/problems/exchange-seats/
Solution: Write a SQL query to swap the seat id of every two consecutive students.
If the number of students is odd, the last student's seat is not swapped.
We can use a CASE statement with MOD and LEAD/LAG or self-join.
"""

SELECT
    (CASE
        WHEN MOD(id, 2) != 0 AND counts != id THEN id + 1
        WHEN MOD(id, 2) != 0 AND counts = id THEN id
        ELSE id - 1
    END) AS id,
    student
FROM
    seat,
    (SELECT COUNT(*) AS counts FROM seat) AS seat_counts
ORDER BY id