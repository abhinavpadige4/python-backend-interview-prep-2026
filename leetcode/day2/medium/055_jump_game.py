"""
Problem: 55. Jump Game
Link: https://leetcode.com/problems/jump-game/
Solution: Greedy approach. Track the farthest index we can reach.
Time Complexity: O(n) where n is the length of the array.
Space Complexity: O(1).
"""

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        Returns True if you can reach the last index, False otherwise.
        """
        max_reach = 0
        for i, num in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + num)
            if max_reach >= len(nums) - 1:
                return True
        return max_reach >= len(nums) - 1

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: [2,3,1,1,4] -> True
    nums1 = [2,3,1,1,4]
    print(f"Test 1: {sol.canJump(nums1)}")  # Expected: True
    
    # Test case 2: [3,2,1,0,4] -> False
    nums2 = [3,2,1,0,4]
    print(f"Test 2: {sol.canJump(nums2)}")  # Expected: False
    
    # Test case 3: [0] -> True
    nums3 = [0]
    print(f"Test 3: {sol.canJump(nums3)}")  # Expected: True
    
    # Test case 4: [1,0,1,0] -> False
    nums4 = [1,0,1,0]
    print(f"Test 4: {sol.canJump(nums4)}")  # Expected: False