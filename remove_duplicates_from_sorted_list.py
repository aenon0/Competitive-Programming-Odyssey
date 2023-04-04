# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        # if not head:
        #     return head
        if head and head.next:
            first, second = head, head.next
            while second:
                if first.val == second.val:
                    temp = second.next
                    first.next = temp
                    second = temp
                else:
                    first = first.next
                    second = second.next
        return head
