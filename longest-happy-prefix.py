class Solution:
    def longestPrefix(self, s: str) -> str:
        lps = [0] * len(s)
        left, right = 0, 1
        while right < len(s):
            if s[left] == s[right]:
                lps[right] = left + 1
                left += 1
                right += 1
            elif left != 0:
                left = lps[left - 1]
            else:
                right += 1
        print(lps)
        _max = lps[-1]
        return s[0: _max]