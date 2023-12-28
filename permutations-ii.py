class Solution(object):
    def permuteUnique(self, nums):
        temp = [ ]
        indices = [ ]
        ans = [ ]
        def backtrack(nums):
            if len(temp) == len(nums):
                if temp not in ans:
                    ans.append(temp[:])
                return 
            for indx in range(len(nums)):
                if indx not in indices:
                    temp.append(nums[indx])
                    indices.append(indx)
                    backtrack(nums)
                    temp.pop()
                    indices.pop()
        backtrack(nums)
        return ans