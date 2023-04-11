class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        adjacency_list = defaultdict(list)
        self.count = 0 
        for row_indx in range(len(grid)):
            for col_indx in range(len(grid[0])):
                if grid[row_indx][col_indx] == 1:
                    grid[row_indx][col_indx] 
                    if col_indx - 1 >= 0 and grid[row_indx][col_indx  - 1] == 1:
                        adjacency_list[(row_indx, col_indx)].append((row_indx, col_indx - 1))
                    if col_indx + 1 < len(grid[0]) and grid[row_indx][col_indx  + 1] == 1:
                        adjacency_list[(row_indx, col_indx)].append((row_indx, col_indx + 1))    
                    if row_indx - 1 >= 0 and grid[row_indx - 1][col_indx] == 1:
                        adjacency_list[(row_indx, col_indx)].append((row_indx - 1, col_indx))
                    if row_indx + 1 < len(grid) and grid[row_indx + 1][col_indx] == 1:
                        adjacency_list[(row_indx, col_indx)].append((row_indx + 1, col_indx))
        for key in adjacency_list.keys():
            print(key, adjacency_list[key])
    
        def dfs(node):
            grid[node[0]][node[1]] = 2
            self.count += 1
            for neighbor in adjacency_list[node]:
                if grid[neighbor[0]][neighbor[1]] == 1:
                    dfs(neighbor)
        max_count = 0
        for row_indx in range(len(grid)):
            for col_indx in range(len(grid[0])):
                if grid[row_indx][col_indx] == 1:
                    self.count = 0 
                    dfs((row_indx, col_indx))
                    max_count = max(self.count, max_count)
        return max_count