class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = set()
        belongs = defaultdict(lambda: 0)
        ans = [ ] 
        
        def rep(node):
            return belongs[node]
        
        def union(node1, node2):
            nodes.add(node1)
            nodes.add(node2)
            if belongs[node1] == 0:
                belongs[node1] = node1
            if belongs[node2] == 0:
                belongs[node2] = node2
                
            rep1 = rep(node1)
            rep2 = rep(node2)
                     
            if rep1 == rep2:
                ans.append([node1, node2]) 
            else:
                for node in nodes:
                    if belongs[node] == rep2:
                        belongs[node] = rep1  
                
                
        for node1, node2 in edges:
            union(node1, node2)
        
        return ans[-1]