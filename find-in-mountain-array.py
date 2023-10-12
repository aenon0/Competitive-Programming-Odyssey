# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        if length < 10:
            for i in range(length):
                if mountain_arr.get(i) == target:
                    return i
            return -1
            
        left, right = -1, length
        while left + 1 < right:
            mid = (left + right) // 2
            if mid - 1 >= 0 and mid < length and mountain_arr.get(mid - 1) < mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid
            else:
                right = mid
        peak = left + 1
        if target == mountain_arr.get(peak):
            return peak
        
        left = -1
        right = peak
        while left + 1 < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < target:
                left = mid
            else:
                right = mid
        if left + 1 < length and mountain_arr.get(left + 1) == target:
            return left + 1
        
        left = peak
        right = length
        while left + 1 < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) > target:
                left = mid
            else:
                right = mid
        if mountain_arr.get(left + 1) == target:
            return left + 1
        return -1
        # return 0