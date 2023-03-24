class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for indx in range(len(nums)):
            while nums[indx] != indx + 1:
                
                if nums[nums[indx] - 1] == nums[indx]:
                    return nums[indx]
                nums[nums[indx] - 1], nums[indx] = nums[indx], nums[nums[indx] - 1]
        
        # print(nums)
            
                
