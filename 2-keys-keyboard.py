class Solution:
    def minSteps(self, n: int) -> int:
        # bottom-up dp
        dp = [i for i in range(n + 1)]
        dp[1] = 0 
        for i in range(1, len(dp)):
            for j in range(i // 2, 1, -1):
                if (i % j) == 0:
                    dp[i] = min(dp[i], dp[j] + (i // j))
       
        return dp[-1]