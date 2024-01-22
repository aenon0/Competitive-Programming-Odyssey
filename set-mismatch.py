class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counting_arr = [0] * len(nums)
        for num in nums:
            counting_arr[num - 1] += 1
        
        result = [0, 0]
        for indx in range(len(counting_arr)):
            if counting_arr[indx] == 2:
                result[0] = indx + 1
            if counting_arr[indx] == 0:
                result[1] = indx + 1
        
        return result