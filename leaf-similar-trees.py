# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [ ]
            if not node.right and not node.left:
                return [node.val]
            res = [ ]
            res.extend(dfs(node.left))
            res.extend(dfs(node.right))
            return res
        return dfs(root1) == dfs(root2)