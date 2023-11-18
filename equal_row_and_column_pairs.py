class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count_matches = 0
#storing the rows as tuples in a counter
        rows = [ ]
        for row in grid:
            rows.append(tuple(row))
        ctr = Counter(rows)
        
# transpose the matrix/// just to simplify accessing
        for row_index in range(len(grid)):
            for col_index in range(len(grid)):
                if col_index >= row_index:
                    grid[row_index][col_index],grid[col_index][row_index] = grid[col_index][row_index], grid[row_index][col_index]
                    
# compare the transposed matrix with the counter 
        for row in grid:
            
            if ctr[tuple(row)] != 0:
                count_matches += ctr[tuple(row)]
        
        return count_matches
                
        
        
            

            
                
            
            
        
