class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = [ g - c for g, c in zip(gas, cost)]
        if sum(res) < 0:
            return -1

        g = 0
        idx = 0
        for i, curr_gas in enumerate(res):
            g += curr_gas
            if g < 0:
                g = 0 
                idx = i + 1
        return idx