class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        top_ptr = 0 
        bottom_ptr = len(matrix) - 1
        while bottom_ptr > top_ptr:
            matrix[top_ptr], matrix[bottom_ptr] = matrix[bottom_ptr], matrix[top_ptr]
            top_ptr += 1
            bottom_ptr -= 1
        
        for row_index in range(len(matrix)):
            for col_index in range(len(matrix[0])):
                if row_index > col_index:
                    matrix[row_index][col_index], matrix[col_index][row_index] = matrix[col_index][row_index], matrix[row_index][col_index]
                else:
                    break
        
        return matrix
        
