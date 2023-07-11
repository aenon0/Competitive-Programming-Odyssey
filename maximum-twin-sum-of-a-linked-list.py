# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # getting the middle pointer using fast and slow pointer
        before_middle = fast = head
        while fast and fast.next and fast.next.next:
            before_middle, fast = before_middle.next, fast.next.next

        # cutting the connection between the first and second half of the linkedlist
        middle = before_middle.next
        before_middle.next = None
        
        # reversing the second half
        prev, curr, nxt = None, middle, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # looping through both the first half(head) and the second reversed half(prev) and finding the max sum
        max_twin_sum = 0
        while prev:
            _sum = prev.val + head.val
            max_twin_sum = max(max_twin_sum, _sum)
            prev = prev.next
            head = head.next
        
        return max_twin_sum