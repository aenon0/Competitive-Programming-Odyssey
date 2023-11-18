class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        
        stack = [ ]
        for p in path:
            if p ==  "..":
                if stack:
                    stack.pop()
            elif p in [".", ""]:
                continue
            else:
                stack.append(p)
        
    
        return "/" + "/".join(stack)
            
            
        
        
