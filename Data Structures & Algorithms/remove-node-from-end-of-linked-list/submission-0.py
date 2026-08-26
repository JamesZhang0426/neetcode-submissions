# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0 
        cur = head
        while cur:
            length+= 1
            cur = cur.next
        todelete = length - n
        if todelete == 0:
                return head.next
        cur = head
        count = 0 
        while cur:
            if count +1 == todelete:
                cur.next = cur.next.next
                break
            else:
                cur = cur.next 
                count +=1 
        return head


            