# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        p1 = list1
        p2 = list2
        new_list_copy = new_list = ListNode(0)# a dum node
        while p1 and p2:
            temp1 = p1.next
            temp2 = p2.next
            if p1.val <= p2.val:
                p1.next = None
                new_list_copy.next = p1
                new_list_copy = new_list_copy.next
                p1 = temp1
            else:
                p2.next = None
                new_list_copy.next = p2
                new_list_copy = new_list_copy.next
                p2 = temp2
        if p1:
            new_list_copy.next = p1
        if p2:
            new_list_copy.next = p2
        return new_list.next
        
                
        
