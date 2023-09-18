class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        def inbound(row, col):
            return row >= 0 and col >= 0 and row < len(dungeon) and col <len(dungeon[0]) 


        for row in range(len(dungeon) - 1, -1, -1):
            for col in range(len(dungeon[0]) - 1, -1, -1):
                curr = dungeon[row][col]
                _min = -inf
                if inbound(row + 1, col):
                    _min = max(_min, dungeon[row + 1][col])
                if inbound(row, col + 1):
                    _min = max(_min, dungeon[row][col + 1])                    
                
                if _min != -inf and _min < 0:
                    curr += _min
                dungeon[row][col] = curr
        
        # for row in dungeon:
        #     print(row)
        if dungeon[0][0] < 0:
            return (-1 * dungeon[0][0]) + 1
        return 1