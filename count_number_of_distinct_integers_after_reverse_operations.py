class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        for num_index in range(len(nums)):
            temp = int(str(nums[num_index])[::-1])
            nums.append(temp)
            
        num_of_uniques = len(set(nums))
        
        return num_of_uniques
        
        
