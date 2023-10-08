# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = None
        self.found = False
        def postorder(node):
            if not node:
                return set()
            res = set()
    
            res.update(postorder(node.left))
            res.update(postorder(node.right))
            res.add(node.val)

            if (p.val in res) and (q.val in res) and (not self.found):
                self.lca = node
                self.found = True
            return res

        postorder(root)
        return self.lca