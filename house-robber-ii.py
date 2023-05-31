class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def max_rob(num, curr):
            if curr < 0:
                return 0 
            
            return max(_list[curr],_list[curr] + max_rob(num, curr - 2), max_rob(num, curr - 1))
        
        if len(nums) == 1:
            return nums[0]
        # if len(nums) == 3 or len(nums) == 2:
        #     return max(nums)
        _list = nums[ : -1]
        _max = max_rob(0, len(_list) - 1)
        _list = nums[1 : ]
        _max = max(_max, max_rob(1, len(_list) - 1))
        return _max