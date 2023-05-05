class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for indx in range(len(piles)):
            piles[indx] *= -1
        heapq.heapify(piles)
        for _ in range(k):
            largest =  -1 * heapq.heappop(piles)
            largest -= (largest // 2)
            largest *= -1
            heapq.heappush(piles, largest)
        
        min_total = 0 
        while piles:
             stone = -1 * (heapq.heappop(piles))
             min_total += stone
        return min_total