class Solution:
    def checkInclusion(self, string1: str, string2: str) -> bool:
        if len(string1) > len(string2):
            return False
        
        string1_ctr = Counter(string1[0: len(string1)])
        temp_ctr = defaultdict(int)
        for i in range(len(string1) - 1):
            temp_ctr[string2[i]] += 1
        
        
        left = 0
        right = len(string1) - 1
        while right < len(string2):
            temp_ctr[string2[right]] += 1
            if temp_ctr == string1_ctr:
                return True
        
            temp_ctr[string2[left]] -= 1
            if temp_ctr[string2[left]] == 0:
                del temp_ctr[string2[left]]
                
            left += 1
            right += 1
        return False
            
            
            
        
