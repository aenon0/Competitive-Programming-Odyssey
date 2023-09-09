class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [0] * len(labels)        
        adj_list = defaultdict(list)
        for node1, node2 in edges:
            adj_list[node1].append(node2)  
            adj_list[node2].append(node1)  

            
        def dfs(node):
            alphabet = [0] * 26
            alphabet[ord(labels[node]) - 97] += 1
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    returned = dfs(neighbor)              
                    for i in range(len(returned)):
                        alphabet[i] += returned[i]

            ans[node] = alphabet[ord(labels[node]) - 97]
            return alphabet
        visited = set()
        visited.add(0)
        dfs(0)
        return ans