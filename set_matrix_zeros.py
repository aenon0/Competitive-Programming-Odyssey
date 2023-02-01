class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_row = set()
        zero_col = set()        
        for row_index in range(len(matrix)):
            for col_index in range(len(matrix[0])):
                if matrix[row_index][col_index] == 0:
                    zero_row.add(row_index)
                    zero_col.add(col_index)
                    
        for row in zero_row:
            for col_index in range(len(matrix[0])):
                    matrix[row][col_index] = 0 
        
        for col in zero_col:
            for row_index in range(len(matrix)):
                    matrix[row_index][col] = 0 
                    
        return matrix
   
