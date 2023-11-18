class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        indx_map = defaultdict()
        for indx, value in enumerate(nums):
            indx_map[value] = indx
        
        for operation in operations:
            nums[indx_map[operation[0]]] = operation[1]
            indx_map[operation[1]] = indx_map[operation[0]]
            # del indx_map[operation[0]]
            
        
#         for operation in operations:
            
#             nums[indx_map[operation[0]]] = operation[1]
#             del indx_map[operation[0]]
            
            # indx_map[operation[1]] = indx_map[operation[0]]
        # print(indx_map)
        return nums
            
