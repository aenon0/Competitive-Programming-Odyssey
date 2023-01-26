class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()#[3,5,1,5] k = 2-------[1,3,5,5] 
        left_ptr = 0 
        right_ptr = len(nums) - 1
        count_operation = 0
        while right_ptr > left_ptr:
            if nums[left_ptr] + nums[right_ptr] > k:
                right_ptr -= 1
            elif nums[left_ptr] + nums[right_ptr] < k:
                left_ptr += 1
                            
            else:
                count_operation += 1
                right_ptr -= 1
                left_ptr += 1
        
        return count_operation
        
