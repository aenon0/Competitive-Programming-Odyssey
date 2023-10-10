# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = [ ]
        def helper(root):
            if not root:
                return 
            helper(root.left)
            inorder.append(root.val)
            helper(root.right)
            
        helper(root)
        for indx in range(len(inorder) - 1):
            if inorder[indx] >= inorder[indx + 1]:
                return False
        return True