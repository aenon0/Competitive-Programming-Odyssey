class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms[0]:
            return False
        
        queue = deque()
        queue.append(0)
        visited = set()
        def bfs():
            while queue:
                key = queue.popleft()
                if key not in visited and rooms[key]:
                    queue.extend(rooms[key])
                visited.add(key)
                
        bfs()
        if len(visited) == len(rooms):
            return True
        return False