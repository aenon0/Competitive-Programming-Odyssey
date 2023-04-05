class Solution(object):
    def hasGroupsSizeX(self, deck):
        def gcd(num1, num2):
            if num2 == 0:
                return num1
            return gcd(num2, num1 % num2)
        
        num_dict = defaultdict(int)
        for num in deck:
            num_dict[num] +=  1
        
        temp_gcd = num_dict.values()[0]
        for value in num_dict.values():
            temp_gcd = gcd(temp_gcd, value)
        
        if temp_gcd != 1:
            return True
        return False
