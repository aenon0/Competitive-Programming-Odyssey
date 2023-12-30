class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words) == 1:
            return True
        freq = defaultdict(int)
        for word in words:
            for char in word:
                freq[char] += 1
        
        for char in freq.keys():
            if freq[char] % len(words) != 0:
                return False
        return True