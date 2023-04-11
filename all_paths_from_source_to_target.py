class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        last_node = len(graph) - 1
        adjacency_list = defaultdict(list)
        for indx in range(len(graph)):
            adjacency_list[indx] = graph[indx]
        
        paths = [ ]
        path = [ ]
        # visited = set()
        # print(adjacency_list)
        def dfs(node):
            
            path.append(node)
            # if node != last_node:
            #     visited.add(node)
            if  path and path[-1] == last_node:
                paths.append(path[:])
                return 
               
            for neighbor in adjacency_list[node]:
                # if neighbor not in visited:
                dfs(neighbor)
                path.pop()
                    
        # print(visited)         
        dfs(0)
        return paths
                
            