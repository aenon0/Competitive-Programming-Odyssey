class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
 
        dic ={
        }
        for i in range(len(order)):
            dic[order[i] ]=i

        for word_index in range(len(words)-1, 0, -1):
            min_length= min(len(words[word_index-1]), len(words[word_index]))

            check = False
            for i in range(min_length):
                #aac acd checking the first, 2nd ...
                if dic[words[word_index-1][i]] < dic[words[word_index][i]]:
                    check = True
                    break
                # consider abc and aac checks the wrong
                if dic[words[word_index-1][i]] > dic[words[word_index][i]]:
                    return False
            # apple and app
            if len(words[word_index-1]) > len(words[word_index]) and not check:
                return False
        return True
