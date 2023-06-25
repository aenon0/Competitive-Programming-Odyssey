# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dum1 = ListNode()
        dum2 = ListNode()
        temp1 = dum1
        temp2 = dum2
        temp = head
        while temp:
            if temp.val < x:
                temp1.next = ListNode(temp.val)
                temp1 = temp1.next
            else:
                temp2.next = ListNode(temp.val)
                temp2 = temp2.next
            temp = temp.next

        dum2 = dum2.next
        temp = dum1
        while temp and temp.next:
            temp = temp.next
        
        temp.next = dum2
        return dum1.next