class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        uniques = dict()
        def inbound(row, col):
            return row >= 0 and col >= 0 and row < m and col < n

        def paths(row, col):
            if row == m - 1 and col == n - 1:
                return 1
            if (row, col) in uniques:
                return uniques[(row, col)]
            uniques[(row, col)] = 0 
            if inbound(row, col + 1):
                uniques[(row, col)] += paths(row, col + 1)
            if inbound(row + 1, col):
                uniques[(row, col)] += paths(row + 1, col)
            return uniques[(row, col)]
        return paths(0, 0)