# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findFrequentTreeSum(self, root):
        sum_freq = defaultdict(int)
        def recursion(node):
            _sum = 0
            if not node:
                return 0 
            
            _sum += (node.val + recursion(node.left) + recursion(node.right))
                
            sum_freq[_sum] += 1
            return _sum
            
        recursion(root)
        result = [key for key in sum_freq.keys() if sum_freq[key] == max(sum_freq.values())]
        return result
            
            
