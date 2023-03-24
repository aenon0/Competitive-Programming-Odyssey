class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        for indx in range(len(arr)):
            while arr[indx] != 0 and arr[indx] != indx + 1:
                arr[arr[indx] - 1], arr[indx] = arr[indx], arr[arr[indx] - 1]
                
        for indx in range(len(arr)):
            if arr[indx] != indx + 1:
                return indx + 1
        
        return 0
