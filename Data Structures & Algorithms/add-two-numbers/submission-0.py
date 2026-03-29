# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_one = l1
        cur_two = l2
        carry = 0

        dummy = ListNode(0, None)
        cur = dummy
        while cur_one or cur_two or carry:
            value_one = cur_one.val if cur_one else 0
            value_two = cur_two.val if cur_two else 0

            total = value_one + value_two + carry
            carry = total // 10 # Get the floor
            digit = total % 10

            cur.next = ListNode(digit)
            cur = cur.next

            cur_one = cur_one.next if cur_one else None
            cur_two = cur_two.next if cur_two else None
        
        return dummy.next

        