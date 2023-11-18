# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        level_dict = defaultdict(list)
        
        def bfs(node, level):
            if not node:
                return
            level_dict[level].append(node.val)
            if node.left:
                bfs(node.left, level + 1)
            if node.right:
                bfs(node.right, level + 1)
        
        bfs(root, 0)
        return [value for value in level_dict.values()]
