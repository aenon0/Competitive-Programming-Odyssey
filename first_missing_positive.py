class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for indx in range(len(nums)):
            count = 0 
            while nums[indx] != indx + 1:
                if nums[indx] <= 0:
                    break
                if nums[indx] - 1 < len(nums):
                    if nums[indx] != nums[nums[indx] - 1]:
                        nums[nums[indx] -1], nums[indx] = nums[indx], nums[nums[indx] -1]
                    else:
                        break
                else:
                    break
        for indx in range(len(nums)):
            if nums[indx] != indx + 1:
                return indx + 1
            
        return nums[-1] + 1
                
        
