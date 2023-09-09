class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj_list = defaultdict(list)
        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        difference = [0] * n
        visited = set()
        def dfs(node):
            distance = 0 
            found = False
            if hasApple[node]:
                found = True
           
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    f, d = dfs(neighbor)
                    if f:
                        distance += (d + 2)
                        found = True
            
            return (found, distance)
        
        visited = set()
        visited.add(0) 
        return dfs(0)[1]