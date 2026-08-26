"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}
        hashmap[None] = None
        cur = head
        while cur:
            newNode = Node(0)
            newNode.val = cur.val
            hashmap[cur] = newNode 
            cur= cur.next
        
        cur = head
        newhead = hashmap[head]
        newcur = newhead
        while cur:
            newcur.next = hashmap[cur.next]
            newcur.random = hashmap[cur.random]
            cur = cur.next
            newcur = newcur.next

        return newhead


        