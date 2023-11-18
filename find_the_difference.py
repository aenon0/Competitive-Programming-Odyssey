class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        added_letter=""
        for char in t:
            if char not in s or s.count(char)< t.count(char):
                return char
