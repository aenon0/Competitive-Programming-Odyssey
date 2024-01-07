class Solution:
    def wordBreak(self, string: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        self.result = set()
        def backtrack(idx, building):
            if idx == len(string):
                self.result.add(" ".join(building))
                return 
            
            for i in range(idx, len(string)):
                if string[idx : i + 1] in wordDict:
                    building.append(string[idx : i + 1])
                    backtrack(i + 1, building)
                    building.pop()
        backtrack(0, [ ])
        return list(self.result)