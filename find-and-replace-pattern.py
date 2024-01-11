class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = [ ]
        for word in words:
            idx = 0 
            if len(word) != len(pattern):
                continue

            match = dict()
            check = True
            for char in word:
                if (char in match and match[char] != pattern[idx]) or (char not in match and pattern[idx] in match.values()):
                    check = False
                    break
                if char not in match:
                    match[char] = pattern[idx]
                
                idx += 1
            if check:
                result.append(word)
        return result