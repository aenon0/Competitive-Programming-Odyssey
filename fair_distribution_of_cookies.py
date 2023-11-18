class Solution(object):
    def distributeCookies(self, cookies, k):
        kids = [0] * k
        total_sum = sum(cookies)
        self._max = float("inf")
        cookies.sort(reverse=True)
        def backtrack(curr_cookie):
            
            if sum(kids) == total_sum:
                self._max = min(max(kids), self._max)
                return 
            
            if self._max <= max(kids):
                return
            
            
            for indx in range(len(kids)):
                kids[indx] += cookies[curr_cookie]
                backtrack(curr_cookie + 1)
                kids[indx] -= cookies[curr_cookie]
                                                    
                
        backtrack(0)
        return self._max
                
            
