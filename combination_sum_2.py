class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        arr = [ ]
        result = set()
        self.temp_sum = 0
        total_sum = sum(candidates)
        visited_comb = set()
        def backtrack(indx):
            if total_sum == target:
                result.add(tuple(candidates))
                return
               
            if total_sum < target:
                return
            
            if self.temp_sum > target:
                return 
            
            
#             base case
            if self.temp_sum == target:
                result.add(tuple(arr))
                return
            

            for i in range(indx, len(candidates)):
                self.temp_sum += candidates[i]
                arr.append(candidates[i])
                if tuple(arr) not in visited_comb:
                    backtrack(i + 1)
                visited_comb.add(tuple(arr))
                self.temp_sum -= candidates[i]
                arr.pop()

        backtrack(0)
        return result
    
#    
