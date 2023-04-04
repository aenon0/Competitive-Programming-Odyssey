# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        firsts_tail = seconds_head = fast = head
        while fast and fast.next:
            firsts_tail = seconds_head
            seconds_head = seconds_head.next
            fast = fast.next.next
        # print(firsts_tail, seconds_head, fast)
        if fast != None:
            seconds_head = seconds_head.next
        firsts_tail.next = None
        
        prev = None
        nxt = seconds_head
        while nxt:
            temp = nxt.next 
            nxt.next = prev
            prev = nxt
            nxt = temp
            
            
        p1 = prev
        p2 = head
        while p1 and p2:
            if p1.val == p2.val:
                p1 = p1.next
                p2 = p2.next
            else:
                return False
        return True
        
