# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        levels = defaultdict(list)
        def collect(node, level):
            if not node:
                return 
            levels[level].append(node.val)
            collect(node.left, level + 1)
            collect(node.right, level + 1)

        def isEvenOdd(node, level):
            if not node:
                return True
            if (level % 2 == 0 and node.val % 2 == 0) or (level % 2 != 0 and node.val % 2 != 0):
                    return False
            return isEvenOdd(node.left, level + 1) and isEvenOdd(node.right, level + 1)

        collect(root, 0)

        for key in levels.keys():
            if len(levels[key]) != len(set(levels[key])):
                return False
            if key % 2 == 0:
                if levels[key] != sorted(levels[key]):
                    print("a")
                    return False
            else:
                 if levels[key] != sorted(levels[key], reverse = True):
                    return False
        
        return isEvenOdd(root, 0)