class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [node for node in range(n)]
        
        self.remaining_nodes = n
        
        adj_list = defaultdict(list)
        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        
        def bfs(queue):
            while self.remaining_nodes > 2:
                length = len(queue)
                self.remaining_nodes -= length
                new_queue = [ ]
                
                for node in queue:
                    neighbor = adj_list[node].pop()
                    adj_list[neighbor].remove(node)
                    
                    if len(adj_list[neighbor]) == 1:
                        new_queue.append(neighbor)
                        
                queue = new_queue
                    
            return queue
                
            
        queue = [ ]
        for node in adj_list.keys():
            if len(adj_list[node]) == 1:
                queue.append(node)
                
        return bfs(queue)