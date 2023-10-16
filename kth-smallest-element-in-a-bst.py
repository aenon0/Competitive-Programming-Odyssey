# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        _list = [ ]
        def inorder(node):
            if not node:
                return
            if node.left:
                inorder(node.left)
            _list.append(node.val)
            if node.right:
                inorder(node.right)
        
        inorder(root)
        
        return _list[k - 1]