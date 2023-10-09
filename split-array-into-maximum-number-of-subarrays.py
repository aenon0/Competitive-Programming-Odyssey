class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        curr = nums[0]
        count = 0 
        for i in range(len(nums)):
            curr = curr & nums[i]
            if not curr:
                print(i)
                count += 1
                if (i + 1) < len(nums):
                    curr = nums[i + 1]
        #
        return 1 if not count else count