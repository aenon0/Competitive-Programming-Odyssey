# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans = 0 
        def dfs(self, node, parent, grandparent):
            if not node:
                return 

            if grandparent % 2 == 0:
                self.ans += node.val
                
            grandparent = parent
            parent = node.val

            if node.left:
                dfs(self, node.left, parent, grandparent)
            if node.right:
                dfs(self, node.right, parent, grandparent)
        dfs(self, root, 1, 1)
        return self.ans