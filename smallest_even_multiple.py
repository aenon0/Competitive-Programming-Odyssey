class Solution:
    def smallestEvenMultiple(self, num: int) -> int:
        if num % 2 == 0:
            return num
        else :
            return 2 * num  
            
