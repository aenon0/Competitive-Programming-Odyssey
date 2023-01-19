class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0 , 0 , 0]
        for num in nums:
            if num == 0:
                count[0] += 1
            elif num == 1:
                count[1] += 1
            elif num == 2:
                count[2] += 1
      
        num_index = 0
        for freq_index in range(len(count)):
            while count[freq_index] > 0:
                nums[num_index] = freq_index
                num_index += 1
                count[freq_index] -= 1
                
                
       
                
