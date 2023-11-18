from collections import defaultdict
sizes_of_groups = list(map(int, input().split()))

group_a = [ ]
for letter in range(sizes_of_groups[0]):
    group_a.append(input())

group_b = [ ]
for letter in range(sizes_of_groups[1]):
    group_b.append(input())

def_dict = defaultdict(list)

for letter_index in range(len(group_a)):
    def_dict[group_a[letter_index]].append(letter_index + 1)

for letter in group_b:
    if def_dict.get(letter) == None:
        print(-1)
    else:
        print(*def_dict[letter])
    
    
    
    
    
