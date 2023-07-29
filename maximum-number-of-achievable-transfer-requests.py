class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        self.result = -inf
        def backtrack(idx, net_transfer, used):
            if idx == len(requests):
                balanced = True
                for bldg_net in net_transfer:
                    if bldg_net != 0:
                        balanced = False
                        break
                if balanced:
                    self.result  = max(self.result, used)
                return 

            
            start, end = requests[idx]
            net_transfer[start] -= 1
            net_transfer[end] += 1
            backtrack(idx + 1, net_transfer, used + 1)
            net_transfer[start] += 1
            net_transfer[end] -= 1
            backtrack(idx + 1, net_transfer, used)
        backtrack(0, [0] * n, 0)
        return self.result