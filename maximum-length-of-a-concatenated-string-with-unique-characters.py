class Solution:
    def maxLength(self, array: List[str]) -> int:
#         building a new array in which there is no word that has repeated letter 
        arr = [ ]
        for word in array:
            repeatition = defaultdict(bool)
            repeated = False
            for char in word:
                if repeatition[char] == False:
                    repeatition[char] = True
                else:
                    repeated = True
                    break
            if not repeated:
                arr.append(word)    
                    
        self.max_length = -inf
        self.length = 0 
        seen = set()
        def backtrack(idx):
            if idx == len(arr):
                self.max_length = max(self.max_length, self.length)
                return 
            if not seen or (not set(arr[idx]).intersection(seen)) and (len(set(arr[idx])) == len(list(arr[idx]))):
                for char in arr[idx]:
                    seen.add(char)
                self.length += len(arr[idx])
                backtrack(idx + 1)
                for char in arr[idx]:
                    if char in seen:
                        seen.remove(char)
                self.length -= len(arr[idx])

            backtrack(idx + 1)
        backtrack(0)
        return self.max_length