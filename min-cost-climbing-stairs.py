class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [0] * len(cost)
        min_cost[0] = cost[0]
        min_cost[1] = cost[1]

        for i in range(2, len(cost)):
            min_cost[i] = cost[i] + min( min_cost[i - 2], min_cost[i - 1])

        return min(min_cost[-1], min_cost[-2])


        
        #   dp_arr = [0] * len(cost)

    #     dp_arr[0], dp_arr[1] = cost[0], cost[1]
    # #  def path(step):
    #         if step <= 1:
    #             return cost[step]
    #         if dp_arr[step] != 0:
    #             return dp_arr[step]
    #         dp_arr[step] = cost[step] + min(path(step - 2), path(step - 1))
    #         return dp_arr[step]
        

    #     return min(path(len(cost) - 1), path(len(cost) - 2))