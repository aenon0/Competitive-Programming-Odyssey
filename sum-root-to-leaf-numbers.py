# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        to_be = [ ]
        self.ans = 0
        def dfs(self, node):
            to_be.append(str(node.val))

            if not node.left and not node.right:
                self.ans += int("".join(to_be))
                return       

            if node.left:
                dfs(self, node.left)
                to_be.pop()
            if node.right:
                dfs(self, node.right)
                to_be.pop()

        dfs(self, root)
        return self.ans