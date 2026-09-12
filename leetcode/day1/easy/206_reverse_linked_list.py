"""
Problem: 206. Reverse Linked List
Link: https://leetcode.com/problems/reverse-linked-list/
Solution: Iterative and recursive approaches to reverse a singly linked list.
Time Complexity: O(n) for both iterative and recursive
Space Complexity: O(1) for iterative, O(n) for recursive (due to call stack)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Iterative approach to reverse a linked list.
        """
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    
    def reverseListRecursive(self, head: ListNode) -> ListNode:
        """
        Recursive approach to reverse a linked list.
        """
        if not head or not head.next:
            return head
        p = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return p

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
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: [1,2,3,4,5]
    head1 = create_linked_list([1,2,3,4,5])
    print("Original list:")
    print_linked_list(head1)
    reversed1 = sol.reverseList(head1)
    print("Reversed list (iterative):")
    print_linked_list(reversed1)
    
    # Test case 2: [1,2]
    head2 = create_linked_list([1,2])
    print("\nOriginal list:")
    print_linked_list(head2)
    reversed2 = sol.reverseListRecursive(head2)
    print("Reversed list (recursive):")
    print_linked_list(reversed2)
    
    # Test case 3: Empty list
    head3 = create_linked_list([])
    print("\nOriginal list (empty):")
    print_linked_list(head3)
    reversed3 = sol.reverseList(head3)
    print("Reversed list (empty):")
    print_linked_list(reversed3)
    
    # Test case 4: Single element
    head4 = create_linked_list([10])
    print("\nOriginal list (single):")
    print_linked_list(head4)
    reversed4 = sol.reverseListRecursive(head4)
    print("Reversed list (single):")
    print_linked_list(reversed4)