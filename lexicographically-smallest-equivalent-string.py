class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        belongs = defaultdict(str)
        for i in range(97, 123):
            belongs[chr(i)] = chr(i)

        # print(belongs)
        def find(letter):
            return belongs[letter]

        def union(letter1, letter2):
            rep1 = find(letter1)
            rep2 = find(letter2)
            check = True if rep1 > rep2 else False            
            for l in belongs.keys():
                if check and belongs[l] == rep1:
                    belongs[l] = rep2
                if not check and belongs[l] == rep2:
                    belongs[l] = rep1
        
        for i in range(len(s1)):
            union(s1[i], s2[i])
            
        ans = ""
        for c in baseStr:
            ans += find(c)
        return ans