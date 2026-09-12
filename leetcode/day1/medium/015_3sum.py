"""
Problem: 15. 3Sum
Link: https://leetcode.com/problems/3sum/
Solution: Sort the array and use two pointers for each element.
Time Complexity: O(n^2) where n is the length of the array.
Space Complexity: O(1) or O(n) depending on the sorting algorithm (we use Timsort in Python which uses O(n) space).
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Returns all unique triplets in the array which gives the sum of zero.
        """
        res = []
        nums.sort()
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        
        return res

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: nums = [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]
    nums1 = [-1,0,1,2,-1,-4]
    print(f"Test 1: {sol.threeSum(nums1)}")
    
    # Test case 2: nums = [] -> []
    nums2 = []
    print(f"Test 2: {sol.threeSum(nums2)}")
    
    # Test case 3: nums = [0] -> []
    nums3 = [0]
    print(f"Test 3: {sol.threeSum(nums3)}")
    
    # Test case 4: nums = [0,0,0] -> [[0,0,0]]
    nums4 = [0,0,0]
    print(f"Test 4: {sol.threeSum(nums4)}")
    
    # Test case 5: nums = [1,2,-2,-1] -> []
    nums5 = [1,2,-2,-1]
    print(f"Test 5: {sol.threeSum(nums5)}")