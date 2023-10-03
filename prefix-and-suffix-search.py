class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]


class WordFilter:
    def __init__(self, words: List[str]):
        self._find = defaultdict(int)
        self.root = TrieNode()
        self._dict = defaultdict(list)
        self.word_dict = defaultdict(int)
        def insert(word: str) -> None:
            curr = self.root
            for i, c in enumerate(word):
                if not curr.children[ord(c) - 97]:
                    curr.children[ord(c) - 97] = TrieNode()
                curr = curr.children[ord(c) - 97]
         
        for i, word in enumerate(words):
            self.word_dict[word] = i
            
            for i in range(1, len(word) + 1):
                self._dict[word[-1 * i: len(word)]].append(word)
                insert(word[-1 * i: len(word)])

        # for suff in self._dict.keys():
        #     print(suff, ":", self._dict[suff])


               

    def f(self, prefix: str, suffix: str) -> int:
        def starts_with(prefix : str) -> bool:
            temp = self.root
            for i, ch in enumerate(prefix):
                if not temp.children[ord(ch) - 97]:
                    return False
                temp = temp.children[ord(ch) - 97]
            return True
        if self._find[(prefix, suffix)]:
            return self._find[(prefix, suffix)]
        res = [ ]
        if starts_with(suffix):            
            for word in self._dict[suffix]:
                if word[0: len(prefix)] == prefix:
                    res.append(self.word_dict[word])
        
        res.sort()
        res = -1 if not res else res[-1]
        self._find[(prefix, suffix)] = res
        return res

        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)