class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = [0] * len(values)
        dp[0] = values[0]
        _max = 0
        for i in range(1, len(values)):
            dp[i] = max(dp[i - 1], (values[i - 1] + i - 1))
            _max = max(_max, dp[i] + values[i] - i)
        
        return _max