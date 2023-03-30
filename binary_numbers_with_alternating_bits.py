class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        while n != 0:
            prev_bit = n & 1 
            n = n >> 1
            curr_bit = n & 1
            if prev_bit == curr_bit:
                return False
        return True
