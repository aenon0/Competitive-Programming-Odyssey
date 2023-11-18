from collections import Counter

k = int(input())
ctr = Counter(list(map(int, input().split(" "))))

room_of_captain = 0
for key in ctr.keys():
   
    if ctr[key] == 1:
        room_of_captain = key
        break    
print(room_of_captain)
