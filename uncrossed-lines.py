class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dp(candidate, curr_possible):
            if candidate == len(nums1) or curr_possible == (len(nums2)):
                return 0
            
            _max = 0
            for idx in range(curr_possible, len(nums2)):
                    for c in range(candidate, len(nums1)):
                        if nums1[c] == nums2[idx]:
                            connecting_candidate = 1 + dp(c + 1, idx + 1)
                            _max = max(_max, connecting_candidate)
                            # skipping_candidate1 = dp(c + 1, curr_possible)
                            # skipping_candidate2 = dp(c, curr_possible + 1)

                            # _max = max(_max, skipping_candidate1)
                            # _max = max(_max, skipping_candidate2)

            return _max
        return dp(0, 0)