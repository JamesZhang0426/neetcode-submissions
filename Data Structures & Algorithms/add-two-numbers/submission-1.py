# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        newhead = ListNode(0)
        cur = newhead
        carry = 0 
        while l1 or l2 or carry: 
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            totalval = (v1+v2+carry)%10
            carry = (v1+v2+carry)//10
            newnode = ListNode(totalval)
            cur.next = newnode
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            cur = cur.next
        return newhead.next
