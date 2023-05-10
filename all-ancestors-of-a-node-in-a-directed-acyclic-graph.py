class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph_list = defaultdict(list)
        incoming = [0] * n
        for parent, child in edges:
            graph_list[parent].append(child)
            incoming[child] += 1
            
        def bfs(queue, ancestors):
            while queue:
                parent = queue.popleft()
                for child in graph_list[parent]:
                    incoming[child] -= 1
                    ancestors[child].append(parent)
                    ancestors[child].extend(ancestors[parent])
                    if incoming[child] == 0:
                        queue.append(child)
                        ancestors[child] = sorted(set(ancestors[child]))
            return ancestors
        
        queue = deque()
        for indx, indegree in enumerate(incoming):
            if indegree == 0:
                queue.append(indx)        
                
        return bfs(queue, [[] for _ in range(n)])