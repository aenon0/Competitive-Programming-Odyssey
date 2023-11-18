class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        
        left = -1
        right = len(nums)
        while left + 1 < right:
            mid = left + ((right - left) // 2)
            if nums[mid] < target:
                left = mid
            else:
                right = mid     
        ans = [right]
        end = right
        for indx in range(right + 1, len(nums)):
            if nums[indx] == target:
                end = indx
                
        ans.append(end)
        
        return ans
        
