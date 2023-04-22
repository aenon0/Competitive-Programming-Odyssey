# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.string = ""
        def preorder(self, node):
            if not node:
                return 
            self.string += str(node.val)
            if node.left:
                self.string += "("
                preorder(self, node.left)
                self.string += ")"
            if node.right:
                if not node.left:
                    self.string += "()"
                self.string += "("
                preorder(self, node.right)
                self.string += ")"

        preorder(self, root)
        return self.string