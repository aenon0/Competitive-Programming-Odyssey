class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for num_index in range( 1, len(nums)):
            nums[num_index] += nums[num_index - 1]
        
        return nums
