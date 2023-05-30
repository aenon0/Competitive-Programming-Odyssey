class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = dict()
        def backtrack(curr, _sum):
            if curr == len(nums):
                if _sum == target:
                    return 1
                return 0
            if (curr, _sum) in dp:
                return dp[(curr, _sum)]

            dp[(curr, _sum)] = backtrack(curr + 1, _sum + nums[curr]) + backtrack(curr + 1, _sum - nums[curr])
            return dp[(curr, _sum)]
        
        return backtrack(0, 0)








        # def backtrack1(current_state):
        #     if current_state is a goal state:
        #         return current_state
        #     for move in possible_moves:
        #         new_state = make_move(current_state, move)
        #         if new_state is valid:
        #             result = backtrack1(new_state)
        #             if result is not None:
        #                 return result
        #             undo_move(current_state, move)
        #     return None