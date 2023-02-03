class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            print(row)
#       row validation
        for row in board:
            temp = [ ]
            temp = [col for col in row if col.isdigit() and row.count(col) > 1]
            if len(temp) != 0:
                return False
#         col_validation
        for col_indx in range(len(board[0])):
            temp = [ ]
            for row_indx in range(len(board)):
                temp.append(board[row_indx][col_indx])
            temp1 = [value for value in temp if value.isdigit() and temp.count(value) > 1]
            if len(temp1) != 0:
                return False
#        sub-box checker
        for row_indx in range(1,len(board) - 1, 3):
            for col_indx in range(1,len(board[0]) - 1, 3):
                temp = [ ]
                if  board[row_indx][col_indx].isdigit():              temp.append(board[row_indx][col_indx])
                if  board[row_indx][col_indx + 1].isdigit():          temp.append(board[row_indx][col_indx + 1])
                if  board[row_indx][col_indx - 1].isdigit():          temp.append(board[row_indx][col_indx - 1])
                if  board[row_indx - 1][col_indx].isdigit():          temp.append(board[row_indx - 1][col_indx])
                if  board[row_indx - 1][col_indx + 1].isdigit():      temp.append(board[row_indx - 1][col_indx + 1])
                if  board[row_indx - 1][col_indx - 1].isdigit():      temp.append(board[row_indx - 1][col_indx - 1])
                if  board[row_indx + 1][col_indx].isdigit():          temp.append(board[row_indx + 1][col_indx])
                if  board[row_indx + 1][col_indx + 1].isdigit():      temp.append(board[row_indx + 1][col_indx + 1])
                if  board[row_indx + 1][col_indx - 1].isdigit():      temp.append(board[row_indx + 1][col_indx - 1])
                temp1 = [num for num in temp if temp.count(num) > 1]
                if len(temp1) != 0:
                    return False
                
        return True
                
                          
                
                
        
       
            
