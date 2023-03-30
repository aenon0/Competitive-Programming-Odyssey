class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [ ]
        temp = [ ]
        self.checker = 0 << (max(nums))
        def backtrack(arr):
            if len(temp) == len(nums):
                result.append(temp[:])
                return
            
            for indx in range(len(arr)):
                
                mask = 1
                mask = mask << indx

                if (self.checker & mask) != (2 ** indx):
                    self.checker = (self.checker | mask)
                    temp.append(arr[indx])  
                    backtrack(arr)
                    self.checker = self.checker ^ mask
                    temp.pop()
        backtrack(nums)
        return result 
