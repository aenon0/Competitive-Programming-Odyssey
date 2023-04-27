class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[len(grid) - 1][len(grid[0]) - 1] != 0:
            return -1
        
        def inbound(row, col):
            return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0])
        
        queue = deque()
        queue.append((0,0))
        self.distance = 0
        def bfs(self):
            while queue:
                size = len(queue)
                self.distance += 1
                for _ in range(size):
                    row,col = queue.popleft()
                    if grid[row][col] == 2:
                        continue
                    if row == len(grid) - 1 and col == len(grid[0]) - 1:
                        return self.distance
                    
                 
                    grid[row][col] = 2
                    for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1),(1, -1), (-1, 1)]:
                        new_row = row + x
                        new_col = col + y
                        if inbound(new_row, new_col) and grid[new_row][new_col] == 0:
                            queue.append((new_row, new_col))
            return -1
               
        return bfs(self)