# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    
    def firstBadVersion(self, n: int) -> int:
        # if n == 2:
        #     return 1
        left = 0
        right = n + 1
        mid = left + ((right - left) // 2)
        while left + 1 < right:
            mid = left + ((right - left) // 2)
            # print(left, mid, right)
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
        return right
            
        
