class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0] * (len(nums) + 1)
        for start, end in requests:
            prefix[start] += 1
            prefix[end + 1] -= 1
        
        for indx in range(1, len(prefix)):
            prefix[indx] += prefix[indx - 1]
        
        prefix.sort(reverse = True)
        nums.sort(reverse = True)
        
        _sum = 0 
        
        for indx in range(len(nums)):
            if prefix[indx] == 0:
                break
            _sum += nums[indx] * prefix[indx]
        
        return _sum % (1_000_000_000 + 7) 
            
