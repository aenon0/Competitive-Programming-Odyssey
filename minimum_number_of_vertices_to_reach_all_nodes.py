class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        visitables = set()
        for edge in edges:
            visitables.add(edge[1])
            
        result = [ ]
        for node in range(n):
            if node not in visitables:
                result.append(node)
        
        return result
