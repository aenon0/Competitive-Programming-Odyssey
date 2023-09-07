class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def inbound(row, col):
            return row >= 0 and col >= 0 and row < len(matrix) and col < len(matrix[0])

        def get_parents(row, col):
            parents = [ ]
            for x, y in [(-1, -1), (-1, 0), (-1, +1)]:
                pr, pc = row + x, col + y
                if inbound(pr, pc):
                    parents.append((pr, pc))
            return parents
        
        @cache
        def dp(row, col):
            _min = inf
            for pr, pc in get_parents(row, col):
                dp(pr, pc)
                _min = min(_min, matrix[pr][pc])
            if _min != inf:
                matrix[row][col] += _min
        for col in range(len(matrix[len(matrix) - 1])):
            dp(len(matrix) - 1, col)    
        
        return min(matrix[-1])