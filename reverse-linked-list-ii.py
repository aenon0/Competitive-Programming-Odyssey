# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:     
        if left == right:
            return head
        
        dummy_node = ListNode(0, head)
        f_start = dummy_node
        for i in range(left - 1):
            if f_start:
                f_start = f_start.next
            else:
                f_start = None
        # print(f_start.val)   
        s_end = head
        for i in range(right - 1):
            if s_end:
                s_end = s_end.next
        # print(s_end.val)
        s_start = f_start.next
        f_end = s_end.next
        # print(f_end.val)
        if f_start.next:
            f_start.next = None
        if s_end.next:
            s_end.next = None 
        # print(s_start.val)
        prev = None
        nxt = s_start
        while nxt:
            temp = nxt.next
            nxt.next = prev
            prev = nxt
            nxt = temp
        
        f_start.next = prev
        # print(f_start)
        while f_start and f_start.next:
            f_start = f_start.next
        
        f_start.next = f_end
        
        return dummy_node.next