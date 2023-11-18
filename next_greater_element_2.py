class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        nums.extend(nums)
        next_greaters = [-1] * len(nums)
        for indx in range(len(nums)):
            
            while stack and nums[stack[-1]] < nums[indx]:
                temp = stack.pop()
                next_greaters[temp] = nums[indx]
                
            stack.append(indx)
            
        return next_greaters[:(len(next_greaters) // 2)]
                
