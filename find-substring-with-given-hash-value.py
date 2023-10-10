class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:   
        def generate_hash(string):
            hash_result = 0 
            n = len(string)
            for i in range(len(string)):
                hash_result = (hash_result * power) + (ord(string[i]) - 96)
            return hash_result % modulo

        def add_last(hashed_val, last):
            return (power * (hashed_val) + (ord(last) - 96)) % modulo

        def poll_first(hashed_val, first):
            return (hashed_val - (ord(first) - 96) * (pow(power, k - 1, modulo))) % modulo
        
        s = s[:: -1]
        left, right = 0, k - 1
        window_hashed = generate_hash(s[: k - 1])
        res_left = res_right = 0 
        while right < len(s):
            window_hashed = add_last(window_hashed, s[right])
            right += 1
            # print(s[left: right][::-1], window_hashed)
            if window_hashed == hashValue:
                res_left = left
                res_right = right
                
            window_hashed = poll_first(window_hashed, s[left])
            left += 1
        return s[res_left : res_right][::-1]