class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        result = [ ]
        for row_index in range(1, len(grid) - 1, 1):
            
            temp = [ ]
            for col_index in range(1, len(grid[0]) - 1, 1):
                temp.append(max(grid[row_index][col_index],
                           grid[row_index][col_index - 1],
                           grid[row_index][col_index + 1],
                           grid[row_index + 1][col_index],
                           grid[row_index + 1][col_index - 1],
                           grid[row_index + 1][col_index + 1],
                           grid[row_index - 1][col_index],
                           grid[row_index - 1][col_index - 1],
                           grid[row_index - 1][col_index + 1]
                          ))
                
            result.append(temp)
        return result
    
                
        
