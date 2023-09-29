class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i, c in enumerate(word):
            if not curr.children[ord(c) - 97]:
                curr.children[ord(c) - 97] = TrieNode()
            curr = curr.children[ord(c) - 97]
            if i == len(word) - 1:
                curr.is_end = True

    def find(self, word) -> bool:
        temp = self.root
        for i, ch in enumerate(word):
            if not temp.children[ord(ch) - 97].is_end:
                return False
            
            temp = temp.children[ord(ch) - 97]
            
        return True



#     # def printt(self):
#     #     temp = self.root
#     #     def print1(node):
#     #         print(node.children)
#     #         for child in node.children:
#     #             if child:
#     #                 print1(child)
#     #     print1(temp)
            

            

            
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key = lambda x : (len(x), x))
        _trie = Trie()
        for word in words:
            _trie.insert(word)
        res = ""
        for word in words:
            if _trie.find(word) and len(word) != len(res):
                res = word
        return res