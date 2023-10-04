class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort()
        def gcd(num1, num2):
            if num2 == 0:
                return num1
            return gcd(num2, num1 % num2)

        # self.max_score = -inf
        @cache
        def backtrack(curr_space, oper):
            if len(curr_space) == 2:
                return oper * math.gcd(curr_space[0], curr_space[1])
            
            ans = 1
            for i in range(len(curr_space)):
                
                for j in range(i + 1, len((curr_space))):
                    nxt_score = (oper * (math.gcd(curr_space[i], curr_space[j])))
                    nxt_space = list(curr_space)
                    nxt_space.pop(i)
                    nxt_space.pop(j-1)
                    
                    ans = max(ans, nxt_score + backtrack(tuple(nxt_space), oper + 1))
            return ans
                    
        return backtrack(tuple(nums), 1)