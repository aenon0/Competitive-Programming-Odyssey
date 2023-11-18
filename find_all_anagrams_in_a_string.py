class Solution:
    def findAnagrams(self, string: str, word: str) -> List[int]:
        
        word_ctr = Counter(word)
        
        anagrams = [ ]
        string = [*string]
        k = len(word)
        left = 0 
        right = k 
        string_ctr = Counter(string[left: right])
        if string_ctr == word_ctr:
            anagrams.append(left)
        
        
        while right < len(string):
            string_ctr[string[left]] -= 1
            string_ctr[string[right]] += 1
            if string_ctr == word_ctr:
                anagrams.append(left + 1)
            left += 1
            right += 1
            
        return anagrams
        
            
