# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def max_thievery(flag, node):
            if not node:
                return 0

            result = 0 
            if flag:
                result += max((node.val + max_thievery(not flag, node.left) + max_thievery(not flag, node.right)), (max_thievery(flag, node.left) + max_thievery(flag, node.right)))

            else:
                result += max(max_thievery(not flag, node.left) + max_thievery(not flag, node.right), max_thievery(flag, node.left) + max_thievery(flag, node.right))
            return result

        return max(max_thievery(True, root), max_thievery(False, root))