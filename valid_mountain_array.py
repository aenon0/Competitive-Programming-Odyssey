class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        mountain_peak = [ ]
        for arr_index in range(1, len(arr) - 1):
            if arr[arr_index] > arr[arr_index + 1] and arr[arr_index - 1] < arr[arr_index]:
                mountain_peak.append(arr_index)
        
        if len(mountain_peak) != 1:
            return False
        
        for arr_index in range(0, mountain_peak[0]):
            if arr[arr_index] >= arr[arr_index + 1]:
                return False
            
        for arr_index in range(mountain_peak[0] + 1, len(arr)):  
            if arr[arr_index] >= arr[arr_index - 1]:
                return False
            
        if arr.count(arr[(mountain_peak[0])]) != 1 or arr[mountain_peak[0]] != max(arr):
            return False
        
        return True
        
