class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1.replace(" ", "")
        num2.replace(" ", "")
        
        temp1_index = num1.index("+")
        num1_real = int(num1[: temp1_index]) 
        num1_img = int(num1[(temp1_index + 1): -1])
        
        temp2_index = num2.index("+")
        num2_real = int(num2[: temp2_index])
        num2_img = int(num2[(temp2_index + 1): -1])
        
        result_real = str((num1_real * num2_real) + (-1 * num1_img * num2_img)) +  "+"
        result_img = str((num2_real * num1_img) + (num1_real * num2_img)) + "i"
        
        return result_real+result_img
        
