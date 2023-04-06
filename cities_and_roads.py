from collections import defaultdict

vertices = int(input())
matrix = [ ]
count_ones = 0

for i in range(vertices):
    matrix.append(list(map(int, input().split())))

for row_indx in range(len(matrix)):
    for col_indx in range(len(matrix[0])):
        if matrix[row_indx][col_indx] == 1:
            count_ones += 1


print(count_ones // 2)
