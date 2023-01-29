class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        indices = [ ]
        nums.sort()
        for indx in range(len(nums)):
            if nums[indx] == target:
                indices.append(indx)
        return indices
