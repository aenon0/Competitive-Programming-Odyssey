class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_freq = [0] * 26
        t_freq = [0] * 26
        for char in s:
            s_freq[ord(char) - 97] += 1
        for char in t:
            t_freq[ord(char) - 97] += 1
        
        result = 0 
        for i in range(26):
            result += abs(s_freq[i] - t_freq[i])
        
        return result