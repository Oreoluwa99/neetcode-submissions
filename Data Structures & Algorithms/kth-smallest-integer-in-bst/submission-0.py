# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

            # get the smallest value first (it lives all the way left)
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left 
            # now we have the smallest number
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val

            curr = curr.right