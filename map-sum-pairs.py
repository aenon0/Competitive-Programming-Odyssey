class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, val: int) -> None:
        curr = self.root
        for i, c in enumerate(word):
            if not curr.children[ord(c) - 97]:
                curr.children[ord(c) - 97] = TrieNode()
            
            curr = curr.children[ord(c) - 97]
        curr.val = val             

    def sum(self, prefix: str) -> int:
        temp = self.root
        flag = True
        def dfs(node, idx):
            res = 0 
            if flag and idx == len(prefix):
                res += node.val

            if idx < len(prefix):
                if node.children[ord(prefix[idx]) - 97]:
                    res += dfs(node.children[ord(prefix[idx]) - 97], idx + 1)
                else:
                    found = False
            else:
                for child in node.children:
                    if child:
                        res += dfs(child, idx)
            return res
        if not temp.children[ord(prefix[0]) - 97]:
            return 0
        return dfs(temp, 0)
        

        


class TrieNode:
    def __init__(self):
        self.val = 0
        self.children = [ None for _ in range(26) ]


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)