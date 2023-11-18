num_of_rows = int(input())
size_of_rows = [ ]
rows = [ ]
for row in range(num_of_rows):
    size_of_rows.append(int(input()))
    rows.append(list(map(int, input().split())))


for row_index in range(len(rows)):
    left_ptr = 0
    right_ptr = len(rows[row_index]) - 1
    top = max(rows[row_index][left_ptr], rows[row_index][right_ptr])
    if top == rows[row_index][left_ptr]:
        left_ptr += 1
    else:
        right_ptr -= 1 
        
    checker = True
    while left_ptr < right_ptr:
        if max(rows[row_index][left_ptr], rows[row_index][right_ptr]) > top:
            checker = False
            break
        else:
            if rows[row_index][left_ptr] >= rows[row_index][right_ptr]:
                top = rows[row_index][left_ptr]
                left_ptr += 1
            elif rows[row_index][right_ptr] > rows[row_index][left_ptr]:
                top = rows[row_index][right_ptr]
                right_ptr -= 1
    if checker:
        print("Yes")
    else: 
        print("No")
            
        
        
        
    
