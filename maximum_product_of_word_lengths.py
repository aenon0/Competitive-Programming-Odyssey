class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_length_product = 0
        letter_bits = [ ]
        for indx in range(len(words)):
            
            word = 0 
            for char in words[indx]:
                mask = 1
                mask = mask << (ord(char) - 97)
                word = word | mask
                
            letter_bits.append(word)
        
        for i in range(len(letter_bits)):
            first_word = letter_bits[i]
            for j in range(i + 1, len(letter_bits)):
                second_word = letter_bits[j]
                if first_word & second_word == 0:
                    length_product = len(words[i]) * len(words[j])
                    max_length_product = max(max_length_product, length_product)
                    
        return max_length_product

                    
                
                
            
