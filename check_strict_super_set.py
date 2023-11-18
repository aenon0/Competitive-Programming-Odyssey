set_a = set(input().split(" "))
num_of_sets = int(input())
list_of_sets = []
for index in range(num_of_sets):
    list_of_sets.append(set(input().split(" ")))

flag = True
for smaller_set in list_of_sets:
    if (len(smaller_set) < len(set_a) and
        smaller_set.issubset(set_a)):
        flag = True
    else:
        flag = False
        print(flag)
        break
if flag:
    print(flag)
