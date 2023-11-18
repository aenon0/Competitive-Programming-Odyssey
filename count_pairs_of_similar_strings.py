class Solution:
    def similarPairs(self, words: List[str]) -> int:   
        similarity_dict = defaultdict(int)
        for word in words:
            temp = ["0"] * 26
            for char in word:
                temp[ord(char) - 97] = "1"
            
            temp = "".join(temp)
            similarity_dict[temp] += 1
        
        # n(n- 1) / 2
        count_similar = 0
        for value in similarity_dict.values():
            if value > 1:
                count_similar += (value * (value - 1) / 2)
        
        return int(count_similar)
    
