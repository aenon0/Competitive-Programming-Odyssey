class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def recursion(n, k):
            if n == 1:
                return "0"
            prev_length = (2 ** (n- 1) - 1)
            length = ((2 ** (n)) - 1)

            if k <= (prev_length):
                return recursion(n - 1, k)
            elif k == (prev_length + 1):
                return "1"
            else:
                return str(1 - int(recursion(n - 1, (length - k + 1))))
        return recursion(n, k)
