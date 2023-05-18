class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        belongs, size, cost = defaultdict(int), defaultdict(int), defaultdict(float)
        for node in range(n):
            belongs[node + 1], size[node + 1], cost[node + 1] = node + 1, 1, float("inf") 
        
        def find(node):
            if node == belongs[node]:
                return node
            rep = find(belongs[node])
            belongs[node] = rep
            return rep
        
        def union(node1, node2, _cost):
            rep1 = find(node1)
            rep2 = find(node2)
            size1 = size[rep1]
            size2 = size[rep2]

            if size2 < size1:
                rep1, rep2 = rep2, rep1
            
            cost[rep1] = min(cost[rep1], cost[rep2], _cost)

            if rep1 != rep2:
                size[rep1] += size[rep2]
                belongs[rep2] = rep1


        for city1, city2, road_weight in roads:
            union(city1, city2, road_weight)
        
        return cost[find(1)]