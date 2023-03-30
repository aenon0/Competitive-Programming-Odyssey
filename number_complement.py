class Solution:
    def findComplement(self, num: int) -> int:
        length = num.bit_length()
        all_ones =  0
        for _ in range(length):
            all_ones = (all_ones << 1) | 1
        
        return all_ones ^ num       
