# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [] # add in in order traversal then pop later
        curr = root
        count = 0

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left # go down to left

            curr = stack.pop() # process leftmost node
            count += 1
            if k == count:
                return curr.val

            curr = curr.right # move to right most child