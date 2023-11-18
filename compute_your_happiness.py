set_sizes = input().split(" ")
arr = input().split(" ")
set_a = set(input().split(" "))
set_b = set(input().split(" "))

happiness = 0 
for element in arr:
    if element in set_a:
        happiness += 1
    elif element in set_b:
        happiness -= 1
print(happiness)
