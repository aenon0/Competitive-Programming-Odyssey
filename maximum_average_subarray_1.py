class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[0: k])
        max_sum = total
        left = 0
        right = k-1
        while right < len(nums) - 1:
            total -= nums[left]
            right += 1
            total += nums[right]
            left += 1
            max_sum = max(max_sum, total)
        return max_sum / k
        
