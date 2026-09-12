"""
Problem: 42. Trapping Rain Water
Link: https://leetcode.com/problems/trapping-rain-water/
Solution: Use two pointers to track the maximum height from left and right.
Time Complexity: O(n) where n is the length of the array.
Space Complexity: O(1).
"""

class Solution:
    def trap(self, height: list[int]) -> int:
        """
        Returns the total amount of trapped rain water.
        """
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0
        
        while left < right:
            if height[left] < height[right]:
                left += 1
                left_max = max(left_max, height[left])
                water_trapped += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water_trapped += right_max - height[right]
        
        return water_trapped

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: [0,1,0,2,1,0,1,3,2,1,2,1] -> 6
    height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(f"Test 1: {sol.trap(height1)}")  # Expected: 6
    
    # Test case 2: [4,2,0,3,2,5] -> 9
    height2 = [4,2,0,3,2,5]
    print(f"Test 2: {sol.trap(height2)}")  # Expected: 9
    
    # Test case 3: [4,2,3] -> 1
    height3 = [4,2,3]
    print(f"Test 3: {sol.trap(height3)}")  # Expected: 1
    
    # Test case 4: [5,5,1,7,1,1,5,2,7,6] -> 23
    height4 = [5,5,1,7,1,1,5,2,7,6]
    print(f"Test 4: {sol.trap(height4)}")  # Expected: 23