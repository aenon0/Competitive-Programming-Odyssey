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
    
    def starts_with(self, prefix : str) -> bool:
        temp = self.root
        count = 0
        for i, ch in enumerate(prefix):
            if len(set(temp.children)) == 2 and temp.children[ord(ch) - 97] != None:
                temp = temp.children[ord(ch) - 97]
                count += 1
            else:
                return count
            
        return count 
    
         
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]



class Solution:
    def longestCommonPrefix(self, strings: List[str]) -> str:
        if len(strings) == 1:
            return strings[0]
        strings.sort(key = lambda x : len(x))
        _trie = Trie()
        for i in range(1, len(strings)):
            _trie.insert(strings[i])
        
        ans = ""
        smallest = strings[0]

        count = _trie.starts_with(smallest)
        ans = smallest[0 : count]
        return ans