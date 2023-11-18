class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        size = 0
        for num, initial, final in trips:
            size = max(final, size)
        
        arr = [0] * (size + 1)
        for num, initial, final in trips:
            arr[initial] += num
            arr[final] -= num
            
        for indx in range(1, len(arr)):
            arr[indx] += arr[indx - 1]
        
        for indx in range(len(arr)):
            if arr[indx] > capacity:
                return False
        return True
        
