class Solution(object):
    def findRightInterval(self, intervals):
        for indx in range(len(intervals)):
            intervals[indx].append(indx)
        
        intervals = sorted(intervals, key = lambda x: x[0])
       
        
        result = [0] * len(intervals)
        
        
        for indx in range(len(intervals)):
            
            target = intervals[indx][1]
            left = -1
            right = len(intervals)
            while left + 1 < right:
                mid = left + ((right - left) // 2)
                if target <= intervals[mid][0]:
                    right = mid
                else:
                    left = mid
                    
            result[intervals[indx][2]] = intervals[right][2] if right < len(intervals) else -1
        return result
