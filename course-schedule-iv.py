class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        pre_dict = defaultdict(set)
        visited = set()
        
        for prerequisite, course in prerequisites:
            graph[prerequisite].append(course)
        
        def dfs(node):      
            visited.add(node)
            # i dont understand why the very next line of code matters(the solution doesnt work if i comment it)
            pre_dict[node].add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
                pre_dict[node].update(pre_dict[neighbor])
                    
            return pre_dict[node]
        
        result = [ ]
        for c in range(numCourses):
            if c not in visited:
                dfs(c)
                
        for c1, c2 in queries:
            if c2 in pre_dict[c1]:
                result.append(True)
            else:
                result.append(False)
                
        return result
    
    
#   aman's code
        # vis = set()
#         graph = defaultdict(list)
#         pre = defaultdict(set)
        
#         for u, v in prerequisites:
#             graph[u].append(v)

#         def dfs(node):
    
            
#             vis.add(node)
#             pre[node].add(node)
#             for nbr in graph[node]:
#                 if nbr not in vis:
#                     dfs(nbr)
#                 pre[node]|=pre[nbr]


#         res = []
#         for node in range(numCourses):
#             if node not in vis:
#                 dfs(node)
#         for u, v in queries:
#             res.append(v in pre[u])
#         return res