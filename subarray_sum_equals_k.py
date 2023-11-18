class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            if nums[0] == k:
                return 1
            else:
                return 0
            
        num_dict = defaultdict(int)
        num_dict[nums[0]] += 1
       
            
        subarrays = 0 
        if nums[0] == k:
            subarrays += 1
        for indx in range(1, len(nums)):
            nums[indx] += nums[indx - 1]
            if nums[indx] == k:
                subarrays += 1
            if (nums[indx] - k) in num_dict.keys():
                subarrays += num_dict[nums[indx] - k]
            num_dict[nums[indx]] += 1
        
        return subarrays
       
                
            
        
        
    
#      
