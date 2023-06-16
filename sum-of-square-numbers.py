class Solution:
    def judgeSquareSum(self, num: int) -> bool:
        p1, p2 = 0, round(sqrt(num))
        while p1 <= p2:
            curr = (p1 ** 2 + p2 ** 2)
            if curr == num:
                return True
            elif curr < num:
                p1 += 1
            else:
                p2 -= 1
        return False