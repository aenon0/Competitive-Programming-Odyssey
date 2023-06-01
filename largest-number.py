class Solution:
    def largestNumber(self, nums: List[int]) -> str:
    #    two pointers
        for i in range(len(nums)):
            nums[i] = str(nums[i])

        for p1 in range(len(nums) - 1):
            p2 = p1 + 1
            while p2 < len(nums):
                if nums[p2] + nums[p1] > nums[p1] + nums[p2]:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 += 1
        return "".join(nums) if int("".join(nums)) != 0 else "0"