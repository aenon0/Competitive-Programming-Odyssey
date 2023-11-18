class Solution:
    def splitString(self, s: str) -> bool:
        
        def backtrack(prev , string):
            if not string and len(prev)!=1:
                return True
            
            for i in range(len(string)):
                prev.append(int(string[:i + 1]))
                
                check = False
                possible_candidate = len(prev) == 1 or prev[-2] - 1 == prev[-1]
                if possible_candidate:
                    check = backtrack(prev,string[i+1 : ])
                    if check:
                        return True
                # else:
                prev.pop()
            # return False
        return backtrack([], s)
        
        
        
        
        
        
        
        
        
        
        
        
        
#         prev = s[0]
#         def backtrack(indx):
#             if int(prev) - w == 1:
#                 return True
            
#             for i in range(indx, len(s)):
#                 temp = "
#                 if int(s[i] - 1) == int(s[i]):
#                     prev = s[i]
#                 else:
#                     temp += s[i]
                    
                    
