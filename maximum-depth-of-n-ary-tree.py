"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        self.max_length = 0 
        self.length = 0 
        def dfs(self, node):
            self.length += 1
            
            if node.children == [ ]:
                self.max_length = max(self.max_length, self.length)
                return
            
            for child in node.children:
                dfs(self, child)
                self.length -= 1
        
        dfs(self, root)
        return self.max_length