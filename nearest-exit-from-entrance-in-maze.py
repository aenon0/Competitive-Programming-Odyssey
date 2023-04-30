class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        entrance = tuple(entrance)
        def inbound(row, col):
            return col >= 0 and row >= 0 and col < len(maze[0]) and row < len(maze)
        
        def reached(row, col):
            return (row, col) != entrance and (row == 0 or col == 0 or row == len(maze) - 1 or col == len(maze[0]) - 1)
        
        def get_neighbors(row, col):
            neighbors = [ ]
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_row = row + x
                new_col = col + y
                if inbound(new_row, new_col) and maze[new_row][new_col] == ".":
                    neighbors.append((new_row, new_col))
            return neighbors
        
        def bfs(queue):
            steps = -1
            while queue:
                steps += 1
                size = len(queue)
                for _ in range(size):
                    row, col = queue.popleft()
                    if reached(row, col):
                        return steps
                    for nr, nc in get_neighbors(row, col):
                        if (nr, nc) in visited:
                            continue
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return -1
            
        queue = deque()
        visited = set()
        visited.add(entrance)
        queue.append(entrance)
        return bfs(queue)