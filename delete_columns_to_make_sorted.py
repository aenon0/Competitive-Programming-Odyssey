import numpy
class Solution:
    def minDeletionSize(self, words: List[str]) -> int:
        
        letter_matrix = [ ]
        for word in words:
            
            temp_list = [ ]
            for letter in word:
                temp_list.append(letter)
            letter_matrix.append(temp_list)
        
        letter_matrix = numpy.transpose(letter_matrix)
        
        
        alphabet_dict = {
            "a": 1,
            "b": 2,
            "c": 3,
            "d": 4,
            "e": 5,
            "f": 6,
            "g": 7,
            "h": 8,
            "i": 9,
            "j": 10,
            "k": 11,
            "l": 12,
            "m": 13,
            "n": 14,
            "o": 15,
            "p": 16,
            "q": 17,
            "r": 18,
            "s": 19,
            "t": 20,
            "u": 21,
            "v": 22,
            "w": 23,
            "x": 24,
            "y": 25,
            "z": 26
        }
        deleted = 0
        for row in letter_matrix:
            for col_index in range(len(letter_matrix[0]) - 1):
                if alphabet_dict.get(row[col_index]) > alphabet_dict.get(row[col_index + 1]):
                    deleted += 1
                    break
        
        return deleted
        
            
                
