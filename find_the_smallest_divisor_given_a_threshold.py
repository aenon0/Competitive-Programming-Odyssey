class Solution(object):
    def smallestDivisor(self, nums, threshold):
               
        left = 0
        right = max(nums) + 1 
        
        while left + 1 < right:
            
            mid = left + ((right - left) // 2)
            temp_sum = 0 
            for num in nums:
                temp_sum += math.ceil((1.00 * num) / mid)
                
            if temp_sum > threshold:
                left = mid 
            else:
                right = mid
            
                
        
            
        return right
