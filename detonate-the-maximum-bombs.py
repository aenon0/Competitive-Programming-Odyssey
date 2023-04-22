class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def inbound(bomb1, bomb2):
            x1, y1, r1 = bomb1
            x2, y2, r2 = bomb2
            distance = math.sqrt(((y1 - y2) ** 2) + ((x1 - x2) ** 2))
            if distance > r1:
                return False
            return True
        
        
        def dfs(bomb_indx, count):
            if bomb_indx in visited:
                return 

            visited.add(bomb_indx)
            count = 1
            for b_indx in range(len((bombs))):
                if b_indx not in visited and inbound(bombs[bomb_indx], bombs[b_indx]):
                    # print(bomb, bombs[b_indx])
                    count += dfs(b_indx, count)
            return count
        
        max_bombs = 0 
        for bomb_indx in range(len(bombs)):
            visited = set()
            detonated = dfs(bomb_indx, 0)
            # print(bomb, detonated)
            max_bombs = max(max_bombs, detonated)
            # print()

        return max_bombs