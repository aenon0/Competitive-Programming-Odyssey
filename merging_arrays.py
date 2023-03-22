temp = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
 
p1 = 0
p2 = 0
 
result = [ ]
while p1 < len(arr1) and p2 < len(arr2):
    if arr1[p1] < arr2[p2]:
        result.append(arr1[p1])
        p1 += 1
    else:
        result.append(arr2[p2])
        p2 += 1
result.extend(arr1[p1 : ])
result.extend(arr2[p2 :])
 
print(*result)
