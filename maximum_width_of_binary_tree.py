# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        queue1 = deque()
        queue2 = deque()
        max_width = 1
        
        queue1.append([1, root])
        
        while queue1 or queue2:
            
            while queue1:
                max_width = max(max_width, (queue1[-1][0] -  queue1[0][0] + 1))
                temp1 = queue1.popleft()
                num, temp = temp1[0] ,temp1[1] 

                if temp.left:
                    queue2.append([2 * num - 1 , temp.left])
                if temp.right:
                    queue2.append([2 * num, temp.right])

            queue1, queue2 = queue2, queue1
            
        return max_width
