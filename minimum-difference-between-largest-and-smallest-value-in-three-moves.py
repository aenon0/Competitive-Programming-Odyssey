class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        min_diff = float("inf")
        left = 0 
        right = -4
        while right < 0:
            min_diff = min(min_diff, nums[right] - nums[left])
            left += 1
            right += 1
        return min_diff