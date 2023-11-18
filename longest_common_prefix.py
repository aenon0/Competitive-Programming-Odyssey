class Solution(object):
    def longestCommonPrefix(self, strs):
        shortest_word_index = 0 
        common_prefix = ""
        checker = False
        for word in strs:
            if len(word) < len(strs[shortest_word_index]):
                shortest_word_index = strs.index(word)
       
        for i in range(len(strs[shortest_word_index])):
            for word in strs: 
                if word[i] == strs[shortest_word_index][i]:
                    checker = True
                else:
                    checker = False
                    break
            if checker:
                common_prefix += strs[shortest_word_index][i]
            else:
                break
        return common_prefix
