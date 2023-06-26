# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # using floyd's method O(1) space
        if not head:
            return False

        tor, hare = head, head.next
        while hare:
            if hare == tor:
                return True
            tor = tor.next
            if not hare.next or not hare.next.next:
                return False
            hare = hare.next.next
        return False