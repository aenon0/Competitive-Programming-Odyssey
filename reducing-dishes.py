class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)
        
        result = total = 0 
        
        
        for level in satisfaction:
            if level + total < 0:
                break
            total += level
            result += total
        
        return result