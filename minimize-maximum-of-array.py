class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        _max = running_sum = 0 
        for i in range(len(nums)):
            running_sum += nums[i]
            _max = max(_max, running_sum / (i + 1))
        return math.ceil(_max)