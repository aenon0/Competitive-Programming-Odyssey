class Solution(object):
    def combinationSum(self, candidates, target):
        # candidates.sort(reverse = True)
        
        temp = [ ]
        ans = [ ]
        def backtrack(i):
            if sum(temp) == target:
                ans.append(temp[:])
                return 
            
            
            for indx in range(i, len(candidates)):
                temp.append(candidates[indx])
                if sum(temp) <= target:
                    backtrack(indx)
                temp.pop()
                
        backtrack(0)
        return ans
