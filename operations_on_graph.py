from collections import defaultdict

adjacency_list = defaultdict(list)
vertices = int(input())
operations = int(input())
for _ in range(operations):
    # print(matrix)
    temp = list(map(int, input().split()))
    if len(temp) == 3:
        adjacency_list[temp[1]].append(temp[2])
        adjacency_list[temp[2]].append(temp[1])
    else:
        ans = adjacency_list[temp[1]]
        if len(ans) != 0:
            print(*ans)
