from collections import Counter 

num = int(input())

words = [ ]
for index in range(num):
    words.append(str(input()))
ctr = Counter(words)
num_of_uniques = len(ctr)
print(num_of_uniques)
for value in ctr.values():    
    print(value, end = " ")

