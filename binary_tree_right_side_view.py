# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
        ans = [ ]
        for value in level_dict.values():
            ans.append(value[-1])
        return ans
       
