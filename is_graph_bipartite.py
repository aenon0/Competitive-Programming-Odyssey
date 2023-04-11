class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        adjacency_list = defaultdict(list)
        for indx in range(len(graph)):
            adjacency_list[indx] = graph[indx]
        
        colors = [0] * len(adjacency_list)
        def dfs(node, color):
            checker = True
            colors[node] = color
            for neighbour in adjacency_list[node]:
                if colors[neighbour] == 0:
                     checker = dfs(neighbour, (color * -1)) and checker
                
                elif colors[neighbour] == colors[node]:
                    return False
            if checker:
                return True
            else:
                return False
        
        for node in range(len(graph)):
            
            if colors[node] == 0:
                if not dfs(node, 1):
                    return False
                
        return True
                    
                    
            
        