class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        char_dict = {
            "a" : [0] * len(words),
            "b" : [0] * len(words),
            "c" : [0] * len(words), 
            "d" : [0] * len(words),
            "e" : [0] * len(words),
            "f" : [0] * len(words),
            "g" : [0] * len(words),
            "h" : [0] * len(words),
            "i" : [0] * len(words),
            "j" : [0] * len(words),
            "k" : [0] * len(words),
            "l" : [0] * len(words),
            "m" : [0] * len(words),
            "n" : [0] * len(words),
            "o" : [0] * len(words),
            "p" : [0] * len(words),
            "q" : [0] * len(words),
            "r" : [0] * len(words),
            "s" : [0] * len(words),
            "t" : [0] * len(words),
            "u" : [0] * len(words),
            "v" : [0] * len(words),
            "w" : [0] * len(words),
            "x" : [0] * len(words),
            "y" : [0] * len(words),
            "z" : [0] * len(words)
        }
        for word_index in range(len(words)):
            indx = word_index
            for char_index in range(len(words[word_index])):
                ((char_dict[words[word_index][char_index]])[indx]) += 1
         
        result = [ ]
        for key in char_dict.keys():
            temp = min(char_dict[key])
            while temp > 0:
                result.append(key)
                temp -= 1
        
        return result
            
        
        
            
