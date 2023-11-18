class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
#         first row prefix
        for col_indx in range(1, len(self.matrix[0])):
            matrix[0][col_indx] += self.matrix[0][col_indx - 1]
#         first col prefix
        for row_indx in range(1, len(self.matrix)):
            self.matrix[row_indx][0] += self.matrix[row_indx - 1][0]
#         the others
        for row_indx in range(1, len(self.matrix)):
            for col_indx in range(1, len(self.matrix[0])):
                temp = self.matrix[row_indx - 1][col_indx] + self.matrix[row_indx][col_indx - 1] - self.matrix[row_indx - 1][col_indx - 1]
                self.matrix[row_indx][col_indx] += temp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.matrix[row2][col2]
        if row1 == 0:
            return self.matrix[row2][col2]  - self.matrix[row2][col1 - 1] 
        if col1 == 0:
            return self.matrix[row2][col2] - self.matrix[row1 - 1][col2]
        
        return self.matrix[row2][col2] - self.matrix[row1 - 1][col2] - self.matrix[row2][col1 - 1] + self.matrix[row1 - 1][col1 - 1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
