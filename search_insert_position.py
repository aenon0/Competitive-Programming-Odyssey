class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = -1
        right = len(nums)
        while left + 1 < right:
            mid = left + ((right - left) // 2)
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        return right
                
                
                
