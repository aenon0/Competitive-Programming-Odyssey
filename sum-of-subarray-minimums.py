class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mins_sum =  0
        stack = [-1]
        arr.append(-1)
        for indx in range(len(arr)):
            while stack and arr[indx] < arr[stack[-1]]:
                mid = stack.pop()
                left = stack[-1]
                right = indx
                mins_sum += (arr[mid] * ((right - mid) * (mid - left)))
            stack.append(indx)
        return mins_sum % ((10**9) + 7)