from collections import defaultdict

vertices = int(input())
matrix = [ ]

for _ in range(vertices):
    matrix.append(list(map(int, input().split())))

node_dict = defaultdict(lambda : [0, 0])
for row_indx in range(len(matrix)):
    for col_indx in range(len(matrix[0])):
        node_dict[row_indx + 1][0] += matrix[row_indx][col_indx]
        node_dict[col_indx + 1][1] += matrix[row_indx][col_indx]


sources = [0]
sources_num = 0 
sinks = [0]
sinks_num = 0 
for key in node_dict.keys():
    if node_dict[key][0] == 0:
        sinks.append(key)
        sinks_num += 1
    if node_dict[key][1] == 0:
        sources.append(key)
        sources_num += 1
sinks.sort()
sources.sort()
sinks[0] = sinks_num 
sources[0] = sources_num 

print(*sources)
print(*sinks)


