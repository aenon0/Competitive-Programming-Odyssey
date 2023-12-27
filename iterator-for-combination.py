class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.string = characters
        self.length = combinationLength
        self.result = set()
        def backtrack(idx, building):
            if len(building) == self.length:
                self.result.add(building)
                return
            if idx == len(self.string):
                return 
            backtrack(idx + 1, building + self.string[idx])
            backtrack(idx + 1, building)
        backtrack(0, "")
        self.result = sorted(list(self.result))
        self.ptr = 0 


    def next(self) -> str:
        self.ptr += 1
        return self.result[self.ptr - 1]

    def hasNext(self) -> bool:
        if self.ptr == len(self.result):
            return False
        return True


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()