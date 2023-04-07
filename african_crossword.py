from collections import defaultdict
sizes = list(map(int, input().split()))
matrix = [ ]
for _ in range(sizes[0]):
    matrix.append(list(input()))

col_dict = defaultdict(lambda : [0] * 26)
row_dict = defaultdict(lambda : [0] * 26)

for row_indx in range(len(matrix)):
    for col_indx in range(len(matrix[0])):
        ch = matrix[row_indx][col_indx]
        col_dict[col_indx][ord(ch) - 97] += 1
        row_dict[row_indx][ord(ch) - 97] += 1

for row_indx in range(len(matrix)):
    for col_indx in range(len(matrix[0])):
        ch = matrix[row_indx][col_indx]
        if col_dict[col_indx][ord(ch) - 97] > 1 or row_dict[row_indx][ord(ch) - 97] > 1:
            matrix[row_indx][col_indx] = 0
result = ""

for row in matrix:
    for element in row:
        if element != 0:
            result += element
print(result) 
