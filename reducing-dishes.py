class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        @cache
        def dp(idx, multiplier):
            if idx == len(satisfaction):
                return 0
            res = max((satisfaction[idx] * multiplier) + dp(idx + 1, multiplier + 1), dp(idx + 1, multiplier))
            print(idx, res)
            return res
        
        return dp(0, 1)