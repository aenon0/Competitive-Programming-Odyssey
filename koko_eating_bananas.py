class Solution:
    def hours(self, k):
        total_time = 0 
        for pile in self.piles:
            total_time += ceil(pile / k)
        return total_time
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.h = h
        self.piles = piles
        speed  = [ ]
        left = 0
        right = max(piles) + 1
        while left + 1 < right:
            mid = left + ((right - left) // 2)
            if self.hours(mid) <= h:
                 right = mid
            else:
                 left = mid
                    
        return right                
