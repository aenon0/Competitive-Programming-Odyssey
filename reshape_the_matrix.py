class Solution:
    def matrixReshape(self, mat: List[List[int]], row: int, col: int) -> List[List[int]]:
        reshaped = [0] * (len(mat) * len(mat[0]))
        for row_indx in range(len(mat)):
            for col_indx in range(len(mat[0])):
                unique_id = row_indx * len(mat[0]) + col_indx
                reshaped[unique_id] = mat[row_indx][col_indx]
                
        if row * col != len(reshaped):
            return mat
        
        mat.clear()
        for indx in range(0, len(reshaped) - col + 1, col):
            mat.append(reshaped[indx: indx + col])
        
        return mat
