# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #split 
        #reverse second
        #merge

        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second_half = slow.next
        slow.next = None 

        prev = None 
        cur = second_half

        while cur:
            nextnode = cur.next
            cur.next=prev
            prev = cur
            cur = nextnode
        second_half = prev

        cur1 = head
        cur2 = second_half
        while cur1 and cur2:
            next1 = cur1.next
            next2 = cur2.next
            cur1.next = cur2
            cur2.next = next1
            cur1 = next1
            cur2 = next2
        
        