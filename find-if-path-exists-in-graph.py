class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjacency_list = defaultdict(list)
        self.visited = set()
        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])
            adjacency_list[edge[1]].append(edge[0])
        
        # print(adjacency_list)
        
        def dfs(self, vertex):
            if vertex == destination:
                return True
            
            
            self.visited.add(vertex)
            for neighbour in adjacency_list[vertex]:
                if neighbour not in self.visited:
                    if dfs(self, neighbour):
                        return True
                
            return False
                
        return dfs(self, source)