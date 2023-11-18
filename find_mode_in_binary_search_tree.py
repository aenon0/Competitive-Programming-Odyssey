# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        freqs = defaultdict(int)
        def helper(node):
            if not node:
                return 
            freqs[node.val] += 1
            helper(node.left)
            helper(node.right)
        
        helper(root)
        
        ans = [ ]
        _max = max(freqs.values())
        for num in freqs.keys():
            if freqs[num] == _max:
                ans.append(num)
        return ans
            
