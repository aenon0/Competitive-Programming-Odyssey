from collections import defaultdict
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        diagonal_dict = defaultdict(set)
        
        for row_index in range(len(matrix)):
            for col_index in range(len(matrix[0])):
                diagonal_dict[row_index - col_index].add(matrix[row_index][col_index])
                
    
        for value in diagonal_dict.values():
            if len(value) > 1:
                return False
        
        return True
            
