class RandomizedSet:

    def __init__(self):
        self.container = [ ]
        self.indx = { }
    def insert(self, val: int) -> bool:
        if val not in self.indx:
            self.indx[val] = len(self.container)
            self.container.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.indx:
            return False
        idx = self.indx[val]
        self.container[idx], self.container[-1] = self.container[-1], self.container[idx]
        self.indx[self.container[idx]] = idx
        del self.indx[self.container[-1]]
        self.container.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.container)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()