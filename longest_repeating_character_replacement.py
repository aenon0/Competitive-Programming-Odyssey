class Solution:
    def characterReplacement(self, string: str, k: int) -> int:
        max_length = 1
        left = 0 
        right = 1
        letter_dict = defaultdict(int)
        letter_dict[string[left]] += 1
        max_freq = letter_dict[string[left]]
        for right in range(1, len(string)):
            letter_dict[string[right]] += 1
            if letter_dict[string[right]] > max_freq:
                max_freq = letter_dict[string[right]]
            freq_sum = sum(letter_dict.values()) - max_freq
            while freq_sum > k:
                letter_dict[string[left]] -= 1
                if letter_dict[string[left]] == 0:
                    del letter_dict[string[left]]
                freq_sum -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
            
            
            
            
            
            
            
            
            
            
        
