class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
#         building the adjacency list
        self.adjacency_list = defaultdict(list)
        for row_indx in range(len(grid)):
            for col_indx in range(len(grid[0])):
                if grid[row_indx][col_indx] == 1:
                    key = (row_indx, col_indx)                 
                    if row_indx - 1 >= 0 and grid[row_indx - 1][col_indx] == 1:
                        self.adjacency_list[key].append((row_indx - 1, col_indx))
                    if col_indx - 1 >= 0 and grid[row_indx][col_indx - 1] == 1:
                        self.adjacency_list[key].append((row_indx, col_indx - 1))
                    if col_indx + 1 < len(grid[0]) and grid[row_indx][col_indx + 1] == 1:
                        self.adjacency_list[key].append((row_indx, col_indx + 1))
                    if row_indx + 1 < len(grid) and grid[row_indx + 1][col_indx] == 1:
                        self.adjacency_list[key].append((row_indx + 1, col_indx))
#         dfs function 
        if not self.adjacency_list:
             return 4
        
        self.perimeter = 0 
        visited = set()
        def dfs(self, cell):
            self.perimeter += (4 - len(self.adjacency_list[cell]))
            visited.add(cell)
                    
            for neighbor in self.adjacency_list[cell]:
                if neighbor not in visited:
                    dfs(self, neighbor)
            
                
        for key in self.adjacency_list.keys():
            dfs(self, key)
            break
        return self.perimeter
        
        