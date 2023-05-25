class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0 
        tens = 0 
        twenties = 0 
        for bill in bills:
            # print(bill, fives, tens, twenties)
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives == 0:
                    return False
                fives -= 1
                tens += 1
            else:
                if fives < 3 and (fives == 0 or tens == 0):
                    return False
                if tens >= 1 and fives >= 1:
                    tens -= 1    
                    fives -= 1
                else:
                    fives -= 3
        return True