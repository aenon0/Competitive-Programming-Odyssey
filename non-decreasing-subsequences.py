class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = set()
        on_way = [ ]
        def backtrack(idx):
            if idx == len(nums):
                if len(on_way) >= 2:
                    result.add(tuple(on_way))
                return 
                
            if not on_way or on_way[-1] <= nums[idx]:
                on_way.append(nums[idx])
                backtrack(idx + 1)
                on_way.pop()
            backtrack(idx + 1)  
        
        backtrack(0)
        return result