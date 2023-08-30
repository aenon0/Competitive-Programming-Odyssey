class Solution:
    def racecar(self, target_pos: int) -> int:
        pos = 0 
        speed = 1
        def getNext(instruction, pos, speed):
            if instruction == 'A':
                pos += speed
                speed *= 2
            elif instruction == 'R':
                if speed > 0:
                    speed = -1
                else:
                    speed = 1
            return(pos, speed)


        def bfs(queue, visited):
            distance = 0
            while queue:
                # print(queue)
                length = len(queue)
                for _ in range(length):
                    curr_pos, curr_speed = queue.popleft() #pos speed 
                    if curr_pos == target_pos:
                        return distance
                    for instruction in ['A', 'R']:
                        nxt = getNext(instruction, curr_pos, curr_speed)
                        if nxt in visited:
                            continue
                        queue.append(nxt)
                        visited.add(nxt)
                distance += 1
            return -1
        
        queue = deque()
        queue.append((0, 1))
        visited = set()
        return bfs(queue, visited)