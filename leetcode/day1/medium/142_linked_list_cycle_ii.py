"""
Problem: 142. Linked List Cycle II
Link: https://leetcode.com/problems/linked-list-cycle-ii/
Solution: Use Floyd's Tortoise and Hare to detect cycle, then find the start of the cycle.
Time Complexity: O(n) where n is the number of nodes in the list.
Space Complexity: O(1).
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        Returns the node where the cycle begins, or None if there is no cycle.
        """
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        
        # First, detect if there is a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            # No cycle
            return None
        
        # Now, find the start of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow

# Helper function to create a linked list from a list and optionally create a cycle
def create_linked_list(lst, pos=-1):
    """
    Creates a linked list from a list of values.
    If pos >= 0, creates a cycle by connecting the last node to the node at index pos.
    Returns the head of the list and the node at index pos (if pos>=0) for testing.
    """
    if not lst:
        return None, None
    
    nodes = []
    for val in lst:
        nodes.append(ListNode(val))
    
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    cycle_node = None
    if pos >= 0 and pos < len(nodes):
        nodes[-1].next = nodes[pos]
        cycle_node = nodes[pos]
    
    return nodes[0], cycle_node

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: [3,2,0,-4] with cycle at index 1 (node with value 2)
    head1, cycle_node1 = create_linked_list([3,2,0,-4], pos=1)
    result1 = sol.detectCycle(head1)
    print("Test 1:", result1.val if result1 else None)  # Expected: 2
    
    # Test case 2: [1,2] with cycle at index 0 (node with value 1)
    head2, cycle_node2 = create_linked_list([1,2], pos=0)
    result2 = sol.detectCycle(head2)
    print("Test 2:", result2.val if result2 else None)  # Expected: 1
    
    # Test case 3: [1] with no cycle
    head3, cycle_node3 = create_linked_list([1], pos=-1)
    result3 = sol.detectCycle(head3)
    print("Test 3:", result3.val if result3 else None)  # Expected: None
    
    # Test case 4: Empty list
    head4, cycle_node4 = create_linked_list([])
    result4 = sol.detectCycle(head4)
    print("Test 4:", result4.val if result4 else None)  # Expected: None
    
    # Test case 5: [1,2,3,4,5] with no cycle
    head5, cycle_node5 = create_linked_list([1,2,3,4,5], pos=-1)
    result5 = sol.detectCycle(head5)
    print("Test 5:", result5.val if result5 else None)  # Expected: None