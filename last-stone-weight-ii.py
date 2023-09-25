class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        _sum = 0 
        
        @cache
        def dp(idx, _sum):
            if idx == len(stones):
                return abs(_sum)
            
            res = min(dp(idx + 1, _sum + stones[idx]), dp(idx + 1, _sum - stones[idx]))
            return res
        
        return dp(0, 0)