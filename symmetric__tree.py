# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        _nodes = [ ]
        def inorder(node):
            if not node:
                return 
            
            if not node.left:
                _nodes.append(node.left)
            if not node.right:
                _nodes.append(node.right)
            inorder(node.left)
            _nodes.append(node.val)
            inorder(node.right)
            if not node.left:
                _nodes.append(node.left)
            if not node.right:
                _nodes.append(node.right)
            
        inorder(root)
        
        if len(_nodes) % 2 == 0:
            return False
        middle = len(_nodes) // 2
        temp1 = _nodes[0: middle]
        temp2 = _nodes[middle + 1 : len(_nodes)]
        temp2.reverse()
        # print(_nodes)
        
        if temp1 == temp2:
            return True
        
        return False
