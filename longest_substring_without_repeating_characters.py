class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        temp_dict  = defaultdict(int)
        max_length = 0
        left = 0 
        for right in range(len(string)):
            temp_dict[string[right]] += 1
            
            while temp_dict[string[right]] > 1 :
                temp_dict[string[left]] -= 1
                if temp_dict[string[left]] == 0:
                    del temp_dict[string[left]]
                left += 1
            max_length = max(max_length, right - left  + 1)
            
        return max_length
            
