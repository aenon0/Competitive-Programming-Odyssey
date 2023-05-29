class Solution:
    def tribonacci(self, n: int) -> int:
        arr = {
            0 : 0,
            1 : 1,
            2 : 1,
        }
        
        def helper(n):
            if n in arr:
                return arr[n]
            arr[n] = (helper(n- 1) + helper(n - 2) + helper(n - 3))
            return arr[n]
        
        return helper(n)