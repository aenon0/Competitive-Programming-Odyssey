class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i, c in enumerate(word):
            if not curr.children[ord(c) - 97]:
                curr.children[ord(c) - 97] = TrieNode()
            curr = curr.children[ord(c) - 97] 
        curr.is_end = True


    def search(self, word: str) -> bool:
        def dfs(node, idx):
            curr = node
            for i in range(idx, len(word)):
                if word[i] != ".":
                    nxt = ord(word[i]) - 97
                    if not curr.children[nxt]:
                        return False
                    curr = curr.children[nxt]
                else:
                    for child in curr.children:
                        if child and dfs(child, i + 1):
                            return True
                    return False            
            return curr.is_end
        return dfs(self.root, 0)
              
        
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)