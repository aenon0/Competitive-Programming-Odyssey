class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        def inbound(row, col):
            return row >= 0 and col >= 0 and row < len(grid2) and col < len(grid2[0])
        
        
        def dfs(row, col, check):
            grid2[row][col] = -1 # to mark the visited ones
            if grid1[row][col] == 0:
                check = False
            for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                # check = True
                new_row = row + x 
                new_col = col + y
                if inbound(new_row, new_col) and grid2[new_row][new_col] == 1:
                    check = dfs(new_row, new_col, check)
                
            return check
        
        count = 0 
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if grid2[row][col] == 1 and dfs(row, col, True):
                    count += 1
        return count