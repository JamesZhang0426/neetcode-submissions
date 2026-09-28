# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:   
    def sametree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot or root.val != subRoot.val:
            return False
        return self.sametree(root.left,subRoot.left) and self.sametree(root.right,subRoot.right)



    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        cur = root
        q = deque()
        q.append(cur)

        while q:
            node = q.popleft()
            if node.val == subRoot.val:
                if self.sametree(node,subRoot):
                    return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return False


