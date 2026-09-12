"""
Problem: 19. Remove Nth Node From End of List
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Solution: Use two pointers (fast and slow) with a dummy head to handle edge cases.
Move fast pointer n steps ahead, then move both until fast reaches the end.
Then remove the node after slow.
Time Complexity: O(L) where L is the length of the list.
Space Complexity: O(1).
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        Removes the nth node from the end of the list and returns the head.
        """
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        
        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # Move both until fast reaches the last node
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # Remove the nth node
        slow.next = slow.next.next
        
        return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print linked list
def print_linked_list(head):
    current = head
    values = []
    while current:
        values.append(str(current.val))
        current = current.next
    print(" -> ".join(values))

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: [1,2,3,4,5], n=2 -> [1,2,3,5]
    head1 = create_linked_list([1,2,3,4,5])
    print("Original list:", end=" ")
    print_linked_list(head1)
    result1 = sol.removeNthFromEnd(head1, 2)
    print("After removing 2nd from end:", end=" ")
    print_linked_list(result1)
    
    # Test case 2: [1], n=1 -> []
    head2 = create_linked_list([1])
    print("\nOriginal list:", end=" ")
    print_linked_list(head2)
    result2 = sol.removeNthFromEnd(head2, 1)
    print("After removing 1st from end:", end=" ")
    print_linked_list(result2)
    
    # Test case 3: [1,2], n=1 -> [1]
    head3 = create_linked_list([1,2])
    print("\nOriginal list:", end=" ")
    print_linked_list(head3)
    result3 = sol.removeNthFromEnd(head3, 1)
    print("After removing 1st from end:", end=" ")
    print_linked_list(result3)
    
    # Test case 4: [1,2], n=2 -> [2]
    head4 = create_linked_list([1,2])
    print("\nOriginal list:", end=" ")
    print_linked_list(head4)
    result4 = sol.removeNthFromEnd(head4, 2)
    print("After removing 2nd from end:", end=" ")
    print_linked_list(result4)