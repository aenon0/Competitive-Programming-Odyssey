
vertices = int(input())
matrix = [ ]
node_dict = defaultdict(list)

for i in range(vertices):
    matrix.append(list(map(int, input().split())))
    node_dict[i + 1].append(0)

for row_indx in range(len(matrix)):
    for col_indx in range(len(matrix[0])):
        if matrix[row_indx][col_indx] == 1:
            node_dict[row_indx + 1].append(col_indx + 1)
            node_dict[row_indx + 1][0] += 1


for value in node_dict.values():
    print(*value)
