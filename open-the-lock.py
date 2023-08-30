class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        
        def getNeighbours(node):
            neighbors = [ ]
            for i in range(4):
                key = node[i]
                for nxt in [1, -1]:
                    new_key = str(node[ : i] + (str((nxt + int(key) + 10) % 10)) + node[i + 1 : ])
                    neighbors.append(new_key)
            return neighbors
                   
        def isVisited(node):
            return node in visited
        
        def reachedTarget(node):
            return node == target
        
        queue = deque()
        queue.append("0000")
        self.distance = -1
        visited = set()
        
        def bfs(self):
            while queue:
                size = len(queue)
                self.distance += 1
                for _ in range(size):
                    node = queue.popleft()

                    if reachedTarget(node):
                        return self.distance
                    
                    for nei in getNeighbours(node):
                        if not isVisited(nei) and nei not in deadends or nei == "0000":
                            queue.append(nei)
                            visited.add(nei)
            return -1
        
        
        queue = deque()    
        queue.append("0000")
        visited = set()
        return bfs(self)