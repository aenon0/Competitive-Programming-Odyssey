class Solution:
    def floodFill(self, matrix: List[List[int]], i: int, j: int, color: int) -> List[List[int]]:
        adjacency_list = defaultdict(list)
        initial_color = matrix[i][j]
        for row_indx in range(len(matrix)):
            for col_indx in range(len(matrix[0])):
                if matrix[row_indx][col_indx] == initial_color:
                    if col_indx - 1 >= 0 and matrix[row_indx][col_indx - 1] == initial_color:                    
                        adjacency_list[(row_indx, col_indx)].append((row_indx, col_indx - 1))
                    if col_indx + 1 < len(matrix[0]) and matrix[row_indx][col_indx + 1] == initial_color:
                        adjacency_list[(row_indx, col_indx)].append((row_indx, col_indx + 1))
                    if row_indx - 1 >= 0 and matrix[row_indx - 1][col_indx] == initial_color:
                        adjacency_list[(row_indx, col_indx)].append((row_indx - 1, col_indx))
                    if row_indx + 1 < len(matrix) and matrix[row_indx + 1][col_indx] == initial_color:
                        adjacency_list[(row_indx, col_indx)].append((row_indx + 1, col_indx))
                        
        def dfs(node):
            
            x, y = node
            matrix[x][y] = color
            for neighbor in adjacency_list[node]:
                if matrix[neighbor[0]][neighbor[1]] != color:
                    dfs(neighbor)
        dfs((i, j))
        return matrix