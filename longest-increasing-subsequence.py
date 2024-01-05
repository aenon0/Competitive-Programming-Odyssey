class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums.insert(0, -inf)
        lengths = [1] * len(nums)
        lengths[0] = 0
        for i in range(1, len(nums)):
            _max = -inf
            for j in range(i):
                if nums[j] < nums[i]:
                    _max = max(_max, lengths[j] + 1)
            lengths[i] = max(lengths[i], _max)
        
        # print(lengths)
        return max(lengths)