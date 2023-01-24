class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for num_index in range(len(nums) -  1):
            if nums[num_index] == nums[num_index + 1]:
                nums[num_index] *= 2
                nums[num_index + 1] = 0
        
        first_size = len(nums)
        num_index = 0 
        while num_index < len(nums):
            if nums[num_index] == 0:
                nums.pop(num_index)
                num_index -= 1
            num_index += 1
            
        last_size = len(nums)
        for _ in range(first_size - last_size):
            nums.append(0)
            
            
##################################################################################################
                
        # print(nums)
        # print(count_zeros)
                
                
            
#         left_ptr = 0
#         right_ptr = 1
        
#         while right_ptr < len(nums) and left_ptr < len(nums):
#             print(left_ptr, right_ptr)
#             if  nums[left_ptr] != 0:
#                 left_ptr += 1 
#             if nums[right_ptr] == 0:
#                 right_ptr += 1
                
#             if nums[left_ptr] != 0 and nums[right_ptr] == 0: 
#                 nums[left_ptr], nums[right_ptr] = nums[right_ptr], nums[left_ptr]
#                 # print("been here")
            
                
        return nums
        
        
                
