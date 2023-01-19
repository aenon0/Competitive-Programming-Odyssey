class Solution: 
    def select(self, arr, current_index): 
        min_index = current_index 
        for indx in range(current_index + 1, len(arr)):
            if arr[indx] < arr[min_index]:
                min_index = indx
        return min_index
            
    def selectionSort(self, arr,n):
        for current_index in range(len(arr)):
            min_index = Solution.select(self, arr, current_index)
            arr[current_index],arr[min_index] = arr[min_index], arr[current_index] 
