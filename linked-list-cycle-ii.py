# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # using floyd's method
        if not head:
            return 
        tor, hare = head, head
        flag = False
        while hare:
            if tor == hare and flag:
                break
            if not hare.next or not hare.next.next:
                return 
            tor = tor.next
            hare = hare.next.next
            flag = True 

        # print(head.val, hare.val)
        while head != hare:
            head = head.next
            hare = hare.next
        return head