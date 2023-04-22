class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dislike_dict = defaultdict(set)
        for dislike in dislikes:
            dislike_dict[dislike[0] - 1].add(dislike[1] - 1)
            dislike_dict[dislike[1] - 1].add(dislike[0] - 1)
        
        def dfs(p, color):
            colors[p] = color
            for neighbor in dislike_dict[p]:
                if colors[neighbor] == 0 and not dfs(neighbor, -1 * color):
                    return False
                if colors[neighbor] == color:
                    return False
            return True
            
        
        colors = [0] * n
        for p in range(n):
            if colors[p] == 0 and not dfs(p, 1):
                return False
        
        return True