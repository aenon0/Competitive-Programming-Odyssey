class Solution(object):
    def spiralOrder(self, matrix):
        col_begin = 0 
        col_end = len(matrix[0]) - 1
        row_begin = 0
        row_end = len(matrix) - 1
        
        result = [ ]
        if len(matrix) == 0:
            return result
        
        while row_begin <= row_end and col_begin <= col_end:
#             to the right
            for c in range(col_begin, col_end + 1):
                result.append(matrix[row_begin][c])
            
            row_begin += 1
#             down 
            for r in range(row_begin, row_end + 1):
                result.append(matrix[r][col_end])
            
            col_end -= 1
#             to the right
            if row_begin <= row_end:
                for c in range(col_end, col_begin -1, -1):
                    result.append(matrix[row_end][c])
            
            row_end -= 1
#             up
            if col_begin <= col_end:
                 for r in range(row_end, row_begin - 1, -1):
                    result.append(matrix[r][col_begin])
                                  
            col_begin += 1
        return result
            
            
