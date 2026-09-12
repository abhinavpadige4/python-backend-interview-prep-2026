"""
Problem: 88. Merge Sorted Array
Link: https://leetcode.com/problems/merge-sorted-array/
Solution: Merge two sorted arrays into nums1, which has enough space to hold the result.
We start from the end of both arrays to avoid overwriting elements in nums1.
Time Complexity: O(m + n) where m and n are the number of elements in nums1 and nums2 initially.
Space Complexity: O(1) - we modify nums1 in-place.
"""

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Start from the end of nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1  # Pointer for the end of the merged array
        
        # While there are elements to compare in nums1 and nums2
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If there are remaining elements in nums2, copy them
        # (if there are remaining elements in nums1, they are already in place)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3 -> [1,2,2,3,5,6]
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    sol.merge(nums1, m, nums2, n)
    print(f"Test 1: {nums1}")  # Expected: [1,2,2,3,5,6]
    
    # Test case 2: nums1 = [1], m = 1, nums2 = [], n = 0 -> [1]
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    sol.merge(nums1, m, nums2, n)
    print(f"Test 2: {nums1}")  # Expected: [1]
    
    # Test case 3: nums1 = [0], m = 0, nums2 = [1], n = 1 -> [1]
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    sol.merge(nums1, m, nums2, n)
    print(f"Test 3: {nums1}")  # Expected: [1]
    
    # Test case 4: nums1 = [4,5,6,0,0,0], m = 3, nums2 = [1,2,3], n = 3 -> [1,2,3,4,5,6]
    nums1 = [4,5,6,0,0,0]
    m = 3
    nums2 = [1,2,3]
    n = 3
    sol.merge(nums1, m, nums2, n)
    print(f"Test 4: {nums1}")  # Expected: [1,2,3,4,5,6]