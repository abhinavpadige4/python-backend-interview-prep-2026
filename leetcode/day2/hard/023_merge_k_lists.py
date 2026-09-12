"""
Problem: 23. Merge k Sorted Lists
Link: https://leetcode.com/problems/merge-k-sorted-lists/
Solution: Use a min-heap to efficiently get the smallest element from the heads of all lists.
Time Complexity: O(N log k) where N is the total number of nodes and k is the number of lists.
Space Complexity: O(k) for the heap.
"""

import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        """
        Merge k sorted linked lists and return the head of the merged list.
        """
        # Create a min-heap
        heap = []
        # Push the first node of each list into the heap
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i, lst))
        
        dummy = ListNode()
        current = dummy
        
        while heap:
            # Pop the smallest node
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            # If there is a next node in the same list, push it into the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
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
    
    # Test case 1: [[1,4,5],[1,3,4],[2,6]] -> [1,1,2,3,4,4,5,6]
    lists1 = [
        create_linked_list([1,4,5]),
        create_linked_list([1,3,4]),
        create_linked_list([2,6])
    ]
    print("Input lists:")
    for i, lst in enumerate(lists1):
        print(f"List {i+1}:", end=" ")
        print_linked_list(lst)
    result1 = sol.mergeKLists(lists1)
    print("Merged list:", end=" ")
    print_linked_list(result1)
    
    # Test case 2: [] -> []
    lists2 = []
    print("\nInput lists: []")
    result2 = sol.mergeKLists(lists2)
    print("Merged list:", end=" ")
    print_linked_list(result2)
    
    # Test case 3: [[]] -> []
    lists3 = [create_linked_list([])]
    print("\nInput lists: [[]]")
    result3 = sol.mergeKLists(lists3)
    print("Merged list:", end=" ")
    print_linked_list(result3)