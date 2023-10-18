class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        diff, extension = (max(nums) - min(nums)), (2 * k)
        if diff > extension:
            return diff - extension

        return 0