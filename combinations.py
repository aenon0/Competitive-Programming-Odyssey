class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans, temp = [ ], [ ]
        num = 0 
        def backtrack(start):
            if len(temp) == k:
                ans.append(temp[:])
                return
            for num in range(start, n + 1):
                temp.append(num)
                backtrack(num + 1)
                temp.pop()
                
        backtrack(1)
        return ans
