class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        belongs = defaultdict()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                belongs[(row, col)] = (row, col)
        direction = defaultdict(list)
        up = (-1, 0)
        down = (1, 0)
        right = (0, 1)
        left = (0, -1)
        direction[1] = [left, right]
        direction[2] = [up, down]
        direction[3] = [left, down]
        direction[4] = [right, down]
        direction[5] = [left, up]
        direction[6] = [right, up]

        match = defaultdict(list)
        match[1] = [(1, 4, 6), (1, 3, 5)]
        match[2] = [(2, 3, 4), (2, 5, 6)]
        match[3] = [(1, 4, 6), (2, 5, 6)]
        match[4] = [(1, 3, 5), (2, 5, 6)]
        match[5] = [(1, 4, 6), (2, 3, 4)]
        match[6] = [(1, 3, 5), (2, 3, 4)]


        def inbound(row, col):
            return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0])
        def rep(row, col):
            _rep = belongs[(row, col)]
            while _rep != belongs[_rep]:
                _rep = belongs[_rep]
            return _rep

        def union(row1, col1, row2, col2):
            rep1 = rep(row1, col1)
            rep2 = rep(row2, col2)
            if rep1 != rep2:
                belongs[rep2] = rep1
        
        def find(row1, col1, row2, col2):
            rep1 = rep(row1, col1)
            rep2 = rep(row2, col2)
            return rep1 == rep2
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                for i, (x, y) in enumerate(direction[grid[row][col]]):
                    nr = row + x
                    nc = col + y
                    if inbound(nr, nc) and grid[nr][nc] in match[grid[row][col]][i]:
                        union(row, col, nr, nc)
        # print(belongs)
        return find(0, 0, len(grid) - 1, len(grid[0]) - 1)