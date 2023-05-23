class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        size = [1] * len(s)
        def find(node):
            compress = [ ]
            while node != rep[node]:
                compress.append(node)
                node = rep[node]
            for i in compress:
                rep[i] = node
            return node
            
        def union(node1, node2):
            rep1 = find(node1)
            rep2 = find(node2)
            size1 = size[rep1]
            size2 = size[rep2]
            if rep1 == rep2:
                return 
            if size1 < size2:
                rep1, rep2 = rep2, rep1
            size[rep1] += size[rep2]
            rep[rep2] = rep1


        rep = defaultdict(str)
        for i in range(len(s)):
            rep[i] = i
        
        for i1, i2 in pairs:
            union(i1, i2)

        ans = list(s)
        group = defaultdict(list)
        for key in rep.keys():
            group[find(key)].append(key)
        
        # print(group)
        for indices in group.values():
            temp = [s[i] for i in sorted(indices)]
            temp.sort()
            # print(indices, temp)
            for i, indx in enumerate(indices):
                ans[indx] = temp[i]
        
        return "".join(ans)