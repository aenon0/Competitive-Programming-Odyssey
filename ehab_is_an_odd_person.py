
size = int(input())
arr = list(map(int, input().split()))
 
odds = 0
evens = 0
for num in arr:
    if num % 2 == 0:
        evens += 1
    else:
        odds += 1
 
if odds >= 1 and evens >= 1:
    print(*sorted(arr)) 
else:
    print(*arr)
