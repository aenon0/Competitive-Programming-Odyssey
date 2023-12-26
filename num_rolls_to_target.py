class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def dp(dices, _sum):
            if _sum == 0 and dices == 0:
                return 1
            if dices == 0:
                return 0
            
            count = 0 
            for i in range(1, k + 1):
                count += (dp(dices - 1, _sum - i)) 
            return count 
        return dp(n, target) % ((10**9) + 7)