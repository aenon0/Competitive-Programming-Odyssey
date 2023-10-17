class Solution:
    def largestIsland(self, matrix: List[List[int]]) -> int:
        # just pre stuff for union find
        rep = defaultdict(tuple)
        size = defaultdict(int)
        visited = set()
        # O(n ** 2)
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                rep[(row, col)] = (row, col)
                if matrix[row][col] == 1:
                    size[(row, col)] = 1
                else: 
                    size[(row, col)] = 0

        def inbound(row, col):
            return row > -1 and col > -1 and row < len(matrix) and col < len(matrix[0])

        def get_neighbors(row, col):
            neighbors = [ ]
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nrow = row + x
                ncol = col + y
                if inbound(nrow, ncol) and matrix[nrow][ncol] == 1:
                    neighbors.append((nrow, ncol))
            return neighbors

        def find(row, col):
            if rep[(row, col)] != (row, col):
                curr = rep[(row, col)]
                rep[(row, col)] = find(curr[0], curr[1])
            return rep[(row, col)]

        def union(row1, col1, row2, col2):
            rep1 = find(row1, col1)
            rep2 = find(row2, col2)
            if rep1 == rep2:
                return 
            
            if size[rep1] > size[rep2]:
                rep[(row2, col2)] = rep1
                size[rep1] += size[rep2]
            else:
                rep[(row1, col1)] = rep2
                size[rep2] += size[rep1]

            return max(size[rep1], size[rep2])

        def bfs(row, col):
            queue = deque([(row, col)])
            visited.add((row, col))
            while queue:
                curr_row, curr_col = queue.popleft()
                
                for nrow, ncol in get_neighbors(curr_row, curr_col):
                    if (nrow, ncol) in visited:
                        continue
                    union(curr_row, curr_col, nrow, ncol)               
                    visited.add((nrow, ncol))
                    queue.append((nrow, ncol))

        # unioning those in the same island using bfs
        # O(n ** 2)
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 1 and (row, col) not in visited:
                    bfs(row, col)


        # flipping every zero and unioning it with its four neighbors one by one, keeping track which union will end up with the largest island
        
        _max = max(size.values())
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    _reps = set()
                    for nrow, ncol in get_neighbors(row, col):
                        _reps.add(find(nrow, ncol))
        
                    temp = 0
                    for r in _reps:
                        temp += size[r]
                    _max = max(_max, temp + 1)
        return _max