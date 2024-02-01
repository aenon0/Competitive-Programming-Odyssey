class Solution:
    def generate(self, rows: int) -> List[List[int]]:
        pascals = [ ]
        for i in range(1, rows + 1):
            pascals.append([0] * i)
        pascals[0][0] = 1

        for row in range(1, len(pascals)):
            for col in range(row + 1):
                if col  == 0:
                    pascals[row][col] = pascals[row - 1][col]
                elif col == (row):
                    pascals[row][col] = pascals[row - 1][col - 1]
                else:
                    pascals[row][col] = pascals[row - 1][col - 1] + pascals[row - 1][col]
        return pascals