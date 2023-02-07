class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(height) - 1
        
        max_water = 0 
        while left_ptr < right_ptr:
            water_amount = (right_ptr - left_ptr) * min(height[left_ptr], height[right_ptr])
            max_water = max(max_water, water_amount)
            if height[left_ptr] < height[right_ptr]:
                left_ptr += 1
            else :
                right_ptr -= 1
                
        return max_water
            
