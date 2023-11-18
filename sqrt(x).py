class Solution:
    def mySqrt(self, num: int) -> int:
        if num == 1 or num == 0:
            return num
        right = num
        left = -1
        while left + 1 < right:
            mid = left + ((right - left) // 2)
            ans = mid ** 2
            if ans > num:
                right = mid
            elif ans <= num:
                left = mid
        return left 
           
