class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse =True) 
        for index in range(len(nums)-2):    
            if nums[index+1]+nums[index+2] > nums[index]:
                largest_perimeter = nums[index] + nums[index+1] + nums[index+2]
                return largest_perimeter
        return 0
