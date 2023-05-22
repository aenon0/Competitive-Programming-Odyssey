class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def get_neighbors(row, col):
            neighbors = [ ]
            for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                new_row = row + x
                new_col = col + y 
                if inbound(new_row, new_col):
                    neighbors.append((new_row, new_col))
            return neighbors                    
        
        def inbound(row, col):
            return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0])
        
        def bfs(queue, visited):
            min_flip = -1 
            while queue:
                min_flip += 1
                size = len(queue)
                for _ in range(size):
                    row, col = queue.popleft()
                    for nr, nc in get_neighbors(row, col):
                        if (nr, nc) not in visited:
                            if grid[nr][nc] == 1:
                                return min_flip
                            if grid[nr][nc] == 0:
                                visited.add((nr, nc))
                                queue.append((nr, nc))
                            
            return min_flip
               
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    visited = set()
                    visited.add((row, col))
                    queue = deque()
                    queue.append((row, col))
                    while queue:
                        row, col = queue.popleft()
                        for nr, nc in get_neighbors(row, col):
                            if (nr, nc) not in visited and grid[nr][nc] == 1:
                                visited.add((nr, nc))
                                queue.append((nr, nc))

                    ans = bfs(deque(visited), visited)
                    return ans