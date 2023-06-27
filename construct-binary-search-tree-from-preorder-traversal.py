# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.idx = 0 
        def build_bst(bound):
            if self.idx == len(preorder) or preorder[self.idx] > bound: return None
            node = TreeNode(preorder[self.idx])
            self.idx += 1
            node.left = build_bst(node.val)
            node.right = build_bst(bound)
            return node
        return build_bst(inf)