class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
     
        min_len = float("inf")
        left = 0 
        summ = 0
        for right in range(len(nums)):
            summ += nums[right]
            while summ >= target:
                summ -= nums[left]
                min_len = min(min_len, right - left + 1)
                left += 1
                
            
        if min_len != float("inf"):
            return min_len
        return 0



          
