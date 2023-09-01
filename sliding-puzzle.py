class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def solved(tiles):
            return tiles[0][0] == 1 and tiles[0][1] == 2 and tiles[0][2] == 3 and tiles[1][0] == 4 and tiles[1][1] == 5

        def inbound(row, col):
            return row >= 0 and col >= 0 and row < 2 and col < 3
        
        def get_neighbors(row, col):
            neighbors = [ ]
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nrow, ncol = row + x, col + y
                if inbound(nrow, ncol):
                    neighbors.append((nrow, ncol))
            return neighbors
        
        def bfs(queue):
            visited = set()
            distance = 0
            while queue:
                length = len(queue)
                for _ in range(length):
                    curr_state, row, col = queue.popleft()
                    if solved(curr_state):
                        return distance
                    for nr, nc in get_neighbors(row, col):
                        matrix = curr_state[ : ]
                        # turning it into list of list so its gonna possible to modify it
                        matrix = list(matrix)
                        
                        for r in range(len(matrix)):
                            matrix[r] = list(matrix[r])                        
                        # modifying it
                        matrix[row][col], matrix[nr][nc] = matrix[nr][nc], matrix[row][col]
                        # turning it back to tuple so its gonna be hashable 
                        for r in range(len(matrix)):
                            matrix[r] = tuple(matrix[r])
                        matrix = tuple(matrix)

                        if tuple(matrix) in visited:
                            continue
                        visited.add(tuple(matrix))
                        queue.append((matrix, nr, nc))

                distance += 1
            return -1
        
        queue = deque()
        row = col = 0
        for r in range(len(board)):
            board[r] = tuple(board[r])
            for c in range(len(board[0])):
                if board[r][c] == 0:
                    row, col = r, c
        board = tuple(board)
        print(board)
                    
        
        queue.append((board, row, col))
        return bfs(queue)