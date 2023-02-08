class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            for col_indx in range(len(row)):
                if target < row[0]:
                    return False
                elif target > row[len(row) - 1]:
                    break
                else:
                    if target in row:
                        return True
                    else:
                        return False
                
        
        
        

            
            



                    
