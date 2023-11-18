class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""
        min_length= min(len(word1), len(word2))
        for index in range(min_length):
            ans+= word1[index]
            ans+= word2[index]
        if len(word1) > len(word2):
            ans+= word1[min_length: ]
        elif len(word1) < len(word2):
            ans+= word2[min_length: ]
        return ans
