class Trie:
    def __init__(self):
        self.root = { }

    def insert(self, binary: str) -> None:
        curr = self.root
        for digit in binary:
            if int(digit) in curr:
                curr = curr[int(digit)]
            else:
                curr[int(digit)] = { }
                curr = curr[int(digit)]
                
    
    def search(self, binary: str) -> bool:
        temp = self.root
        ans = 0 
        for digit in binary:
            opposite = 1 - int(digit)
            if opposite in temp:
                ans = (ans << 1) | 1
                temp = temp[opposite]
            else:
                ans = (ans << 1)
                temp = temp[int(digit)]

        return ans
        
# class TrieNode:
#     def __init__(self):
#         self.val = 0
#         self.children = defaultdict(TrieNode)

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        max_length = len(bin(max(nums))) - 2
        result = -inf
        for num in nums:
            num = bin(num)[2: ].zfill(max_length)
            trie.insert(num)
            result = max(result, trie.search(num))
        return result