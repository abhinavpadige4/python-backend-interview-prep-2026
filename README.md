# Python Backend Interview Preparation - 3 Day Plan

This repository contains solutions to LeetCode problems and backend projects prepared for a Python backend interview over 3 days.

## Structure

- `leetcode/` - LeetCode solutions organized by day and difficulty
- `backend/` - Backend projects (Flask and Django)
- Each solution file includes:
  - Problem description
  - Solution code
  - Time and space complexity analysis

## Day 1 - Python Fundamentals & LeetCode Easy/Medium

### LeetCode Easy Problems
- [206. Reverse Linked List](./leetcode/day1/easy/206_reverse_linked_list.py)
- [141. Linked List Cycle](./leetcode/day1/easy/141_linked_list_cycle.py)
- [21. Merge Two Sorted Lists](./leetcode/day1/easy/21_merge_two_sorted_lists.py)
- [704. Binary Search](./leetcode/day1/easy/704_binary_search.py)
- [88. Merge Sorted Array](./leetcode/day1/easy/88_merge_sorted_array.py)

### LeetCode Medium Problems
- [2. Add Two Numbers](./leetcode/day1/medium/002_add_two_numbers.py)
- [19. Remove Nth Node From End of List](./leetcode/day1/medium/019_remove_nth_from_end.py)
- [142. Linked List Cycle II](./leetcode/day1/medium/142_linked_list_cycle_ii.py)
- [15. 3Sum](./leetcode/day1/medium/015_3sum.py)
- [36. Valid Sudoku](./leetcode/day1/medium/036_valid_sudoku.py)

### Backend Project
- [Flask Todo API](./backend/day1/flask_todo_app.py) - CRUD API for Todo resource
- [Requirements](./backend/day1/requirements.txt)

## Day 2 - OOP, Design Patterns & LeetCode Medium/Hard

### LeetCode Medium Problems
- [11. Container With Most Water](./leetcode/day2/medium/011_container_most_water.py)
- [42. Trapping Rain Water](./leetcode/day2/medium/042_trapping_rain_water.py)
- [76. Minimum Window Substring](./leetcode/day2/medium/076_min_window_substring.py)
- [300. Longest Increasing Subsequence](./leetcode/day2/medium/300_lis.py)
- [55. Jump Game](./leetcode/day2/medium/055_jump_game.py)

### LeetCode Hard Problems
- [23. Merge k Sorted Lists](./leetcode/day2/hard/023_merge_k_lists.py)
- [84. Largest Rectangle in Histogram](./leetcode/day2/hard/084_largest_rectangle_histogram.py)
- [124. Binary Tree Maximum Path Sum](./leetcode/day2/hard/124_binary_tree_max_path_sum.py)
- [146. LRU Cache](./leetcode/day2/hard/146_lru_cache.py)

### Backend Project
- [Django Blog API](./backend/day2/django_blog/) - CRUD API for Blog posts using Django REST Framework
- [Requirements](./backend/day2/django_blog/requirements.txt)

## Day 3 - Databases, System Design & Mock Interview

### LeetCode SQL Problems
- [176. Second Highest Salary](./leetcode/day3/sql/176_second_highest_salary.sql)
- [180. Consecutive Numbers](./leetcode/day3/sql/180_consecutive_numbers.sql)
- [182. Duplicate Emails](./leetcode/day3/sql/182_duplicate_emails.sql)
- [196. Delete Duplicate Emails](./leetcode/day3/sql/196_delete_duplicate_emails.sql)
- [595. Big Countries](./leetcode/day3/sql/595_big_countries.sql)
- [607. Sales Person](./leetcode/day3/sql/607_sales_person.sql)
- [626. Exchange Seats](./leetcode/day3/sql/626_exchange_seats.sql)
- [1045. Customers Who Bought All Products](./leetcode/day3/sql/1045_customers_all_products.sql)

## How to Use

1. Clone the repository
2. For LeetCode solutions: Run the Python files directly (they include test cases)
3. For backend projects:
   - Flask: `pip install -r backend/day1/requirements.txt` then `python backend/day1/flask_todo_app.py`
   - Django: `pip install -r backend/day2/django_blog/requirements.txt` then follow Django setup instructions

## Concepts Covered

- Python fundamentals (data structures, OOP, decorators, generators)
- Linked list problems (reverse, cycle detection, merge)
- Array/two-pointer techniques (3Sum, container with most water, trapping rain water)
- String algorithms (minimum window substring, longest increasing subsequence)
- Binary search and sorting
- Hash table usage (LRU cache, 3Sum, valid Sudoku)
- Heap and priority queue (merge k sorted lists)
- Tree DFS (binary tree max path sum)
- Dynamic programming (jump game, longest increasing subsequence)
- SQL queries (aggregates, joins, subqueries)
- REST API design (Flask, Django REST Framework)
- CRUD operations
- Database modeling

## Notes

- All solutions are written in Python 3
- LeetCode solutions include iterative and recursive approaches where applicable
- Backend projects use in-memory storage for simplicity (Flask) and SQLite (Django)
- SQL solutions are tested with SQLite in-memory