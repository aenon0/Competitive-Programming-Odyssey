class Solution:
    def countVowels(self, word: str) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        vowel_count = 0 
        n = len(word)
        for i in range(len(word)):
            if word[i] in vowels:                
                vowel_count += (i + 1) * (n - i)
        return vowel_count