class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loser_dict = dict()
        freq = 0
        for match in matches:
            loser_dict[match[1]] = loser_dict.get(match[1], 0) + 1
        
        once_losers = [ ]
        for key in loser_dict.keys():
            if loser_dict[key] == 1:
                once_losers.append(key)
        
        perfect_winners = set()
        for match in matches:
            if match[0] not in loser_dict:
                perfect_winners.add(match[0])
        
        ans = [sorted(perfect_winners), sorted(once_losers) ]
        
        return ans
        
                
        
        
                
            
        
        
        
        
        
            
                
        
        
        
        
        
 
            
        
