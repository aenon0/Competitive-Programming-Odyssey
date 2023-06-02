class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # bottom-up
        dp = [0] * len(questions)
        for i in range(len(questions) - 1, -1, -1):
            nxt_q = 0 
            solve_nxt = 0 
            if i + questions[i][1] + 1 < len(questions):
                nxt_q = dp[i + questions[i][1] + 1]
            if i + 1 < len(questions):
                solve_nxt = dp[i + 1]
            dp[i] = max((questions[i][0] + nxt_q), solve_nxt)
        
        return dp[0]