testcases = int(input())
arrays = []

for _ in range(testcases):
    length = int(input())
    arrays.append(list(map(int, input().split())))

for array in arrays:
    chosen_num = array[0]
    sign = array[0] // abs(array[0])
    _sum = 0
    
    for num in array:
        curr_sign = num // abs(num)

        if curr_sign == sign:
            chosen_num = max(chosen_num, num)
        else:
            _sum += chosen_num
            sign = curr_sign
            chosen_num = num
            
    _sum += chosen_num
    print(_sum)

