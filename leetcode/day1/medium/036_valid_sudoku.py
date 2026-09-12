"""
Problem: 36. Valid Sudoku
Link: https://leetcode.com/problems/valid-sudoku/
Solution: Check if a 9x9 Sudoku board is valid by verifying rows, columns, and 3x3 sub-boxes.
We use sets to track seen numbers in each row, column, and box.
Time Complexity: O(1) since the board size is fixed at 9x9.
Space Complexity: O(1) for the same reason.
"""

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        Returns True if the Sudoku board is valid, False otherwise.
        """
        # Initialize sets for rows, columns, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                
                # Check row
                if num in rows[i]:
                    return False
                rows[i].add(num)
                
                # Check column
                if num in cols[j]:
                    return False
                cols[j].add(num)
                
                # Check box
                box_index = (i // 3) * 3 + j // 3
                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)
        
        return True

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: Valid Sudoku board
    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(f"Test 1 (valid): {sol.isValidSudoku(board1)}")  # Expected: True
    
    # Test case 2: Invalid Sudoku board (duplicate in first row)
    board2 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(f"Test 2 (invalid): {sol.isValidSudoku(board2)}")  # Expected: False
    
    # Test case 3: Empty board
    board3 = [["." for _ in range(9)] for _ in range(9)]
    print(f"Test 3 (empty): {sol.isValidSudoku(board3)}")  # Expected: True