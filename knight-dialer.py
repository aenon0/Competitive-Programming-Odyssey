class Solution:
    def knightDialer(self, n: int) -> int:
        def inbound(row, col):
            return (row >= 0) and (col >= 0) and (row < 4) and (col < 3) and (row, col) != (3, 0) and (row, col) != (3, 2)

        def get_neighbors(row, col):
            neighbors = [ ]
            for x, y in [(2, 1), (2, -1), (1, 2), (1, -2),(-1, -2), (-1, 2), (-2, -1),(-2, 1)]:
                nr = row + x
                nc = col + y
                if inbound(nr, nc):
                    neighbors.append((nr, nc))
            return neighbors
        
        # def dp(row, col, moves, res):
        #     if moves == 0:
        def get_value(row, col):
            if (row, col) == (3, 1):
                return 0
            else:
                return (3 * row) + col + 1
        
        @cache
        def dp(row, col, move):
            if move == 0:
                return 1
            
            r = 0 
            for nr, nc in get_neighbors(row, col):
                if (nr, nc, move - 1) not in visited:
                    visited.add((nr, nc, move - 1))
                    r += dp(nr, nc, move - 1)
                    visited.remove((nr, nc, move - 1))
            return r

        result = 0 
        for r in range(4):
            for c in range(3):
                if (r, c) != (3, 0) and (r, c) != (3, 2):
                    visited = set({(r, c, n - 1)})
                    result += dp(r, c, n - 1)
                    
        
        return result % ((10**9) + 7)