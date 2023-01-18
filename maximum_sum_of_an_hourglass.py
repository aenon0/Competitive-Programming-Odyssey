class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = 0
        for row_index in range(1,len(grid) - 1):
            for col_index in range(1, len(grid[0]) - 1):
                sum = grid[row_index][col_index] + grid[row_index - 1][col_index] +  grid[row_index - 1][col_index + 1] + grid[row_index - 1][col_index - 1] + grid[row_index + 1][col_index] + grid[row_index + 1][col_index + 1]+ grid[row_index + 1][col_index - 1]
                max_sum = max(max_sum, sum)
        return max_sum
                
                
        
