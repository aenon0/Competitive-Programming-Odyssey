class Solution:
    def compress(self, chars: List[str]) -> int:
        # result = ""
        p = p1 = p2 = 0 
        while p1 < len(chars) and p2 < len(chars):
            while p2 < len(chars) and chars[p1] == chars[p2]:
                p2 += 1
            chars[p] = chars[p1]
            p += 1
            if (p2 - p1) != 1:
                length = list(str(p2 - p1))
                for i in range(len(length)):
                    chars[p] = length[i]
                    p += 1
            p1 = p2
            
        return p