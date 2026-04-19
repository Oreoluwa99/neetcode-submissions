# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            
            left_length = dfs(node.left)
            if left_length == -1:
                return -1
            
            right_length = dfs(node.right)
            if right_length == -1:
                return -1
            
            diff = abs(right_length - left_length)
            if diff > 1:
                return -1
            
            return 1 + max(left_length, right_length)
        return dfs(root) != -1
