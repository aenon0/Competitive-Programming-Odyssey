class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        def_dict = defaultdict(list)
        col_size = len(matrix[0])
        row_size = len(matrix)
        for row_index in range(row_size):
            for col_index in range(col_size):
                def_dict[row_index + col_index].append(matrix[row_index][col_index])
        
        
        reverse_next = True 
        traversed_elements= [ ]
        for value in def_dict.values():
            if reverse_next:
                value.reverse()                
                reverse_next = False
            else:
                reverse_next = True
            traversed_elements.extend(value)
            
        return traversed_elements
            
        
        
       
        
                
        
        
        
