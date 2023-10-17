class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        nums = [True for _ in range(n )]
        nums[0] = nums[1] = False
        
        d = 2
        while d * d <= n:
            if nums[d]:
                for m in range(d * 2, n, d):
                    nums[m] = False
            d += 1
        return nums.count(True)