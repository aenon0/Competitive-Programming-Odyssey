class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for num_index in range(len(nums) - 1):
            if nums[num_index] == nums[num_index + 1]:
                nums[num_index] = "_"
                count += 1
        ptr = 0 
        while ptr < len(nums):
            if nums[ptr] == "_":
                nums.pop(ptr)
            else:
                ptr += 1
        
        
            
