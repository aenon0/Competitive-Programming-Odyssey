class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        for node1, node2 in richer:
            graph[node2].append(node1)
        for key in graph.keys():
            print(key, graph[key])
            
        @cache
        def dfs(node, least_quite):
            for neighbor in graph[node]:

                if quiet[neighbor] < quiet[least_quite]:
                    least_quite = neighbor
                least_quite = dfs(neighbor, least_quite)
            
            return least_quite

        ans = [0] * len(quiet)
        for node in range(len(quiet)):
            ans[node] = dfs(node, node)
        return ans