"""
Problem: 300. Longest Increasing Subsequence
Link: https://leetcode.com/problems/longest-increasing-subsequence/
Solution: Use dynamic programming with binary search (patience sorting) for O(n log n) time.
Time Complexity: O(n log n) where n is the length of the array.
Space Complexity: O(n) for the dp array (or O(n) for the tails array in the binary search method).
"""

from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        """
        Returns the length of the longest increasing subsequence.
        """
        if not nums:
            return 0
        
        # tails[i] is the smallest tail of all increasing subsequences of length i+1
        tails = []
        
        for num in nums:
            # Find the index of the first element in tails that is >= num
            idx = bisect_left(tails, num)
            
            # If num is greater than all elements in tails, append it
            if idx == len(tails):
                tails.append(num)
            else:
                # Otherwise, replace the first element that is >= num
                tails[idx] = num
        
        return len(tails)

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: [10,9,2,5,3,7,101,18] -> 4
    nums1 = [10,9,2,5,3,7,101,18]
    print(f"Test 1: {sol.lengthOfLIS(nums1)}")  # Expected: 4
    
    # Test case 2: [0,1,0,3,2,3] -> 4
    nums2 = [0,1,0,3,2,3]
    print(f"Test 2: {sol.lengthOfLIS(nums2)}")  # Expected: 4
    
    # Test case 3: [7,7,7,7,7,7,7] -> 1
    nums3 = [7,7,7,7,7,7,7]
    print(f"Test 3: {sol.lengthOfLIS(nums3)}")  # Expected: 1