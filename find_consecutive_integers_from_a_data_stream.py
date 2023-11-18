class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.queue = deque()
        self.dict = defaultdict(int)

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        self.dict[num] += 1
        
        if len(self.queue) < self.k:
            return False
        elif len(self.queue) == self.k:
            if len(self.dict) == 1 and num == self.value and self.dict[num] == self.k:
                self.dict[self.queue[0]] -= 1
                if self.dict[self.queue[0]] == 0:
                    del self.dict[self.queue[0]]
                self.queue.popleft()
                return True
            
            self.dict[self.queue[0]] -= 1
            if self.dict[self.queue[0]] == 0:
                del self.dict[self.queue[0]]
            self.queue.popleft()
            return False
            
