class Solution:
    def countPairs(self, deliciousness_list: List[int]) -> int:
        count_delicious = 0
        
        power_list = [1]
        previous = 1
        for power in range(1, ceil(math.log(pow(2,22),2))):
            previous *= 2
            power_list.append(previous)
            
        # print(power_list)
        
        deliciousness_ctr = Counter(deliciousness_list)
        
        # [1,2,4,8]
        extra = 0 
        for power in power_list: # 2*10^1
            for key in deliciousness_ctr.keys(): # 10^5
                #2*10^6
                if deliciousness_ctr.get(power - key) != None:
                    if power - key == key:
                        n = deliciousness_ctr[power-key]
                        count_delicious += n*(n-1)//2
                    else:
                        # print(power-key, key)
                        count_delicious += ((deliciousness_ctr.get(power - key) * deliciousness_ctr.get(key)))/2
                   
        return int(count_delicious)%(pow(10, 9) + 7)
                    

