class LRUCache:

    def __init__(self, capacity: int):
        self.lru_cache = { }
        self.freespace = capacity

    def get(self, key: int) -> int:
        if key in self.lru_cache:
            self.lru_cache[key] = self.lru_cache.pop(key)
            return self.lru_cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru_cache:
           self.lru_cache.pop(key)
        else:
            if self.freespace:
                self.freespace -= 1
            else:
                self.lru_cache.pop(next(iter(self.lru_cache)))
        self.lru_cache[key] = value
                
                
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)