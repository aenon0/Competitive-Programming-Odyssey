class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        def gcf(num1, num2):
            if num2 == 0:
                return num1
            return gcf(num2, num1 % num2)
        
        return gcf(nums[-1], nums[0])
        
