class Solution:
    def restoreIpAddresses(self, string: str) -> List[str]:
        if len(string) > 12:
            return [ ]

        result = set()
        curr = [ ]

        def backtrack(idx):
            if len(curr) > 4:
                return 
            if idx >= len(string):
                if len(curr) == 4:
                    result.add(".".join(curr))
                return 

            for i in range(1, 4):
                if int(string[idx : idx + i]) < 256 and (len(string[idx : idx + i]) == 1 or string[idx] != "0"):
                    curr.append(string[idx : idx + i])
                    backtrack(idx + i)
                    curr.pop()
        
        backtrack(0)
        return list(result)