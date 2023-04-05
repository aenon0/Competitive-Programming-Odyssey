# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ans = sum_list = ListNode(-1)
        carry = 0 
        while l1 or l2:
            # print(carry)
            _sum = 0 
            if l1:
                _sum += l1.val
                l1 = l1.next
            if l2:
                _sum += l2.val
                l2 = l2.next
            
            _sum += carry 
            
            
            carry = _sum // 10
            _sum %= 10
            
            sum_list.next = ListNode(_sum)
            sum_list = sum_list.next
        if carry != 0:
            sum_list.next = ListNode(carry)
            
        return ans.next
            
            
        
        
