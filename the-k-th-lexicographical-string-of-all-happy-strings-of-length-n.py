class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_strings = set()
        def backtrack(building):
            if len(building) == n:
                happy_strings.add(building)
                return
            
            if not building:
                backtrack("a")
                backtrack("b")
                backtrack("c")
            else:
                if building[-1] != "a":
                    backtrack(building + "a")
                if building[-1] != "b":
                    backtrack(building + "b")
                if building[-1] != "c":
                    backtrack(building + "c")
        backtrack("")
        if k - 1 < len(happy_strings):
            return sorted(happy_strings)[k - 1]
        return ""