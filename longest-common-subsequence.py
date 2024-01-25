class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.max_length = 0
        @cache
        def build_subsequences(sub1, sub2, idx1, idx2):
            if sub1 == sub2:
                print(sub1, sub2)
                self.max_length = max(self.max_length, len(sub1))
            
            if idx1 < len(text1):
                # pick 
                build_subsequences(sub1 + text1[idx1], sub2, idx1 + 1, idx2)
                # dont pick
                build_subsequences(sub1, sub2, idx1 + 1, idx2)
            if idx2 < len(text2):
                # pick
                build_subsequences(sub1, sub2 + text2[idx2], idx1, idx2 + 1)
                # don't pick
                build_subsequences(sub1, sub2, idx1, idx2 + 1)

        build_subsequences("", "", 0, 0)
        return self.max_length