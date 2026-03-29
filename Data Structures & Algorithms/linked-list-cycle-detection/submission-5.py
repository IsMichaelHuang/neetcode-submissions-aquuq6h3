# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Edge Case: If Head is none or singular node with no edge(s)
        if not head or not head.next:
            return False        
        
        turtle = head
        hare = head
        while hare.next:
            if hare.next.next:
                hare = hare.next.next
                turtle = turtle.next
            else:
                return False

            # Hare ptr looped back around and this is a cyclical list
            if hare == turtle:
                return True
        return False
        