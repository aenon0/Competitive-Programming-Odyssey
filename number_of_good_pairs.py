class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums.sort()
        good_pair_counter=i=0
        while i < len(nums)-1:
            j=i+1
            while j <= len(nums)-1:
                if nums[i] == nums[j]:
                    good_pair_counter+=1
                j+=1
            i+=1
        return good_pair_counter
