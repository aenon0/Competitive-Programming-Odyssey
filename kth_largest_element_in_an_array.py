class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        _min = min(nums)
        _max = max(nums)
        counting_arr = [0] * (_max - _min + 1)
        
        for num in nums:
            counting_arr[num - _min] += 1
        
        result = [ ]
        for indx in range(len(counting_arr) - 1, -1, -1):
            while counting_arr[indx] > 0:
                result.append((indx + _min ))
                counting_arr[indx] -= 1
        
        return result[k - 1] 
