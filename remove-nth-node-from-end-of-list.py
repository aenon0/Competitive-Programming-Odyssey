# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum = ListNode(0, head)
        temp = dum
        size = -1
        while temp:
            size += 1
            temp = temp.next
        
        before = dum
        # print(size, n)
        for _ in range(size - n):
            before = before.next
        if before == dum:
            return head.next

        if before and before.next and before.next.next:
            before.next = before.next.next
        else:
            before.next = None
        return head