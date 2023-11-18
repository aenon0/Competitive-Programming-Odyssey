class Solution:
    def scoreOfParentheses(self, string: str) -> int:
        stack = [ ]
        
        for char in string:
            if char == '(':
                stack.append(-1)
            else:
                if stack and stack[-1] == -1:
                    stack.pop()
                    stack.append(1)
                else:
                    score = 0 
                    while stack[-1] != -1:
                        score += stack.pop()
                    stack.pop()
                    stack.append(2 * score)
        result = 0
        while stack:
            result += stack[-1]
            stack.pop()
        return result
            
                    
