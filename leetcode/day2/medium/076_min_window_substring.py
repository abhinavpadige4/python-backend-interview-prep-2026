"""
Problem: 76. Minimum Window Substring
Link: https://leetcode.com/problems/minimum-window-substring/
Solution: Use sliding window with two pointers and a hash map to track characters.
Time Complexity: O(|s| + |t|) where s and t are the input strings.
Space Complexity: O(|s| + |t|) for the hash maps.
"""

from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Returns the minimum window in s which will contain all the characters in t.
        If there is no such window, return empty string.
        """
        if not t or not s:
            return ""
        
        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = defaultdict(int)
        for char in t:
            dict_t[char] += 1
        
        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)
        
        # Left and right pointer
        l, r = 0, 0
        
        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        formed = 0
        
        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = defaultdict(int)
        
        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None
        
        while r < len(s):
            # Add one character from the right to the window
            character = s[r]
            window_counts[character] += 1
            
            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            
            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]
                
                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                
                # Move the left pointer ahead, this would help to look for a new window.
                l += 1    
            
            # Keep expanding the window once we are done contracting.
            r += 1    
        
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: s = "ADOBECODEBANC", t = "ABC" -> "BANC"
    s1 = "ADOBECODEBANC"
    t1 = "ABC"
    print(f"Test 1: '{sol.minWindow(s1, t1)}'")  # Expected: "BANC"
    
    # Test case 2: s = "a", t = "a" -> "a"
    s2 = "a"
    t2 = "a"
    print(f"Test 2: '{sol.minWindow(s2, t2)}'")  # Expected: "a"
    
    # Test case 3: s = "a", t = "aa" -> ""
    s3 = "a"
    t3 = "aa"
    print(f"Test 3: '{sol.minWindow(s3, t3)}'")  # Expected: ""