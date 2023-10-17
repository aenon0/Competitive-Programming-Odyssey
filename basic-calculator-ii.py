class Solution:
    def calculate(self, string: str) -> int:
        string = string.replace(" ", "")
        oper = "+"
        idx = 0
        stack = [ ]
        while idx < len(string):
            if string[idx] in {"+", "-", "*", "/"}:
                oper = string[idx]
                idx += 1
            else:
                i = idx
                while idx < len(string) and string[idx] not in {"+", "-", "*", "/"}:
                    idx += 1
                
                
                if oper == "+":
                    stack.append(int(string[i : idx]))
                elif oper == "-":
                    stack.append(-1 * int(string[i : idx]))
                elif oper == "/":
                    num1 = stack.pop()
                    stack.append(int(num1 / int(string[i : idx])))
                    # print(num1, int(string[i: idx]))
                else:
                    num1 = stack.pop()
                    stack.append(num1 * int(string[i : idx]))
            # print(stack, oper)
                
        return sum(stack)