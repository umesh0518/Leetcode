# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start_head = ListNode(0)
        current = start_head
        carry = 0

        # run either no l1 or l2 or no carry
        while l1 or l2 or carry:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            digit = total % 10
            carry = total // 10

            # current node will now point to the sum
            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        #return the next of dummy head since it has inital fake node with 0 
        return start_head.next

            




        