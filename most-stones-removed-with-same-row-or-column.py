class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        rep = defaultdict(set)

        for x, y in stones:
            rep[(x, y)] = (x, y)
            row_dict[x].add((x, y))
            col_dict[y].add((x, y))
        
        def find(node):
            return rep[node]

        def union(node1, node2):
            rep1 = find(node1)
            rep2 = find(node2)
            if rep1 != rep2:
                for node in rep.keys():
                    if rep[node] == rep2:
                        rep[node] = rep1        
       
        for x, y in stones:
            for x1, y1 in row_dict[x]:
                if rep[(x, y)] != rep[(x1, y1)]:
                    union((x, y), (x1, y1))
            for x2, y2 in col_dict[y]:
                if rep[(x, y)] != rep[(x2, y2)]:
                    union((x, y), (x2, y2))
        
        # for key in rep.keys():
        #     print(key, rep[key])

        size = defaultdict(int)
        for key in rep.keys():
            size[rep[key]] += 1
        ans = 0
        for key in size.keys():
            ans += (size[key] - 1)
            
        return ans