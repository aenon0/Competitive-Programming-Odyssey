class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def inbound(row, col):
            return row < len(board) and col < len(board[0]) and row >= 0 and col >= 0 
            
        def dfs(row, col):           
            board[row][col] = -1
            for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                new_row = row + x 
                new_col = col + y
                
                if inbound(new_row, new_col) and board[new_row][new_col] == "O" :
                    dfs(new_row, new_col)
                
            
   
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    if row == 0 or col == 0 or row == len(board) - 1 or col == len(board[0]) - 1:
                        dfs(row, col)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == -1:
                    board[row][col] = "O"
                    
        # for row in range(len(board)):
        #     for col in range(len(board[0])):