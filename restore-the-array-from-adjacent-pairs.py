class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for node1, node2 in adjacentPairs:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        def dfs(node, visited, nums):
            nums.append(node)
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited, nums)
            return nums

        for node in graph.keys():
            if len(graph[node]) == 1:
                return dfs(node, set(), [ ])