"""
Problem: 124. Binary Tree Maximum Path Sum
Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
Solution: Use recursion to compute the maximum path sum for each node.
The maximum path sum through a node is node.val + max(left, 0) + max(right, 0).
We update a global maximum during the recursion.
Time Complexity: O(n) where n is the number of nodes.
Space Complexity: O(h) where h is the height of the tree (recursion stack).
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        Returns the maximum path sum of the binary tree.
        """
        self.max_sum = float('-inf')
        
        def max_gain(node):
            if not node:
                return 0
            
            # Max sum on the left and right sub-trees of node
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # Price to start a new path where `node` is the highest point
            price_newpath = node.val + left_gain + right_gain
            
            # Update max_sum if it's better to start a new path
            self.max_sum = max(self.max_sum, price_newpath)
            
            # For recursion, return the max gain if continue the same path
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return self.max_sum

# Helper function to build a tree from a list (level order)
def build_tree(values):
    """
    Builds a binary tree from a list of values (level order).
    None indicates a missing node.
    """
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if values[i] is not None:
            left = TreeNode(values[i])
            node.left = left
            queue.append(left)
        i += 1
        if i < len(values) and values[i] is not None:
            right = TreeNode(values[i])
            node.right = right
            queue.append(right)
        i += 1
    return root

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: [1,2,3] -> 6
    root1 = build_tree([1,2,3])
    print(f"Test 1: {sol.maxPathSum(root1)}")  # Expected: 6
    
    # Test case 2: [-10,9,20,null,null,15,7] -> 42
    root2 = build_tree([-10,9,20,None,None,15,7])
    print(f"Test 2: {sol.maxPathSum(root2)}")  # Expected: 42
    
    # Test case 3: [-3] -> -3
    root3 = build_tree([-3])
    print(f"Test 3: {sol.maxPathSum(root3)}")  # Expected: -3
    
    # Test case 4: [2,-1] -> 2
    root4 = build_tree([2,-1])
    print(f"Test 4: {sol.maxPathSum(root4)}")  # Expected: 2