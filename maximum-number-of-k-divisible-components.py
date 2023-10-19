class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        self.components = 0 
        adj_list = defaultdict(list)
        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)
       
        def dfs(node):
            curr_sum = values[node]
            for child in adj_list[node]:
                if child in visited:
                    continue
                visited.add(node)
                curr_sum += dfs(child)
            
            if curr_sum % k == 0:
                self.components += 1
                return 0
            return curr_sum
        
        visited = set([0])
        dfs(0)
        return self.components