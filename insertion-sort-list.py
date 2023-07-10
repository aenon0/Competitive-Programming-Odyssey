# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-6000)
        curr = head
        
        while curr:
            prev = dummy
            new_node = ListNode(curr.val)
            while prev and prev.next and prev.next.val < new_node.val:
                prev = prev.next
                
            new_node.next = prev.next
            prev.next = new_node
            # print(dummy)
            curr = curr.next
        
        return dummy.next