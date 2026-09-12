"""
Problem: 146. LRU Cache
Link: https://leetcode.com/problems/lru-cache/
Solution: Use a combination of a doubly linked list and a hash map (dictionary) for O(1) operations.
Time Complexity: O(1) for both get and put.
Space Complexity: O(capacity) for storing the cache.
"""

class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with positive size capacity.
        """
        self.capacity = capacity
        self.cache = {}  # Map key to node
        # Dummy head and tail nodes to avoid edge cases
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        """
        Add a node right after the head.
        """
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """
        Remove a node from the linked list.
        """
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node):
        """
        Move a node to the head (most recently used).
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        Pop the current tail (least recently used).
        Returns the popped node.
        """
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key: int) -> int:
        """
        Returns the value of the key if the key exists, otherwise -1.
        """
        node = self.cache.get(key)
        if not node:
            return -1
        # Move the accessed node to the head (most recently used)
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Update the value of the key if the key exists.
        Otherwise, add the key-value pair to the cache.
        If the cache reaches its capacity, evict the least recently used item.
        """
        node = self.cache.get(key)
        if node:
            # Update the value and move to head
            node.value = value
            self._move_to_head(node)
        else:
            # Create a new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            
            # Check if we exceed capacity
            if len(self.cache) > self.capacity:
                # Pop the tail (least recently used)
                tail = self._pop_tail()
                del self.cache[tail.key]

# Test cases
if __name__ == "__main__":
    # Test case 1
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # returns 1
    cache.put(3, 3)      # evicts key 2
    print(cache.get(2))  # returns -1 (not found)
    cache.put(4, 4)      # evicts key 1
    print(cache.get(1))  # returns -1 (not found)
    print(cache.get(3))  # returns 3
    print(cache.get(4))  # returns 4
    
    # Test case 2: Single capacity
    cache2 = LRUCache(1)
    cache2.put(2, 1)
    print(cache2.get(2))  # returns 1
    cache2.put(3, 2)      # evicts key 2
    print(cache2.get(2))  # returns -1
    print(cache2.get(3))  # returns 2