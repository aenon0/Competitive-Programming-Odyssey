# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        def dfs(self, node):
            queue = deque()
            queue.append(node)
            self.averages = [ ]
            while queue:
                size = len(queue)
                total = 0 
                for _ in range(size):
                    curr = queue.popleft()
                    total += curr.val
                    # averages.append(sum(queue[:])/ len(queue))
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                self.averages.append(total / size)
            
        dfs(self, root)
        return self.averages