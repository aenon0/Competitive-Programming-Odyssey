class Solution(object):
    def subsets(self, nums):
        ans = [ ]
        temp = [ ]
        def backtrack(i):
            if len(temp) > len(nums):
                return 
            
            ans.append(temp[:])
            
            for indx in range(i, len(nums)):
                temp.append(nums[indx])
                backtrack(indx + 1)
                temp.pop()
        backtrack(0)
        return ans
