class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counting_arr = [0] * len(nums)
        for num in nums:
            counting_arr[num - 1] += 1
        
        result = [ ]
        for indx in range(len(counting_arr)):
            if counting_arr[indx] == 2:
                result.append(indx + 1)
        return result
                
        
