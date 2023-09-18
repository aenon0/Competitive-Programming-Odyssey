class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        @cache
        def dp(idx, last_picked, sign):
            # print(idx, last_picked, sign)
            if idx == len(nums):
                return 0

            result = 0 
            check = (nums[idx] - nums[last_picked])

            # if the curr number fulfills the expected difference sign 
            # we pick the current one or not
            # else we just pass it and continue picking
            if (check // sign) > 0:

                _max = max((1 + (dp(idx + 1, idx, -1 * sign))) , dp(idx + 1, last_picked, sign))
                result = _max            
            else:
                _max = dp(idx + 1, last_picked, sign)
                result += _max
                
            return result

        return 1 + max(dp(1, 0, 1), dp(1, 0, -1))