class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0 
        _sum = 0 
        remainder_dict = defaultdict(int)
        for num in nums:
            _sum += num
            if _sum  % k == 0:
                count += 1
            if _sum % k in remainder_dict:
                count += remainder_dict[_sum % k]
            remainder_dict[_sum % k] += 1
            
        return count
            
