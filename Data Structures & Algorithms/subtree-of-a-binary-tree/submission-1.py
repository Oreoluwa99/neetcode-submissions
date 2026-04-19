# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return True
        if not root:
            return False
        
        # check if they are the same trees
        if self.isSameTree(root, subRoot):
            return True
        
        # check left or right
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    # first we can check is they are actually the same tree
    def isSameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
        else:
            return False
