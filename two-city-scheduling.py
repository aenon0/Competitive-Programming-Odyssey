class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda c: c[0] - c[1])
        size = len(costs)
        ans = 0 
        for i in range(size // 2):
            ans += costs[i][0]
        for i in range(size // 2, size):
            ans += costs[i][1]
        return ans