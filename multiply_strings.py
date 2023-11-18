class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        int_num1 = 0
        int_num2 = 0
        for index1 in range(len(num1)):
            int_num1 += (10**(len(num1)-1-index1) * (ord(num1[index1]) - 48))
        
        for index2 in range(len(num2)):
            int_num2 += (10**(len(num2)-1-index2) * (ord(num2[index2]) - 48))

        product = int_num1 * int_num2
        return str(product)
