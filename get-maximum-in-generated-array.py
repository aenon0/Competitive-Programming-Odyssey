class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
            return n
        nums= [0] * (n + 1)
        nums[1] = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                nums[i] = nums[i // 2]
            else:
                nums[i] = nums[i // 2] + nums[(i // 2) + 1]
        return max(nums)










        # nums = [0] * (n + 1)
        # if len(nums) == 1:
        #     return 0
        # nums[1] = 1
        # def build(num):
        #     if num <= 1:
        #         return num
        #     if num == 2:
        #         return 1
        #     if nums[num] != 0:
        #         return nums[num]
            
        #     if num % 2 == 0:
        #         nums[num] = build(num // 2)
        #     else:
        #         nums[num] = build((num) // 2) + build(((num) // 2) + 1)
        #     return nums[num]
        # for i in range(3, n + 1):
        #     build(i)
            
        # return max(nums)