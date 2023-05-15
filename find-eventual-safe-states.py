class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        colors = [0] * len(graph)
        def dfs(node):
            if colors[node] == 2:
                return False
            if colors[node] == 1:
                return True
            colors[node] = 1
            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True
            colors[node] = 2
            return False
        
        safe_nodes = [ ]
        for node in range(len(graph)):
            if not dfs(node):
                safe_nodes.append(node)
        return safe_nodes