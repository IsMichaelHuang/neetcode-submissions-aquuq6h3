"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_copy = { None: None }

        # Two pass apporach

        # Create a copy of all nodes present
        cur = head
        while cur:
            copy = Node(cur.val)
            old_to_copy[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            # Get the current node from the hashtable
            copy_node = old_to_copy[cur]

            # Populate it with the original next/random
            copy_node.next = old_to_copy[cur.next]
            copy_node.random = old_to_copy[cur.random]

            # Move ptr
            cur = cur.next
        
        return old_to_copy[head]
        