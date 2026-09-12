"""
Problem: 2. Add Two Numbers
Link: https://leetcode.com/problems/add-two-numbers/
Solution: Add two numbers represented by linked lists in reverse order.
We traverse both lists, add corresponding digits along with carry, and create a new list.
Time Complexity: O(max(m, n)) where m and n are the lengths of the two lists.
Space Complexity: O(max(m, n)) for the new list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Returns the sum of two numbers represented by linked lists.
        """
        dummy = ListNode()
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            current.next = ListNode(digit)
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next

# Helper function to create a linked list from a list (in reverse order as per problem)
def create_linked_list(lst):
    """
    Creates a linked list from a list of integers, where the first element is the head.
    Note: The problem stores numbers in reverse order, so we create the list in the given order.
    """
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print linked list (for verification)
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
    
    # Test case 1: l1 = [2,4,3], l2 = [5,6,4] -> [7,0,8]
    l1 = create_linked_list([2,4,3])
    l2 = create_linked_list([5,6,4])
    print("List 1:", end=" ")
    print_linked_list(l1)
    print("List 2:", end=" ")
    print_linked_list(l2)
    result = sol.addTwoNumbers(l1, l2)
    print("Sum:", end=" ")
    print_linked_list(result)
    
    # Test case 2: l1 = [0], l2 = [0] -> [0]
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    print("\nList 1:", end=" ")
    print_linked_list(l1)
    print("List 2:", end=" ")
    print_linked_list(l2)
    result = sol.addTwoNumbers(l1, l2)
    print("Sum:", end=" ")
    print_linked_list(result)
    
    # Test case 3: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] -> [8,9,9,9,0,0,0,1]
    l1 = create_linked_list([9,9,9,9,9,9,9])
    l2 = create_linked_list([9,9,9,9])
    print("\nList 1:", end=" ")
    print_linked_list(l1)
    print("List 2:", end=" ")
    print_linked_list(l2)
    result = sol.addTwoNumbers(l1, l2)
    print("Sum:", end=" ")
    print_linked_list(result)