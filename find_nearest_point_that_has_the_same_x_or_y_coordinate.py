class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_difference = float("inf")
        ans = [ ]
        for indx in range(len(points)):
            
            if x == points[indx][0] or y == points[indx][1]:
                m_distance = abs(x -  points[indx][0]) + abs( y - points[indx][1])
                if m_distance < min_difference:
                    min_difference = m_distance
                    ans.append(indx)
        
        if not ans: 
            return -1
        return ans[-1]
        
