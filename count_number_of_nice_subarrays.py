class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        left = 0 
        odds = 0 
        nices = 0 
        count = 0 
        for right in range(len(nums)):
            if nums[right] % 2 != 0:
                odds += 1
                count = 0 
                
            while odds == k:
                count += 1
                if nums[left] % 2 != 0:
                    odds -= 1
                left += 1
                print(left, right)
            print(count)
            nices += count 
                
            
        return nices
    
    
       
