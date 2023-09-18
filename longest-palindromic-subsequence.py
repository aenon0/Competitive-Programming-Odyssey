class Solution:
    def longestPalindromeSubseq(self, string: str) -> int:
        @cache
        def dp(left, right):
            if left == right:
                return 1
            if left > right:
                return 0
            
            if string[left] == string[right]:
                return dp(left + 1, right - 1) + 2
            else:
                return max(dp(left + 1, right), dp(left, right - 1))
        
        return dp(0, len(string) - 1)