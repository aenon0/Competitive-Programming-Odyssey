class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i, c in enumerate(word):
            if not curr.children[ord(c) - 97]:
                curr.children[ord(c) - 97] = TrieNode()
            curr = curr.children[ord(c) - 97]
            curr.val += 1

    def starts_with(self, prefix : str) -> bool:
        temp = self.root
        res = 0 
        for i, ch in enumerate(prefix):
            temp = temp.children[ord(ch) - 97]
            res += temp.val

        return res
        



class TrieNode:
    def __init__(self):
        self.val = 0
        self.children = [ None for _ in range(26) ]



class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        ans = [0] * len(words)
        for i, word in enumerate(words):
            ans[i] = trie.starts_with(word)
        return ans