class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        window_size = len(needle)
        alphas = [ ]
        MOD = (10 ** 9 + 7)

        def generate_hash(string):
            hash_result = 0 
            n = len(string)
            for i in range(len(string)):
                hash_result = (hash_result *27) + (ord(string[i]) - 96)
            return hash_result % MOD
        
        def add_last(hashed_val, last):
            return (27 * (hashed_val) + (ord(last) - 96)) % MOD 

        def poll_first(hashed_val, first):
            return (hashed_val - (ord(first) - 96) * (27 ** (window_size-1)) ) % MOD
        
        needle_hash = generate_hash(needle)
        curr_hash = generate_hash(haystack[: len(needle)])
        left, right = 0, len(needle) - 1

        while right < len(haystack)-1:
            if curr_hash == needle_hash:
                return left

            curr_hash = poll_first(curr_hash, haystack[left])
            left += 1
            right += 1
            curr_hash = add_last(curr_hash, haystack[right])
            
        if curr_hash == needle_hash:
                return left
            
        return -1