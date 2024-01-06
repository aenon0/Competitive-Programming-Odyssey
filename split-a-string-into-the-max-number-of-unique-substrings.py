class Solution:
    def maxUniqueSplit(self, string: str) -> int:
        self.result = 0
        def backtrack(idx, visited):
            if idx == len(string):
                self.result = max(self.result, len(visited))
                return
            
            for i in range(idx, len(string)):
                if string[idx: i + 1] in visited:
                    continue
                visited.add(string[idx: i + 1])
                backtrack(i + 1, visited)
                visited.remove(string[idx: i + 1])
        backtrack(0, set())
        return self.result