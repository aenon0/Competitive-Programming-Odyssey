class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        belongs = defaultdict(list)
        def find(node):
            rep = belongs[node]
            return rep

        def union(node1, node2):
            rep1 = find(node1)
            rep2 = find(node2)

            
            check = True if rep1 < rep2 else False
            for node in belongs.keys():
                if check and belongs[node] == rep2:
                    belongs[node] = rep1
                if not check and belongs[node] == rep1:
                    belongs[node] = rep2
                    
                    
        for node1, sign, _, node2 in equations:
            if not belongs[node1]:
                    belongs[node1] = node1
            if not belongs[node2]:
                belongs[node2] = node2
            if sign == "=":
                union(node1, node2)
                
        # for key in belongs.keys():
        #     print(key, belongs[key])
        

        for node1, sign, _, node2 in equations:
            if sign == "!":
                if find(node1) == find(node2):
                    print(find(node1), find(node2))
                    return False
        return True