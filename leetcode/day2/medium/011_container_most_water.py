"""
Problem: 11. Container With Most Water
Link: https://leetcode.com/problems/container-with-most-water/
Solution: Use two pointers, one at the beginning and one at the end.
Move the pointer pointing to the shorter line inward.
Time Complexity: O(n) where n is the length of the array.
Space Complexity: O(1).
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        Returns the maximum area of water a container can store.
        """
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate the current area
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            max_area = max(max_area, area)
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: [1,8,6,2,5,4,8,3,7] -> 49
    height1 = [1,8,6,2,5,4,8,3,7]
    print(f"Test 1: {sol.maxArea(height1)}")  # Expected: 49
    
    # Test case 2: [1,1] -> 1
    height2 = [1,1]
    print(f"Test 2: {sol.maxArea(height2)}")  # Expected: 1
    
    # Test case 3: [4,3,2,1,4] -> 16
    height3 = [4,3,2,1,4]
    print(f"Test 3: {sol.maxArea(height3)}")  # Expected: 16
    
    # Test case 4: [1,2,1] -> 2
    height4 = [1,2,1]
    print(f"Test 4: {sol.maxArea(height4)}")  # Expected: 2