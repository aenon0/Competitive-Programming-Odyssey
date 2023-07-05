class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merged_word = ""
        while word1 and word2:
            if word1 > word2:
                merged_word += word1[0]
                word1 = word1[1 : ]
            else:
                merged_word += word2[0]
                word2 = word2[1 : ]
        merged_word += word1
        merged_word += word2
        return merged_word