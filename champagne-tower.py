class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        def inbound(row, col):
            return col >= 0 and col <= row
        
        dp = [ ]
        for r in range(query_row + 1):
            curr = [0] * (r + 1)
            dp.append(curr)
        dp[0][0] = poured 
        
        for row in range(1, query_row + 1):
            for col in range(r + 1):
                if inbound(row - 1, col - 1) and dp[row - 1][col - 1] > 1:
                    dp[row][col] += (dp[row - 1][col - 1] - 1) 
                    dp[row - 1][col - 1] = 1
                if inbound(row - 1, col) and dp[row - 1][col] > 1:
                    dp[row][col] += ((dp[row - 1][col] - 1) / 2)
                    dp[row - 1][col] = 1 + (dp[row - 1][col] - 1) / 2
        
        return dp[query_row][query_glass] if dp[query_row][query_glass] <= 1 else 1