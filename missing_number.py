class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maximum= max(nums)
        for num in range(maximum+2):
            if num not in nums:
                return num
