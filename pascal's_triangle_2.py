class Solution:
    def getRow(self, row_index: int) -> List[int]:
        if row_index == 0:
            return [1]
        
        curr = [0] * (row_index + 1)
        prev = self.getRow(row_index - 1)
        for indx in range(len(curr)):
            if indx == 0 or indx == len(curr) - 1:
                curr[indx] = 1
            else:
                curr[indx] = prev[indx -1] + prev[indx]
                
        return curr
            
