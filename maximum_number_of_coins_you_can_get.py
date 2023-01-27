class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_coins = 0 
        for num_index in range(len(piles) - 2, (len(piles) // 3) - 1, - 2):
            max_coins += piles[num_index]     
        return max_coins
            
        
        
