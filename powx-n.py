class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return 1
        
        def helper(x, n):
            
            if n < 0:
                x = (1 / x)
                n *= -1

            if n == 1:
                return x
            if n == 0:
                return 1
            if x == 0:
                return 0
            
            temp = helper(x, n // 2)
            temp *= temp
            if n % 2 == 0:
                return temp
            return (x * temp)
        
        
        return helper(x, n)
        
        # 2 ^ - 4
        # 0.5 ^ 4
#         4 9
# 4 4 4