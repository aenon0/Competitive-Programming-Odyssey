testcases = int(input())
arrays = [ ]
for _ in range(testcases):
    t = int(input())
    arrays.append(list(map(int, input().split())))
 
for array in arrays:
    left = len(array)
    array.sort()
    p1, p2 = len(array) - 2, len(array) - 1 
    while p1 >= 0 and p2 >= 0:
        if (array[p2] - array[p1]) <= 1:
            left -= 1
        p1 -= 1
        p2 -= 1
 
    if left == 1:
        print("YES")
    else:
        print("NO")
