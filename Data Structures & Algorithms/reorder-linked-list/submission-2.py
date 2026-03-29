# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find mid point
        tortoise, hare = head, head.next
        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
        
        # Reverse second half of list
        second = tortoise.next
        prev = tortoise.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # Merge two list back together
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        