# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode(0, head)
        prev = curr = dum
        while curr:
            while curr and curr.next and curr.val == curr.next.val:
                curr = curr.next
            if prev.next == curr:
                prev = curr
            else:
                prev.next = curr.next

            curr = curr.next
        return dum.next