"""
Problem: 21. Merge Two Sorted Lists
Link: https://leetcode.com/problems/merge-two-sorted-lists/
Solution: Merge two sorted linked lists by comparing nodes and building a new list.
Time Complexity: O(n + m) where n and m are the lengths of the two lists.
Space Complexity: O(1) - we only use a few pointers, not counting the output list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        """
        Merge two sorted linked lists and return the head of the merged list.
        """
        dummy = ListNode()
        current = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach the remaining part of either list
        current.next = list1 if list1 else list2
        
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
    
    # Test case 1: [1,2,4] and [1,3,4]
    l1 = create_linked_list([1,2,4])
    l2 = create_linked_list([1,3,4])
    print("List 1:", end=" ")
    print_linked_list(l1)
    print("List 2:", end=" ")
    print_linked_list(l2)
    merged = sol.mergeTwoLists(l1, l2)
    print("Merged:", end=" ")
    print_linked_list(merged)
    
    # Test case 2: Empty lists
    l3 = create_linked_list([])
    l4 = create_linked_list([])
    print("\nList 1 (empty):", end=" ")
    print_linked_list(l3)
    print("List 2 (empty):", end=" ")
    print_linked_list(l4)
    merged2 = sol.mergeTwoLists(l3, l4)
    print("Merged (empty):", end=" ")
    print_linked_list(merged2)
    
    # Test case 3: One empty, one non-empty
    l5 = create_linked_list([])
    l6 = create_linked_list([0])
    print("\nList 1 (empty):", end=" ")
    print_linked_list(l5)
    print("List 2:", end=" ")
    print_linked_list(l6)
    merged3 = sol.mergeTwoLists(l5, l6)
    print("Merged:", end=" ")
    print_linked_list(merged3)