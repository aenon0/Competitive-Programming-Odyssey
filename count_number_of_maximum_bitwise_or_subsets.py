class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        subsets = [ ]
        temp = [ ]
        def backtrack(nums, i):
            if i == len(nums):
                return 
            
            for indx in range(i, len(nums)):
                temp.append(nums[indx])
                backtrack(nums, indx + 1)
                subsets.append(temp[:])
                temp.pop()
        backtrack(nums, 0)
        
        or_dict = defaultdict(int)
        _max = float("-inf")
        for subset in subsets:
            or_result = 0 
            for num in subset:
                or_result = or_result | num
            or_dict[or_result] += 1
            _max = max(_max, or_result)
        
        return or_dict[_max]
