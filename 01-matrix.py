class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        def inbound(row, col):
            return row >= 0 and col >= 0 and row < len(matrix) and col < len(matrix[0])
        
        visited = set()
        queue = deque()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    visited.add((row, col))
                    queue.append((row, col))
                    
        while queue:
            r, c = queue.popleft() 

            for x,  y in [(1, 0),(0, 1),(-1, 0),(0, -1)]:
                new_row = r + x
                new_col = c + y
                if  (new_row, new_col) in visited:
                    continue
                if inbound(new_row, new_col) and matrix[new_row][new_col] not in visited:
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))
                    matrix[new_row][new_col] = matrix[r][c] + 1
                        
                
                        
        return matrix