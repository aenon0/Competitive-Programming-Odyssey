class Solution:
    def minOperations(self, num: str) -> int:
        
        # start with one
        flag = 1
        count = 0 
        for digit in num:
            if int(digit) != flag:
                count += 1
            flag = 1 - flag
        
        min_count = count 
        print(count)
        # start with zero
        flag = 0
        count = 0 
        for digit in num:
            if int(digit) != flag:
                count += 1
            flag = 1 - flag
        print(count)
        return min(count, min_count)