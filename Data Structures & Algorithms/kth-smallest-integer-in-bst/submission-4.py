# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def traverse(node, k_left):
            if not node:
                return None, k_left
            
            left_res, k_left = traverse(node.left, k_left)
            if left_res is not None:
                return left_res, k_left

            k_left -= 1
            if k_left == 0:
                return node.val, k_left

            return traverse(node.right, k_left)
        ans, _ = traverse(root, k)
        return ans