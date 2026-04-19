# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # use a queue to process nodes level by level
        queue = deque([root]) # start with the root
        
        result = []

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                # take all nodes from the current level
                node = queue.popleft() 
                level_nodes.append(node.val) # add their values to a list

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_nodes)

        return result