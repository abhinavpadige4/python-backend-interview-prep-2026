"""
Problem: 704. Binary Search
Link: https://leetcode.com/problems/binary-search/
Solution: Implement binary search on a sorted array.
Time Complexity: O(log n) where n is the length of the array.
Space Complexity: O(1) - only a few variables used.
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Returns the index of target in nums if found, otherwise -1.
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: nums = [-1,0,3,5,9,12], target = 9 -> Output: 4
    nums1 = [-1,0,3,5,9,12]
    target1 = 9
    print(f"Test 1: {sol.search(nums1, target1)}")  # Expected: 4
    
    # Test case 2: nums = [-1,0,3,5,9,12], target = 2 -> Output: -1
    nums2 = [-1,0,3,5,9,12]
    target2 = 2
    print(f"Test 2: {sol.search(nums2, target2)}")  # Expected: -1
    
    # Test case 3: nums = [5], target = 5 -> Output: 0
    nums3 = [5]
    target3 = 5
    print(f"Test 3: {sol.search(nums3, target3)}")  # Expected: 0
    
    # Test case 4: nums = [5], target = -5 -> Output: -1
    nums4 = [5]
    target4 = -5
    print(f"Test 4: {sol.search(nums4, target4)}")  # Expected: -1
    
    # Test case 5: Empty array
    nums5 = []
    target5 = 0
    print(f"Test 5: {sol.search(nums5, target5)}")  # Expected: -1