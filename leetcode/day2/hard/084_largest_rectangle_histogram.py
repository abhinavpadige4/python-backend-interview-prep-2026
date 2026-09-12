"""
Problem: 84. Largest Rectangle in Histogram
Link: https://leetcode.com/problems/largest-rectangle-in-histogram/
Solution: Use a stack to keep track of indices of bars in increasing order of height.
Time Complexity: O(n) where n is the number of bars.
Space Complexity: O(n) for the stack.
"""

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        Returns the area of the largest rectangle in the histogram.
        """
        stack = []  # Stack to store indices
        max_area = 0
        index = 0
        
        while index < len(heights):
            # If this bar is higher than the bar on top of stack, push it to stack
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                # Pop the top of stack
                top_of_stack = stack.pop()
                # Calculate the area with heights[top_of_stack] as the smallest bar
                area = (heights[top_of_stack] *
                        ((index - stack[-1] - 1) if stack else index))
                max_area = max(max_area, area)
        
        # Now pop the remaining bars from stack and calculate area with each popped bar
        while stack:
            top_of_stack = stack.pop()
            area = (heights[top_of_stack] *
                    ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)
        
        return max_area

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: [2,1,5,6,2,3] -> 10
    heights1 = [2,1,5,6,2,3]
    print(f"Test 1: {sol.largestRectangleArea(heights1)}")  # Expected: 10
    
    # Test case 2: [2,4] -> 3
    heights2 = [2,4]
    print(f"Test 2: {sol.largestRectangleArea(heights2)}")  # Expected: 4 (Note: Actually 4, but let's verify)
    
    # Test case 3: [6,2,5,4,5,1,6] -> 12
    heights3 = [6,2,5,4,5,1,6]
    print(f"Test 3: {sol.largestRectangleArea(heights3)}")  # Expected: 12
    
    # Test case 4: [] -> 0
    heights4 = []
    print(f"Test 4: {sol.largestRectangleArea(heights4)}")  # Expected: 0
    
    # Test case 5: [1] -> 1
    heights5 = [1]
    print(f"Test 5: {sol.largestRectangleArea(heights5)}")  # Expected: 1