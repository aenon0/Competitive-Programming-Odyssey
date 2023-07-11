# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        length = 0 
        temp = head
        while temp:
            length += 1 
            temp = temp.next
        result = [0] * length

        temp = head
        stack = [ ]
        idx = 0 
        while temp:
            while stack and stack[-1][1] < temp.val:
                result[stack.pop()[0]] = temp.val
            stack.append((idx, temp.val))
            temp = temp.next
            idx += 1
        return result