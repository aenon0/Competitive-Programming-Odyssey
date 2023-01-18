from collections import defaultdict
 
num_of_testcases = int(input())
 
test_cases = [ ]
for _ in range(num_of_testcases):
    size = list(map(int, input().split()))
 
    temp = [ ]
    for i in range(size[0]):
        temp.append(list(map(int, input().split())))
    test_cases.append(temp)
 
 
 
for matrix in test_cases:
    
    
    to_right_diagonal =  defaultdict(int)
    to_left_diagonal = defaultdict(int)
    for row_index in range(len(matrix)):
 
        for col_index in  range(len(matrix[row_index])):
            to_left_diagonal[row_index + col_index] += matrix[row_index][col_index]
            to_right_diagonal[col_index - row_index] += matrix[row_index][col_index]
 
 
    max_sum = 0
    for row_index in range(len(matrix)):
        for col_index in  range(len(matrix[row_index])):
            max_sum = max(max_sum, to_left_diagonal[col_index + row_index] + to_right_diagonal[col_index - row_index] - matrix[row_index][col_index])
    print(max_sum)
