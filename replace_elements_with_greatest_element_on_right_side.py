class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        max_num = -1
        new_nums = [-1]
        for num_indx in range(len(nums) - 1, 0, -1):
            if nums[num_indx] >= max_num: 
                max_num = nums[num_indx]
            new_nums.insert(0, max_num)

        return new_nums
