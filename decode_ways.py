class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        @cache 
        def decode(indx):
            if indx >= len(s):
                return 1
                           
            decoding_ways = 0 
            
            if s[indx] != "0":
                decoding_ways += decode(indx + 1)
                
                
                if (indx + 1) < len(s) and int(s[indx] + s[indx + 1]) <= 26:
                    decoding_ways += decode(indx + 2)
                    
            return decoding_ways
        
        return decode(0)
                
            