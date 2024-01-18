class Solution(object):
    def climbStairs(self, n):
        dp = [0] * (n + 1)
        dp[-1] = dp[-2] = 1
        for i in range(len(dp) - 3, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]
        return dp[0]