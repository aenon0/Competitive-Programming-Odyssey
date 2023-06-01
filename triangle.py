class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # bottom-up dp
        def inbound(row, col):
            return row < len(triangle)
        for row in range(len(triangle) - 1, -1, -1):
            for col in range(len(triangle[row])):
                _min = inf
                if inbound(row + 1, col):
                    _min = min(_min, triangle[row + 1][col])
                if inbound(row + 1, col + 1):
                    _min = min(_min, triangle[row + 1][col + 1])
                if _min != inf:
                    triangle[row][col] += _min
        return triangle[0][0]