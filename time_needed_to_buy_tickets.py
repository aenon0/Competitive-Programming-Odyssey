class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        for indx, num in enumerate(tickets):
            queue.append([indx, num])
        time = 0 
        while queue:
            queue[0][1] -= 1
            time += 1
            if queue[0][1] == 0 and queue[0][0] == k:
                return time
            if queue[0][1] == 0:
                queue.popleft()
            else:
                queue.append(queue[0])
                queue.popleft()
                
        return time
    
            
