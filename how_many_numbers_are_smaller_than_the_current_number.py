class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ctr = Counter(nums)
        # print(ctr)    
        
        result = [0] * len(nums)
        
        for num_index in range(len(nums)):
            for key in ctr.keys():
                if key < nums[num_index]:
                    result[num_index] += ctr[key]
        
        return result
        
