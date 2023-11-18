class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums))
        for indx in range(0,len(nums)):
            self.prefix[indx] += self.prefix[indx - 1] + nums[indx]
        self.prefix.insert(0, 0)
                        
        
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
