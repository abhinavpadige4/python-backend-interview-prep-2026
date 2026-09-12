"""
Problem: 141. Linked List Cycle
Link: https://leetcode.com/problems/linked-list-cycle/
Solution: Use Floyd's Tortoise and Hare algorithm (fast and slow pointers) to detect a cycle.
Time Complexity: O(n) where n is the number of nodes in the list.
Space Complexity: O(1) - only two pointers used.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Returns True if there is a cycle in the linked list, False otherwise.
        """
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True

# Helper function to create a linked list from a list and optionally create a cycle
def create_linked_list(lst, pos=-1):
    """
    Creates a linked list from a list of values.
    If pos >= 0, creates a cycle by connecting the last node to the node at index pos.
    """
    if not lst:
        return None
    
    nodes = []
    for val in lst:
        nodes.append(ListNode(val))
    
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    if pos >= 0 and pos < len(nodes):
        nodes[-1].next = nodes[pos]
    
    return nodes[0] if nodes else None

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: [3,2,0,-4] with cycle at index 1 (node with value 2)
    head1 = create_linked_list([3,2,0,-4], pos=1)
    print("Test 1 (with cycle):", sol.hasCycle(head1))  # Expected: True
    
    # Test case 2: [1,2] with cycle at index 0 (node with value 1)
    head2 = create_linked_list([1,2], pos=0)
    print("Test 2 (with cycle):", sol.hasCycle(head2))  # Expected: True
    
    # Test case 3: [1] with no cycle
    head3 = create_linked_list([1], pos=-1)
    print("Test 3 (no cycle):", sol.hasCycle(head3))  # Expected: False
    
    # Test case 4: Empty list
    head4 = create_linked_list([])
    print("Test 4 (empty list):", sol.hasCycle(head4))  # Expected: False
    
    # Test case 5: [1,2,3,4,5] with no cycle
    head5 = create_linked_list([1,2,3,4,5], pos=-1)
    print("Test 5 (no cycle):", sol.hasCycle(head5))  # Expected: False