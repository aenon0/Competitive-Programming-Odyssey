temp = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
 
result = [0] * len(arr2)
 
p1 = 0
p2 = 0 
while p1 < len(arr1) and p2 < len(arr2):
    if arr2[p2] > arr1[p1]:
        result[p2] += 1
        p1 += 1
    else:
        p2 += 1
 
for indx in range(1, len(result)):
    result[indx] += result[indx - 1]
print(*result)
