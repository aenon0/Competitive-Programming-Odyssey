class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        left = -2
        right = num + 2
        
        while left + 1 < right:
            mid = (left + right) // 2
            if (mid - 1) + (mid) + (mid + 1) < num:
                left = mid
            elif (mid - 1) + (mid) + (mid + 1) > num:
                right = mid
            else:
                return [mid - 1, mid, mid + 1]
        return [ ]
            
