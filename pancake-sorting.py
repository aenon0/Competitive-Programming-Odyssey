class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if arr == sorted(arr):
            return [ ]

        def flip(k):
            for idx in range(round(k / 2)):
                arr[idx], arr[k - idx - 1] = arr[k - idx - 1], arr[idx]
                
        num = len(arr)
        result = [ ]
        while num > 0:
            idx = arr.index(num)
            if num != idx + 1:
                if idx != 0:
                    result.append(idx + 1)
                    flip(idx + 1)
                result.append(num)
                flip(num)
            
            num -= 1
        return result