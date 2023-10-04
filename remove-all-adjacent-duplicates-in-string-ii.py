class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [ ]
        for letter in s:
            if stack:
                if stack[-1][0] == letter:
                    stack.append((letter, stack[-1][1] + 1))
                else:
                    stack.append((letter, 1))
            else:
                stack.append((letter, 1))
            temp = k
            if stack[-1][1] == k:
                while temp:
                    temp -= 1
                    stack.pop()

        return "".join([s[0] for s in stack])