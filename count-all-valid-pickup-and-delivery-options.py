class Solution:
    def countOrders(self, n: int) -> int:
        modulo = 10 ** 9 + 7
        @cache
        def rec(n, m):
            if n == 0 == m:
                return 1
            
            if n == 0:
                return (m * rec(n, m - 1)) % modulo

            if m == 0:
                return (n * rec(n - 1, m + 1)) % modulo

            return (m * rec(n, m - 1) + n * rec(n - 1, m + 1)) % modulo  
        return rec(n, 0) % modulo