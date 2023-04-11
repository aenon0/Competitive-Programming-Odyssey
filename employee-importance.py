"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importance_dict = defaultdict()
        adjacency_list = defaultdict(list)
        for e in employees:
            adjacency_list[e.id].extend(e.subordinates)
            importance_dict[e.id] = e.importance
        
        # for key in adjacency_list.keys():
        #     print(key, adjacency_list[key])

        visited = set()
        self.count_importance = 0 
        def dfs(node):
            visited.add(node)
            self.count_importance += importance_dict[node]
            for neighbor in adjacency_list[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        dfs(id)
        return self.count_importance