class Solution:
    def hammingDistance(self, num1: int, num2: int) -> int:
        hamming_distance = 0 
        result = num1 ^ num2
        while result:
            hamming_distance += (result & 1)
            result >>= 1
        return hamming_distance
