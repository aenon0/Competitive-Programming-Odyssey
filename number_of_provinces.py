class Solution:
    def findCircleNum(self, matrix: List[List[int]]) -> int:
        adjacency_list = defaultdict(list)
        for row_indx in range(len(matrix)):
            # main_col = 0
            for col_indx in range(len(matrix[0])):
                if matrix[row_indx][col_indx] == 1:
                    adjacency_list[row_indx].append(col_indx)
        
        # for key in adjacency_list.keys():
        #     print(key, adjacency_list[key])
        visited = [0] * len(matrix)
        def dfs(node):
            
            visited[node - 1] = -1

            for neighbor in adjacency_list[node]:
                if visited[neighbor - 1] == 0:
                    dfs(neighbor)
        
        provinces = 0 
        for node in adjacency_list.keys():
            if visited[node - 1] == 0:
                dfs(node)
                provinces += 1
        
        return provinces 
            
                    
                    
        