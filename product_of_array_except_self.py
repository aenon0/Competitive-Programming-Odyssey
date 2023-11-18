class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1]
        product = 1
        for indx in range(1, len(nums)):
            product *= nums[indx - 1]
            prefix.append(product)
        
        product = 1
        for indx in range(len(nums) - 2, -1, -1):
            product *= nums[indx + 1]
            postfix.append(product)
        postfix.reverse()

        result = [ ]
        for indx in range(len(nums)):
            result.append(prefix[indx] * postfix[indx])
        
        
        return result
            
