class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        belongs = defaultdict()
        for node in range(n):
            belongs[node] = node

        def find(node1, node2):
            rep1 = rep(node1)
            rep2 = rep(node2)
            return rep1 == rep2

        def rep(node):
            rep = belongs[node]
            while rep != belongs[rep]:
                rep = belongs[rep]
            return rep

        def union(node1, node2):
            rep1 = rep(node1) 
            rep2 = rep(node2)
            belongs[rep2] = rep1
        
        for node1, node2 in edges:
            union(node1, node2)
        
        return find(source, destination)