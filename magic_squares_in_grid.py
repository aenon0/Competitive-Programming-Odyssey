class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        for row in grid: 
            print(row)
        count_magic_squares = 0 
        for row_indx in range(1, len(grid) - 1):
            for col_indx in range(1, len(grid[0]) - 1):
                check_sum = set()
                check_uniqueness = set()
                if grid[row_indx][col_indx] < 10 and grid[row_indx][col_indx] >0: check_uniqueness.add(grid[row_indx][col_indx])
                if grid[row_indx][col_indx - 1] < 10 and grid[row_indx][col_indx - 1] > 0:check_uniqueness.add(grid[row_indx][col_indx - 1])
                if grid[row_indx][col_indx + 1] < 10 and grid[row_indx][col_indx + 1] > 0: check_uniqueness.add(grid[row_indx][col_indx + 1])
                if grid[row_indx - 1][col_indx - 1] < 10 and grid[row_indx - 1][col_indx - 1] > 0: check_uniqueness.add(grid[row_indx - 1][col_indx - 1])
                if grid[row_indx - 1][col_indx] < 10 and grid[row_indx - 1][col_indx] >0:check_uniqueness.add(grid[row_indx - 1][col_indx])
                if grid[row_indx - 1][col_indx + 1] < 10 and grid[row_indx - 1][col_indx + 1] > 0: check_uniqueness.add(grid[row_indx - 1][col_indx + 1])
                if grid[row_indx + 1][col_indx - 1] < 10 and grid[row_indx + 1][col_indx - 1] > 0: check_uniqueness.add(grid[row_indx + 1][col_indx - 1])
                if grid[row_indx + 1][col_indx] < 10 and grid[row_indx + 1][col_indx] > 0: check_uniqueness.add(grid[row_indx + 1][col_indx])
                if grid[row_indx + 1][col_indx + 1] < 10 and grid[row_indx + 1][col_indx + 1] > 0: check_uniqueness.add(grid[row_indx + 1][col_indx + 1])
                    
                if len(check_uniqueness) == 9 :
#                   row sums
                    check_sum.add(grid[row_indx][col_indx - 1] + grid[row_indx][col_indx] + grid[row_indx][col_indx + 1])
                    check_sum.add(grid[row_indx - 1][col_indx - 1] + grid[row_indx - 1][col_indx] + grid[row_indx - 1][col_indx + 1])
                    check_sum.add(grid[row_indx + 1][col_indx - 1] + grid[row_indx + 1][col_indx] + grid[row_indx + 1][col_indx + 1])
#                   col sums
                    check_sum.add(grid[row_indx + 1][col_indx] + grid[row_indx][col_indx] + grid[row_indx - 1][col_indx])
                    check_sum.add(grid[row_indx + 1][col_indx - 1] + grid[row_indx][col_indx - 1] + grid[row_indx - 1][col_indx - 1])
                    check_sum.add(grid[row_indx + 1][col_indx + 1] + grid[row_indx][col_indx + 1] + grid[row_indx - 1][col_indx + 1])
#                   diagonal sums
                    check_sum.add(grid[row_indx][col_indx] + grid[row_indx - 1][col_indx - 1] + grid[row_indx + 1][col_indx + 1])
                    check_sum.add(grid[row_indx][col_indx] + grid[row_indx + 1][col_indx - 1] + grid[row_indx - 1][col_indx + 1])
               
                if len(check_sum) == 1:
                    count_magic_squares += 1
        return count_magic_squares
                
                
