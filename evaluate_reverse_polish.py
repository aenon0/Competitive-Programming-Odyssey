class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        for indx in range(len(tokens)):
            if tokens[indx] not in {"+", "-", "*", "/"}:
                tokens[indx] = int(tokens[indx])
                
        stack = [ ]
        for token in tokens:
            
            if token in {"+", "-", "*", "/"}:
                # print(stack)
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "/":
                    stack.append(int(num1 / num2))
                elif token == "*":
                    stack.append(num1 * num2)
                elif token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
            else:
                stack.append(token)
                
        return stack.pop()
    
