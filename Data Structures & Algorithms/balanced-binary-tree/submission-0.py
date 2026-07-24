# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance = True
        def get_height(node):
            nonlocal balance
            if not node:
                return 0
            left_h = get_height(node.left)
            right_h = get_height(node.right)

            if abs(left_h-right_h) > 1:
                balance = False
            
            return 1 + max(left_h, right_h) # add parent node
        
        get_height(root)
        return balance
            