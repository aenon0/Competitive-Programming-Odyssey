# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        temp = head
        length = 0 
        # getting the length of the linked list
        while temp:
            temp = temp.next
            length += 1
        # gotta take the modulo b/c that's the pattern the example leads us to
        k %= length
        
        if not k:
            return head
        #finding the new tail and consequently the new head
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        print(new_tail, new_head)
        temp = new_head
        while temp and temp.next:
            temp = temp.next
        if temp:
            temp.next = head
        
        return new_head