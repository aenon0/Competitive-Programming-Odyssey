class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        size = len(board)
        board.reverse()
        print(board)
        def inbound(row, col):
            return row >= 0 and col >= 0 and row < size and col < size
        def get_indices(num):
            row = (num - 1) // size
            col = (num - 1) % size
            if row % 2:
                col = size - 1 - col
            return (row, col)
        
        def bfs(queue):
            while queue:
                curr, moves = queue.popleft()                
                for i in range(1, 7):
                    nxt = curr + i 
                    nr, nc = get_indices(nxt)
                    if inbound(nr, nc) and board[nr][nc] != -1:
                        nxt = board[nr][nc]
                    if curr == size * size:
                        return moves
                    if nxt not in self.visited:
                        queue.append((nxt, moves + 1))
                        self.visited.add(nxt)

            return -1
        
        self.visited = set() 
        queue = deque()
        queue.append((1, 0))
        return bfs(queue)