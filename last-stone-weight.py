class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for indx in range(len(stones)):
            stones[indx] *= -1
        heapq.heapify(stones)
        
        while len(stones) > 0:
            
            if len(stones) == 1:
                return  -1 * stones[0]
            
            largest = -1 * heapq.heappop(stones)
            next_largest = -1 * heapq.heappop(stones)
            if largest != next_largest:
                heapq.heappush(stones,  -1 * (largest - next_largest))    
    
        return 0