class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def recursion(n, k):
            if n == 1:
                return 0
            length = 2 ** (n - 1) 
            if k <= length // 2:
                return recursion(n - 1, k)
            else:
                return 1 - recursion(n - 1, k - (length // 2))

        return recursion(n, k)
