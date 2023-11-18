class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        nums = [nums[nums[index]] for index in range(len(nums))]    
        return nums
        
