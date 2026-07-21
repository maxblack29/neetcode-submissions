# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def BSTcheck(root, low, high):
            curr = root
            if curr is None:
                return True
            if curr.val <= low or curr.val >= high:
                return False
            return BSTcheck(curr.left, low, curr.val) and BSTcheck(curr.right, curr.val, high)

        return BSTcheck(root, -1001, 1001)