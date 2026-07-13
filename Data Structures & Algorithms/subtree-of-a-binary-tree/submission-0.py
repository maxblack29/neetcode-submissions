# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        elif root:
            if self.isSametree(root, subRoot) == True:
                return True
            else: 
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def isSametree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is not None and q is None:
            return False
        if p is None and q is not None:
            return False
        if p.val == q.val:
            return self.isSametree(p.left, q.left) and self.isSametree(p.right, q.right)