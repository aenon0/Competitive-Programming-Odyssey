class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        f = lambda c: c * 1.80 + 32.00 
        k = lambda c: c + 273.15
        temperature_list = [round(k(celsius), 5), round(f(celsius), 5)]
        return temperature_list
        
