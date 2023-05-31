class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = dict()
        def backtrack(curr, _sum):
            if _sum > amount or curr >= len(coins):
                return float("inf")
            if _sum == amount:
                return 0
            if (curr, _sum) in dp:
                return dp[(curr, _sum)]

            dp[(curr, _sum)] = min(backtrack(curr, _sum + coins[curr]) + 1, backtrack(curr + 1, _sum))
            
            return dp[(curr, _sum)]
        ans = backtrack(0, 0)
        return ans if ans != float("inf") else -1