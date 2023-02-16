class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left_ptr = 0
        right_ptr = len(nums) - 1
        indices = [0, 0]
        while left_ptr < right_ptr:
            if target < nums[left_ptr] + nums[right_ptr]:
                right_ptr -= 1
            elif target > nums[left_ptr] + nums[right_ptr]:
                left_ptr += 1
            else:
                indices[0], indices[1] = left_ptr + 1, right_ptr + 1
                break
        
        return indices
                
