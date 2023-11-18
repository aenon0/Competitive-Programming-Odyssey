import numpy
class Solution:
    def printVertically(self, sentence: str) -> List[str]:
        word_list = sentence.split(" ")
#     turning the sentence into words
        longest_word_len = 0
        for word in word_list:
            longest_word_len = max(longest_word_len, len(word))
        
#     building a character matrix// turning the words into characters
        char_matrix = [ ]
        for word in word_list: 
            char_row = []
            for char in word:
                char_row.append(char)
            
            for index in range(longest_word_len - len(word)):
                char_row.append(" ")
                
            char_matrix.append(char_row)
#     transposing the matrix
        char_matrix = numpy.transpose(char_matrix)
    
#     converting the matrix it to list of strings
        vertically_read = [ ]
        for word in char_matrix:
            vertically_read.append("".join(word).rstrip())
                   
            
        return vertically_read
        
            
        
       
     
                
            
        
