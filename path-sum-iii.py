# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: 
            return 0

        def dfs(node, _sum):
            if not node:
                return 0 
            count = 0 
            if node.val == _sum:
                count += 1
            count += dfs(node.left, _sum - node.val)
            count += dfs(node.right, _sum - node.val)
            return count 
            
        c = dfs(root, targetSum)
        c += self.pathSum(root.left, targetSum)
        c += self.pathSum(root.right, targetSum)
        print(root.val, c)
        return c